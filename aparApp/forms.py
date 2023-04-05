from django import forms
from .models import *
from django.forms import ModelForm

class FormUpdateApar(ModelForm):
    class Meta:
        model = Apar
        fields = '__all__'
        exclude = ['tanggal_periksa']
        labels = {'nomor':'Nomor APAR'}
        widgets = {
            'nomor': forms.TextInput({'class':'form-control'}),
            'lokasi': forms.TextInput({'class':'form-control'}),
            'jenis': forms.TextInput({'class':'form-control'}),
            'ukuran': forms.TextInput({'class':'form-control'}),
            'expired': forms.TextInput({'class':'form-control'}),
            'tanggal_periksa': forms.TextInput({'class':'form-control'}),
            'path_foto': forms.TextInput({'class':'form-control'}),
            'path_QR': forms.TextInput({'class':'form-control'}),
            }

