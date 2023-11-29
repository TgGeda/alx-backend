# 0x02-i18n Backend Specialization Project

## Description
This project focuses on developing a Flask application with internationalization support using Flask Babel. The application includes features such as language detection, user authentication, and displaying the current time with the appropriate time zone. The project is divided into several tasks, each addressing a specific aspect of the application.

## Installation
1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the project dependencies by running `pip install -r requirements.txt`.
4. Set up the database by running the necessary migrations and creating the user table.

## Task List
1. **Task 0: Basic Flask App**
   - Create a basic Flask app with a single route ("/") and an index.html template that displays "Welcome to Holberton" as the page title and "Hello world" as the header.

2. **Task 1: Basic Babel Setup**
   - Install the Flask Babel extension and instantiate the Babel object in the app.
   - Create a Config class with a LANGUAGES attribute set to ["en", "fr"] to define the available languages.
   - Set the default locale to "en" and the timezone to "UTC" using the Config class.

3. **Task 2: Get Locale from Request**
   - Implement a get_locale function with the babel.localeselector decorator to determine the best match for the supported languages based on the request's accept languages.

4. **Task 3: Parametrize Templates**
   - Use the _ or gettext function to parametrize templates, utilizing the message IDs home_title and home_header.
   - Create a babel.cfg file to configure the translations in Python and Jinja2 templates.
   - Initialize translations and dictionaries for English and French languages.
   - Provide translations for the message IDs in the translations files.
   - Compile the translations for use in the app.

5. **Task 4: Force Locale with URL Parameter**
   - Implement a mechanism to force a specific locale by passing the locale=fr parameter in the app's URLs.
   - Modify the get_locale function to detect the locale argument in the request and return it if it is a supported locale.

6. **Task 5: Mock Logging In**
   - Create a user table to emulate a user login system.
   - Define a get_user function to retrieve user information based on the provided user ID.
   - Implement a before_request function to be executed before other functions, which sets the logged-in user as a global variable.
   - Display a welcome message in the HTML template if a user is logged in.

7. **Task 6: Use User Locale**
   - Modify the get_locale function to prioritize a user's preferred locale if available.
   - The order of priority is: locale from URL parameters, locale from user settings, locale from request header, default locale.

8. **Task 7: Infer Appropriate Time Zone**
   - Define a get_timezone function and use the babel.timezoneselector decorator.
   - The function determines the time zone based on URL parameters, user settings, or defaults to UTC.
   - Validate the time zone by using pytz.timezone and handling the pytz.exceptions.UnknownTimeZoneError exception.

9. **Task 8: Display the Current Time (Advanced)**
   - Display the current time on the home page based on the inferred time zone.
   - The time is displayed in the default format, with translations provided for English and French.

## Usage
1. Start the Flask server by running `flask run`.
2. Access the application in your browser at `http://localhost:5000`.
3. Explore the different features of the application, such as language detection, user authentication, and displaying the current time with the appropriate time zone.

## Contributing
This project is not open to external contributions at the moment.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact Information
For any inquiries or feedback, please contact [Birhan Abuhay] at [burahabtam@gmail.com].
