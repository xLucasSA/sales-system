from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

def login_view(request):

    if request.method == "GET":
        return render(request, 'login.html')
    
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('vendas')  
         
        else:
            return render(request, "login.html", context={"mensagem":"Login ou senha incorreta"}) 