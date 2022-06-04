from django.shortcuts import render, redirect
from django.contrib import auth


# Create your views here.
def login(request):
    # POST 요청 들어오면 로그인
    if request.method == 'POST':
        usr = request.POST['username']
        pwd = request.POST['password']
        # User 모델에 usr와 pwd가 일치하는 객체 있는지 확인
        # 있으면 해당 객체, 없으면 None 반환
        user = auth.authenticate(request, username=usr, password=pwd)

        if user is not None: # 유저가 존재할 경우
            auth.login(request, user)
            return redirect('main:showhome')
        else:
            # 만약 유저 없을경우 다시 로그인 화면으로
            return render(request, 'login.html')
    
    # GET 요청 들어오면 login form 담은 html 보여줌
    elif request.method == 'GET':
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main:showhome')