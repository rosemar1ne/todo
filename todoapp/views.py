from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, FormView

from todoapp.forms import MyUserCreationForm
from todoapp.models import Task


class TaskView(ListView):
    model = Task
    template_name = "base.html"
    context_object_name = "tasks"


class UpdateTaskView(UpdateView):
    model = Task
    fields = ["description"]
    template_name = "update_todo.html"
    success_url = "/"


class DeleteTaskView(DeleteView):
    model = Task
    template_name = "delete_todo.html"
    success_url = "/"


class CreateTaskView(CreateView):
    model = Task
    template_name = "create_todo.html"
    fields = ["title", "description"]
    success_url = "/"


class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = MyUserCreationForm
    success_url = "/"

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super(UserRegistrationView, self).get(*args, **kwargs)