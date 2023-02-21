from django.db import models


class Photo(models.Model):
	image = models.ImageField(
		upload_to='gallery')
	caption = models.CharField(
		max_length=50)


	def __str__(self):
		return self.caption

	class Meta:
		ordering = ['-id']


class Video(models.Model):
	embed_code = models.TextField()
	title = models.CharField(
		max_length=100)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']

		