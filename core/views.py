from django.views import View
from django.views.generic import TemplateView, ListView
from rest_framework.renderers import TemplateHTMLRenderer

from core.models import *
from core.serializers import VacancySerializer, ApplyingSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'vacancy': reverse('vacancy-list', request=request, format=format),
        # 'applying': reverse('applying-list', request=request, format=format),
    })


class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.filter(is_active=True)
    serializer_class = VacancySerializer


class ApplyingList(generics.ListCreateAPIView):
    queryset = Applying.objects.all()
    serializer_class = ApplyingSerializer


class ApplyingDetail(generics.CreateAPIView):
    queryset = Applying.objects.all()
    serializer_class = ApplyingSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        return super().post(request, *args, **kwargs)


class IndexView(ListView):
    template_name = 'core/index.html'
    model = Vacancy
    queryset = Vacancy.objects.filter(is_active=True)
