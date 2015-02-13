from rest_framework import serializers
from jobs.models import *
from django.contrib.auth.models import User

class JobSerializer(serializers.HyperlinkedModelSerializer):
	required_skills = serializers.HyperlinkedRelatedField(many=True, view_name='skill-detail')
	benefits = serializers.HyperlinkedRelatedField(many=True, view_name='benefit-detail')
	locations = serializers.HyperlinkedRelatedField(many=True, view_name='location-detail')
	contacts = serializers.HyperlinkedRelatedField(many=True, view_name='contact-detail')
	employer = serializers.HyperlinkedRelatedField(many=True, view_name='employer-detail')
	candidates = serializers.HyperlinkedRelatedField(many=True, view_name='candidate-detail')
	class Meta:
		model = Job
		fields = ('id', 'title', 'description', 'overview', 'job_type', 'industry', 'category', 'compensation', 'currency', 'role', 'start', 'end', 'duration', 'role', 'required_skills', 'benefits', 'locations', 'contacts', 'employer', 'candidates')

class BenefitSerializer(serializers.HyperlinkedModelSerializer):
	job = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail')
	class Meta:
		model = Benefit
		fields = ('id', 'benefit', 'description', 'job')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
	job = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail')
	class Meta:
		model = Location
		fields = ('id', 'job', 'street', 'city', 'state', 'country', 'zipcode')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	job = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail')
	class Meta:
		model = Contact
		fields = ('id', 'job', 'mobile', 'work', 'email')
