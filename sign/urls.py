from django.urls import path
from . import views
urlpatterns = [
    path('about',views.about,name='about'),
    path('',views.index,name='index'),
    path('sign',views.sign,name='sign'),
    path('login',views.login_view,name='login'),
    path('cart',views.cart,name='cart'),
    
]