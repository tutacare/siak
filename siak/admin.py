from django.contrib import admin
from models import *

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'tahun_akademik',)
    search_fields = ('nim', 'nama')

class BannerAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False

class ProfileSoftwareAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False

class MataKuliahAdmin(admin.ModelAdmin):
    pass
    
class RegisterAkademikAdmin(admin.ModelAdmin):
    list_display = ('tahun_akademik', 'aktif')

class RegisterMahasiswaAdmin(admin.ModelAdmin):
    list_display = ('tahun_akademik', 'nim', 'tanggal_register', 'aktif')
    list_filter = ('tahun_akademik',)
	
class JadwalAdmin(admin.ModelAdmin):
    list_display = ('tahun_akademik', 'prodi', 'mata_kuliah', 'jurusan')

class KrsAdmin(admin.ModelAdmin):
    list_display = ('nama_mahasiswa', 'nama_mata_kuliah')

admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(ProfileSoftware, ProfileSoftwareAdmin)
admin.site.register(Agama)
admin.site.register(Dosen)
admin.site.register(Fakultas)
admin.site.register(NamaHari)
admin.site.register(ProgramStudi)
admin.site.register(Jurusan)
admin.site.register(Krs, KrsAdmin)
admin.site.register(RegisterMahasiswa, RegisterMahasiswaAdmin)
admin.site.register(Jadwal, JadwalAdmin)
admin.site.register(RegisterAkademik, RegisterAkademikAdmin)
admin.site.register(MataKuliah, MataKuliahAdmin)