from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=20)
    family=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name+' '+self.family

class Info(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title=models.CharField(max_length=25)
    dsc=models.TextField()
    img=models.ImageField(upload_to='images/')
    pub_date=models.DateTimeField()
    
     
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    info=models.ForeignKey(Info, on_delete=models.CASCADE)
    comment_title=models.CharField(max_length=50)
    comment_dsc=models.CharField(max_length=350)
    def __str__(self) -> str:
        return self.comment_title