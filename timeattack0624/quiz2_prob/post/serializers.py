from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet, SkillSet, JobType

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['company_name', 'id']

class JobtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['id']

class JobPostSerializer(serializers.ModelSerializer):
    position_type = serializers.SerializerMethodField(read_only=True)
    company = CompanySerializer(read_only=True)
    skillsets = serializers.SerializerMethodField(read_only=True)
    def get_skillsets(self, obj):
        return [skill_set.name for skill_set in obj.skillset_set.all()]
    def get_position_type(self, obj):
        return obj.job_type.job_type

    # skill_set = serializers.SerializerMethodField()
    # def get_skill_set(self,obj):
    #     return [obj.skill_set.name for obj in obj.joppostskillset_set.all()]

    def validate(self, data):
        print(f"data:{data}, context : {self.context.get('request')}")

        return data

    def create(self, validated_data):
        # print("validated_data : ",validated_data)
        # # job_type_obj = get_object_or_404(JobPost, id = validated_data.pop('job_type'))
        # new_job_post = JobPost(**validated_data)
        # return super().create(validated_data)

        request_data = self.context.get('request').data
        job_type = request_data.get("job_type")
        company_name = request_data.get("company_name")
        skillsets = list(map(int,request_data.get('skillsets')))
        job_post = JobPost.objects.create(**validated_data)
        job_post.job_type = JobType.objects.get(id= job_type)
        company_obj, _ = Company.objects.get_or_create(company_name = company_name)
        job_post.company = company_obj
        job_post.skillset_set.add(*skillsets)
        job_post.save()
        return job_post

    class Meta:
        model = JobPost
        fields = ["id","position_type", "company", "job_description","salary", "skillsets"]

class SkillSet_Serializer(serializers.ModelSerializer):
    job_posts = JobPostSerializer(many=True)
    class Meta:
        model = SkillSet
        fields = ['name', 'job_posts']

class JobPostSkillSet_Serializer(serializers.ModelSerializer):
    job_post = JobPostSerializer()
    class Meta:
        model = JobPostSkillSet
        fields = ['skill_set', 'job_post']
