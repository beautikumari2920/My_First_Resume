from django.urls import path
from .views import resume_view
from . import views

urlpatterns = [
    path('', resume_view, name='resume'),
    path('send-email/', views.send_email, name='send_email'),  # Add your send_email route
]