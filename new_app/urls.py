from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('product_list/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product,name='delete_product'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),


]

   




#ur admin