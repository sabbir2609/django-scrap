from rest_framework.throttling import SimpleRateThrottle

class ConcurrencyThrottleApiKey(SimpleRateThrottle):
    scope = 'api_key_concurrency'

    def get_rate(self):
        # Return the custom rate directly in the class (e.g., 1 request per minute)
        return '1/minute'

    def get_cache_key(self, request, view):
        # Extract API key from headers (or any other identifier, e.g., API key)
        auth_header = request.headers.get('Authorization', '').split(" ")[1]
        if not auth_header:
            return None
        return f"rate_limit_api_key_{auth_header}"
