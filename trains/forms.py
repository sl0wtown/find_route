from django import forms
from trains.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(
        label='Номер поїзда', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введить номер поїзда'}))
    travel_time = forms.IntegerField(
        label='Час в дорозі', widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Час в дорозі'}))
    from_city = forms.ModelChoiceField(
        label='Звідки', queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    to_city = forms.ModelChoiceField(
        label='Куди', queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Train
        fields = '__all__'
