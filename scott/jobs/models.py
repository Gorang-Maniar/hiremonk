from django.db import models
from profiles.models import Candidate, Employer, Skill
from django.core.validators import RegexValidator

class Job(models.Model):
        JOB_TYPES = (
                ("P", "Part Time"),
                ("F", "Full Time")
        )
        CURRENCY_TYPES = (
                ("USD", "US Dollar"),
                ("INR", "Indian Rupee")
        )
	INDUSTRY_TYPES = (
                ("IT", "Information Technology"),
                ("EDU", "Education"),
                ("MKT", "Marketing")
        )
	CATEGORY_TYPES = (
                ("SW", "Software"),
                ("RnD", "Research and Development")
        )

	title = models.CharField(max_length = 200)
	description = models.TextField()
	overview = models.TextField()
        job_type = models.CharField(max_length = 1, choices = JOB_TYPES)
        industry = models.CharField(max_length = 3, choices = INDUSTRY_TYPES)#Add more Choices
        category = models.CharField(max_length = 3, choices = CATEGORY_TYPES)#Add more Choices
        compensation = models.PositiveIntegerField()
        currency = models.CharField(max_length = 3, choices = CURRENCY_TYPES)
        role = models.CharField(max_length = 50)
	start = models.DateField()
        end = models.DateField()
        duration = models.PositiveSmallIntegerField()#Days
	required_skills = models.ManyToManyField(Skill, related_name="jobs")
	employer = models.ForeignKey(Employer, related_name="jobs_employer")
	candidates = models.ManyToManyField(Candidate, related_name="jobs_candidates")
	#Benefits - OneToMany in Benefit
	#Contacts - OneToMany in Contact
	#Locations - OneToMany in Location

        def save(self, *args, **kwargs):
                self.duration=((self.end)-(self.start)).days
                super(Experience, self).save(*args, **kwargs)

class Benefit(models.Model):
	benefit = models.CharField(max_length = 100)
        description = models.TextField()
        job = models.ForeignKey(Job, related_name='benefits')

class Location(models.Model):
        numeric = RegexValidator(r'[0-9]*$', 'Only numbers are allowed')

        street = models.CharField(max_length = 200)
        city = models.CharField(max_length = 50)
        state = models.CharField(max_length = 50)
        country = models.CharField(max_length = 50)#Enumerate countries and use code??
        zipcode = models.CharField(max_length = 6, validators = [numeric])#Length??
        job = models.ForeignKey(Job, related_name='locations')

class Contact(models.Model):
        numeric = RegexValidator(r'[0-9]*$', 'Only numbers are allowed')

        mobile = models.CharField(max_length = 10, validators = [numeric])#Length?? include country code as a separate field??
        work = models.CharField(max_length = 10, validators = [numeric])#Length??
        email = models.EmailField(max_length = 50)
        job = models.ForeignKey(Job, related_name='contacts')
