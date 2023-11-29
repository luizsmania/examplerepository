from django.urls import path
from . import views
from django.urls import path
from .views import your_view

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('book_table/', views.book_table, name='book_table'),
    path('delete_reservation/<int:id>/', views.delete_reservation, name='delete_reservation'),
    path('update_reservation/<int:id>/', views.update_reservation, name='update_reservation'),
    path('user_page/', views.user_page, name='user_page'),
    path('register/', views.register_view, name='register'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('menu_items/', views.menu_items, name='menu_items'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('your-view/', your_view, name='your_view'),
]
