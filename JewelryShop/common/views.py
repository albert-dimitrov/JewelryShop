from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from JewelryShop.common.forms import SearchForm, ReviewCreateForm
from JewelryShop.common.models import Reviews
from JewelryShop.jewelries.models import Jewelry


# Create your views here.

class HomePage(ListView):
    model = Jewelry
    template_name = ''
    context_object_name = 'all_jewelries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('jewelry_name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class AddReviewView(LoginRequiredMixin, CreateView):
    model = Reviews
    form_class = ReviewCreateForm

    def form_valid(self, form):
        jewelry_id = self.kwargs.get('jewelry_id')
        jewelry = get_object_or_404(Jewelry, id=jewelry_id)

        form.instance.user = self.request.user
        form.instance.jewelry = jewelry

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('jewelry_details', kwargs={'pk': self.kwargs.get('jewelry_id')})


class DeleteReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reviews

    def test_func(self):
        review = get_object_or_404(Reviews, pk=self.kwargs['pk'])
        return review.user == self.request.user

    def get_success_url(self):
        return reverse_lazy('jewelry_details', kwargs={'pk': self.object.jewelry.pk})



def about_us_page(request):
    return render(request, '')
