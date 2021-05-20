from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import status


# Create your views here.
from .serializers import UserSerializer , UserListSerializer
from .models import User

#Account Main 확인용.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#User 로그인.
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

#User 회원가입.
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
        return JsonResponse({
            "data" : serializer.data,
            "message" : "유효하지 않은 형식입니다."
        })
        # return Response("이미 사용된 이메일입니다.", status = status.HTTP_400_BAD_REQUEST)

#모든 User 정보 호출.
@api_view(['GET'])
def getUserAll(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    user_list = []
    for user in serializer.data:
        user_list.append(user)
    return_data = {
        "data" : user_list
    }
    return JsonResponse(return_data)

#해당 User 정보 삭제.
@api_view(['POST'])
def deleteUser(request):
    print("시작!!!!!!!!!!!!!!!!!!!!!!")
    print(request.data)
    user = get_object_or_404(User, email=request.data['email'])
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)