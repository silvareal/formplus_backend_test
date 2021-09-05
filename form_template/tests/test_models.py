from django.test import TestCase
from form_template.models import Template


class TemplateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        template_instance = Template.objects.create(name='deserunt', description='cillum culpa', link="https://form.pl.template",
                                                    created="2021-08-28T07:29:48.174917")
        template_instance.category.create(name="health")

    def test_name_max_length(self):
        template = Template.objects.get(id=1)
        max_length = template._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_link_max_length(self):
        template = Template.objects.get(id=1)
        max_length = template._meta.get_field('link').max_length
        self.assertEqual(max_length, 50)

    def test_description_max_length(self):
        template = Template.objects.get(id=1)
        max_length = template._meta.get_field('description').max_length
        self.assertEqual(max_length, 200)

    def test_category_exist(self):
        template = Template.objects.get(id=1)
        self.assertTrue(template.category.exists())

    def test_exactly_category_created(self):
        template = Template.objects.get(id=1)
        self.assertTrue(template.category, 'health')
