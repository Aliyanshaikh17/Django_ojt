from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Student , Information
from django.views.decorators.csrf import csrf_exempt




def home(request):
    return render(request,'sample_app/home.html')



"""
Author: Aliyan Shaikh
Created On: 12-4-2026
Description: Learn Function Base Apis 
            1. learn POST method and implement it
"""

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        info = Information.objects.create(
            name=data.get('name'),
            username=data.get('username'),
            password=data.get('password'),
            city=data.get('city')
        )

        return JsonResponse({
            'message': 'data post successfully',
            'id': info.id
        })

    return JsonResponse({
        'error': 'Only POST method allowed'
    })



'''Description: Learn Function Base Apis 
                2. learn GET method and implement it'''


def get_all_data(request):
    if request.method == "GET":
        Students = list(Information.objects.values())
        return JsonResponse(Students, safe=False)
    
    return JsonResponse({'error': 'Only GET method allowed'})

