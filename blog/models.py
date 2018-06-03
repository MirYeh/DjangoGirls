from django.db import models
from django.utils import timezone

#Post is a subclass of django.db.models.Model
class Post(models.Model):
    #author is a foreign key in model Post
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #published_date allowed to be black and empty values will be stored as null
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
