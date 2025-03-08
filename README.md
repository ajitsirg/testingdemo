Chat Application
Django DRF WebSockets JWT

The Chat Application is a Django-based web application that allows users to register, log in, send messages, and create group chats. It uses JWT authentication, WebSockets for real-time communication, and provides interactive API documentation with Swagger UI.

Features
User Features
Registration & Authentication: Register, log in, and manage user profiles using JWT authentication.

Profile Management: Update user profile information (e.g., full name, avatar, bio).

Online/Offline Status: View the online/offline status of other users.

Messaging Features
Real-Time Messaging: Send and receive messages in real-time using WebSockets.

Message Editing: Edit messages within 5 minutes of sending.

Message Read Status: Mark messages as read.

Unread Message Counts: View unread message counts for users.

Group Chat Features
Group Chat Creation: Create and manage group chats.

Manage Group Members: Add or remove members from group chats.

Group Chat Messaging: Send and receive messages in group chats.

API Documentation
Interactive API: Swagger UI for interactive API documentation.

Technologies Used
Backend: Django, Django REST Framework (DRF)

Authentication: JWT (JSON Web Tokens)

Real-Time Communication: Django Channels, WebSockets

API Documentation: drf-yasg (Swagger)

Database: SQLite (default), PostgreSQL (optional for production)

Message Queue: Redis (for Channels)

Prerequisites
Before running the project, ensure you have the following installed:

Python 3.8 or higher

pip (Python package manager)

SQLite (default)

Setup Instructions
1. Clone the Repository
Clone the repository to your local machine:


https://github.com/ajitsirg/testingdemo.git
cd testingdemo
2. Create a Virtual Environment
Create and activate a virtual environment:

On Windows:


python -m venv venv
venv\Scripts\activate
On Mac/Linux:


python -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required Python packages:

pip install -r requirements.txt

4. Run Migrations
Apply the database migrations:


python manage.py makemigrations
python manage.py migrate
6. Create a Superuser
To access the Django admin panel, create a superuser:

python manage.py createsuperuser

7. Run the Development Server
Start the Django development server:

python manage.py runserver
The application will be available at http://localhost:8000/.

Accessing the API Documentation
Swagger UI: Visit http://localhost:8000/swagger/ to interact with the API documentation.

Using the Application
1. Register a New User
Send a POST request to /api/register/ with the following JSON data:

json
{
  "username": "your_username",
  "password": "your_password",
  "email": "your_email@example.com"
}
2. Log In
Send a POST request to /api/token/ with the following JSON data:

json
{
  "username": "your_username",
  "password": "your_password"
}
You will receive a JWT token in the response. Use this token to authenticate subsequent requests.

3. Send a Message
Send a POST request to /api/messages/ with the following JSON data:

json
{
  "receiver": "receiver_username",
  "content": "Hello, this is a test message!"
}
4. Create a Group Chat
Send a POST request to /api/groupchats/ with the following JSON data:

json

{
  "name": "My Group Chat",
  "members": ["user1", "user2"]
}
5. Real-Time Messaging
To send and receive messages in real-time, connect to the WebSocket endpoint at:

Copy
ws://localhost:8000/ws/chat/<room_name>/
