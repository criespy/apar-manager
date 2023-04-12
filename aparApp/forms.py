from django import forms
from .models import *
from django.forms import ModelForm

class FormCreateApar(ModelForm):
    class Meta:
        model = Apar
        fields = '__all__'
        exclude = ['tanggal_periksa']
        labels = {'nomor':'Nomor APAR', 'path_foto': 'Gambar APAR', 'ukuran':'Ukuran (Kg)', 'path_QR':'QR Code'}
        widgets = {
            'nomor': forms.TextInput({'class':'form-control', 'onChange':'isiQR()' }),
            'lokasi': forms.TextInput({'class':'form-control'}),
            'jenis': forms.TextInput({'class':'form-control'}),
            'ukuran': forms.TextInput({'class':'form-control'}),
            'expired': forms.TextInput({'class':'form-control'}),
            'tanggal_periksa': forms.TextInput({'class':'form-control'}),
            'path_foto': forms.FileInput({'class':'form-control'}),
            'path_QR': forms.TextInput({'class':'form-control', 'hidden':'hidden'}),
            }

class FormUpdateApar(ModelForm):
    class Meta:
        model = Apar
        fields = '__all__'
        exclude = ['tanggal_periksa']
        labels = {'nomor':'Nomor APAR', 'path_foto': 'Gambar APAR', 'ukuran':'Ukuran (Kg)', 'path_QR':'QR Code'}
        widgets = {
            'nomor': forms.TextInput({'class':'form-control', 'onChange':'isiQR()', 'readonly':'readonly' }),
            'lokasi': forms.TextInput({'class':'form-control'}),
            'jenis': forms.TextInput({'class':'form-control'}),
            'ukuran': forms.TextInput({'class':'form-control'}),
            'expired': forms.TextInput({'class':'form-control'}),
            'tanggal_periksa': forms.TextInput({'class':'form-control'}),
            'path_foto': forms.FileInput({'class':'form-control'}),
            'path_QR': forms.TextInput({'class':'form-control', 'hidden':'hidden'}),
            }

class FormPemeriksaan(ModelForm):
    class Meta:
        model = Pemeriksaan
        fields = '__all__'
        widgets = {
            'apar': forms.Select({'class':'form-control form-select'}),
            'tekanan': forms.TextInput({'class':'form-control'}),
            'tabung': forms.TextInput({'class':'form-control'}),
            'pin': forms.TextInput({'class':'form-control'}),
            'handle': forms.TextInput({'class':'form-control'}),
            'label': forms.TextInput({'class':'form-control'}),
            'selang': forms.TextInput({'class':'form-control'}),
            'keterangan': forms.TextInput({'class':'form-control'}),
        }

class FormPemeriksaanById(ModelForm):
    class Meta:
        model = Pemeriksaan
        fields = '__all__'
        labels = {'apar':'Nomor APAR'}
        widgets = {
            'apar': forms.TextInput({'class':'form-control', 'readonly':'readonly'}),
            'tekanan': forms.TextInput({'class':'form-control'}),
            'tabung': forms.TextInput({'class':'form-control'}),
            'pin': forms.TextInput({'class':'form-control'}),
            'handle': forms.TextInput({'class':'form-control'}),
            'label': forms.TextInput({'class':'form-control'}),
            'selang': forms.TextInput({'class':'form-control'}),
            'keterangan': forms.TextInput({'class':'form-control'}),
    }