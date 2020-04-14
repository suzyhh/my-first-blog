from django.db import models
from django.conf import settings
from django.utils import timezone

# Create an object called Post
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # Make a function called publish, so this one records the publication date time
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # This function returns the title of the Post
    def __str__(self):
        return self.title

