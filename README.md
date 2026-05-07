# NaUKMA Faculty of Informatics Website

## Project Overview
This is a web application for the Faculty of Informatics at the National University of Kyiv-Mohyla Academy (NaUKMA). The platform provides information about academic departments, educational programs, teaching staff, and specific disciplines. It is designed to help students and visitors navigate the faculty's structure and academic offerings.

## Tech Stack
* **Framework:** Django
* **Database:** SQLite

## Features
* **Homepage Management:** Dynamic content for various sections (Faculty info, Programs, Teachers, International relations, and Contacts) managed via the `HomePageText` model.
* **Academic Departments:** Comprehensive list of departments with details about the department head and associated staff.
* **Educational Programs:** Detailed view of study programs, including program codes, descriptions, and coordinator information.
* **Faculty Directory:** Information about teachers, their positions, academic degrees, and department affiliations.
* **Curriculum Overview:** Information regarding disciplines associated with specific educational programs.

## Database Schema
The project uses the following relational structure:
* **Department:** Stores department names and their heads.
* **Teacher:** Contains profiles of teaching staff, linked to their respective departments.
* **Program:** Details academic programs, linked to a coordinator (Teacher) and a department.
* **Discipline:** Lists subjects taught within specific programs.
* **HomePageText:** A singleton-style model to manage the main page's textual content.

## How to run project

1. Create virtual env
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash
python manage.py migrate
```
4. Run the server
```bash
python manage.py runserver
```

## Endpoints

### Home
- `/` - homepage

### Programs
- `/programs/` - list of all programs
- `/programs/<int:id>/` - page of a program

### Departments
- `/departments/` - list of all departments
- `/departments/<int:id>/` - page of a department
