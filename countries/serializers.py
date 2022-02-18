from rest_framework import serializers
from countries.models import 

class CountriesSerializer(serializers.ModelSerializer);

    class Meta:
            Model = Countries
            fields = ('id', 'name', 'capital')