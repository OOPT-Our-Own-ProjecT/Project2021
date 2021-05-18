from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import status


# Create your views here.
from .serializers import UserSerializer
from .models import User

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['POST'])
def login(request):
    if User.objects.filter(email=request.data['email']).exists():
        user = get_object_or_404(User, email=request.data['email'])
        if request.data['pw'] != user.pw:
            return Response("비밀번호가 틀렸습니다.", status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(user)
            #제이슨 타입으로 리턴
            return JsonResponse({
			    "data" : serializer.data
		    })
    else:
        return Response("존재하지 않는 이메일입니다.", status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def signUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        #제이슨 타입으로 리턴
        return JsonResponse({
            "data" : serializer.data
        })
    else:
        return Response("이미 사용된 이메일입니다.", status = status.HTTP_400_BAD_REQUEST)



