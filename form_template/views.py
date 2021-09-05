from django.db.models import query
from form_template.models import Template
from django.shortcuts import render
from rest_framework import pagination
from .serializers import TemplateSerializer
from rest_framework import generics


class CustomPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 500
    page_query_param = 'page'


class TemplateListView(generics.ListAPIView):
    serializer_class = TemplateSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        """
         Optionally restricts the returned template to a given Category,
         by filtering against a `category_name` query parameter in the URL.
         Searching against a `template_name` query parameter in the URL.
         sorting against the `template_name` and `template_created_date` query parameter in the URL.
         """

        sort_by_query = self.request.query_params.get('sort_by')
        order_by_query = self.request.query_params.get('order_by')
        search_query = self.request.query_params.get('search')
            
        queryset = Template.objects.all()
        category = self.request.query_params.get('category')
        
        if (category is not None) & (category !=  "All"):
            queryset = queryset.filter(category__name=category)

        if sort_by_query is not None:
            if (order_by_query == "Descending"):
                queryset = queryset.order_by(f"-{sort_by_query}")
            else:
                queryset = queryset.order_by(sort_by_query)

        if search_query is not None:
            queryset = queryset.filter(name__contains=search_query)
        return queryset
