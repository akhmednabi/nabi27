import json
from django.http import JsonResponse
from .models import Reservation

def reservation_list(request):
    reservations = list(Reservation.objects.values())
    return JsonResponse(reservations, safe=False)

def reservation_detail(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
        return JsonResponse({'id': reservation.id, 'customer': reservation.customer.id, 'table': reservation.table.id, 'date': str(reservation.date), 'time': str(reservation.time)})
    except Reservation.DoesNotExist:
        return JsonResponse({'error': 'Reservation not found'}, status=404)

def reservation_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_id = data['customer']
        table_id = data['table']
        reservation = Reservation.objects.create(customer_id=customer_id, table_id=table_id, date=data['date'], time=data['time'])
        return JsonResponse({'id': reservation.id, 'customer': reservation.customer.id, 'table': reservation.table.id, 'date': str(reservation.date), 'time': str(reservation.time)}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)