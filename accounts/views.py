from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, UserSerializer, UpdateProfileSerializer, AdminCreateUserSerializer, UserRole
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from Base.permissions import IsAdmin  # your custom role-based permission
from .models import Role

# Create your views here.
class AdminCreateUserView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = AdminCreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRoleView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]
        return [AllowAny()]
    def get(self, request):
        roles = Role.objects.all()
        serializer = UserRole(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserRole(data=request.data)
        if serializer.is_valid():
            role = serializer.save()
            return Response(
                UserRole(role).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def get_jwt_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'msg': 'Login successful',
            'data':{
                'token':{
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
                }}

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            token_data = self.get_jwt_token(user)
            token_data["data"]["user"] =  UserSerializer(user).data
                                    

            return Response(token_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request):
        serializer = UpdateProfileSerializer(
            request.user,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            UserSerializer(request.user).data,
            status=status.HTTP_200_OK,
        )
