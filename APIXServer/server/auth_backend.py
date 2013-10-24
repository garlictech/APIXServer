# The authentication method
# This is called by the standard Django login procedure
from django.contrib.auth.models import User as DjangoUser
from models import User as AvisUser
import time

import sys
class AuthBackend:
    def authenticate(self, username=None, password=None):
        print >>sys.stderr, "IN BACKEND"
        print >>sys.stderr, username
        if AvisUser.isAuthenticated(username, password):
            try:
                # Check if the user exists in Django's local database
                DjangoUser.objects.get(username=username)
            except DjangoUser.DoesNotExist:
                # Create a user in Django's local database
                return DjangoUser.objects.create_user(time.time(), username, 'passworddoesntmatter', is_staff=True, is_Active=True,
                    is_superuser=False)
        else:
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        print >>sys.stderr, "IN BACKEND"
        try:
            return DjangoUser.objects.get(pk=user_id)
        except DjangoUser.DoesNotExist:
            return None
