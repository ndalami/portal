from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def verified_member(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #redirect
            return redirect('userpages:home')

        else:
            #redirect
            messages.success(request,'There was an error login in, Try again latter!')
            return redirect('jobs:index_page')
    
    else:
        #
        return render(request,'verifieds/login_modal.html')

def logout_user(request):
    logout(request)
    return redirect('jobs:index_page')