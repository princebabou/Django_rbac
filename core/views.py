from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework import status

# Custom permissions
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Administrator").exists()

class IsAnalyst(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Analyst").exists()

# /data endpoint
class DataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # GET allowed for all authenticated users
        return Response({"message": "Data fetched successfully"})

# /config endpoint
class ConfigView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Configuration data"})

    def post(self, request):
        return Response({"message": "Configuration updated"}, status=status.HTTP_201_CREATED)
