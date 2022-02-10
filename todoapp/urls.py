from django.urls import path
from .views import TaskView, UpdateTaskView, DeleteTaskView, CreateTaskView, UserRegistrationView

urlpatterns = [
    path('accounts/registration/', UserRegistrationView.as_view(), name="registration"),

    path('', TaskView.as_view()),
    path('update_todo/<int:pk>', UpdateTaskView.as_view(), name="update"),
    path('delete_todo/<int:pk>', DeleteTaskView.as_view(), name="delete"),
    path('create_todo', CreateTaskView.as_view(), name="create"),

]