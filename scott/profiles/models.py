from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Skill(models.Model):
        SKILL_TYPES = (
                ("L", "Language"),
                ("O", "Organisational"),
                ("T", "Technical")
        )
        skill_type = models.CharField(max_length = 1, choices = SKILL_TYPES)
        skill = models.CharField(max_length = 30, unique = True)#case-insensitive??
        description = models.CharField(max_length = 200)#length??

class Profile(models.Model):
	USER_TYPES = (
		("FRL", "Freelancer"),
		("CMY", "Company"),
		("MOD", "Moderator")
	)
	identity = models.OneToOneField(User)
	slug = models.SlugField(max_length = 100)
	summary = models.TextField(max_length = 400)
	user_type = models.CharField(max_length = 3, choices = USER_TYPES)
	#image = models.ImageField() #[upload_to, height_field, width_field, max_length
	#thumbnail_url = models.URLField(max_length = 200)
	#Username - foreign key in User
	#First Name - foreign key in User
	#Last Name - foreign key in User
	#Email - foreign key in User
	#Password - foreign key in User
	#Locations - OneToMany in Location
	#Contacts - OneToMany in Contact

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.identity.username)
		super(Profile, self).save(*args, **kwargs)

class Candidate(models.Model):
	profile = models.OneToOneField(Profile)
	description = models.TextField()
	skills = models.ManyToManyField(Skill, related_name="candidates")
	#Expectations - OneToMany in Expectation
	#Educations - OneToMany in Education
	#Past Experiences - OneToMany in Experience
	#Recommendations - OneToMany in Recommendation
	#Portfolios - OneToMany in Portfolio

class Expectation(models.Model):
	JOB_TYPES = (
		("P", "Part Time"),
		("F", "Full Time")
	)
	CURRENCY_TYPES = (
		("USD", "US Dollar"),
		("INR", "Indian Rupee")
	)

	job_type = models.CharField(max_length = 1, choices = JOB_TYPES)
	compensation = models.PositiveIntegerField()
	currency = models.CharField(max_length = 3, choices = CURRENCY_TYPES)
	duration = models.PositiveSmallIntegerField()#DAYS
	role = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	country = models.CharField(max_length = 50)
	candidate = models.ForeignKey(Candidate, related_name='expectations')

class Education(models.Model):
	school_name = models.CharField(max_length = 100)
	degree = models.CharField(max_length = 100)#Choices list??
	description = models.TextField()
	start = models.DateField()
	end = models.DateField()
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	country = models.CharField(max_length = 50)
	candidate = models.ForeignKey(Candidate, related_name='educations')

class Experience(models.Model):
	company_name = models.CharField(max_length = 100)
	role = models.CharField(max_length = 50)
	description = models.TextField()
	start = models.DateField()
	end = models.DateField()
	duration = models.PositiveSmallIntegerField()#Days
	candidate = models.ForeignKey(Candidate, related_name='experiences')

	def save(self, *args, **kwargs):
		self.duration=((self.end)-(self.start)).days
		super(Experience, self).save(*args, **kwargs)

class Recommendation(models.Model):
	recommender_name = models.CharField(max_length = 100)
	description = models.TextField()
	candidate = models.ForeignKey(Candidate, related_name='recommendations')

class Portfolio(models.Model):
	project_name = models.CharField(max_length = 100)
	description = models.TextField()
	link = models.URLField(max_length = 200)
	candidate = models.ForeignKey(Candidate, related_name='portfolios')

class Location(models.Model):
	numeric = RegexValidator(r'[0-9]*$', 'Only numbers are allowed')
	
	street = models.CharField(max_length = 200)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	country = models.CharField(max_length = 50)#Enumerate countries and use code??
	zipcode = models.CharField(max_length = 6, validators = [numeric])#Length??
	profile = models.ForeignKey(Profile, related_name='locations')

class Contact(models.Model):
	numeric = RegexValidator(r'[0-9]*$', 'Only numbers are allowed')

	mobile = models.CharField(max_length = 10, validators = [numeric])#Length?? include country code as a separate field??
	work = models.CharField(max_length = 10, validators = [numeric])#Length??
	email = models.EmailField(max_length = 50)
	profile = models.ForeignKey(Profile, related_name='contacts')

class Employer(models.Model):	
	INDUSTRY_TYPES = (
		("IT", "Information Technology"),
		("EDU", "Education"),
		("MKT", "Marketing")
	)

	profile = models.OneToOneField(Profile)
	organisation_name = models.CharField(max_length = 200)#Length??
	description = models.TextField()
	industry = models.CharField(max_length = 3, choices = INDUSTRY_TYPES)#Add more Choices
	#Jobs - OneToMany in Jobs.Job
