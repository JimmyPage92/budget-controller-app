from django import forms

CHOICES_EXPENSES = (
    ('Rent', 'Rent'),
    ('Food', 'Food'),
    ('Fuel', 'Fuel'),
    ('Entertainment', 'Entertainment'),
    ('Other', 'Other'),
    ('Cosmetics and Chemicals', 'Cosmetics and Chemicals'),
)

class ExpansesPlanForm(forms.Form):
        plan_amount = forms.DecimalField(label="Wpisz kwote ktora chcesz wydac", decimal_places=2, max_digits=7)
        choice_expanses = forms.ChoiceField(choices=CHOICES_EXPENSES, label='Wybierz Rodzaj wydatku', required=True)
