from django.db import models
from django.utils import timezone
from django.forms import ModelForm, Textarea
from django import forms


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': Textarea(attrs={'cols':50, 'rows':1}),
            'text': Textarea(attrs={'cols':50, 'rows':10})
        }

class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.IntegerField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.text

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'cols':50, 'rows':10})
        }


