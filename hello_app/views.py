from django.shortcuts import render, HttpResponse

#hello-django-310602
def hello(request):
    return HttpResponse('Hello Everybody!')
