# Smart Meeting Insights Assistant (S.M.I.A.)
Smart Meeting Insights Assistant (S.M.I.A.) is an innovative application designed to provide powerful insights, video recording, translation, and real-time analysis of virtual meetings. It integrates with platforms like Google Meet, Zoom, and Slack to offer rich functionalities that improve meeting productivity and collaboration. The application leverages AI for various capabilities like transcription, insights generation, and translation.

# Technologies Used
* Backend: Django (Python)
* Frontend: Next.js (TypeScript)
* Database: MySQL
* APIs:
OpenAI (for AI models and insights)
Zoom API (for Zoom integration)
Google Meet API (for Meet integration)
Slack API (for Slack integration)
Translation API (for real-time translation)
Project Structure
This repository is divided into two main sections:

# Backend (/backend):
Django-based project for handling all business logic, database models, API endpoints, and integrations.
Integrates with Zoom, Google Meet, and Slack to fetch data and provide insights.

# Frontend (/frontend):
A Next.js (React) project responsible for the user interface and interacting with the backend.
Provides a dashboard, meeting insights, real-time translation, and video recording features.

# Setup Instructions
Prerequisites
1. Python (for the backend)
2. Node.js (for the frontend)
3. MySQL (for the database)
4. API Keys:
   1. OpenAI
   2. Zoom
   3. Slack
   4. Google Meet
   5. Translation API (if needed)


## Step 1: Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/parvinder204/smart-meeting-insights-assistant.git
cd smart-meeting-insights-assistant

## Step 2: Set Up the Backend
Navigate to the backend folder:

cd backend
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate (on Linux/Mac)
venv\Scripts\activate (on Windows)


Install the required Python dependencies:
pip install -r requirements.txt


Configure your .env file:

Run migrations to set up the database:
python manage.py migrate


# Step 3: Set Up the Frontend
Navigate to the frontend folder:
cd ../frontend

Install the required Node.js dependencies:
npm install

Configure your .env.local file (create it if it doesn't exist):

# Step 4: Running the Project
Run both the Django and Next.js servers using the run.py script in the root directory:
python run.py

# Step 5: Access the Application
The frontend will be available at: http://localhost:3000
The backend API will be available at: http://localhost:8000/api
You can now access the app in your browser and start using its features.

# Features
1. Real-Time Meeting Insights:
Integrates with Zoom, Google Meet, and Slack to fetch meeting data.
Uses OpenAI to generate insights from meeting discussions.
2. Video Recording:
Record meetings directly from the platform (e.g., Zoom, Google Meet) and store them for later review.
3. Real-Time Translation:
Translate meeting conversations into multiple languages using available translation APIs.
4. Speech-to-Text:
Convert speech to text using AI models for better insights and reporting.


# Development Notes
Make sure to keep your API keys secure. Never commit them to version control.
Follow the API documentation for Zoom, Google Meet, and Slack for integration details.
OpenAI API is used to generate insights and provide intelligent summaries from the meeting content.


# Contributing
Feel free to fork the repository and submit pull requests. Please ensure that your code adheres to the project’s coding style and includes appropriate tests.

# Contact
For more details or questions, contact the project maintainer at techpinda1214@gmail.com
