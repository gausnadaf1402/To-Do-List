from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    template_name='base/task_list.html'
    context_object_name='tasks'

class TaskDeatil(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name='task'

    
class TaskCreate(CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy("tasks")
    template_name='base/task_create.html'

class TaskUpdate(UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy("tasks")
    template_name='base/task_create.html'

class TaskDelete(DeleteView):
    model=Task
    context_object_name="task"
    success_url=reverse_lazy("tasks")

class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name='base/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy("tasks")

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

    
