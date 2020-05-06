from django.db import models
from django.conf import settings
from django.utils import timezone

# ここに機能をつくる

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) #なくてもいいよって意味のblankとnullが許可

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #後で管理画面いくときにstrがあると名前を一個一個表示するので便利
