from django.urls import path
from .views import customer_list, customer_detail, customer_create

urlpatterns = [
    path('', customer_list),
    path('<int:pk>/', customer_detail),
    path('create/', customer_create), # Добавляем URL для создания клиента
]