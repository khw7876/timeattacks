from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet, SkillSet

class Company_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['company_name', 'id']

class job_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['job_type']

class JobPost_Serializer(serializers.ModelSerializer):
    job_type = job_type_Serializer()
    company = Company_Serializer(read_only = True)

    skill_set = serializers.SerializerMethodField()
    def get_skill_set(self,obj):
        return [i.skill_set.name for i in obj.joppostskillset_set.all()]

    position_type = serializers.SerializerMethodField()
    def get_position_type(self,obj):
        return obj.job_type.job_type

        
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
        fields = ['id', 'position_type','skill_set', 'company', "job_description", 'salary']

class SkillSet_Serializer(serializers.ModelSerializer):
    job_posts = JobPost_Serializer(many=True)
    class Meta:
        model = SkillSet
        fields = ['name', 'job_posts']

class JobPostSkillSet_Serializer(serializers.ModelSerializer):
    job_post = JobPost_Serializer()
    class Meta:
        model = JobPostSkillSet
        fields = ['skill_set', 'job_post']
