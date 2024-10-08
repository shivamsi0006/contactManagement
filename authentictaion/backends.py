import jwt
from rest_framework import authentication,exceptions
from django.conf import settings
from django.contrib.auth.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        auth_data=authentication.get_authorization_header(request)
    
        if not auth_data:
            return None
        
        token=auth_data.decode('utf-8')
        try:
            payload=jwt.decode(token,settings.JWT_SECRET_KEY,algorithms=["HS256"])
        
            user=User.objects.get(username=payload['username'])
            return (user,token)
        
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your authentication token is invalid')
        
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("your token is expired,login again")
        
        return super().authenticate(request)