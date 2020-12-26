from django.urls import path
from coders import views

app_name='urbancoder'

urlpatterns = [
        path('',views.home,name='home'),
        path('home',views.home,name='home'),
        path('contact',views.form,name='contact'),
        path('about.html',views.about,name='about'),
        path('graphic.html',views.graphic,name='graphic'),
        path('Digi.html',views.digi,name='digi'),
        path('Web.html',views.web,name='web'),
        path('base.css',views.base,name='base')
        
        
    
]