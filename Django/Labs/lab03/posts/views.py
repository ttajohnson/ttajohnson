from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.http import HttpResponseRedirect

class ListChirps(ListView):
    model = Post
    template_name = 'home.html'

class CreateChirp(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DetailChirp(DetailView):
    model = Post 
    template_name = 'chirp_detail.html'

class DeleteChirp(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_chirp.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

