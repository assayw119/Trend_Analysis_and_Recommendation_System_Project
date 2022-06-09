from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', showhome, name='showhome'),
    path('resultall/', showresultall, name='showresultall'),
    path('result/<str:id>', showdetail, name='showdetail'),
    # path('sort/', showsort, name='showsort'),

]