from django.urls import path
from .views import table_list, table_detail, table_create

urlpatterns = [
    path('', table_list),
    path('<int:pk>/', table_detail),
    path('create/', table_create), # Добавляем URL для создания столика
]