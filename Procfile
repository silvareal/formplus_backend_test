web: gunicorn formplus.wsgi  --log-file -

worker: celery -A  worker -B -l info
