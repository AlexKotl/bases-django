from django.db import models

class Base(models.Model):
    name = models.CharField(max_length=255)

    def url_name(self):
        return name

    def get_all(self):
        return ['base1', 'base2']
