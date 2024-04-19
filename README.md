# Blog Platform
Blog Platform is a web application built with Django that allows users to register, create, edit, and delete blog categories and posts. The project includes customizations such as changing the theme of the admin site using django-admin-interface and supports viewing the database entries using SQLiteOnline for ease of access.

![Home](https://github.com/maryam246/Blogs/assets/143519643/4293d2c0-7c0f-49f6-a47d-2a61f0d6b69a)


## Features
- User Registration: Users can create an account to access the platform.
- Category Management: Users can create, edit, and delete blog categories.
- Post Management: Users can create, edit, and delete blog posts within categories.
- Custom Admin Theme: The admin site features a customized theme for better user experience.
- SQLiteOnline: Database entries can be viewed and managed using SQLiteOnline for convenience.
## Requirements
To run this project, you'll need:

- Python 3.x
- Django (install using pip install django)
- Pillow (install using pip install pillow)
- django-admin-interface (install using pip install django-admin-interface)
- SQLiteOnline (optional for viewing database entries)
## Installation
Navigate to the project directory:

cd blog-platform
## Setup
1. Create a virtual environment (recommended):

python -m venv venv
2. Activate the virtual environment:
- On Windows:
 venv\Scripts\activate
- On macOS/Linux:
  source venv/bin/activate
3 Run migrations to set up the database:
- python manage.py migrate
4. Create a superuser for admin access:

- python manage.py createsuperuser
5. Start the development server:

- python manage.py runserver
6. Access the application in your web browser at **http://127.0.0.1:8000/home/**.
## Usage
1. Register a new user account or login with an existing account.
2. Create blog categories under the "Categories" section.
3. Create, edit, or delete blog posts within categories under the "Posts" section.
4. Manage your account and logout as needed.
5. Access the admin site at http://127.0.0.1:8000/admin/ to manage categories, posts, and users with the custom theme provided by django-admin-interface.
## Database Access
If you wish to view and manage database entries:

Install SQLiteOnline (https://sqliteonline.com/).
Open the db.sqlite3 file from the project directory using SQLiteOnline for easy database access.
## Media
- Screenshots
  ![login](https://github.com/maryam246/Blogs/assets/143519643/5b11c654-0da4-45f2-b64a-ff29cbe18b19)

![ad-interface](https://github.com/maryam246/Blogs/assets/143519643/07164fd7-1543-4b71-b8c7-840022311878)

![category](https://github.com/maryam246/Blogs/assets/143519643/e61bf963-0dfc-4716-b8d3-1f4e2f22aabc)

![p](https://github.com/maryam246/Blogs/assets/143519643/1f53cd17-69b3-48e4-846c-4c2e5893fc5e)

![Post](https://github.com/maryam246/Blogs/assets/143519643/29248200-934f-46bc-9da1-501f79fa936b)

Here is a short video showcasing the functionality of the Blog Platform:

