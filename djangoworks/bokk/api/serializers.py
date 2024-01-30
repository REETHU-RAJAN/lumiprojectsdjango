from rest_framework import serializers

from api.models import bokks


class BooksSerializer(serializers.ModelSerializer):

    id=serializers.CharField(read_only=True)

    

    class Meta:
        model=bokks
        fields="__all__"

