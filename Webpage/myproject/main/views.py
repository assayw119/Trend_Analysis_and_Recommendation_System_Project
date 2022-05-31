from gettext import GNUTranslations
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from .models import Data
from django import template
from .forms import RestaurantForm

def showhome(request):
    img = Data.objects.all() # 이미지만 못가져올까
    cluster_img = []    
    for i in range(len(img)):
        cluster_img.append(Data.objects.filter(cluster=i).first())
    return render(request, 'main/01_inflow_page.html', {'imgs':img, 'cluster_imgs':cluster_img})

def showresultall(request):
    # sql = 'select * from demo'
    # database = Database()
    # data = database.executeAll(sql)
    # restaurant = pd.DataFrame(data)
    # print(restaurant['name'])
    restaurant = Data.objects.all().order_by('-total_score','-review_score')

    if request.method=='GET':
        sido = request.GET.get('sido')
        sigugun = request.GET.get('sigugun')
        # dong = request.GET.get('dong')
        img = request.GET.get('inner_img')
        food = int(request.GET.get('food'))
        address = int(str(sido) + str(sigugun))
        context = {
            'sido':sido,
            'sigugun':sigugun,
            # 'dong':dong,
            'image':img,
            'food':food,
            'restaurant':restaurant,
            'address':address
        }

    return render(request, 'main/02_result_page.html', context)

def showdetail(request,id):
    restaurant = get_object_or_404(Data, pk=id)
    return render(request, 'main/03_detail_page.html', {'restaurant':restaurant})

# def category(request):
#     if request.method=='GET':
#         sido = request.GET.get('sido')
#         sigugun = request.GET.get('sigugun')
#         img = request.GET.get('inner_img')
#         food = request.GET.get('food')

#         restaurant = RestaurantForm()
#         restaurant.sido = sido
#         restaurant.sigugun = sigugun
#         restaurant.img = img
#         restaurant.food = food
#         # restaurant.save()
#         context = {
#             'sido':sido,
#             'sigugun':sigugun,
#             'image':img,
#             'food':food
#         }
#         return render(request, '02_result_page.html', context)


# def address(request):
#     if request.method == 'GET':
#         sido = request.GET.get('sido')
#         sigugun = request.GET.get('sigugun')
#         dong = request.GET.get('dong')
#         return redirect('main/02_result_page.html', {'sido':sido, 'sigugun':sigugun, 'dong':dong'})