from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
	user = models.ForeignKey(User,
							 related_name='actions',
							 db_index=True)
	verb = models.CharField(max_length=255)
	# you can define the parameter limit_choices_to 
	# to define the allowed values for target_ct
	target_ct = models.ForeignKey(ContentType,
								  blank=True,
								  null=True,
								  related_name='target_ob')
	target_id = models.PositiveIntegerField(null=True,
											blank=True,
											db_index=True)
	target = GenericForeignKey('target_ct', 'target_id')
	created = models.DateTimeField(auto_now_add=True,
								   db_index=True)

	class Meta:
		ordering = ('-created',)
