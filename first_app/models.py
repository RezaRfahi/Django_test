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
    img=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    pub_date=models.DateTimeField()

    def __str__(self) -> str:
        return self.title