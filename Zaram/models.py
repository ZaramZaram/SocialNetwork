from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
#from mapwidgets.widgets import GooglePointFieldWidget



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="posts")
    body = models.TextField(_('post body'), blank=False)
    #location = models.PointField(widget=GooglePointFieldWidget())
    slug = models.SlugField()
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    update_date = models.DateTimeField(_('update date'), auto_now=True)

    class Meta:
        ordering = ['creation_date']
    def __str__(self):
        return f'{self.slug }'

    def get_absolute_url(self):
        return reverse('home:post_detail', args=(self.id, self.slug))

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)
    avatar = models.ImageField(_('content'), blank=False, upload_to='zarams/')

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='ucomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user - self.body[:30]}'
