from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    published_data = models.DateField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return self.title
    

# restframwork  username admin
# framework pass