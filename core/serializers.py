from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import *


class VacancySerializer(ModelSerializer):
    city = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'name',
            'salary',
            'responsibilities',
            'benefits',
            'city',
            'phone',
            'img',
        ]


class ApplyingSerializer(ModelSerializer):
    # vacancy = serializers.SlugRelatedField(
    #     # read_only=True,
    #     queryset=Vacancy.objects.filter(is_active=True),
    #     slug_field='name'
    # )

    class Meta:
        model = Applying
        fields = [
            'id',
            'name',
            'birthday',
            'email',
            'phone',
            'vacancy',
            'cv',
        ]
