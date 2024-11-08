import requests
from django.conf import settings
from rest_framework import serializers
from .models import Cat

class CatSerializer(serializers.ModelSerializer):
    def validate_breed(self, value):
        response = requests.get("https://api.thecatapi.com/v1/breeds", headers={"x-api-key": 'live_AwGEI91fqYGFD5hBsVaUcbkZvC4UBCkoBnY2u51J5GLhS2PWXFAODFeQFrLfP8UU'})
        breeds = [breed['name'] for breed in response.json()]
        if value not in breeds:
            raise serializers.ValidationError("Invalid breed specified.")
        return value

    class Meta:
        model = Cat
        fields = ['id', 'name', 'years_of_experience', 'breed', 'salary']