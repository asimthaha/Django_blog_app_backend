from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddModel
        fields=(
            'name','image','email','password'
        )