from django.db import models

class StreamModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class WatchModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    platform = models.ForeignKey(StreamModel, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ReviewModel(models.Model):
    rating = models.PositiveIntegerField()
    description = models.TextField()
    watchlist = models.ForeignKey(WatchModel, on_delete=models.CASCADE, related_name='review')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)
