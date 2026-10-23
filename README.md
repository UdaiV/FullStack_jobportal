# SkillHunt — Full-Stack Job Portal

SkillHunt is a full-stack job portal built with Django and MySQL that provides separate interfaces for candidates and companies, along with an administrative panel.

The project includes user authentication and an OTP-based registration process.

## Features

- **Candidate Interface** — Candidate-facing section of the job portal.
- **Company Interface** — Dedicated section for companies.
- **Admin Panel** — Administrative interface for managing the application.
- **Authentication** — User authentication functionality.
- **OTP-Based Registration** — Registration process with OTP verification.

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL

## Project Structure

```text
FullStack_jobportal/
├── jobapp/
├── jproject/
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python
- MySQL Server
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/UdaiV/FullStack_jobportal.git
   cd FullStack_jobportal
   ```

2. Create and activate a virtual environment:

   **Windows:**

   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Configure the database settings in `jproject/settings.py` to match your local MySQL setup. Create the required database before running migrations.

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open `http://127.0.0.1:8000/` in your browser.

## Future Improvements

- Add automated tests for core application features.
- Improve configuration management using environment variables.
- Document API endpoints and application workflows.
- Add deployment instructions.

## Author

**Udai V**

GitHub: [UdaiV](https://github.com/UdaiV)
