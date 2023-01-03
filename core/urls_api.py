from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('vacancy/',
        views.VacancyList.as_view(),
        name='vacancy-list'),
    path('vacancy/<int:pk>/',
        views.VacancyList.as_view(),
        name='vacancy-detail'),
    # path('applying/',
    #     views.ApplyingList.as_view(),
    #     name='applying-list'),
    path('applying',
        views.ApplyingDetail.as_view(),
        name='applying-detail'),
])
