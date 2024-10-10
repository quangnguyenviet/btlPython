from datetime import datetime
from django.db import models
from history.models import Order


class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1) 
    # amount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentDate = models.CharField(max_length=19, null=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))   
    methodChoices = (
        ('Credit Card', 'Credit Card'),
        ('COD', 'COD'),
    )
    paymentMethod = models.CharField(max_length=12, choices=methodChoices, default='Credit Card') 
    # status_choices = (
    #     ('Pending', 'Pending'), 
    #     ('Completed', 'Completed'),  
    # )
    # paymentStatus = models.CharField(max_length=10, choices=status_choices, default='Pending') 

    class Meta:
        db_table = 'payment'