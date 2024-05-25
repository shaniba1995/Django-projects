from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model


class UserSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    def create(self,validated_data):
        user=get_user_model().objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=['username','password']

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields=['id','todo_name','todo_desc','date_created','completed']