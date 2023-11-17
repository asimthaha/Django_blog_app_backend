from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogAddModel
        fields=(
            'userid','title','post'
        )