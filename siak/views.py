# -*- coding: utf-8 -*-

from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from forms import *

# umum bagian site
def get_profile_software(request):
    profile = ProfileSoftware.objects.order_by('id')[0]
    return profile

def get_banner(request):
    banner = Banner.objects.all().order_by("urutan")
    return banner

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def cek_login_mahasiswa(request):
	if request.user.is_authenticated():
		mhs = get_or_none(Mahasiswa, user_id=request.user.id)
		if mhs is not None:
			return 1
		else:
			return 0
	else:
		return 0

def main(request):
    tahun_akademik = RegisterAkademik.objects.get(aktif=1)
    return render_to_response('main.html',
		{
			'tahun_akademik':tahun_akademik,
			'slides':get_banner(request),
			'profiles':get_profile_software(request)
		}, RequestContext(request))

# bagian mahasiswa
def mahasiswa(request):
	#if request.user.is_authenticated():
	#	return HttpResponseRedirect('/mhs-dashboard');
	#else:
	#	return render_to_response('main-page.htt', {}, RequestContext(request))
	profiles = ProfileSoftware.objects.order_by('id')[0]
	if request.method == 'GET':
		return render_to_response('login_mahasiswa.html', {'profiles':get_profile_software(request)}, RequestContext(request))
	else:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username = username, password = password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/mhs-dashboard')
		else:
			return render_to_response('login_mahasiswa.html', {'error': u'Password login tidak valid', 'profiles':get_profile_software(request)}, RequestContext(request))
			
def mhs_dashboard(request):
	if cek_login_mahasiswa(request) == 0:
		return HttpResponseRedirect('/mahasiswa')
	mhs =  Mahasiswa.objects.get(user__id=request.user.id)
	tahun_akademik = RegisterAkademik.objects.get(aktif=1)
	return render_to_response('mhs_dashboard.html', {
		'tahun_akademik':tahun_akademik.tahun_akademik,
		'nama_mahasiswa':mhs.nama,
		'profiles':get_profile_software(request)
		}, RequestContext(request))

def mhs_jadwal(request):
	if cek_login_mahasiswa(request) == 0:
		return HttpResponseRedirect('/mahasiswa')
	mhs =  Mahasiswa.objects.get(user__id=request.user.id)
	tahunakademik = RegisterAkademik.objects.get(aktif=1)
	jadwal_list = Jadwal.objects.select_related('tahun_akademik__mata_kuliah').filter(tahun_akademik__tahun_akademik=tahunakademik)
	return render_to_response('mhs_jadwal.html', {
		'tahun_akademik':tahunakademik.tahun_akademik,
		'nama_mahasiswa':mhs.nama,
		'jadwalb':jadwal_list,
		'profiles':get_profile_software(request)
		}, RequestContext(request))

def mhs_krs(request):
	if cek_login_mahasiswa(request) == 0:
		return HttpResponseRedirect('/mahasiswa')
	mhs =  Mahasiswa.objects.get(user__id=request.user.id)
	tahunakademik = RegisterAkademik.objects.get(aktif=1)
	jadwal_list = Jadwal.objects.select_related('tahun_akademik__mata_kuliah').filter(tahun_akademik__tahun_akademik=tahunakademik)
	try:
		x = RegisterMahasiswa.objects.get(tahun_akademik=tahunakademik)
		foo = x.tahun_akademik
	except RegisterMahasiswa.DoesNotExist:
		foo = None
	#form = KrsAmbilForm()
	return render_to_response('mhs_krs.html', {
		'tahun_akademik':tahunakademik.tahun_akademik,
		'krs':foo,
		'nama_mahasiswa':mhs.nama,
		'mahasiswa_list':mhs,
		'jadwal_list': jadwal_list,
		'profiles':get_profile_software(request)
		}, RequestContext(request))