from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from authentication.models import SpTnstate,Districts,Blocks
from django.core.serializers import serialize

# Create your views here.



def index(request):
    if request.user.is_authenticated:
            return redirect('/home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '':
            messages.info(request, 'Username required')
            return redirect("/")
        if password == '':
            messages.info(request, 'Password required')
            return redirect("/")

        user = auth.authenticate(username = username, password =password  )

        if user is not None:
            auth.login(request , user)
            return redirect('/home')    
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request,'index.html')


# def register(request):

#     if request.method == 'POST':

#         email = request.POST['email']
#         username = request.POST['username']
#         password= request.POST['password']


#         user = User.objects.create_user(username = username , password = password , email = email)
#         user.save()
#         print('user created')
#         return redirect('/custom')

#     return render(request,'register.html')


# def custom(request):
#     return render(request, 'custom.html')

@login_required
def home(request):
    data = serialize('geojson', SpTnstate.objects.all(),geometry_field='geom',fields=('state_name',))
    data1 = serialize('geojson', Districts.objects.all(),geometry_field='geom',fields=('gid','district',))
    data2 = serialize('geojson', Blocks.objects.all(),geometry_field='geom',fields=('gid','district','blkname'))
    return render(request, 'home.html',{'geo_json': data,'district':data1,'block':data2},)
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")