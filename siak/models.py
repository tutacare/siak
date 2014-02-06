from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import datetime

YEAR_CHOICES = []
for y in range((datetime.datetime.now().year - 7), (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((y, y))

SEX_CHOICES =  (
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan'),
    )

STATUS_CHOICES =  (
    (0, 'Tidak Aktif'),
    (1, 'Aktif'),
    )

URUTAN_CHOICES =  (
    (1, 1),
    (2, 2),
    (3, 3)
    )
    
class Agama(models.Model):
    nama = models.CharField('Nama', max_length = 100)
    aktif = models.BooleanField('Ya/Tidak', help_text= 'Centang jika ingin mengaktifkan')
            
    def __unicode__(self):
        return self.nama
                    
    class Meta:
        db_table = 'agama'
        verbose_name_plural = u'Agama'    

class Fakultas(models.Model):
    kode_fakultas = models.CharField('Kode Fakultas', max_length=10, unique = True)
    nama_fakultas = models.CharField('Nama Fakultas', max_length=100)
    
    def __unicode__(self):
        return self.nama_fakultas
    
    class Meta:
        db_table = 'fakultas'
        verbose_name_plural = 'Fakultas'

class Jurusan(models.Model):
    kode_jurusan = models.CharField('Kode Jurusan', max_length=10, unique = True)
    nama_jurusan = models.CharField('Nama Jurusan', max_length=100)
    fakultas = models.ForeignKey(Fakultas, verbose_name='Fakultas')
    jenjang = models.CharField('Jenjang', max_length=5)
    
    def __unicode__(self):
        return self.nama_jurusan
    
    class Meta:
        db_table = 'tbjurusan'
        verbose_name_plural = 'Jurusan'

class RegisterAkademik(models.Model):
    tahun_akademik = models.CharField('Tahun Akademik', max_length = 5)
    aktif = models.BooleanField('Aktif', help_text= 'Centang jika ingin mengaktifkan tahun akademik')
    
    def __unicode__(self):
        return self.tahun_akademik
                    
    class Meta:
        db_table = 'regakademik'
        ordering = ('-tahun_akademik',)

class ProgramStudi(models.Model):
    kode_prodi = models.CharField('Kode Prodi', max_length=10, unique = True)
    nama_prodi = models.CharField('Nama Prodi', max_length=100)
    
    def __unicode__(self):
        return self.kode_prodi
    
    class Meta:
        db_table = 'tbprodi'
        verbose_name_plural = 'Program Studi'

class Dosen(models.Model):
	nama = models.CharField('Nama', max_length = 100)
	user = models.ForeignKey(User, unique=True)
	tanggal_lahir = models.DateField('Tanggal Lahir', help_text = 'Format Tanggal: YYYY-MM-DD')
	jenis_kelamin = models.CharField('Jenis Kelamin', max_length = 10, choices=SEX_CHOICES, default='Laki-laki')
	agama = models.ForeignKey(Agama, verbose_name='Agama')
	alamat = models.CharField('Alamat', max_length = 100)
	email = models.CharField('Email', max_length = 100)
	telepon = models.CharField('Telepon', max_length = 100)
	keterangan = models.CharField('Keterangan', max_length = 100)
	image = models.ImageField(u'Photo', upload_to = 'dosen-photos')
	aktif = models.BooleanField('Ya/Tidak', help_text= 'Centang jika ingin mengaktifkan')
            
	def __unicode__(self):
		return self.nama
			
	class Meta:
		db_table = 'dosen'
		verbose_name_plural = u'Dosen'

class Mahasiswa(models.Model):
	nim = models.CharField('NIM', max_length = 20, unique = True)
	nama = models.CharField('Nama', max_length = 80)
	user = models.ForeignKey(User, unique=True)
	jenis_kelamin = models.CharField('Jenis Kelamin', max_length = 10, choices=SEX_CHOICES, default='Laki-laki')
	agama = models.ForeignKey(Agama, verbose_name='Agama')
	tanggal_lahir = models.DateField('Tanggal Lahir', help_text = 'Format Tanggal: YYYY-MM-DD')
	alamat = models.CharField('Alamat', max_length = 100)
	telepon = models.CharField('Telepon', max_length = 100)
	email = models.CharField('Email', max_length = 100)
	fakultas = models.ForeignKey(Fakultas, verbose_name='Fakultas')
	jurusan = models.ForeignKey(Jurusan, verbose_name='Jurusan')
	prodi = models.ForeignKey(ProgramStudi, verbose_name='Program Studi')
	tahun_akademik = models.ForeignKey(RegisterAkademik, verbose_name='Angkatan')
	dosen = models.ForeignKey(Dosen, verbose_name='Dosen')
	ipk = models.IntegerField('IPK', max_length = 3)
	#angkatan = models.IntegerField('Angkatan', max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
	image = models.ImageField(u'Photo', upload_to = 'mahasiswa-photos')
	aktif = models.BooleanField('Ya/Tidak', help_text= 'Centang jika ingin mengaktifkan')
    
	def __unicode__(self):
		return ' '.join([
			self.nim,
			self.nama,
			])
        #return self.nim + " - " + self.nama
                    
	class Meta:
		db_table = 'tbmahasiswa'
		verbose_name_plural = u'Mahasiswa'
        
class BahanAjar(models.Model):
    nama = models.CharField('Nama', max_length = 80)
    user_upload = models.CharField('Alamat', max_length = 180)
    tanggal_upload = models.DateField('Tanggal Lahir', help_text = 'Format Tanggal: YYYY-MM-DD')
    jumlah_download = models.IntegerField('Jumlah Download')
    status = models.BooleanField('Status', choices=STATUS_CHOICES, default=0)
    image = models.ImageField(u'File', upload_to = 'gallery-upload')
            
    def __unicode__(self):
        return self.nim
                    
    class Meta:
        db_table = 'tbbahan_ajar'

class MataKuliah(models.Model):
    prodi = models.ForeignKey(ProgramStudi, verbose_name='Program Studi')
    kode_mtk = models.CharField('Kode Mata Kuliah', max_length = 30, unique = True)
    nama_mtk = models.CharField('Nama Mata Kuliah', max_length = 50)
    semester = models.CharField('Semester', max_length = 2)
    sks = models.IntegerField('SKS', max_length = 2)
    fakultas = models.ForeignKey(Fakultas, verbose_name='Fakultas')
    jurusan = models.ForeignKey(Jurusan, verbose_name='Jurusan')
            
    def __unicode__(self):
        return self.nama_mtk
                    
    class Meta:
        db_table = 'tbmatakuliah'
        verbose_name_plural = 'Mata Kuliah'
        
class NamaHari(models.Model):
    nama_hari = models.CharField('Nama Hari', max_length=10, unique = True)
    
    def __unicode__(self):
        return self.nama_hari
    
    class Meta:
        db_table = 'tbhari'
        verbose_name_plural = 'Nama Hari'

class Jadwal(models.Model):
    tahun_akademik = models.ForeignKey(RegisterAkademik, verbose_name='Tahun Akademik')
    prodi = models.ForeignKey(ProgramStudi, verbose_name='Program Studi')
    mata_kuliah = models.ForeignKey(MataKuliah, verbose_name='Mata Kuliah')
    jurusan = models.ForeignKey(Jurusan, verbose_name='Jurusan')
    ruang = models.CharField('Ruang', max_length=10)
    kelas = models.CharField('Kelas', max_length=5)
    dosen = models.ForeignKey(Dosen, verbose_name='Dosen')
    hari = models.ForeignKey(NamaHari, verbose_name='Hari')
    jam_mulai = models.TimeField('Jam Mulai')
    jam_selesai = models.TimeField('Jam Selesai')
    uts_tanggal = models.DateField('Tanggal UTS')
    uts_mulai = models.TimeField('Jam Mulai UTS')
    uts_selesai = models.TimeField('Jam Selesai UTS')
    uts_ruang = models.CharField('Ruangan UTS', max_length=10)
    uas_tanggal = models.DateField('Tanggal UAS')
    uas_mulai = models.TimeField('Jam Mulai UAS')
    uas_selesai = models.TimeField('Jam Selesai UAS')
    uas_ruang = models.CharField('Ruangan UAS', max_length=10)
    
    def __unicode__(self):
        return self.mata_kuliah.nama_mtk
	
	def jadwal_matkul(self):
		return self.mata_kuliah.nama_mtk
    
    class Meta:
        db_table = 'tbjadwal'
        verbose_name_plural = 'Jadwal'

class RegisterMahasiswa(models.Model):
	tahun_akademik = models.ForeignKey(RegisterAkademik, verbose_name='Tahun Akademik')
	nim = models.ForeignKey(Mahasiswa, verbose_name='Mahasiswa')
	tanggal_register = models.DateField('Tanggal Register')
	aktif = models.BooleanField('Ya/Tidak', help_text= 'Centang jika ingin mengaktifkan')
	
	class Meta:
		db_table = 'tbregister_mahasiswa'
		verbose_name_plural = 'Register Mahasiswa'
		
class Krs(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, verbose_name='Mahasiswa')
    tahun_akademik = models.ForeignKey(RegisterAkademik, verbose_name='Tahun Akademik')
    jadwal = models.ForeignKey(Jadwal, verbose_name='Mata Kuliah')
    tugas1 = models.IntegerField('Tugas 1', max_length=3, blank=True, null=True)
    tugas2 = models.IntegerField('Tugas 2', max_length=3, blank=True, null=True)
    tugas3 = models.IntegerField('Tugas 3', max_length=3, blank=True, null=True)
    tugas4 = models.IntegerField('Tugas 4', max_length=3, blank=True, null=True)
    nilai_mid = models.IntegerField('Nilai MID', max_length=3, blank=True, null=True)
    nilai_uas = models.IntegerField('Nilai UAS', max_length=3, blank=True, null=True)

    def nama_mahasiswa(self):
        return self.mahasiswa.nama

    def nama_mata_kuliah(self):
        return self.jadwal.mata_kuliah.nama_mtk

    class Meta:
        db_table = 'tbkrs'
        verbose_name_plural = 'KRS'
		
class Banner(models.Model):
    nama = models.CharField('Nama', max_length = 50)
    urutan = models.IntegerField('Urutan', choices=URUTAN_CHOICES)
    banner = models.ImageField(u'Banner', upload_to = 'img-banner')
            
    def __unicode__(self):
        return self.nama
                    
    class Meta:
        db_table = 'tbbanner'
        
class ProfileSoftware(models.Model):
    nama = models.CharField('Nama', max_length = 30)
    alamat = models.CharField('alamat', max_length = 200)
    
    def __unicode__(self):
        return self.nama
    
    class Meta:
        db_table = 'tbprofile_software'