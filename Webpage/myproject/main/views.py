from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from .models import Demo
from django import template

def showhome(request):
    img = Demo.objects.all() # 이미지만 못가져올까
    cluster_img = []    
    for i in range(len(img)):
        cluster_img.append(Demo.objects.filter(clustering=i).first())
    return render(request, 'main/01_inflow_page.html', {'imgs':img, 'cluster_imgs':cluster_img})

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

def showcluster(request):
    # data = []
    # length = ['0','1','2','3','4']
    # for i in length:
    #     val = Demo.objects.filter(clustering=i)
    #     data.append(val)
    #     continue
    data = Demo.objects.all()
    return render(request, 'main/01_inflow_page.html', {'cluster_imgs' : data})