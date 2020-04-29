from django.db import models
import os
from django.urls import reverse
# Create your models here.


class Post(models.Model):

	titlename = models.CharField(max_length = 100)
	thumbnailimage = models.ImageField(upload_to='thumbnail/')

	def __str__(self):
		return f'{self.title_name}'


	def delete(self , using=None , keep_parents=False):
		self.thumbnailimage.storage.delete(self.thumbnailimage.name)
		super().delete()








class Photo(models.Model):

	post = models.ForeignKey(Post,on_delete=models.DO_NOTHING)
	image = models.ImageField(upload_to='photo/',blank=True,null=True)

	def __str__(self):
		return self.post.titlename
	
	def delete(self , using=None , keep_parents=False):
		self.image.storage.delete(self.image.name)
		super().delete()


	def get_absolute_url(self):
		return reverse('image-detail',kwargs = {'pk':self.pk})