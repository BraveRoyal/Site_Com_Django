from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'blog'

urlpatterns = [
    path('', login_required(views.PostListView.as_view()), name='list'),
    path('<slug:slug>/', login_required(views.PostDetailView.as_view()), name='detail'),
]