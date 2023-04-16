# Sleeksites.in-Flask-Internship-


# Making two template

Flask is a web framework for Python that allows you to build web applications quickly and easily. One of the features of Flask is the ability to use templates to generate HTML dynamically.

In this context, creating two templates refers to creating two HTML files that Flask will use to render different pages of a web application. For example, you might create a "login.html" template that contains a login form, and a "secret.html" template that contains a secret page that is only accessible to logged-in users.


Here's what the code does:
1. It defines a Flask application and sets a secret key for session management.
2. The `index()` function checks if the user is logged in by checking if the "username" key is in the session. If the user is logged in, it redirects them to the secret page. If the user is not logged in, it redirects them to the login page.
3. The `login()` function handles both GET and POST requests to the login page. If the request method is POST, it checks if the credentials are valid (in this case, the username must be "admin" and the password must be "password"). If the credentials are valid, it sets the "username" key in the session and redirects the user to the secret page. If the credentials are invalid, it renders the login template with an error message. If the request method is GET, it just renders the login template.
4. The `secret()` function checks if the user is logged in by checking if the "username" key is in the session. If the user is logged in, it renders the secret template. If the user is not logged in, it redirects them to the login page.
5. The `logout()` function removes the "username" key from the session and redirects the user to the login page.

To run this code, you need to create two templates: `login.html` and `secret.html`
