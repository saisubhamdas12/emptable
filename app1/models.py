from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=30,unique=True)
    loc=models.CharField(max_length=100)
    
    def __str__ (self):
        return self.dname
 
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30,null=False)
    job=models.CharField(max_length=30,null=False)
    hiredate=models.DateField(null=False)
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename
    
