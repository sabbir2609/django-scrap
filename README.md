# Django Scrap

## Description

Django Scrap is a web application that allows multiple users to register and authenticate using unique API keys. Users can scrape email addresses from provided URLs and track their request history. Optional rate limiting can be implemented to prevent abuse of the service.

## Features

1. **User Registration & Authentication**:
    - Multiple users can register and will be assigned unique API keys.
    - The API key will be used to authenticate users when they make requests.

2. **URL Scraping Endpoint**:
    - Users can call an API endpoint, providing a URL.
    - The system will scrape the provided URL and return all email addresses found on that webpage.

3. **History Tracking**:
    - Each user can view their past requests, including the URLs they have previously submitted for scraping.

4. **Rate Limiting (Optional)**:
    - Limit the number of requests a user can make within a given timeframe to prevent abuse of the service.

## Used Packages

- `django`
- `djangorestframework`
- `djangorestframework-api-key`
- `"celery[redis]"`
- `selenium`
- `webdriver_manager`
- `python-dotenv`

## Commands

- To start the server:
  ```sh
  python manage.py runserver
  ```

- To start Celery:
  ```sh
  python -m celery -A core worker -l info -E -P threads
  ```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/django-scrap.git
    cd django-scrap
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory and add your environment variables.

5. Run database migrations:
    ```sh
    python manage.py migrate
    ```

6. Start the server and Celery worker:
    ```sh
    python manage.py runserver
    python -m celery -A core worker -l info -E -P threads
    ```

## Usage

1. Register a new user to get a unique API key.
2. Use the API key to authenticate your requests.
3. Call the URL scraping endpoint with the URL you want to scrape.
4. View your request history to see previously submitted URLs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contact

For any inquiries, please contact [sabbirhasan2999@gmail.com](mailto:sabbirhasan2999@gmail.com).
