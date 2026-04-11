# WSAA-coursework

# Web Services and Applications Assessment

## Table of Contents
 - [Project Purpose](#project-purpose)
 - [Install Dependencies](#install-dependencies)
 - [Setup Instructions](#setup-instructions)
 - [Implementations](#implementations)
    - [Assignment 2](#assignments/assignment2-carddraw.ipynb)
    - [Assignment 3](#assignments/assignment03-cso.ipynb)
    - [Assignment 4](#assignment05-github.ipynb)

## Project Purpose
This repository contains my assignment submissions for the Web Services and Applications module completed as part of the Higher Diploma in Science in Computing in Data Analytics at ATU.

## Install Dependencies
All required libraries are listed in requirements.txt  

## Setup Instructions
Clone this GitHub repository:
<pre> git clone https://github.com/vanelyraa/programming-for-data-analytics.git </pre>

Navigate the project directory:
<pre> cd https://github.com/vanelyraa/programming-for-data-analytics.git </pre>

Create a virtual environment (optional):
<pre> python3 -m venv venv </pre>

Activate virtual environment (optional):  
For windows: <pre> source venv/bin/activate </pre> 
For MacOS: <pre> source venv/bin/activate  </pre> 

Install required dependencies:
<pre> pip install -r requirements.txt </pre>

## Implementations

#### Assignment 2 – Card draw
This program uses the Deck of Cards API with Python libraries such as requests and collections. Counter simulates dealing and evaluating the drawn cards. It begins by sending an HTTP request with requests.get() to shuffle a new deck and retrieve a deck_id, then makes a second request to draw 5 cards. The JSON response is parsed using .json(), and a for loop is used to iterate through the returned cards, extracting and printing each card’s value and suit while storing them in lists.
A dictionary is used to map face cards (JACK, QUEEN, KING, ACE) to numeric values, and another loop converts all card values into integers for easier comparison. The Counter class is then applied to count occurrences of card values and suits, enabling detection of pairs, triples, and whether all cards share the same suit. For straight detection, the program uses set() to remove duplicates, sorted() to order the values, and conditional checks to determine if the numbers form a sequence.

#### Assignment 3 - CSO
This program retrieves data from the Central Statistics Office Ireland API using libraries requests and json. It sends an HTTP request with requests.get() for the Exchequer Account (Historical Series) and converts the response into a Python dictionary using .json(). The dataset is then written to a local file named cso.json by opening the file in write mode and using json.dump() to serialize the data into JSON format and prints the confirmation that the file has been saved.

#### Assignment 4 - GitHub
This program interacts with the GitHub API using the requests library and the github library to automate reading and updating a file in a repository. Its authentication is handled by using a personal access token stored in config.py file, which is passed to Github to establish a connection. The repository is accessed with get_repo(), and the target file is retrieved using get_contents(), which provides both file metadata and a download URL.
The file content is fetched using requests.get() and converted to text, then the replace() string method is used to substitute all instances of "Andrew" with "Vanessa". Finally, the updated content is committed and pushed back to the repository using update_file(), which requires the file path, a commit message, the new content, and the file’s SHA to ensure the correct version is updated. 

** End **
