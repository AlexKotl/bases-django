from django.db import models

class Base(models.Model):
    name = models.CharField(max_length=255)
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

    def __str__(self):
        return self.name

    def url_name(self):
        return name

    def get_all(self):
        return Base.objects.raw('''
            SELECT * FROM bases
            WHERE flag="ok"
            ORDER BY vip DESC, vip_end_date DESC, id DESC''')

    def get_latest(self):
        return Base.obkects.raw('''
            SELECT * FROM bases where flag='ok'
            ORDER BY FIELD(vip, 1) DESC,
            CASE
                WHEN vip = 1
                THEN vip_end_date
                ELSE id
                END
            DESC LIMIT 12''')

class Comments(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    band = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    date = models.DateTimeField()
    ip = models.CharField(max_length=15)