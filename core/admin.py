from django.contrib import admin
from core.models import *
from import_export.admin import ExportActionMixin


admin.site.register(City)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'city', 'count_applying', 'is_active')


@admin.register(Applying)
class ApplyingAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'vacancy', 'date_applying')
