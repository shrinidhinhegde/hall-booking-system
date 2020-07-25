from django import forms
from .models import Booking


class NewBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['hall1', 'hall2', 'date', 'ftime', 'ttime', 'purpose']
        labels = {'hall1':'Hall 1', 'hall2':'Hall 2', 'date': 'Date', 'ftime': 'Beginning Time', 'ttime': 'Ending Time', 'purpose': 'Purpose'}
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'ftime': forms.TimeInput(attrs={'type': 'time'}),
            'ttime': forms.TimeInput(attrs={'type': 'time'})
        }