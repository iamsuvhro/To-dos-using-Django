from django.shortcuts import redirect, render, HttpResponse
from home.models import Task


def home(request):
    context = {'success' :False}
    if request.method == "POST":
        task_head = request.POST["task_head"]
        task_dres = request.POST["task_dres"]
        print(task_head,task_dres)
        ins = Task(task_head=task_head,task_dres=task_dres)
        ins.save()
        context = {'success' :True}
    return render(request,"index.html",context)


def todo(request):
    data = Task.objects.all()
    context = {'tasks':data}
    return render(request,"todo.html",context)


