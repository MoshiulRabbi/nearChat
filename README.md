# Nearby Chat
This Django app allows users to sign up and view the real-time locations of other users within a customizable range (default is 20km). Users can also chat with each other through the use of Django Channels and websockets.



## Features
1. User sign up and authentication
2. Real-time location tracking using the Geolocation API
3. Customizable range for location tracking
4. Chatting functionality through Django Channels and websockets
5. The conversation is saved in the database. 

## Requirements
1. Django
2. Django Channels
3. Geolocation

## Usage
1. Sign up for an account on the app
2. Allow the app to access your location
3. You will be able to see the real-time location of other users on the chat page
4. Click on a user's tab to start chatting with them

## Installation
1. Clone this repository to your local machine
2. Install the required packages by running `pip install -r requirements.txt`
3. Run migrations by running `python manage.py makemigrations` and `python manage.py migrate` 
/ `python manage.py migrate --run-syncdb`
4. Run the development server by running `python manage.py runserver`

## Installation with Docker
1.todo

## Thoughts
*
