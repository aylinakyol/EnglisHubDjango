sudo docker compose --env-file ~/Projects/EnglisHub/EnglisHubCommon/dev-environment.env -f ~/Projects/EnglisHub/EnglisHubCommon/dev-compose.yml up -d

sudo docker run -v ~/Projects/EnglisHub/EnglisHubDjango:/app --rm -it django-project-creator

django-admin startproject englishubdjango .

python manage.py startapp englishubdjango_app_api

sudo chown -R aylin:aylin ~/Projects/EnglisHub/EnglisHubDjango