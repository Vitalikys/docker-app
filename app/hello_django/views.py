from django.shortcuts import render

# https://django.fun/tutorials/dokerizaciya-django-s-pomoshyu-postgres-gunicorn-i-nginx/
def home(request):
    return render(request, 'index.html')
