from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

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
    STATUS_CHOICES = (
    (True, 'OK'),
    (False, 'Tidak OK' )
    )
    #class Status(models.TextChoices):
    #    OK = 'OK',_('OK')
    #    NOT_OK = 'Not OK',_('Not OK')

    apar = models.ForeignKey(Apar, on_delete=models.CASCADE)
    tekanan = models.BooleanField(choices=STATUS_CHOICES, default=False)
    tabung = models.BooleanField(choices=STATUS_CHOICES, default=False)
    pin = models.BooleanField(choices=STATUS_CHOICES, default=False)
    handle = models.BooleanField(choices=STATUS_CHOICES, default=False)
    label = models.BooleanField(choices=STATUS_CHOICES, default=False)
    selang = models.BooleanField(choices=STATUS_CHOICES, default=False)
    tanggal = models.DateField(auto_now_add=True, blank=True, null=True)
    keterangan = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.tanggal) + "-" + str(self.apar)

    def get_absolute_url(self):
        #return reverse('scanmenu', args=[str(self.apar.slug)])
        return reverse('DashboardHome')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.apar.tanggal_periksaa = self.tanggal
        self.apar.save()

