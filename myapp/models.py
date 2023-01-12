from django.db import models


class Siswa(models.Model):
    pilihan = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )
    nis = models.CharField(max_length=12)
    jk = models.CharField(max_length=1, choices=pilihan)
    nama = models.CharField(max_length=50)
    def __str__(self):
        return self.nama

class Kehadiran(models.Model):
    id_siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=1)
    tanggal = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id_siswa.nama
