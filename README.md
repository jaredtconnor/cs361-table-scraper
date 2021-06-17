# Wikipedia table scraping microservice

This is a basic API that pulls tables from (Wikipedia)[https://www.wikipedia.org] pages. This service is written in Python. There are only GET methods implemented and all responses return a dictionary/JSON object to be utilized within other services.

Following API endpoints are exposed:

- `GET /search` - Searches based upon the Wikipedia slug (i.e. - The page for [https://en.wikipedia.org/wiki/100_metres](https://en.wikipedia.org/wiki/100_metres) would be the `100_metres` slug)

## Parameters: 

1) `/search/slug`: (required) - Endpoint of the specific Wikipedia page that contains the tables to parse
2) `search/slug/table_num`: (required) - The index of the table to pull from the page

## Example: 
API request - GET - `http://wikipedia-table-scraper.herokuapp.com/search/C_(programming_language)/1`

Returns: 
```
{
    Year:{ 
            0: 1972,
            1: 1978, 
            2: 1989, 
            3: 1999, 
            4: 2005,
            5: 2017, 
            6: TBD
    }, 
    C Standard: { 
        0: Birth, 
        1: K&R C, 
        2: ANSI C and ISO C, 
        3: C99, 
        4: C11, 
        5: C17, 
        6: C2x
    }
```

## Building and running

1) Install dependencies: 
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2) Run app: 
``` 
python app.py
```

## License

MIT