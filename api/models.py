from django.db import models


class Applicant(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=80)
    applicant = models.ForeignKey(
        Applicant, related_name="skills", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
