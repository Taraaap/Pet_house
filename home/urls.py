from django.contrib import admin
from django.urls import path
from  home import views
urlpatterns = [
    path ("",views.index,name='home'),
    path ("service",views.service,name='service'),
    path ("contact",views.contact,name='contact'),
    path ("product",views.product,name='product'),
    path ("cart",views.cart,name='cart'),
    path("login/", views.login_view, name="login"),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),
    path("add-to-cart/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("update-cart/<int:id>/", views.update_cart, name="update_cart"),
    path("remove-from-cart/<int:id>/", views.remove_from_cart, name="remove_from_cart"),
    path('checkout/', views.checkout, name='checkout'),
    path('previousorder/',views.previousorder,name='previousorder'),
     path('policy/', views.policy, name='policy'),
   
]

