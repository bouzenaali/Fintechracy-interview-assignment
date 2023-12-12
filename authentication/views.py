from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import SignUpForm

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


def logout(request):
    logout(request)
    return redirect('recipes:index')
