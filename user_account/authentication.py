from django.contrib.auth.models import User

class EmailBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
                return None
        except:
            return User.DoesNotExist
    def get_user(selfself, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except:
            return None