
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('Green_corner/', views.ShopListView.as_view(), name='green_corner'),
]
