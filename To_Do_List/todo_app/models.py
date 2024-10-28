from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_list = models.CharField(max_length=100)
    date = models.DateTimeField()
    complit = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.todo_list}_{self.date}" 
    
    class Meta:
        ordering = ['-date'] 

