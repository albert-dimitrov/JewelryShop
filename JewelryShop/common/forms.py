from django import forms

from JewelryShop.common.models import Reviews, Order


class SearchForm(forms.Form):
    jewelry_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Search for rings, necklaces, bracelets...'
            }
        ),
        label=''
    )


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('text', 'rating', )


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('shipping_address', 'phone')