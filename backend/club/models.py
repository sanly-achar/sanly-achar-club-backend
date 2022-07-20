from django.db import models
from datetime import datetime

class Status(models.Model):
	title = models.CharField(max_length=32)
	level = models.IntegerField()

	def __str__(self):
		return self.title

class MaterialGroup(models.Model):
	TYPE = [
		('video', 'video'),
		('audio', 'audio'),
		('book', 'book'),
	]
	title = models.CharField(max_length=32)
	status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True, related_name='materialgroup')
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="groups/" ,null=True, blank=True)
	intro_video = models.TextField(null=True, blank=True)
	group_type = models.CharField(max_length=32, choices=TYPE, default="video")

	def __str__(self):
		return self.title

class Video(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to="videos/", null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE, related_name='videos')
	video_ru = models.TextField()
	video_tm = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title


class Audio(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to="audio/", null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE, related_name='audios')
	audio_ru = models.TextField()
	audio_tm = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.now)
	pdf_ru = models.TextField(blank=True, null=True)
	pdf_tm = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title


class PDFMaterial(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to="pdf/", null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE, related_name='pdfmaterial')
	pdf_ru = models.TextField()
	pdf_tm = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title