from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import User
from .serializers import UserSerializerIn, UserSerializerOut

@api_view(["GET", "POST"])  # Define function-base view for /users
def handle_users(request: Request) -> Response:
    if request.method == "GET":  # Draw all users and dump them as JSON
        users = User.objects.all()
        serializer = UserSerializerOut(users, many=True)
        return Response(serializer.data)
    elif request.method == "POST":  # Create a new user from JSON payload and dump all user properties as JSON
        serializer_in = UserSerializerIn(data=request.data)
        if serializer_in.is_valid():
            user = serializer_in.save()
            serializer_out = UserSerializerOut(user)
            return Response(serializer_out.data, status.HTTP_201_CREATED)
        return Response(serializer_in.errors, status.HTTP_400_BAD_REQUEST)