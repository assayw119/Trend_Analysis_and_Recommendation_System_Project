from django.shortcuts import render
from main.models import Data
from django.contrib.auth.models import User
# Create your views here.

# def mypage(request):
#     user = request.user
#     my_restaurant = Data.objects.filter(saver = user)
#     return render(request, 'users/mypage.html', {'my_restaurant':my_restaurant})
