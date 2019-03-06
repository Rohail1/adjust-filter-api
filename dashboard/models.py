from django.db import models

# Create your models here.


class Dataset(models.Model):

    IOS = 'ios'
    ANDROID = 'android'
    LANGUAGE_OPTIONS = (
        (IOS, 'Ios'),
        (ANDROID, 'Android')
    )

    date = models.DateField()
    channel = models.CharField(max_length=50)
    country = models.CharField(max_length=3)
    os = models.CharField(choices=LANGUAGE_OPTIONS, default=IOS, max_length=10)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.DecimalField(max_digits=8, decimal_places=2)
    revenue = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Dataset'

    @property
    def get_cpi(self):
        return round(self.spend/self.installs, 2)
