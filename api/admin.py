from django.contrib import admin

from .models import Applicant, Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ApplicantAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ("id", "name")
    search_fields = ("name",)


admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Skill)
