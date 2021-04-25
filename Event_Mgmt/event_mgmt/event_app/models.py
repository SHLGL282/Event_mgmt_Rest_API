from django.db import models

# Create your models here.
class CategoryMaster(models.Model):
    category_name = models.CharField(max_length=100)
    parent_category = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class EventMaster(models.Model):
    event_name =  models.CharField(max_length=100)
    place =  models.CharField(max_length=100)
    time =  models.DateTimeField()
    duration = models.DurationField()
    cast = models.CharField(max_length=100)
    #category_name = models.ForeignKey(CategoryMaster, on_delete=models.CASCADE, null=True)
    category_name = models.ForeignKey(CategoryMaster, on_delete=models.CASCADE, null=True)
    def __str__(self):
        # return self.event_name
        return self.event_name
