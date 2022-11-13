from django import forms

class ExpanseForm(forms.Form):
        amount = forms.DecimalField(label="Wpisz kwote ktora chcesz wydac", decimal_places=2, max_digits=7)