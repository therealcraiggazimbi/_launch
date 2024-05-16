from rest_framework import generics
from .models import Applicant, Skill
from .serializers import ApplicantSerializer, SkillSerializer


class ApplicantListCreate(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class ApplicantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class SkillCreate(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
