from django.contrib.auth import get_user_model
from django.db.models import Q

class PhoneAuthenticationBackend:
    
    def authenticate(self, request, phone=None, password=None):
        custom_user = get_user_model()
        try:
            user = custom_user.objects.get(
                phone=phone
            )
            pwd_valid = user.check_password(password)
            if pwd_valid:
                return user
            return None
        except custom_user.DoesNotExist:
            return None

    def get_user(self, user_id):
        custom_user = get_user_model()
        try:
            return custom_user.objects.get(pk=user_id)
        except custom_user.DoesNotExist:
            return None
