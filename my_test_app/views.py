from django.http import JsonResponse

def hello(request):
    return JsonResponse({"mesaage":"안녕요"})