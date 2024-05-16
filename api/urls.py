from django.urls import path
from .views import ApplicantListCreate, ApplicantRetrieveUpdateDestroy, SkillCreate

urlpatterns = [
    path("applicants/", ApplicantListCreate.as_view(), name="applicant-list-create"),
    path(
        "applicant/<int:pk>/",
        ApplicantRetrieveUpdateDestroy.as_view(),
        name="applicant-detail",
    ),
    path("applicant/<int:pk>/skill/", SkillCreate.as_view(), name="skill-create"),
]
