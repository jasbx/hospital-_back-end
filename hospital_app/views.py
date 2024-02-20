
from django.shortcuts import render

# Create your views here.

from .models import *
from .filter import Boking


from .models import LOGIN
    
def index(request):
    
        
    
    
        
    if request.method=='POST':
        
     
      x=request.POST.get('name')
      y=request.POST.get('number')
      z=request.POST.get('doctor')
      e=request.POST.get('age')
      f=request.POST.get('gender')
      h=request.POST.get('data')
      
     
      s=LOGIN(name1=x,number=y,doctor=z,age=e,gender=f,data=h)
     
      s.save()
     
    last={
     "item":LOGIN.objects.all()
    }
    
    return render(request,'index.html',context=last)
      
def nav(request):
    return render(request,'navbar.html')

def home(request):
    return render(request,'home.html')   


def serves(request):
    
    return render(request,'servec.html')
def blog(request):
    return   render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def doctor(request):
    return render(request,'doctor.html')
def foter(request):
    return render(request,'conect.html')

def card(request):
    return render(request,'card.html')


def admin(request):
    return render(request, 'admin.html'   )

# class Listv(ListView):
#     model=LOGIN
#     template_name='list.html'
#     context_object_name='items'

# def filter1(request):
#     if request.method=='POST':
#     # {filter}
#         boking=Boking()
#         context={
#             'boking':boking,
#             'item':LOGIN.objects.all()
#         }
#         return render (request,'filter.html',context=context)
#     return render (request,'filter.html')
# views.py
from django.shortcuts import render
from .models import LOGIN

def search_doctors(request):
    query = request.GET.get('q')
    if query:
        search_doctors = Search_doctors.objects.filter(name__icontains=query)
    else:
        search_doctors = Search_doctors.objects.all()
    
    return render(request, 'doctors_search.html', {'search_doctors': search_doctors, 'query': query})

