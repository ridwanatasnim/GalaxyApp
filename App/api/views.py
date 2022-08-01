from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.core.mail import send_mail

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getRoutes(request):

    routes=[
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)



@api_view(['POST','GET'])
def contact(request):
    if request.method == "POST":
        email_subject = request.data.get('Subject')
        sent_to = request.data.get('To')
        email_body = request.data.get('Email Body')
        
        send_mail(
            email_subject, # subject
            email_body, # message
            'galaxyapp365@gmail.com', # from email
            sent_to, # to email
        )
    return Response('Email Sent!')
