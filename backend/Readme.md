# Django4 Project

## Overview
This is a Django 5.1.4 backend project that powers an interview simulation platform. It provides REST APIs for authentication, interview management, and resume handling.

## Features
- User authentication
- Interview simulation with audio/video recording
- Resume upload and management
- REST API endpoints
- PostgreSQL database
- Media file handling

## Setup Instructions
1. Extract the zipped project to your desired location
2. Navigate to the Django4 directory:

   cd path/to/extracted/backend 

3. Create a virtual environment:

   - Windows: python -m venv venv
   - macOS/Linux: python3 -m venv venv

4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

5. Install dependencies:

   pip install -r requirements.txt


## Configuration
1. Create a `.env` file in the `django4/` directory with the following variables:

   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   DJ_Gem =Your Gemini API Key
   DG_API_KEY =Your Deepgram API key

## Migrations 

1. Run the following commands to create and apply database migrations:
 python manage.py makemigrations
 python manage.py migrate

## Add venv to interpreter path
Run command
pipenv --venv
get venv path and then enter it in interpreter path

## Running the Server

python manage.py runserver

## API Documentation
The API documentation can be accessed at `http://localhost:8000/swagger/` when the server is running.

## Directory Structure
```
django4/
├── authentification/    # Authentication app
├── common/               # Shared models and utilities
├── interview_simulation/ # Interview simulation logic
├── resumes/              # Resume management
├── django4/              # Project settings
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Dependencies
- Django 5.1.4
- Django REST Framework
- django-cors-headers
- psycopg2 (PostgreSQL adapter)
- python-decouple