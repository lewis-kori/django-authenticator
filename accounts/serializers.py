from djoser.serializers import UserCreateSerializer
from .models import User

class UserRegistrationSerializer(UserCreateSerializer):
    """
    Overrides djoser registration behavior to accept phone_number field on sign up
    """
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields = ('username','email','first_name','last_name','phone_number','password')