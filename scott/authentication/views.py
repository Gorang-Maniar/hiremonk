
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.contrib.auth import authenticate, login
from authentication.serializers import UserSerializer, GroupSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@csrf_exempt
def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            serialized_obj = serializers.serialize('json', 
                                                [User.objects.get(username=username),], 
                                                fields=('username','first_name','last_name','groups','email'))
            return HttpResponse(serialized_obj, content_type="json")
            # Redirect to a success page.
        else:
            pass
            # Return a 'disabled account' error message
    else:
        return HttpResponse("User couldn't be authenticated", content_type="json")

@csrf_exempt
def signup(request):

    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    try:
        new_user = User.objects.create_user(username, email, password)
        new_user.save()

    except:
        user = authenticate(username=username,password=password)
        if request.user.is_authenticated():
            new_user = User.objects.get(username=user.username)

    if new_user is not None:
        if new_user.is_active:
            serialized_obj = serializers.serialize('json', 
                                                [User.objects.get(username=username),], 
                                                fields=('username','first_name','last_name','groups','email'))
            return HttpResponse(serialized_obj, content_type="json")
            # Redirect to a success page.
        else:
            pass
            # Return a 'disabled account' error message
    else:
        return HttpResponse("User couldn't be created", content_type="json")