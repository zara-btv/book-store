from rest_framework import serializers
from Book.models import Books
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):

    # def to_internal_value(self, data):
    #     print(data)
    #     result = super().to_internal_value(data=data)
    #     print(result)
    #     return data

    # def validate(self, attrs):
    #     pass
    # def to_representation(self, instance):
    #     pass
    class Meta:
        model = Books
        fields = "__all__"