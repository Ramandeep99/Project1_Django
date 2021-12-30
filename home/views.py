from django.contrib.messages.api import success
from django.shortcuts import redirect, render , HttpResponse
from datetime import datetime
from home.models import User

from django.contrib import messages  

# Create your views here.


def index(request):
    Username = None
    if 'Username' in request.session:

        Username = User.objects.get(email =  request.session['email']).Username
    
    variable = {
        'name' : Username
    }
    #  we will fetch data from db and send it in html through variables
    return render(request , 'index.html' , variable )

def userRegister(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Phoneno = request.POST.get('Phoneno')
        Password = request.POST.get('Password')
        Confirm_password = request.POST.get('Confirm_password')
        if Password != Confirm_password:
            messages.success(request, 'Password not Matched with Confirm Password')
            return render(request , 'userRegister.html')

        b = User.objects.filter(email=Email).exists()
        if b:
            messages.success(request, 'User Already  Registered')
            return redirect('userLogin')
        user = User(Username = Username , email = Email , Phoneno = Phoneno , password = Password , date = datetime.today() )
        user.save()
        messages.success(request, 'User Registered')
        return redirect('/userLogin')
    return render(request , 'userRegister.html')

def userLogin(request):
    if request.method == "POST":
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        try:
            storedData = User.objects.get(email = Email , password = Password )

            data = {}
            data['name'] = storedData.Username
            data['email'] = storedData.email

            if storedData and storedData.password == Password:
                messages.success(request, 'Logged in')

                request.session['Username'] = storedData.Username
                request.session['email'] = storedData.email

                return redirect( '/' , data)
            else:
                messages.info(request, 'Invalid Login Credentials')
                return render(request , 'userLogin.html')
        except:
            messages.info(request, 'Entered Email Not Found')
            return render(request , 'userLogin.html')
    return render(request , 'userLogin.html')

def userEdit(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Phoneno = request.POST.get('Phoneno')
        Password = request.POST.get('Password')
        Confirm_password = request.POST.get('Confirm_password')
        # print(Password , Confirm_password)
        if Password != Confirm_password :
            messages.success(request, 'Password not Matched with Confirm Password')
            userData = User.objects.get(email = request.session['email'])
            userDataDict = {}
            userDataDict['Username']  = userData.Username
            userDataDict['Email']  = userData.email
            userDataDict['Phoneno']  = userData.Phoneno
            userDataDict['Password']  = userData.password
            request.session['Username'] = userData.Username
            request.session['email'] = userData.email
            return render(request , 'userEdit.html' , userDataDict)


        user = User.objects.get(email = request.session['email'])
        user.Username = Username 
        user.email = Email  
        user.Phoneno = Phoneno 
        user.password = Password 
        user.date = datetime.today()
        user.save()
        request.session['email'] = Email
        request.session['Username'] = Username
        messages.success(request, 'User Updated')

        # updating for home page
        userData = User.objects.get(email = request.session['email'])
        userDataDict = {}
        userDataDict['Username']  = userData.Username
        userDataDict['Email']  = userData.email
        userDataDict['Phoneno']  = userData.Phoneno
        userDataDict['Password']  = userData.password
        return redirect('/' , userDataDict)

    elif 'Username' in request.session:
        userData = User.objects.get(email = request.session['email'])
        userDataDict = {}
        userDataDict['Username']  = userData.Username
        userDataDict['Email']  = userData.email
        userDataDict['Phoneno']  = userData.Phoneno
        userDataDict['Password']  = userData.password
        request.session['Username'] = userData.Username
        request.session['email'] = userData.email
        print(request.session['Username'] , request.session['email'])
        return render(request , 'userEdit.html' , userDataDict)
    else:
        messages.info(request , 'User NOt Logged In')
        return render(request , 'userLogin.html')

def userLogout(request):
    Username = None
    if 'Username' in request.session:
        request.session['Username'] = None
        return redirect('/userLogin')
    return render(request , 'userLogin')


def adminLogin(request):
    return HttpResponse('from admin page')
