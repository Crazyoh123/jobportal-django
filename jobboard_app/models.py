from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    qualification = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    location = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    application_deadline = models.DateField()

    def __str__(self):
        return self.title
