from flask import Flask, json, render_template, jsonify
from flask_restful import Api, Resource, abort
import requests
import pandas as pd

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

        # Define Wikipedia url
        wikipedia_page = "https://en.wikipedia.org/wiki/" + search

        # Verification
        resp = requests.get(wikipedia_page)
        check_link(resp)

        # Using pandas to read and prase the table elements from Wikipedia
        tables = pd.read_html(wikipedia_page)

        data = tables[table_num].to_dict()

        # Return table indexed by request paramerters 
        return data

# Second class to parse table and filter based upon Wikipedia input
class filter_table(Resource):

    # Function to pull the table based on the endpoint url provided
    def get(self, search, table_num, top_n):

        # Define Wikipedia url
        wikipedia_page = "https://en.wikipedia.org/wiki/" + search

        # Verification
        resp = requests.get(wikipedia_page)
        check_link(resp)

        # Using pandas to read and prase the table elements from Wikipedia
        tables = pd.read_html(wikipedia_page)
        filtered_table = tables[table_num].head(n = top_n)

        data = filtered_table.to_dict()

        # Return table indexed by request paramerters 
        return data

@app.route('/')
def description(): 
    return render_template('index.html')

api.add_resource(parse_table, "/search/<string:search>/<int:table_num>")
api.add_resource(filter_table, "/filter/<string:search>/<int:table_num>/<int:top_n>")

if __name__ == "__main__":
    app.run(debug=True, port=5001)