from django.db import models
from django.conf import settings
from django.utils import timezone

class Apar(models.Model):
    nomor = models.IntegerField()
    lokasi = models.CharField(max_length=100)
    jenis = models.CharField(max_length=16)
    ukuran = models.CharField(max_length=12)
    expired = models.DateField()
    tanggal_periksa = models.DateField()

class Pemeriksaan(models.Model):
    apar = models.ForeignKey(Apar, on_delete=models.CASCADE)
    tekanan = models.CharField(max_length=10)
    tabung = models.CharField(max_length=2)
    pin = models.CharField(max_length=2)
    handle = models.CharField(max_length=2)
    label = models.CharField(max_length=2)
    selang = models.CharField(max_length=2)
    tanggal = models.DateField()
    keterangan = models.CharField(max_length=300)


