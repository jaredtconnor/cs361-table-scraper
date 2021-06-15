from flask import Flask, render_template, jsonify
from flask_restful import Api, Resource, abort
from bs4 import BeautifulSoup
import csv
import requests
import json

app = Flask(__name__)
api = Api(app)

# Function to check to see if request is valid 
def check_link(request):
    if request.status_code > 200:
        abort(404, message="Connection Error")
    else:
        return True

# Main class to parse table based upon Wikipedia input
class parse_table(Resource):

    # Function to pull the table based on the endpoint url provided
    def get(self, search, table_num):

        tables = []

        wikipedia_page = "https://en.wikipedia.org/wiki/" + search

        # Verification
        resp = requests.get(wikipedia_page)
        check_link(resp)

        soup = BeautifulSoup(resp.content, 'html.parser')
        table_data = soup.find_all('table')

        headers = [header.text for header in table.find_all('th')]
        results = [{headers[i]: cell for i, cell in enumerate(row.find_all('td'))}
                    for row in table.find_all('tr')]
        print(table)

        return tables

@app.route('/')
def description(): 
    return render_template('index.html')

api.add_resource(parse_table, "/<string:search>/<int:table_num>")

if __name__ == "__main__":
    app.run(debug=True, port=5001)