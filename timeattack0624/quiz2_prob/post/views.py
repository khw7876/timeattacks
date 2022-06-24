import imp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import JobPostSerializer
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
    # company를 views.py에서 하느냐, serilizers에서 처리를 하느냐
    def post(self, request):
        jobpost_serializer = JobPostSerializer(data = request.data, context = {"request" : request})
        if jobpost_serializer.is_valid():
            jobpost_serializer.save()
            return Response(jobpost_serializer.data, status=status.HTTP_200_OK)
        return Response(jobpost_serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        # job_type = int( request.data.get("job_type", None) )
        # company_name = request.data.get("company_name", None)
        # job_description = request.data.get("job_description", None)
        # salary = request.data.get("salary", None)
            

        
