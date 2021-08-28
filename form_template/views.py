from form_template.models import Template
from django.shortcuts import render
from rest_framework import pagination
from .serializers import TemplateSerializer
from rest_framework import generics

class CustomPagination(pagination.PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param = 'page'

class TemplateListView(generics.ListAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    pagination_class = CustomPagination

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return Purchase.objects.filter(purchaser=user)