from django.urls import path

from a3h1collegestore import views

app_name = 'a3h1collegestore'

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

]