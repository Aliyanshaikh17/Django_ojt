from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Student , Information , User
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



'''Description: Learn Function Base Apis 
                GET by id ( in this api i use primary key) '''

def get_one(request, pk):
    try:
        user = Information.objects.get(id=pk)
        data = {
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'city': user.city
        }
        return JsonResponse(data)
    except Information.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)





'''Description: Learn Function Base Apis 
                learn PUT method and implement it  '''


@csrf_exempt
def put_stu(request, pk):
    if request.method == 'PUT':
        try:
            info = Information.objects.get(id=pk)
            data = json.loads(request.body)
            
            info.name = data.get('name', info.name)
            info.username = data.get('username', info.username)
            info.password = data.get('password', info.password)
            info.city = data.get('city', info.city)
            
            info.save()

            return JsonResponse({'message': 'information updated successfully'})
        
        except Information.DoesNotExist:
            return JsonResponse({'error': 'information not found'}, status=404)
        
    return JsonResponse({'error': 'Only PUT method allowed'})




'''Description: Learn Function Base Apis 
                learn DELETE method and implement it  '''



@csrf_exempt
def delete_stu(request, pk):
    if request.method == 'DELETE':
        try:
            info = Information.objects.get(id=pk)
            info.delete()
            return JsonResponse({'message': 'information deleted successfully'})
        
        except Information.DoesNotExist:
            return JsonResponse({'error': 'information not found'}, status=404)
        
    return JsonResponse({'error': 'Only DELETE method allowed'})




'''Description: Learn Function Base Apis 
                write user register api  '''
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error':'Email already exists'},status=404)
        
        user = User.objects.create(
            username=username,
            email=email,
            password=password,
        )

        return JsonResponse({'message':'user register successfully'})
    
    return JsonResponse({'error':'Only POST method allowed'})
        



'''Description: Learn Function Base Apis 
                learn and write login register api  '''
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')  

        try:
            user = User.objects.get(email=email,password=password)
            return JsonResponse({
                'message':'login successful',
                'username':user.username
            })
        except User.DoesNotExist:
            return JsonResponse({'error':'invalid email or password'},status=401)
    
    return JsonResponse({'error':'Only POST method allowed'})