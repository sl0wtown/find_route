from django import forms
from cities.models import City


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(
        label='Звідки', queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(
        label='Куди', queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))
    cities = forms.ModelMultipleChoiceField(
        label='Через міста', queryset=City.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'}))
    travelling_time = forms.IntegerField(
        label='Час в дорозі', widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Час в дорозі'}))

