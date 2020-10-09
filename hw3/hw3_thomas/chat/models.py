from django.db import models

class Room(models.Model):
	
	# Room title
	title = models.CharField(max_length=255)
	
	def __str__(self):
		return self.title
