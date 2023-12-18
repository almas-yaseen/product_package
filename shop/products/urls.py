from django.urls import path 
from .import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('ship/',views.ship,name='ship'),
    path('single_product/<str:id>/',views.single_product,name='single_product'),
    path('user_logout/',views.user_logout,name='user_logout'),
]
