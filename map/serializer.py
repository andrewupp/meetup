from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    user_id =serializers.CharField(max_length=20)
    lat = serializers.DecimalField(max_digits=10, decimal_places=7)
    long = serializers.DecimalField(max_digits=10, decimal_places=7)
    last_updated = serializers.DateTimeField()
