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
│ ├── background.jpg # Academic background image
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
