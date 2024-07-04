from django.db import models

class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    about= models.TextField()
    TYPE_CHOICES = (
        ('IT', 'IT'),
        ('None IT', 'None IT'),
        ('mobile phone', 'mobile phone'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    add_date= models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)

    def __str__(self):
        return self.name


    #Employee Api
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    about = models.TextField()
    position = models.CharField(
        max_length=100, 
        choices=(
            ('Manager', 'manager'),
            ('Software Developer', 'SD'),
            ('Project Leader', 'PL')
        )
    )
    company = models.ForeignKey(company,on_delete=models.CASCADE)
