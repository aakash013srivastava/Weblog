from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.title + " - " + self.author

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=10000)
    comment_author = models.CharField(max_length=10000)

    def __str__(self):
        return self.comment_text + " - Comment by - " + self.comment_author
