from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.response import Response
from rest_framework.decorators import api_view

class RegisterViewSet(CreateModelMixin, GenericViewSet):
    class Temp(ModelSerializer):
        class Meta:
            model = User
            fields = ['username', 'password']

        def create(self, data):
            user = User(username = data.get('username'))
            user.set_password(data.get('password'))
            user.save()
            return user

    queryset = User.objects.all()
    serializer_class = Temp
