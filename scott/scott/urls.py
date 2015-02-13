from django.conf.urls import patterns, include, url
from rest_framework import routers
from authentication import views as auth
from profiles import views as prof

router = routers.DefaultRouter()
router.register(r'api/0/skills', prof.SkillViewSet)
router.register(r'api/0/profiles', prof.ProfileViewSet)
router.register(r'api/0/candidates', prof.CandidateViewSet)
router.register(r'api/0/employers', prof.EmployerViewSet)
router.register(r'api/0/expectations', prof.ExpectationViewSet)
router.register(r'api/0/educations', prof.EducationViewSet)
router.register(r'api/0/experiences', prof.ExperienceViewSet)
router.register(r'api/0/recommendations', prof.RecommendationViewSet)
router.register(r'api/0/portfolios', prof.PortfolioViewSet)
router.register(r'api/0/locations', prof.LocationViewSet)
router.register(r'api/0/contacts', prof.ContactViewSet)
router.register(r'api/0/users', auth.UserViewSet)
router.register(r'api/0/groups', auth.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/0/signin/','authentication.views.signin'),
    url(r'^api/0/signup/','authentication.views.signup'),
]
