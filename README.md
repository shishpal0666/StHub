# StHub - Student Hub

StHub is a comprehensive web application designed to help students manage their academic and extracurricular activities efficiently. The platform allows students to create profiles, upload and scan their college ID cards, track academic progress, manage notes, projects, external courses, and even build resumes. It aims to be a one-stop solution for students to organize and streamline their academic life.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

### User Management
- **Login/Register**: Secure authentication with profile creation.
- **Profile Creation**: Upload and scan college ID cards to auto-fill profile information.
- **Personal Information**: Manage details like name, contact information, college, program, and course duration.

### Academic Management
- **Past Semester Results**: Upload and scan results to auto-fill academic details such as subjects, labs, credits, SGPA, and CGPA.
- **Current Semester Management**: Manage subjects, labs, expected SGPA, and CGPA.
- **Notes, References, Lab Work, and Assignments**: Subject-wise management for both past and current semesters.
- **Time Table Management**: Upload and scan time tables, generate alerts for reschedules.

### Projects and External Courses
- **Projects**: Add academic or personal projects, along with descriptions, skills used, URLs, and GitHub repositories.
- **External Courses and Certifications**: Manage additional courses, certifications, and skills.

### Resume and Target Works
- **Resume Management**: Upload existing resumes, calculate ATS scores, and build new resumes from templates.
- **Target Works**: Schedule work, track progress, and manage academic and extracurricular goals.

### CGPA Calculator
- **CGPA Calculation**: Calculate CGPA based on SGPA from past semesters.

## Technologies Used
- **Backend**: Flask, Flask-SQLAlchemy, Flask-WTF, Flask-Login, psycopg2, Gunicorn
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript, Jinja2
- **Database**: PostgreSQL, pgAdmin
- **Image Processing**: TensorFlow.js, Tesseract.js

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/sthub.git
    cd sthub
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**:
    - Ensure PostgreSQL is installed and running.
    - Create a database for the project:
    ```sql
    CREATE DATABASE sthub_db;
    ```
    - Configure the database URI in the `.env` file.

5. **Run Migrations**:
    ```bash
    flask db upgrade
    ```

6. **Run the Application**:
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Register/Login**: Start by registering an account or logging in if you already have one.
2. **Profile Creation**: Upload your college ID card to create your profile.
3. **Manage Academics**: Add past semester results, current semester subjects, and more.
4. **Project Management**: Add and update your projects and external courses.
5. **Resume Building**: Use the built-in resume builder to create or update your resume.
6. **Track Target Works**: Set goals and track progress with the Target Works feature.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

