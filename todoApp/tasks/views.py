from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/lists.html',context)

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance = task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = { 'task':task}
    return render(request, 'tasks/delete.html', context)