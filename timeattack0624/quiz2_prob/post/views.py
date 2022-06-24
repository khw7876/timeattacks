import imp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import JobPost_Serializer
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):
    
    def post(self, request):
        jobpost_serializer = JobPost_Serializer(data = request.data)
        if jobpost_serializer.is_valid():
            jobpost_serializer.save()
            return Response(jobpost_serializer.data, status=status.HTTP_200_OK)
        return Response(jobpost_serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        # job_type = int( request.data.get("job_type", None) )
        # company_name = request.data.get("company_name", None)
        # job_description = request.data.get("job_description", None)
        # salary = request.data.get("salary", None)
            

        
