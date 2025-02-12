from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from JewelryShop.jewelries.forms import JewelryCreateForm, JewelryEditForm
from JewelryShop.jewelries.models import Jewelry


# Create your views here.

class JewelriesAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Jewelry
    form_class = JewelryCreateForm
    template_name = ''

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Moderation Group').exists()

    def get_success_url(self):
        return reverse_lazy('jewelry_details', kwargs={'pk': self.object.pk})


class JewelriesEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jewelry
    form_class = JewelryEditForm
    template_name = ''

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Moderation Group').exists()

    def get_success_url(self):
        return reverse_lazy('jewelry_details', kwargs={'pk': self.object.pk})


class JewelriesDetailsView(DetailView):
    model = Jewelry
    template_name = ''
    context_object_name = 'jewelry'


class JewelriesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jewelry
    template_name = ''
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Moderation Group').exists()
