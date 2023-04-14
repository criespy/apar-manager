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
            'nomor': forms.TextInput({'class':'form-control', 'onChange':'isiQR();isiSlug();' }),
            'lokasi': forms.TextInput({'class':'form-control'}),
            'jenis': forms.TextInput({'class':'form-control'}),
            'ukuran': forms.TextInput({'class':'form-control'}),
            'expired': forms.TextInput({'class':'form-control'}),
            'tanggal_periksa': forms.TextInput({'class':'form-control'}),
            'path_foto': forms.FileInput({'class':'form-control'}),
            'path_QR': forms.TextInput({'class':'form-control', 'hidden':'hidden'}),
            'slug': forms.TextInput({'class':'form-control', 'onChange':'isiQR()', 'readonly':'readonly'}),
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
            'slug': forms.TextInput({'class':'form-control', 'onChange':'isiQR()', 'readonly':'readonly'}),
            }

class FormPemeriksaan(ModelForm):
    tekanan = forms.BooleanField(required=False)
    tabung = forms.BooleanField(required=False)
    pin = forms.BooleanField(required=False)
    handle = forms.BooleanField(required=False)
    label = forms.BooleanField(required=False)
    selang = forms.BooleanField(required=False)
    sign = forms.BooleanField(required=False)

    class Meta:
        model = Pemeriksaan
        fields = '__all__'
        widgets = {
            'apar': forms.Select({'class':'form-control form-select'}),
            'tekanan': forms.CheckboxInput(),
            'tabung': forms.CheckboxInput(),
            'pin': forms.CheckboxInput(),
            'handle': forms.CheckboxInput(),
            'label': forms.CheckboxInput(),
            'selang': forms.CheckboxInput(),
            'sign': forms.CheckboxInput(),
            'keterangan': forms.TextInput({'class':'form-control'}),
            'apar.path_foto': forms.FileInput({'class':'form-control'}),
        }

class FormPemeriksaanById(ModelForm):
    tekanan = forms.BooleanField(required=False)
    tabung = forms.BooleanField(required=False)
    pin = forms.BooleanField(required=False)
    handle = forms.BooleanField(required=False)
    label = forms.BooleanField(required=False)
    selang = forms.BooleanField(required=False)
    sign = forms.BooleanField(required=False)

    class Meta:
        model = Pemeriksaan
        fields = '__all__'
        labels = {'apar':'Nomor APAR'}
        widgets = {
            'apar': forms.TextInput({'class':'form-control', 'readonly':'readonly'}),
            'tekanan': forms.CheckboxInput(),
            'tabung': forms.CheckboxInput(),
            'pin': forms.CheckboxInput(),
            'handle': forms.CheckboxInput(),
            'label': forms.CheckboxInput(),
            'selang': forms.CheckboxInput(),
            'sign': forms.CheckboxInput(),
            'keterangan': forms.TextInput({'class':'form-control'}),
            'apar.path_foto': forms.FileInput({'class':'form-control'}),
    }
        
class FormDetailApar(ModelForm):
    class Meta:
        model = Apar
        fields = '__all__'
        exclude = ['tanggal_periksa']
        labels = {'nomor':'Nomor APAR', 'path_foto': 'Gambar APAR', 'ukuran':'Ukuran (Kg)', 'path_QR':'QR Code'}
        widgets = {
            'nomor': forms.TextInput({'class':'form-control', 'onChange':'isiQR()', 'disabled':'' }),
            'lokasi': forms.TextInput({'class':'form-control', 'disabled':'' }),
            'jenis': forms.TextInput({'class':'form-control', 'disabled':'' }),
            'ukuran': forms.TextInput({'class':'form-control', 'disabled':'' }),
            'expired': forms.TextInput({'class':'form-control', 'disabled':'' }),
            'tanggal_periksa': forms.TextInput({'class':'form-control', 'disabled':'' }),
            'path_foto': forms.FileInput({'class':'form-control'}),
            'path_QR': forms.TextInput({'class':'form-control', 'hidden':'hidden'}),

            }