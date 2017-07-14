from django.db import models
from django.conf import settings

mongo_client= settings.CLIENT
db = mongo_client.test
