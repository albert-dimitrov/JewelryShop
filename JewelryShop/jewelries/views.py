from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

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


class JewelriesProductShowView(ListView):
    model = Jewelry
    template_name = ''

    def get_queryset(self):
        product_category = self.kwargs.get('category')
        return Jewelry.objects.filter(category=product_category)


def category_choose_page(request):
    categories = [
        {'name': 'Rings', 'image': 'ring.jpg'},
        {'name': 'Necklaces', 'image': 'necklace.jpg'},
        {'name': 'Earrings', 'image': 'earring.jpg'},
        {'name': 'Bracelets', 'image': 'bracelet.jpg'},
        {'name': 'Anklets', 'image': 'anklet.jpg'},
        {'name': 'Brooches & Pins', 'image': 'brooch.jpg'},
        {'name': 'Charms', 'image': 'charms.jpg'},
        {'name': 'Jewelry Sets', 'image': 'set.jpg'},
        {'name': 'Watches', 'image': 'watch.jpg'},
    ]

    context = {
        'categories': categories,
    }

    return render(request, 'jewelries/choose-category.html', context)