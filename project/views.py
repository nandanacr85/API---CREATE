from django.shortcuts import render
from .models import Address
from .serializer import AddressSerilaizer
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        address=Address.objects.all()
        serilaizer=AddressSerilaizer(address, many=True)
        return JsonResponse(serilaizer.data, safe=False)
    if request.method=='POST':
        serilaizer=AddressSerilaizer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse(serilaizer.data, safe=False)
    return HttpResponse("Test")
@api_view(['GET','POST','DELETE','PUT'])
def detial(request,id):
    try:
        address=Address.objects.get(pk=id)
    except Address.DoesNotExist:
        return JsonResponse({'error':'Data not found'})
    if request.method=='GET ':
        serilaizer=AddressSerilaizer(address)
        return JsonResponse(serilaizer.data)
    if request.method=='POST':
        serilaizer=AddressSerilaizer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse(serilaizer.data, safe=False)
    if request.method=='DELETE':
        address.delete()
        return JsonResponse({'Success':'Deleted'})
    if request.method=='PUT':
        serilaizer=AddressSerilaizer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse(serilaizer.data)
    return HttpResponse("Test")


