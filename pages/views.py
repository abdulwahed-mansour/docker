from django.shortcuts import render

from pages import views



def home(request):
    
    context = {
            }

    return render(request, 'sign-in/index.html', context)