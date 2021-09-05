from django.test import TestCase

from form_template.models import Template
from rest_framework import status
from rest_framework.test import APITestCase


class TemplateListViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_templates = 13

        for template_id in range(number_of_templates):
            template_instance = Template.objects.create(name='deserunt', description='cillum culpa', link="https://form.pl.template",
                                                        created="2021-08-28T07:29:48.174917")
            template_instance.category.create(name="health")
