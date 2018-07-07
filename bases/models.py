from django.db import models
import os.path
from .settings_private import *

class Base(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    pos_x = models.FloatField(default=0)
    pos_y = models.FloatField(default=0)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    date_added = models.DateTimeField('Date created')
    date_edited = models.DateTimeField('Date edited')
    flag = models.CharField(max_length=10)
    rating = models.FloatField(default=0)
    votes = models.IntegerField(default=0)
    visits = models.IntegerField(default=0)
    # user_id = models.IntegerField(default=0)
    vip = models.IntegerField(default=0)
    vip_end_date = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'bases'

    def __str__(self):
        return "{name} ({id})".format(name=self.name, id=self.id)

    def url_name(self):
        return name

    def get_all(self):
        return Base.objects.raw('''
            SELECT *, (unix_timestamp(now()) - unix_timestamp(date_edited)) as deltatime FROM bases
            WHERE flag="ok"
            ORDER BY vip DESC, vip_end_date DESC, id DESC''')

    def get_latest(self):
        return Base.objects.raw('''
            SELECT * FROM bases where flag='ok'
            ORDER BY FIELD(vip, 1) DESC,
            CASE
                WHEN vip = 1
                THEN vip_end_date
                ELSE id
                END
            DESC LIMIT 12''')

    def get_images(self):
        images = []
        for num in range(1,6):
            if os.path.isfile("{dir}/{base_id}_{num}.jpg".format(dir=PHOTOS_LOCATION, base_id=self.id, num=num)):
                images.append("{server}/{base_id}_{num}.jpg".format(server=PHOTOS_SERVER, base_id=self.id, num=num))
        return images

class Comments(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    band = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    date = models.DateTimeField()
    ip = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'comments'
