from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
  features = Feature.objects.all()
  return render(request, 'index.html', {'features': features})


# def form(request):
#   return render(request, 'form.html')

def counter(request):
  text = request.POST['text']
  number_of_words = len(text.split())
  return render(request, 'counter.html', {'amount': number_of_words})

def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email already used.')
        return redirect('register')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username already used.')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save();
        return redirect('login')
    else:
      messages.info(request, 'Password not the same')
      return redirect('register')
  else:
    return render(request, 'register.html')


# examples used during the course
# def index(request):
  # feature1 = Feature()
  # feature1.id = 0
  # feature1.name = 'Fast'
  # feature1.is_true = True
  # feature1.details = 'Our service is very quick'

  # feature2 = Feature()
  # feature2.id = 1
  # feature2.name = 'cool'
  # feature2.is_true = False
  # feature2.details = 'We do cool things'

  # feature3 = Feature()
  # feature3.id = 2
  # feature3.name = 'Nice'
  # feature3.is_true = True
  # feature3.details = 'We have nice pancakes'

  # feature4 = Feature()
  # feature4.id = 3
  # feature4.name = 'dope'
  # feature4.is_true = False
  # feature4.details = 'Another way of being cool'

  # features = [feature1, feature2, feature3, feature4]
  # for feature in features:
  #   pass
  # return render(request, 'index.html', {'feature': feature1, 'feature2':feature2, 'feature3':feature3,'feature4':feature4})