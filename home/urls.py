from home import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('pricing',views.pricing,name='pricing'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('why',views.why,name='why')

]