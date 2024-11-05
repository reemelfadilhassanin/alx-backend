# Flask Internationalization (i18n) Project

This project demonstrates how to implement internationalization (i18n) in a Flask web application using the `Flask-Babel` extension. The objective is to parametrize templates to support multiple languages, detect locales based on user preferences, and localize timestamps in a Flask app.

## Learning Objectives

- Learn how to parametrize Flask templates to display content in different languages.
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers.
- Learn how to localize timestamps using the `pytz` library.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- Code should adhere to the PEP 8 style guide (version 2.5).
- All files must be executable Python scripts.
- Every file, class, function, and method must include documentation with clear explanations of their purpose.

## Setup Instructions

1. **Install the required dependencies**:

   Install the `Flask-Babel` extension using pip:

   ```bash
   pip3 install flask_babel==2.0.0
