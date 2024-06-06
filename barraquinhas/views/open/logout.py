from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_veiw(request):
    logout(request)
    
    return redirect('index')