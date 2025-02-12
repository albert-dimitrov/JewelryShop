from django import forms

from JewelryShop.common.models import Reviews


class SearchForm(forms.Form):
    jewelry_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Jewelry Name...'}
        )
    )


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('text', 'rating', )