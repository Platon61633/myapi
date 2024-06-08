from django.urls import path
from . import views
 
urlpatterns = [
    path('items/', views.ItemList.as_view(), name='item-list'),
    path('items/&lt;int:pk&gt;/', views.ItemDetail.as_view(), name='item-detail'),
]