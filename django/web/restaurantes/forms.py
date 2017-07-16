from django import forms

class SearchForm(forms.Form):
    restaurant = forms.CharField(label='Restaurante ', max_length=100)
    restaurant.widget = forms.TextInput(attrs={'size': 40, 'placeholder': 'Busca por el nombre del restaurante'})

class AddForm(forms.Form):
    name = forms.CharField(label="Nombre del restaurante ")
    borough = forms.CharField(label="Barrio ")
    cuisine = forms.CharField(label="Tipo de cocina ")

class DelForm(forms.Form):
    name = forms.CharField(label="Nombre del restaurante ")
    name.widget = forms.TextInput(attrs={'size': 40, 'placeholder': 'Nombre del restaurante que quieres borrar'})