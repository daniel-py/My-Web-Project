from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=225)
	slug = models.SlugField(max_length = 225, unique = True)
	created = models.DateTimeField(auto_now_add = True)
	image = models.ImageField(upload_to = 'img')

	class meta:
		ordering = ('-created',)
		def __unicode__(self):
			return '%s'%self.title
	def get_absolute_url(self):
		return reverse('webpage.views.achievement', args= (self.slug))	