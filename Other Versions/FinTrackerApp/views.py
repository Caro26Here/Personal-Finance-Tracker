from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view()
def home(request):
    return Response('Hello World', status=status.HTTP_200_OK)
