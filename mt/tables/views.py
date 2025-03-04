import json
from django.http import JsonResponse
from .models import Table

def table_list(request):
    tables = list(Table.objects.values())
    return JsonResponse(tables, safe=False)

def table_detail(request, pk):
    try:
        table = Table.objects.get(pk=pk)
        return JsonResponse({'id': table.id, 'number': table.number, 'capacity': table.capacity})
    except Table.DoesNotExist:
        return JsonResponse({'error': 'Table not found'}, status=404)

def table_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        table = Table.objects.create(number=data['number'], capacity=data['capacity'])
        return JsonResponse({'id': table.id, 'number': table.number, 'capacity': table.capacity}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)