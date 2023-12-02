# form  لتحويل البيانات إلى  json
from rest_framework import serializers
from .models import Book


class Bookserializers(serializers.ModelSerializer):
    author=serializers.StringRelatedField()
    class Meta:
        model=Book
        fields='__all__'