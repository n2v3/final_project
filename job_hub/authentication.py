from django.contrib.auth.models import User
from rest_framework import authentication


class MyCustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        get_params = request.query_params

        try:
            # Retrieve the user with the username 'natali'
            user = User.objects.get(username="natali")

            # Check the condition
            if get_params.get("password") == "zxcv1234":
                # If condition is met,
                # return the user and no credentials
                return user, None
            else:
                # If condition is not met,
                # return None to indicate authentication failure
                return None, None
        except User.DoesNotExist:
            # If the user does not exist,
            # return None to indicate authentication failure
            return None, None
