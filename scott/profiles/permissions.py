from rest_framework import permissions

class IsCandidateField(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		try:
			return obj.candidate.profile.identity == request.user
		except:
			return False

class IsCandidateOrEmployer(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		try:
			return obj.profile.identity == request.user
		except:
			return False

class IsProfile(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		try:
			return obj.identity == request.user
		except:
			return False
