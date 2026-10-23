SkillHunt — Full-Stack Job Portal

SkillHunt is a full-stack job portal built using Python and Django that connects job seekers with companies. The application includes separate candidate and company interfaces, an admin panel, authentication, and OTP-based registration verification.

Features

- Candidate Portal: A dedicated interface for job seekers.
- Company Portal: A separate interface for companies.
- Admin Panel: Administrative interface for managing the application.
- Authentication: User authentication system.
- OTP Verification: OTP-based registration verification.
- Database Integration: MySQL database support.

Tech Stack

- Backend: Python, Django
- Frontend: HTML, CSS, JavaScript
- Database: MySQL
- Version Control: Git and GitHub

Project Structure

The project includes the following main components:

- "jobapp/" — Main application
- "jproject/" — Django project configuration
- "manage.py" — Django management utility
- "README.md" — Project documentation

Getting Started

Prerequisites

- Python
- pip
- MySQL Server
- Git

1. Clone the repository

git clone https://github.com/UdaiV/FullStack_jobportal.git
cd FullStack_jobportal

2. Create and activate a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

3. Install dependencies

If the project contains a "requirements.txt" file:

pip install -r requirements.txt

If it does not, create one from the dependencies actually used by the project before following this step.

4. Configure the database

Configure MySQL and update the Django database settings to match your local environment. Do not commit database passwords or other secrets to GitHub.

5. Apply migrations

python manage.py migrate

6. Start the development server

python manage.py runserver

Open "http://127.0.0.1:8000/" in your browser.

Future Improvements

- Automated tests for core workflows
- Improved validation and error handling
- API development using Django REST Framework
- Deployment and continuous integration

Author

Udai

GitHub: "UdaiV" (https://github.com/UdaiV)
