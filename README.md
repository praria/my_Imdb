My IMDB API
**************
This is a Flask_based backend application that provides movie data from a CSV file. The application allows users to 
retrieve movies based on genre using different API routes.

Features:
************
- Serves movie data from a CSV file instead of a database
- provides filtering by genre using query parameters
- predefined routes for specific genres like action, adventure, comedy, drama, and romance
- returns responses in json format



Setup and Installation
***********************
1. clone the repository
- git clone https://github.com/praria/my_Imdb.git 
- cd my_Imdb 

2. Create and activate a virtual environment
- python -m venv myvenv
- source myvenv/bin/active 

3. Install dependencies
- pip install -r requirements.txt

4. run the application
- python3 app.py

The server will start on http://localhost:8080 

API Endpoints
***************

1. Get movies by genre
- endpoint: / 
- method: GET
- Query parameter: genre 
- example: curl http://localhost:8080?genre=action 

2. predefined genre routes: Each of the following routes filters movies based on a specific genre
- /action
- /adventure
- /comedy
- /drama
- /romance
- / western

Example Usages

curl http://localhost:8080/action
curl http://localhost:8080/adventure
curl http://localhost:8080/comedy
curl http://localhost:8080/drama
curl http://localhost:8080/romance
curl http://localhost:8080/western 

Example response: 
[{
    "Actors": "Jennifer Lawrence, Chris Pratt, Michael Sheen,Laurence Fishburne",
    "Description": "A spacecraft traveling to a distant colony planet and transporting thousands of people has a malfunction in its sleep chambers. As a result, two passengers are awakened 90 years early.",
    "Director": "Morten Tyldum",
    "Genre": "Adventure,Drama,Romance",
    "Metascore": 41.0,
    "Rank": 10,
    "Rating": 7.0,
    "Revenue (Millions)": 100.01,
    "Runtime (Minutes)": 116,
    "Title": "Passengers",
    "Votes": 192177,
    "Year": 2016
  }]

