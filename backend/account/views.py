from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import status


# Create your views here.
from .serializers import UserSerializer , UserListSerializer
from .models import User

#jwt관련 라이브러리
import jwt
#jwt토큰에서 사용될 시크릿키.
JWT_SECRET_KEY = 'm_&@=qxne#1+=2brho6rt)8a*3s#98$z^hi3uw)yaik(qyuk6!'


#Account Main 확인용.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#User 로그인.
@api_view(['POST'])
def getUser(request):
    if User.objects.filter(email=request.data['email']).exists():
        user = get_object_or_404(User, email=request.data['email'])
        if request.data['pw'] != user.pw:
            return JsonResponse({
                "data" : "",
                "message" : "비밀번호가 틀렸습니다."
            })
            #return Response("비밀번호가 틀렸습니다.", status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(user)
            user_id = serializer.data['email']
            #토큰발행
            token = jwt.encode({'id' : user_id}, JWT_SECRET_KEY, algorithm = "HS256")
            token = token.decode('utf-8')

            #제이슨 타입으로 리턴
            return JsonResponse({
                "token" : token,
			    "data" : serializer.data
		    })
    else:
        return JsonResponse({
            "data" : "",
            "message" : "존재하지 않는 이메일입니다."
        })
        #return Response("존재하지 않는 이메일입니다.", status=status.HTTP_204_NO_CONTENT)

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
    print(request.data)
    user = get_object_or_404(User, email=request.data['email'])
    user.delete()
    return JsonResponse({
            "message" : "삭제 완료했습니다."
        })


#User 정보 수정.
@api_view(['PUT'])
def updateUser(request):
    user = get_object_or_404(User, email=request.data['email'])
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return JsonResponse({
            "message" : "수정 완료했습니다." ,
            "data" : serializer.data
        })
    else:
        return JsonResponse({
            "message" : "수정 실패했습니다.",
            "data" : serializer.data
        })

