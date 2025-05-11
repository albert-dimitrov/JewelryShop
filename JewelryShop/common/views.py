from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, FormView, DetailView

from JewelryShop.cart.models import CartItem
from JewelryShop.common.forms import SearchForm, ReviewCreateForm, CheckoutForm
from JewelryShop.common.models import Reviews, OrderItem, Order
from JewelryShop.jewelries.models import Jewelry


# Create your views here.

class HomePage(ListView):
    model = Jewelry
    template_name = 'common/home.html'
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


class CheckoutView(LoginRequiredMixin, FormView):
    template_name = ''
    form_class = CheckoutForm

    def get_cart_items(self):
        return CartItem.objects.filter(user=self.request.user)

    def form_valid(self, form):
        cart_items = self.get_cart_items()
        if not cart_items.exists():
            form.add_error(None, "Your cart is empty.")
            return self.form_invalid(form)

        order = form.save(commit=False)
        order.customer = self.request.user
        order.total_price = sum(item.jewelry.price * item.quantity for item in cart_items)
        order.save()


        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                jewelry=item.jewelry,
                quantity=item.quantity,
                price=item.jewelry.price
            )

        cart_items.delete()
        return redirect(reverse('order_success', kwargs={'pk': order.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = self.get_cart_items()
        return context


class OrderSuccessView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = ''
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)


def about_us_page(request):
    return render(request, '')
