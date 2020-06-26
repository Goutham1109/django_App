from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoCreateForm
from .models import TODO
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def signupuser(request):
    if request.method == 'GET':
        return render(request,'signup.html' ,{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request,'signup.html' ,{'form':UserCreationForm(),'error':'User name already taken'})    
        else:
            return render(request,'signup.html' ,{'form':UserCreationForm(),'error':'Mismatch'})

@login_required
def todouserdashboard(request):
            todos = TODO.objects.filter(user=request.user,datacompleted__isnull=True,deleted=False)
            return render(request,'todoUser.html' ,{'value':todos})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'login.html' ,{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
                    return render(request,'login.html' ,{'form':AuthenticationForm(),'error':'Invalid Data'})
        else:
            login(request,user)
            return redirect('dashboard')

      
def createnew(request):
            if request.method == 'GET':
                return render(request,'createtodo.html' ,{'form':TodoCreateForm()})
            else:
                try:
                    formvalue = TodoCreateForm(request.POST)
                    todovalue = formvalue.save(commit=False)
                    todovalue.user = request.user
                    todovalue.save()
                    return redirect('dashboard')
                except ValueError:
                        return render(request,'createtodo.html' ,{'form':TodoCreateForm(),'error':'Value not correct'})

@login_required
def updatetodo(request,id):
            todo = get_object_or_404(TODO,pk=id,user=request.user,deleted=False)

            if request.method == 'GET':
                formvalue = TodoCreateForm(instance=todo)
                return render(request,'update.html' ,{'datavalue':formvalue,'value':todo})
            else:
                try:
                    data = TodoCreateForm(request.POST,instance=todo)
                    data.save()
                    return redirect('dashboard')
                except ValueError:
                    return render(request,'update.html' ,{'datavalue':TodoCreateForm(),'error':'Value not correct'})

@login_required
def updatetocomplete(request,id):
        todo = get_object_or_404(TODO,pk=id,user=request.user)
        if request.method == 'POST':
                todo.datacompleted = timezone.now()
                # print(todo.datacompleted)
                # print('hellp')
                todo.save()
                return redirect('dashboard')

@login_required
def deletetodo(request,id):
        todo = get_object_or_404(TODO,pk=id,user=request.user)
        if request.method == 'POST':
                # todo.delete()
                todo.deleted=True
                todo.save()
                return redirect('dashboard')

@login_required
def getcompleted(request):
            todos = TODO.objects.filter(user=request.user,deleted=False,datacompleted__isnull=False).order_by('-datacompleted')
            return render(request,'completedTodo.html' ,{'value':todos})

@login_required
def logoutuser(request):
            if request.method == 'POST':
                logout(request)
                return redirect('todoHome')

def todoHome(request):
            return render(request,'todoHome.html')
