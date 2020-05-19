from django.shortcuts import render, HttpResponse, redirect
from . models import User, Product
from django.contrib import messages
import json


def index(request):
    if 'cart' not in request.session:
        request.session['cart']=[]    
    context = {
        'all_products': Product.objects.all()
    }
    return render(request, 'sandrHome.html', context)

def rend_index(request):
    return render(request, "index.html")

   
def register(request):
    # errors = User.objects.basic_validator(request.POST)
    # print(errors)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect('/')
    # else:
    print("User registered")        
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    messages.success(request, "User successfully added")
    return redirect('/')


def login(request):
    print(request.POST)
    # retrieving a user from the db
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['password']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
        return redirect('/')
    return redirect('/')

# this will display the home page showing a snapshot of all products 

# def home(request):
#     if 'cart' not in request.session:
#         request.session['cart']=[]
#     if 'user' not in request.session:
#         return redirect('/')
#     context = {
#         'all_products':Product.objects.all()
#     }
#     return render(request, 'sandrHome.html', context)


# this will display the page for this clicked product's info and purchase
def view_product(request, id):
    print("View this product")
    context = {
        'a_product': Product.objects.get(id=id)
    }
    return render(request, 'view_product.html', context)


def customize(request,id):
    if 'user' not in request.session:
        return redirect('/rend_index')

    user_product = Product.objects.get(id=id)
    print('lets make YOUR product',"*" *50)
    user_product.color1 = request.POST['color1'] 
    user_product.color2 = request.POST['color2']
    user_product.text = request.POST['text']
    if "logo" not in request.POST:
        user_product.logo=""
    else:
        user_product.logo = request.POST['logo']
    user_product.save()
    
    request.session['cart'].append(user_product)
    request.session['cart']=json.dumps(request.session['cart'])
    request.session.modified = True
    return redirect('/view_cart')


# this will display the home page showing a snapshot of all products the signed-in user has previously purchased
def dashboard(request):
    return render(request,'user_orders.html')

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/home')

# def add_to_cart(request,id):
#     request.session['cart'].append(id)
#     return redirect('/home')


# this will display the cart page showing all products currently queued for final checkout
def view_cart(request):
    context = {
        "cart": request.session['cart']
    }
    return render(request, "cart.html", context)



# # this will display the final checkout view
def checkout(request):
    sum=0
    for id in request.session['cart']:
        sum+=Product.objects.get(id=id).cost
    context = {
        "total_cost": sum
    }
    return render(request, "checkout.html", context)

# def share(request):
#     pass

# Create your views here.
