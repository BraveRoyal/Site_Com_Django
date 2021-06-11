from django.views.generic import DetailView, ListView


from .models import Post

"""pegando a lista toda de blogs"""
class PostListView(ListView):
    model = Post

"""pegando um blog especifico"""
class PostDetailView(DetailView):
    model = Post