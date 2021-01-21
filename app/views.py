from django.shortcuts import render,redirect
from .forms import NUForm, AuthForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def landing(request):
    auth = request.user.is_authenticated
    return render(request, 'app/landing.html', {'form':AuthForm(),'auth':auth})

def log_in(request):
    if request.method=='POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            saved_form = form.save(commit=False)
            user = authenticate(
                    request, 
                    username=saved_form.username, 
                    password=saved_form.password
                )
            if user is not None:
                login(request, user)
                return redirect('landing')
            else:
                return render(request, 'app/landing.html', {'form':AuthForm(),'error':'Неправильный логин или пароль'})
        return render(request, 'app/landing.html', {'form':AuthForm(),'error':'Форма заполнена с ошибками'})
    else:
        return render(request, 'app/landing.html', {'form':AuthForm()})

#регистрация нового юзера
def new_user(request):
    if request.method=='POST':
        form = NUForm(request.POST)
        if form.is_valid():
            saved_form = form.save(commit=False)
            user = authenticate(
                    request, 
                    username=saved_form.username, 
                    password=saved_form.password
                )
            if user is not None: #юзер найден... причем с тем же паролем
                return render(request, 'app/new_user.html', {'form':NUForm(),'error':'Пользователь уже существует'})
            else:
                try: #пробуем найти юзера по имени, вдруг пароль не подошел
                    User.objects.get(username=saved_form.username)
                    return render(request, 'app/new_user.html', {'form':NUForm(),'error':'Пользователь уже существует'})
                except: #юзера нет, создаем нового
                    new_user = User.objects.create_user(username=saved_form.username,
                                            password=saved_form.password,
                                            email=saved_form.email,
                                            first_name=saved_form.first_name,
                                            last_name=saved_form.last_name)
                    new_user.save()
                    user = authenticate(
                        request, 
                        username=saved_form.username, 
                        password=saved_form.password
                    )
                    login(request, user)
                    return redirect('landing')
        return render(request, 'app/new_user.html', {'form':NUForm(),'error':'Форма заполнена с ошибками'})                           
    else:
        #method -> GET
        form = NUForm()
    return render(request, 'app/new_user.html', {'form':form})

def log_out(request):
    logout(request)
    return landing(request)