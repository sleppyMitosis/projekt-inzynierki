from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile



from rest_framework.authtoken.models import Token


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'User logged in',
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # Add additional fields for registration if needed
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number', None)
        vet_phone_number = request.data.get('vet_phone_number', None)

        if not all([username, password, email]):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        UserProfile.objects.create(user=user, phone_number=phone_number, vet_phone_number=vet_phone_number)

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            user_profile = UserProfile.objects.get(user=user)
            return Response({
                'id': user.id,
                'first_name' : user.first_name,
                'last_name' : user.last_name,
                'username': user.username,
                'email': user.email,
                'phone_number': user_profile.phone_number,
                'vet_phone_number': user_profile.vet_phone_number
            }, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile does not exist"}, status=status.HTTP_404_NOT_FOUND)


class EditUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        vet_phone_number = request.data.get('vet_phone_number')

        # Update user model fields
        if username:
            user.username = username
        if email:
            user.email = email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        user.save()

        # Update or create the user profile
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if phone_number is not None:
            user_profile.phone_number = phone_number
        if vet_phone_number is not None:
            user_profile.vet_phone_number = vet_phone_number
        user_profile.save()

        return Response({"message": "User profile updated successfully"}, status=status.HTTP_200_OK)