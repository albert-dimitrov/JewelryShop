from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from JewelryShop.cart.models import CartItem
from JewelryShop.jewelries.models import Jewelry


class CartListView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = ''
    context_object_name = 'items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = context['items']
        context['total'] = sum(item.get_total_price() for item in items)
        return context


class AddToCartView(LoginRequiredMixin, CreateView):
    model = CartItem
    template_name = ''
    success_url = reverse_lazy('cart_detail')

    def post(self, request, *args, **kwargs):
        jewelry = get_object_or_404(Jewelry, pk=self.kwargs['jewelry_id'])
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            jewelry=jewelry
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect(self.success_url)


class RemoveFromCartView(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = reverse_lazy('cart_detail')

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)