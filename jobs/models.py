from __future__ import unicode_literals

from django.db import models

job_types = ( ('remote', 'Remote'), ('visa', 'Visa'), ('intern', 'Intern') )

class JobApplication(models.Model):

    company = models.CharField(max_length=255)
    place = models.CharField(max_length=255)

    source = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)

    application_type = models.CharField(max_length=255, blank=True)
    response = models.CharField(max_length=255, blank=True)
    active = models.BooleanField()

    comments = models.TextField(max_length=512, blank=True)
    job_type = models.CharField(choices=job_types, max_length=32)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return ' - '.join([self.company, self.place])

class JobUpdate(models.Model):
    application = models.ForeignKey(JobApplication, related_name='updates')
    update = models.TextField(max_length=1024)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.update

