from django.contrib import admin
from .models import Author,Book,Review



# customize for admin panel

class Bookadmin(admin.ModelAdmin):
    list_display=['title','price','publish_date']
    list_filter=['price']
    search_fields=['title']

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
