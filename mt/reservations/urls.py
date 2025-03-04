from django.urls import path
from .views import reservation_list, reservation_detail, reservation_create

urlpatterns = [
    path('', reservation_list),
    path('<int:pk>/', reservation_detail),
    path('create/', reservation_create), # Добавляем URL для создания бронирования
]
