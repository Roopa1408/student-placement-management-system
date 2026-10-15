from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    skills = models.TextField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    website = models.URLField()
    job_role = models.CharField(max_length=100)
    package = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    
class Placement(models.Model):

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Shortlisted", "Shortlisted"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_role = models.CharField(max_length=100)
    package = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Applied"
    )
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.company.name}"