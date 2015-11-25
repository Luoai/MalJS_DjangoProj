from django.db import models

# Create your models here.

class Virus(models.Model):
	MD5 = models.CharField(max_length=128)
	size_KB = models.DecimalField(max_digits=128,decimal_places=5,default=0)
	VirusTotal_link=models.URLField()
	Detection = models.TextField()

	def __unicode__(self):
		return self.MD5
