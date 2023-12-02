from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext_lazy as _



'''

models.Model
   - html widget
   - validatons
   - best for database

'''
# Create your models here.
class Author(models.Model):
    #name=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_name')
    name=models.CharField(max_length=100,verbose_name=_('name_author'))
    brith_date=models.DateField(default=datetime.datetime.now)
    biography=models.TextField(max_length=500)

    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    title=models.CharField(max_length=100,verbose_name=_('name_book'))
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book_author')
    publish_date=models.DateTimeField(auto_now=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.title
    
class  Review(models.Model):
    rating=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        
            ]
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='review_book')
    reviewer_name=models.CharField(max_length=100)
    content=models.TextField(max_length=350)
    rate=models.CharField(max_length=50,choices=rating)

    def __str__(self):
        return self.reviewer_name


