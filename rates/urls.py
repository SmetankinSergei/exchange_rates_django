from django.urls import path

from rates import views

app_name = 'rates'

urlpatterns = [
    path('', views.home, name='home'),
    path('get-current-usd/', views.get_current_usd, name='get_current_usd')
]
