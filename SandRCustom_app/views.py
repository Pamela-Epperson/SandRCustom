from django.shortcuts import render,  HttpResponse

def index(request):
    print(request)
    return render(request,'index.html')

   
def register(request):
    errors = User.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
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
            return redirect('/dashboard')
    return redirect('/')

# this will display a page with wishes from all users 

def home(request):
    context = {
        'all_products': Product.objects.all()
    }
    return render(request, 'sandrHome.html', context)

# Create your views here.
