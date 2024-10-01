from django.http import HttpResponse, JsonResponse


def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return JsonResponse(routes, safe=False)