from django.db import models

#title,#publish date,#body# image

class Blog(models.Model):
    title=models.CharField(max_length=200)
    publishdate=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to="images")

