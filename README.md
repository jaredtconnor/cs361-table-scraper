# Wikipedia table scraping microservice

This is a basic API that pulls tables from (Wikipedia)[https://www.wikipedia.org] pages. This service is written in Python. There are only GET methods implemented and all responses return a dictionary/JSON object to be utilized within other services.

Following API endpoints are exposed:

- `GET /search` - Searches based upon the Wikipedia slug (i.e. - The page for [https://en.wikipedia.org/wiki/100_metres](https://en.wikipedia.org/wiki/100_metres) would be the `100_metres` slug)

## Parameters: 

1) `/search/slug`: (required) - Endpoint of the specific Wikipedia page that contains the tables to parse
2) `search/slug/table_num`: (required) - The index of the table to pull from the page

## Example: 
`

## Building and running

```
npm install
JWT_SECRET=foo TODO_API_PORT=8082  npm start
```

## Usage

```
 curl -X POST -H "Authorization: Bearer $token" 127.0.0.1:8082/todos -d '{"content": "deal with that"}'
```