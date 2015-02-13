#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from profiles.serializers import *
from authentication.serializers import *
from django.contrib.auth.models import User
from profiles.models import *
from rest_framework import permissions
from profiles.permissions import *

class SkillViewSet(viewsets.ModelViewSet):
	queryset = Skill.objects.all()
	serializer_class = SkillSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsProfile,)

	def pre_save(self, obj):
		obj.identity = self.request.user

class CandidateViewSet(viewsets.ModelViewSet):
	queryset = Candidate.objects.all()
	serializer_class = CandidateSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsCandidateOrEmployer,)

	def pre_save(self, obj):
		profile = Profile.objects.filter(identity = self.request.user)[0]
		if profile.user_type == 'FRL':
			self.profile = profile
	#ELSE RAISE ERROR LOOK AT REST API EXCEPTION HANDLING

class EmployerViewSet(viewsets.ModelViewSet):
	queryset = Employer.objects.all()
	serializer_class = EmployerSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsCandidateOrEmployer,)

	def pre_save(self, obj):
		profile = Profile.objects.filter(identity = self.request.user)[0]
		if profile.user_type == 'CMY':
			obj.profile = profile
	#ELSE RAISE ERROR

class ExpectationViewSet(viewsets.ModelViewSet):
	queryset = Expectation.objects.all()
	serializer_class = ExpectationSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsCandidateField,)

	def pre_save(self, obj):
		obj.candidate = Candidate.objects.filter( profile = Profile.objects.filter(identity = self.request.user)[0] )[0]

class EducationViewSet(viewsets.ModelViewSet):
	queryset = Education.objects.all()
	serializer_class = EducationSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsCandidateField,)

	def pre_save(self, obj):
		obj.candidate = Candidate.objects.filter( profile = Profile.objects.filter(identity = self.request.user)[0] )[0]

class ExperienceViewSet(viewsets.ModelViewSet):
	queryset = Experience.objects.all()
	serializer_class = ExperienceSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsCandidateField,)

	def pre_save(self, obj):
		obj.candidate = Candidate.objects.filter( profile = Profile.objects.filter(identity = self.request.user)[0] )[0]

class RecommendationViewSet(viewsets.ModelViewSet):
	queryset = Recommendation.objects.all()
	serializer_class = RecommendationSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsCandidateField,)

	def pre_save(self, obj):
		obj.candidate = Candidate.objects.filter( profile = Profile.objects.filter(identity = self.request.user)[0] )[0]

class PortfolioViewSet(viewsets.ModelViewSet):
	queryset = Portfolio.objects.all()
	serializer_class = PortfolioSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsCandidateField,)

	def pre_save(self, obj):
		obj.candidate = Candidate.objects.filter( profile = Profile.objects.filter(identity = self.request.user)[0] )[0]

class LocationViewSet(viewsets.ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsProfile,)

	def pre_save(self, obj):
		obj.profile = Profile.objects.filter(identity = self.request.user)[0]

class ContactViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
			      IsProfile,)

	def pre_save(self, obj):
		obj.profile = Profile.objects.filter(identity = self.request.user)[0]
