from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from JewelryShop.accounts.forms import AppUserCreationForm, ProfileEditForm
from JewelryShop.accounts.models import Profile, CustomUser

# Create your views here.
UserModel = get_user_model()

class UserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = ''
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response

class UserLoginView(LoginView):
    template_name = ''


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = ''

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = ''


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = ''
    success_url = reverse_lazy('login')

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def form_valid(self, form):
        user = CustomUser.objects.get(pk=self.object.pk)
        user.is_active = False
        user.save()

        logout(self.request)

        response = super().form_valid(form)

        return response
