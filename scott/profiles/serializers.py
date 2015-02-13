from rest_framework import serializers
from profiles.models import *
from django.contrib.auth.models import User

class SkillSerializer(serializers.HyperlinkedModelSerializer):
	candidates = serializers.HyperlinkedRelatedField(many=True, view_name='candidate-detail')
	class Meta:
		model = Skill
		fields = ('id', 'candidates', 'skill_type', 'skill', 'description')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	identity = serializers.Field(source='identity.username')
	locations = serializers.HyperlinkedRelatedField(many=True, view_name='location-detail')
	contacts = serializers.HyperlinkedRelatedField(many=True, view_name='contact-detail')
	class Meta:
		model = Profile
		fields = ('id', 'identity', 'user_type', 'summary', 'locations', 'contacts')

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
	profile = serializers.Field(source='profile.identity.username')
	skills = serializers.HyperlinkedRelatedField(many=True, view_name='skill-detail')
	experiences = serializers.HyperlinkedRelatedField(many=True, view_name='experience-detail')
	portfolios = serializers.HyperlinkedRelatedField(many=True, view_name='portfolio-detail')
	recommendations = serializers.HyperlinkedRelatedField(many=True, view_name='recommendation-detail')
	educations = serializers.HyperlinkedRelatedField(many=True, view_name='education-detail')
	expectations = serializers.HyperlinkedRelatedField(many=True, view_name='expectation-detail')
	class Meta:
		model = Candidate
		fields = ('id', 'profile', 'skills', 'experiences', 'portfolios', 'recommendations', 'educations', 'expectations', 'description')

class EmployerSerializer(serializers.HyperlinkedModelSerializer):
	profile = serializers.Field(source='profile.identity.username')
	class Meta:
		model = Employer
		fields = ('id', 'profile', 'organisation_name', 'description')

class ExpectationSerializer(serializers.HyperlinkedModelSerializer):
	candidate = serializers.Field(source='candidate.profile.identity.username')
	class Meta:
		model = Expectation
		fields = ('id', 'candidate', 'job_type', 'compensation', 'currency', 'duration', 'role', 'city', 'state', 'country')

class EducationSerializer(serializers.HyperlinkedModelSerializer):
	candidate = serializers.Field(source='candidate.profile.identity.username')
	class Meta:
		model = Education
		fields = ('id', 'candidate', 'school_name', 'degree', 'description', 'start', 'end', 'city', 'state', 'country')

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
	candidate = serializers.Field(source='candidate.profile.identity.username')
	class Meta:
		model = Experience
		fields = ('id', 'candidate', 'company_name', 'role', 'description', 'start', 'end', 'duration')

class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
	candidate = serializers.Field(source='candidate.profile.identity.username')
	class Meta:
		model = Recommendation
		fields = ('id', 'candidate', 'recommender_name', 'description')

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
	candidate = serializers.Field(source='candidate.profile.identity.username')
	class Meta:
		model = Portfolio
		fields = ('id', 'candidate', 'project_name', 'description', 'link')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
	profile = serializers.Field(source='profile.identity.username')
	class Meta:
		model = Location
		fields = ('id', 'profile', 'street', 'city', 'state', 'country', 'zipcode')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	profile = serializers.Field(source='profile.identity.username')
	class Meta:
		model = Contact
		fields = ('id', 'profile', 'mobile', 'work', 'email')
