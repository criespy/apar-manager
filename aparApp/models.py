from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Apar(models.Model):
    nomor = models.IntegerField()
    lokasi = models.CharField(max_length=100)
    jenis = models.CharField(max_length=16)
    ukuran = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    expired = models.DateField(blank=True, null=True)
    tanggal_periksa = models.DateField(blank=True, null=True)
    path_foto = models.ImageField(upload_to='images/%Y%m')
    path_QR = models.CharField(max_length=1024, null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return str(self.nomor) + " - " +  self.lokasi
    
    def get_absolute_url(self):
        return reverse('updateapar', args=[str(self.id)])

class Pemeriksaan(models.Model):
    apar = models.ForeignKey(Apar, on_delete=models.CASCADE)
    tekanan = models.CharField(max_length=10, blank=True, null=True)
    tabung = models.CharField(max_length=2, blank=True, null=True)
    pin = models.CharField(max_length=2, blank=True, null=True)
    handle = models.CharField(max_length=2, blank=True, null=True)
    label = models.CharField(max_length=2, blank=True, null=True)
    selang = models.CharField(max_length=2, blank=True, null=True)
    tanggal = models.DateField(auto_now_add=True, blank=True, null=True)
    keterangan = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.tanggal) + "-" + str(self.apar)


