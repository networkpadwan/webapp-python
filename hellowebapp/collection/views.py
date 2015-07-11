from django.shortcuts import render

# Create your views here.
def index(request):
    #this the new view
    return render(request, 'index.html')

