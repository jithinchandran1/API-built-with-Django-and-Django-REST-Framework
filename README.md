
---

# API built with Django and Django REST Framework

This is a simple Django-based REST API that allows you to manage a list of students. You can view all students and add new students through this API.

## Features

- View a list of all students
- Add new students
- Each student has a name, address, and phone number

## Technologies Used

- Django: A popular Python web framework
- Django REST Framework: To build RESTful APIs
- SQLite: Lightweight database for data storage

## How to Use

### Prerequisites

Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd <your-project-folder>
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   The server will start at `http://127.0.0.1:8000/`.

### Using the API

- **Get list of students**

  Send a GET request to:

  ```
  http://127.0.0.1:8000/
  ```

- **Add a new student**

  Send a POST request with JSON data, for example:

  ```json
  {
    "name": "John Doe",
    "address": "123 Main St",
    "phone": "1234567890"
  }
  ```

  To the same URL `http://127.0.0.1:8000/`.

## Project Structure

- `models.py`: Defines the Student data model
- `serializers.py`: Converts data to/from JSON format
- `views.py`: Handles API requests
- `urls.py`: Routes URLs to views
- `admin.py`: Registers the Student model for admin panel

## Future Improvements

- Add update and delete functionalities
- Implement user authentication
- Enhance data validation

## Contact

For questions or suggestions, feel free to reach out jithinchandran527@gmail.com .

---
