# BlogAPI

This Django web application provides user authentication and content management features. It includes endpoints for user login, registration, password management, and post creation and manipulation.

## Features

- **User Authentication:** Secure login, logout, and signup with email verification.
- **Password Management:** Password change, reset, and confirmation.
- **User Management:** Retrieve and update user details.
- **Content Management:** Create, update, delete, and retrieve posts.

## Getting Started

### Prerequisites

- Python 3.6+
- Django 3.0+
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/IAmKushagraSharma/BlogAPI.git
   cd BlogAPI
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### Usage

1. **Access the application:**
   Open your browser and navigate to `http://localhost:8000`.

2. **User Registration:**

   - Go to the signup page and create a new account.
   - Verify your email through the verification link sent to your email.

3. **Login:**

   - Use your registered email and password to log in.

4. **Create a Post:**
   - Once logged in, navigate to the posts section.
   - Create, edit, or delete posts as needed.

### API Endpoints

- **Authentication:**

  - `POST /api/v1/auth/login/` - Login user
  - `POST /api/v1/auth/logout/` - Logout user
  - `POST /api/v1/auth/signup/` - Register user
  - `POST /api/v1/auth/password/change/` - Change password
  - `POST /api/v1/auth/password/reset/` - Reset password
  - `POST /api/v1/auth/password/reset/confirm/` - Confirm password reset

- **User Management:**

  - `GET /api/v1/auth/user/` - Get user details
  - `PUT /api/v1/auth/user/` - Update user details
  - `PATCH /api/v1/auth/user/` - Partially update user details

- **Posts:**
  - `GET /api/v1/posts/` - List all posts
  - `POST /api/v1/posts/` - Create a new post
  - `GET /api/v1/posts/{id}/` - Retrieve a specific post
  - `PUT /api/v1/posts/{id}/` - Update a specific post
  - `PATCH /api/v1/posts/{id}/` - Partially update a specific post
  - `DELETE /api/v1/posts/{id}/` - Delete a specific post

## Deployment

1. **Collect static files:**

   ```bash
   python manage.py collectstatic
   ```

2. **Run the application in production:**
   Use a production server like Gunicorn with Nginx.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgments

- Thanks to the Django community for their continuous support and contributions.
