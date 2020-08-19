from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from ckeditor.fields import RichTextField


class AboutManager(models.Manager):
	def get_about(self):
		about = self.all()
		if about:
		    return about[0]
		return None

@python_2_unicode_compatible
class About(models.Model):
	about = RichTextField()
	history = RichTextField()
	image = models.ImageField(
		upload_to='the_club',
		blank=True,
		null=True)
	objects = AboutManager()

	class Meta:
		verbose_name_plural = "About Us"

	def __str__(self):
		return "About Us"

	def save(self, *args, **kwargs):
	    """There should not be more than one About object."""
	    if About.objects.count() == 1 and not self.id:
	        raise Exception('Only one About Page object is allowed. Edit the existing About Page')
	    super(About, self).save(*args, **kwargs)


class SponsorshipManager(models.Manager):
	def get_sponsorship(self):
		sponsorship = self.all()
		if sponsorship:
		    return sponsorship[0]
		return None

@python_2_unicode_compatible
class Sponsorship(models.Model):
	content = RichTextField()
	image = models.ImageField(
		upload_to='the_club',
		blank=True,
		null=True)
	objects = SponsorshipManager()

	class Meta:
		verbose_name_plural = "Sponsorship"

	def __str__(self):
		return "Sponsorship"

	def save(self, *args, **kwargs):
	    """There should not be more than one Sponsorship object."""
	    if Sponsorship.objects.count() == 1 and not self.id:
	        raise Exception('Only one Sponsorship Page object is allowed. Edit the existing Sponsorship Page')
	    super(Sponsorship, self).save(*args, **kwargs)



class AchievementManager(models.Manager):
	def get_achievement(self):
		achievement = self.all()
		if achievement:
		    return achievement[0]
		return None

@python_2_unicode_compatible
class Achievement(models.Model):
	content = RichTextField()
	image = models.ImageField(
		upload_to='the_club',
		blank=True,
		null=True)
	objects = AchievementManager()

	class Meta:
		verbose_name_plural = "Achievement"

	def __str__(self):
		return "Achievement"

	def save(self, *args, **kwargs):
	    """There should not be more than one Achievement object."""
	    if Achievement.objects.count() == 1 and not self.id:
	        raise Exception('Only one Achievement Page object is allowed. Edit the existing Achievement Page')
	    super(Achievement, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Timeline(models.Model):
	year = models.PositiveIntegerField()
	title = models.CharField(max_length=100)
	content = RichTextField()
	achievement = models.ForeignKey(
		Achievement,
		blank=True,
		null=True)

	class Meta:
		ordering = ['-year']

	def __str__(self):
		return self.title


class StadiumManager(models.Manager):
	def get_stadium(self):
		stadium = self.all()
		if stadium:
		    return stadium[0]
		return None

@python_2_unicode_compatible
class Stadium(models.Model):
	content = RichTextField()
	objects = StadiumManager()

	class Meta:
		verbose_name_plural = "Stadium"

	def __str__(self):
		return "About Our Stadium"

	def save(self, *args, **kwargs):
	    """There should not be more than one Stadium object."""
	    if Stadium.objects.count() == 1 and not self.id:
	        raise Exception('Only one Stadium Page object is allowed. Edit the existing Stadium Page')
	    super(Stadium, self).save(*args, **kwargs)


@python_2_unicode_compatible
class StadiumPhoto(models.Model):
	image = models.ImageField(
		upload_to='stadium')
	caption = models.CharField(
		max_length=50)
	stadium = models.ForeignKey(
		Stadium,
		blank=True,
		null=True)

	def __str__(self):
		return self.caption

	class Meta:
		ordering = ['-id']



