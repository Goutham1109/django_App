from django.urls import path,include
from . import views

app_name='blog'
urlpatterns = [

    path('', views.all_blog, name='bloghome'),
    path('<int:id>/', views.blogDetail,name='blogDetail'),

]
