from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)

    def _srt_(self):
        return self.name
