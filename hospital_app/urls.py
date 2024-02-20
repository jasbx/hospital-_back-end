from django.urls import path
# from .views import Listv
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.index,name='login'),
    path('servese',views.serves,name='serv'),
    path('blog',views.blog,name='blog'),
    path('about',views.about,name='about'),
    path('doctor',views.doctor,name='doctor'),
    path('conect',views.card,name='card'),
    path('admin',views.admin,name='admin'),
    path('filter',views.search_doctors,name='filter'),

    # path('list',Listv.as_view(),name='list')
    
    
    
   
]
