from django.db import models
from django.conf import settings
from django.utils import timezone

class Apar(models.Model):
    nomor = models.IntegerField()
    lokasi = models.CharField(max_length=100)
    jenis = models.CharField(max_length=16)
    ukuran = models.CharField(max_length=12)
    expired = models.DateField(blank=True, null=True)
    tanggal_periksa = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.lokasi

class Pemeriksaan(models.Model):
    apar = models.ForeignKey(Apar, on_delete=models.CASCADE)
    tekanan = models.CharField(max_length=10, blank=True, null=True)
    tabung = models.CharField(max_length=2, blank=True, null=True)
    pin = models.CharField(max_length=2, blank=True, null=True)
    handle = models.CharField(max_length=2, blank=True, null=True)
    label = models.CharField(max_length=2, blank=True, null=True)
    selang = models.CharField(max_length=2, blank=True, null=True)
    tanggal = models.DateField(default=timezone.now(), blank=True, null=True)
    keterangan = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.tanggal)


