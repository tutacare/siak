from django.conf.urls import patterns, include, url
from siak import views

urlpatterns = patterns('',
    url(r'^$', 'siak.views.main', name='home'),
    url(r'^logout/?$','siak.views.logout'),
	# url mahasiswa
	url(r'^mahasiswa/?', 'siak.views.mahasiswa'),
    url(r'^mhs-dashboard/?$','siak.views.mhs_dashboard'),
	url(r'^mhs-jadwal/?$','siak.views.mhs_jadwal'),
	url(r'^mhs-krs/?$','siak.views.mhs_krs'),
	url(r'^mhs-krs-add/?$','siak.views.mhs_krs_add'),
)