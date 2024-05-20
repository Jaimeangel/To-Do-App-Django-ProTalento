from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone
from .forms import TaskForm
from .models import Task
from urllib.parse import urlparse
from .forms import RegisterForm

# Create your views here.
@login_required(login_url='/login')
def home(request):
    id_user=request.user.id
    task= Task.objects.filter(user_id=id_user)
    task.reverse()
    return render(request,'index.html',{'tasks':task})

@login_required(login_url='/login')
def completed(request):
    id_user=request.user.id
    task= Task.objects.filter(user_id=id_user,completed_task=True)
    task.reverse()
    return render(request,'completed.html',{'tasks':task})

@login_required(login_url='/login')
def incompleted(request):
    id_user=request.user.id
    task= Task.objects.filter(user_id=id_user,completed_task=False)
    task.reverse()
    return render(request,'incompleted.html',{'tasks':task})

@login_required(login_url='/login')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = request.user
            task.save()
            return redirect('/') 
        else:
            print('Form is not valid')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})


def toogle_task(request, task_id):
    referer = request.META.get('HTTP_REFERER', '/')
    parsed_url = urlparse(referer)
    path = parsed_url.path

    task = get_object_or_404(Task, id=task_id, user_id=request.user.id)

    if task:
        task.completed_task = not task.completed_task
        if task.completed_task == True:
            task.date_completed = timezone.now()
        task.save()
        return redirect(path)

@login_required(login_url='/login')
def detail_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user_id=request.user.id)
    return render(request,'task_detail.html',{'task':task})

@login_required(login_url='/login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user_id=request.user.id)
    return render(request,'delete.html',{'task':task})

def remove_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user_id=request.user.id)
    if task:
        task.delete()
        return redirect('/')

@login_required(login_url='/login')
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user_id=request.user.id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # Redirigir al detalle de la tarea después de editarla
            return redirect('detail-task', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'edit_task.html', {'form': form, 'task': task})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = RegisterForm()
    
    return render(request,'registration/sign_up.html',{'form':form})