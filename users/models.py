from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoice(models.TextChoices):
        male = ("M","남자")
        female = ("F","여자")
    first_name = None
    last_name = None
    name = models.CharField(max_length=20,blank=True,null=True,verbose_name="이름")
    birthday = models.DateField(null=True, blank=True, verbose_name="생년월일")
    gender = models.CharField(max_length=10,choices=GenderChoice.choices,verbose_name="성별")
    phone_number = models.CharField(validators=[RegexValidator(r'010-?[1-9]\d{3}-?\d{4}$')], max_length=13, blank=True)
