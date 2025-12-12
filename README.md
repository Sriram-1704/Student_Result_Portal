# 🎓 Student Result Portal 

A complete Django-based web application to manage students, subjects, marks, and generate results with grades.  

Includes authentication, admin workflows, clean UI, and MySQL database integration.

---

## 📁 Project Folder Structure

StudentResultProject/

├── manage.py

├── requirements.txt

├── StudentResultProject/

│ ├── init.py

│ ├── settings.py # Django settings with MySQL config

│ ├── urls.py # Main URL routing

│ ├── wsgi.py

│ └── asgi.py

└── resultapp/ # Core App

├── migrations/ # Database migrations

├── static/

│ └── resultapp/

│ ├── css/

│ │ └── style.css # Custom CSS with background

│ └── images/

│ ├── background.jpg # Background image

│ └── logo.png # School logo

├── templates/

│ └── resultapp/

│ ├── base.html # Main layout with navbar

│ ├── home.html # Dashboard

│ ├── login.html # Login form

│ ├── register.html # Registration page

│ ├── student_list.html # Students table

│ ├── add_student.html # Add student form

│ ├── add_marks.html # Add marks form

│ └── view_result.html # Results with grades

├── init.py

├── admin.py # Admin model registration

├── apps.py

├── forms.py # ModelForms for students/marks

├── models.py # Student, Subject, Result models

├── urls.py # App URLs

└── views.py # Views for all pages

🚀 Features

User Authentication: Secure login/register for teachers/admins using Django's built-in auth.

Student Management: Add, list, and view students by name, roll number, class, section, and DOB.

Marks Entry: Add subject-wise marks (obtained/max) for individual students.

Result Viewing: Detailed results with totals, percentages, and grades (A+ to F).

Dashboard: Home page with stats (total students/subjects).

Admin Panel: Full Django admin for subjects and data management.

Responsive Design: Mobile-friendly with glassmorphism cards and academic-themed background.

Database: MySQL integration for production-ready storage.

🛠️ Tech Stack

Backend: Django 4.0+ (Python 3.8+)

Database: MySQL 8.0+ (with mysqlclient)

Frontend: HTML5, CSS3 (Poppins font, glassmorphism), Bootstrap-inspired responsive design

Images: Unsplash (background), Icons8 (logo)

Deployment Ready: Static/media file handling

📦 Prerequisites

Python 3.8+

MySQL Server 8.0+

Git (for cloning)

🚀 Quick Start

1. Clone the Repository

Bashgit clone https://github.com/Sriram-1704/Student_Result_Portal.git

cd Student_Result_Portal

2. Set Up Virtual Environment

Bashpython -m venv venv

Windows

venv\Scripts\activate

macOS/Linux

source venv/bin/activate

3. Install Dependencies

Bashpip install -r requirements.txt

4. Configure MySQL Database

Install MySQL: Download from mysql.com

Create database & user:SQLCREATE DATABASE student_result_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE USER 'resultuser'@'localhost' IDENTIFIED BY 'Result@123';

GRANT ALL PRIVILEGES ON student_result_db.* TO 'resultuser'@'localhost';

FLUSH PRIVILEGES;

Update settings.py if needed (default: host='localhost', port='3306').

5. Run Migrations & Create Superuser

Bashpython manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser  # Username: sriram, Password: 123

6. Add Initial Data

Visit /admin/ → Login → Add subjects (e.g., Maths, Science, English).

7. Start the Server

Bash: python manage.py runserver

Open: http://127.0.0.1:8000/

Register/Login → Start adding students!

👨‍💻 Author

Sriram

Email: sriramsattiraju2003@gmail.com

GitHub: https://github.com/Sriram-1704

LinkedIn: https://www.linkedin.com/in/sri-ram-sattiraju-028349211
