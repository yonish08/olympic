from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django_countries.fields import CountryField

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        return super().save(*args, **kwargs)
    

# site user model
class Customer(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    full_name = models.CharField(max_length=200)
    country = CountryField(blank=True, null=True, verbose_name="Counrty/Area of resdence", blank_label="Select Country")
    
    USERNAME_FIELD = 'email'
    
    def getFullName(self):
        return self.full_name

    def save(self, *args, **kwargs):
        group, group_create = Group.objects.get_or_create(name="customer")
        self.user.groups.add(group)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
