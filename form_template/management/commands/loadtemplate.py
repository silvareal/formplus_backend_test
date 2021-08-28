from django.core.management.base import BaseCommand, CommandError
import requests
from functools import lru_cache
import json
from form_template.models import Category, Template
import json
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

@lru_cache()
def fetch_templates(url):
    response = requests.get(url)
    return response

class Command(BaseCommand):
    help = 'Load Data to template DB'

    def handle(self, *args, **options):
        templates = r.get('templates')

        if templates is None:
            template = fetch_templates("https://front-end-task-dot-fpls-dev.uc.r.appspot.com/api/v1/public/task_templates")
            json_template = json.dumps(template.json())
            r.set('templates', json_template)

        for  template in json.loads(templates):
            template_name = template["name"]
            template_link = template["link"]
            template_description = template["description"]
            template_created = template["created"]
            template_category = template["category"]

            template_instance, template_created  = Template.objects.get_or_create(name=template_name, link=template_link, description=template_description, created=template_created)
            for category_name in template_category:
                category_instance, category_created = Category.objects.get_or_create(name=category_name)
                template_instance.category.add(category_instance)

