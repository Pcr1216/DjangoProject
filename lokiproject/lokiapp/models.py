from django.db import models

class Product(models.Model):
    proid = models.AutoField(primary_key=True)
    prodname = models.CharField(max_length=250)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.prodname+" "+str(self.quantity)
    class Meta:
            db_table = 'lokiapp_product'
            
    