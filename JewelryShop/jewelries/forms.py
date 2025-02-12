from django import forms

from JewelryShop.jewelries.models import Jewelry


class JewelryBaseForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        exclude = ('user', 'created', 'updated_at')


class JewelryCreateForm(JewelryBaseForm):
    pass


class JewelryEditForm(JewelryBaseForm):
    pass
