import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer

def customer_list(request):
    """
    Возвращает список всех клиентов в формате JSON.
    """
    customers = list(Customer.objects.values())
    return JsonResponse(customers, safe=False)

def customer_detail(request, pk):
    """
    Возвращает детали конкретного клиента по его ID в формате JSON.
    """
    try:
        customer = Customer.objects.get(pk=pk)
        return JsonResponse({'id': customer.id, 'name': customer.name, 'phone': customer.phone})
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Customer not found'}, status=404)

def customer_create(request):
    """
    Создает нового клиента из данных, переданных в POST-запросе в формате JSON.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        customer = Customer.objects.create(name=data['name'], phone=data['phone'])
        return JsonResponse({'id': customer.id, 'name': customer.name, 'phone': customer.phone}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def customer_list_html(request):
    """
    Отображает список всех клиентов в виде HTML-страницы.
    """
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})