from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=32,verbose_name='用户名称')
    def __str__(self):
        return self.name
class Role(models.Model):
    name=models.CharField(max_length=32,verbose_name='角色名称')
    def __str__(self):
        return self.name
class UserType(models.Model):
    title=models.CharField(max_length=32,verbose_name='类型名称')
    def __str__(self):
        return self.title
