from django.urls import path
from . import views

urlpatterns = {
    path('', views.home_page_view, name="base"),
    path('home/', views.home_page_view, name='home'),
    path('home1/', views.home1_page_view, name='home1'),
    path('home2/', views.home2_page_view, name='home2'),

}
