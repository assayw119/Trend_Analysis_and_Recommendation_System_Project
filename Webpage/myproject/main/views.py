from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from .models import Demo
from django import template
from .forms import RestaurantForm

def showhome(request):
    img = Demo.objects.all() # 이미지만 못가져올까
    cluster_img = []    
    for i in range(len(img)):
        cluster_img.append(Demo.objects.filter(clustering=i).first())
    return render(request, 'main/01_inflow_page.html', {'imgs':img, 'cluster_imgs':cluster_img})

def showresultall(request):
    # sql = 'select * from demo'
    # database = Database()
    # data = database.executeAll(sql)
    # restaurant = pd.DataFrame(data)
    # print(restaurant['name'])
    restaurant = Demo.objects.all()

    return render(request, 'main/02_result_page.html', {'restaurant':restaurant})

def showdetail(request,id):
    restaurant = get_object_or_404(Demo, pk=id)
    return render(request, 'main/03_detail_page.html', {'restaurant':restaurant})

def category(request):
    if request.method=='GET':
        sido = request.GET.get('sido')
        sigugun = request.GET.get('sigugun')
        dong = request.GET.get('gun')
        img = request.GET.get('inner_img')
        food = request.GET.get('food')

        restaurant = RestaurantForm()
        restaurant.sido = sido
        restaurant.sigugun = sigugun
        restaurant.dong = dong
        restaurant.img = img
        restaurant.food = food
        restaurant.save()
        return redirect('main/02_result_page.html', restaurant)