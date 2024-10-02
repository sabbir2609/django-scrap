Features Implemented
====================

User Registration & API Key Generation
--------------------------------------

Users can register at ``/api/users/register/`` with a username, email, and password.
The system responds with the registered username and an API key, which is used for authentication in subsequent requests.

User Profile Retrieval & Update
-------------------------------

Users can retrieve their profile at ``/api/users/me/`` by providing the API key in the headers. The response includes the username, email, and other profile details.
Users can update their profile using a PATCH request to the same endpoint.

Scraping Endpoint
-----------------

Users can submit a URL for scraping at ``/api/main/scraped_data/``, and the system will create a new scraping task. The response confirms that the data is being processed.
Once processing is complete, users can view the results by requesting ``/api/main/scraped_data/<id>``.
History tracking is available, allowing users to see all past scraping requests at ``/api/main/scraped_data/``.

Rate Limiting
-------------

Users are limited to 10 requests per 30 minutes, preventing abuse of the service.