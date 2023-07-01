from django.db import models

from posts.models import Post


class Order(models.Model):
    owner = models.ForeignKey('account.CustomUser', related_name='orders', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='orders', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'




