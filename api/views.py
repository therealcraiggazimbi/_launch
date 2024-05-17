from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Applicant, Skill
from .serializers import ApplicantSerializer, SkillSerializer


class ApplicantListCreate(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class ApplicantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class SkillCreate(APIView):
    def post(self, request, pk, *args, **kwargs):
        try:
            applicant = Applicant.objects.get(pk=pk)
        except Applicant.DoesNotExist:
            return Response(
                {"error": "Applicant not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # Create a mutable copy of request.data
        mutable_data = request.data.copy()
        mutable_data["applicant"] = pk

        serializer = SkillSerializer(data=mutable_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
