from django.db import models
from django.forms import ValidationError

class Mahasiswa(models.Model):
	nim = models.CharField(u'Domain name', max_length = 64, help_text = 'Domain name to serve (example: bsmsite.com)', unique = True)
	nama = models.CharField(u'Notes', max_length = 1024, help_text = 'Anything about this domain')
	def __unicode__(self):
		return self.nim
	class Meta:
		db_table = 'tbmahasiswa'
