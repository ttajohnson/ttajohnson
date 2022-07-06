from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class NewChirpUser(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class ChirperProfile(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

def user_profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    context = {'user_profile':user_profile}
    return render(request, 'profile.html', context)
