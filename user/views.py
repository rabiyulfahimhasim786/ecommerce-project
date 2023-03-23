from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from . models import *
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
import json

def home(request):

    categorys= Catagory.objects.all()
    
    products= Product.objects.all()
    context ={'products':products,'categorys':categorys}  

    # obj = Catagory.objects.get(id=2)
    
    #print(context)
    
    return render(request, 'home.html',context)


def search(request):
          
        query =request.GET.get('search')
        print(query)
        if query:
             categorys= Catagory.objects.all()   
             products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
             context ={'products':products,'categorys':categorys}
        else:
             categorys= Catagory.objects.all()
             products= Product.objects.all()
             context ={'products':products,'categorys':categorys}
        return render(request,'home.html',context)


def filter_by_category(request):
    if request.method == 'GET':
        query = request.GET.get('option')
        category = Catagory.objects.get(id=query).name
        results = Product.objects.filter(category_id=query)
        # 
        # Convert the results to a list of dictionaries
        data = []
        for result in results:
            data.append({
                'id': result.id,
                'name': result.name,
                'description': result.description,
                'product_image': json.dumps(str(result.product_image)),
                'category_name' :category,
            })
        print(data)
        # Return the results as JSON
        return JsonResponse({'results': data})


  
    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
