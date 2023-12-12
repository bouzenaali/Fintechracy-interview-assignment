from django.urls import path
from . import views

app_name = 'receipts'

urlpatterns = [
    path('', views.ListReceipts, name='list'),
    path('new/', views.new, name='new'),
    path('<int:pk>/detail', views.DetailReceipt, name='detail'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]