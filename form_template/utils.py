import requests
import os
from functools import lru_cache
import json
from form_template.models import Category

filepath = os.path.join(os.getcwd(), 'fixtures', "template.json")

@lru_cache
def fetch_templates(url):
    response = requests.get(url)
    return response

templates = fetch_templates( "https://front-end-task-dot-fpls-dev.uc.r.appspot.com/api/v1/public/task_templates")

final_template_fixture = []
for index, template in enumerate(templates.json()):
    template["model"] = "template.template"
    template["pk"] = index
    category = template["category"]
    category_id = []
    for category_name in category:
        category_pk= Category.objects.get_or_create(name=category_name).id
        category_id.push(category_pk) 
    template["category"] = category_id
    final_template_fixture.append(template)

with open(filepath, "w") as file:
    json.dump(final_template_fixture, file)

