from django.db import models

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=200)
    slug = models.CharField(max_length=150)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " by " + self.author