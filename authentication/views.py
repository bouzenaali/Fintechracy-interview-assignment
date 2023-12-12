from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import logout as auth_logout


# Home page
def index(request):
    if request.user.is_authenticated:
        return redirect('receipts:list')
    else:   
        return render(request, 'authentication/base.html')

# Sign up 
def signup(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'authentication/signup.html', {
        'form': form
    })

# Logout 
def logout(request):
    auth_logout(request)
    return redirect('authentication:login')
