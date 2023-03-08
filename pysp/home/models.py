from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(("name"), max_length=50)
    pno=models.CharField(("pno"), max_length=50)
    email=models.CharField(("email"), max_length=50)
    feedback=models.CharField(("feedback"), max_length=50)
    def __str__(self):
        return self.name
    