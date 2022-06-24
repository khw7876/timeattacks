from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet, SkillSet

class Company_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['company_name', 'business_area']

class job_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['job_type']

class JobPost_Serializer(serializers.ModelSerializer):
    job_type = job_type_Serializer()
    company = Company_Serializer()

    def validate(self, data):
        print(f"data:{data}")
        return data

    def create(self, validated_data):
        print("validated_data : ",validated_data)
        job_type_obj = get_object_or_404(JobPost, id = validated_data.pop('job_type'))
        new_job_post = JobPost(**validated_data)
        return super().create(validated_data)

    class Meta:
        model = JobPost
        fields = ['job_type', 'company', "job_description", 'salary']

class SkillSet_Serializer(serializers.ModelSerializer):
    job_posts = JobPost_Serializer(many=True)
    class Meta:
        model = SkillSet
        fields = ['name', 'job_posts']

class JobPostSkillSet_Serializer(serializers.ModelSerializer):
    skill_set = SkillSet_Serializer()
    job_post = JobPost_Serializer()
    class Meta:
        model = JobPostSkillSet
        fields = ['skill_set', 'job_post']
