from django.shortcuts import render, get_object_or_404, redirect
from .models import Demo
from django import template

def showhome(request):
    img = Demo.objects.all() # 이미지만 못가져올까
    return render(request, 'main/01_inflow_page.html', {'imgs':img})

def showresult(request):
    # sql = 'select * from demo'
    # database = Database()
    # data = database.executeAll(sql)
    # restaurant = pd.DataFrame(data)
    # print(restaurant['name'])
    restaurant = Demo.objects.all()

    return render(request, 'main/02_result_page.html', {'restaurant':restaurant})

def showdetail(request):
    return render(request, 'main/03_detail_page.html')


