from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Applicant, Skill


class ApplicantTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.applicant_data = {"name": "Craig Gazimbi"}
        self.applicant = Applicant.objects.create(name="Craig Gazimbi")

    def test_delete_applicant(self):
        response = self.client.delete(f"/api/applicant/{self.applicant.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Applicant.objects.count(), 0)

    def test_partial_update_applicant(self):
        partial_updated_data = {"name": "Craig Smith"}
        response = self.client.patch(
            f"/api/applicant/{self.applicant.id}/", partial_updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Applicant.objects.get(id=self.applicant.id).name, "Craig Smith"
        )

    def test_retrieve_applicant(self):
        response = self.client.get(f"/api/applicant/{self.applicant.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Craig Gazimbi")

    def test_update_applicant(self):
        updated_data = {"name": "Craig Smith"}
        response = self.client.put(f"/api/applicant/{self.applicant.id}/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Applicant.objects.get(id=self.applicant.id).name, "Craig Smith"
        )

    def test_create_skill(self):
        response = self.client.post(
            f"/api/applicant/{self.applicant.id}/skill/",
            {"name": "Python"},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Skill.objects.count(), 1)

    def test_get_all_applicants(self):
        response = self.client.get("/api/applicants/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
