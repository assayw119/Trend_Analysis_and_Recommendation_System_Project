from gettext import GNUTranslations
import re
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from sqlalchemy import null
from .models import Data
from django import template
from .forms import RestaurantForm
from django.contrib.auth.models import User

def showhome(request):
    cluster_img = []  
    for i in range(5):
        cluster_img.append(Data.objects.filter(cluster=i).first())
    return render(request, 'main/01_inflow_page.html', {'cluster_imgs':cluster_img})

def showresultall(request):

    if request.method=='GET':
        sido = request.GET.get('sido')
        sigugun = request.GET.get('sigugun')
        img = request.GET.get('inner_img')
        food = request.GET.get('food')
        
        if sigugun == '':
            address = ''
            restaurant_address = Data.objects.all()
        else:
            address = int(str(sido) + str(sigugun))
            restaurant_address = Data.objects.filter(region_code = address)
        if food == '전체':
            restaurant_food = Data.objects.all()
        else:
            restaurant_food = Data.objects.filter(category = int(food))
        if img == None:
            restaurant_img = Data.objects.all()
        else:
            restaurant_img = Data.objects.filter(cluster = int(img))
        
        restaurant = (restaurant_address & restaurant_food & restaurant_img).order_by('-total_score','-review_score')
        
        context = {'restaurant':restaurant}
        return render(request, 'main/02_result_page.html', context)

# def sort(request, data):
#     restaurant = get_object_or_404(Data, pk=)
#     print(data)





def showdetail(request,id):
    restaurant = get_object_or_404(Data, pk=id)
    return render(request, 'main/03_detail_page.html', {'restaurant':restaurant})

# def sortresult(request):
#     if request.method == "GET":
#         sort = request.GET.get('sort')
#         print(sort)
#         name = request.GET.get('name')
#         address = request.GET.get('address')
#         restaurant_sort = Data.objects.filter(name=name, address=address).order_by('-{}'.format(sort))
#         return render(request, 'main/02_result_page.html', {'restaurant': restaurant_sort})
