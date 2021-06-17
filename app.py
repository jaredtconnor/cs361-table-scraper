from flask import Flask, render_template, jsonify
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

        # Return table indexed by request paramerters 
        return jsonify(tables[table_num].to_json())

@app.route('/')
def description(): 
    return render_template('index.html')

api.add_resource(parse_table, "/search/<string:search>/<int:table_num>")

if __name__ == "__main__":
    app.run(debug=True, port=5001)