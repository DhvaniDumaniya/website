from pyexpat.errors import messages
from django.shortcuts import render,redirect 
# from django.contrib.auth.decorators import login_required
from .models import users
# Create your views here.
def sign(request):
    return render(request,'sign.html')
def home(request):
        if 'id' in request.session:
            return render(request, 'home.html')  
        else:
            return redirect('login')
    
# @login_required
def aboutus(request):
    if 'id' in request.session:
        return render(request, 'aboutus.html')  
    else:
        return redirect('login')
# @login_required
def contact(request):
    if 'id' in request.session:
        return render(request, 'contact.html') 
    else:
        return redirect('login') 
def register(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('password')

        query = users(name=a, email=b,password = c)
        query.save()
        return redirect('sign')
    else:
        pass

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        passwords = request.POST['password']

        try:
            user = users.objects.get(email=email)
            if user.password == passwords:

            # querys = users.objects.get(email=email,password = passwords)
                request.session['id'] = user.email  # Store user email in session
                return redirect('home')
            # request.session['id'] = querys.email
            # return redirect('home1')
            else:
                messages.error(request, "Invalid credentials")
        except users.DoesNotExist:
            print("Invalid credentials")
    return render(request,'login.html')
 # except:
        #     print("ok")
        #     pass


def home1(request):

    try:
        udata = request.session['id']
        querys = users.objects.filter(email=udata)

        context = {
            "user":querys
        }
    except:
        context = {
            "user":None
        }

    return render(request,'home1.html',context)

# @login_required
# def aboutus(request):
#     return render(request, 'aboutus.html')


# def contact(request):
#     return render(request, 'contact.html')

# def users_list(request):
#     user=users.object.exclude(name='inactive')
#     return render(request,'users_list.html',{'user':user})