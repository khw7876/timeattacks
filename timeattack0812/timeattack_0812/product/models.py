from calendar import prcal
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("상품 이름", max_length=20)
    discription = models.CharField('설명', max_length=150)
    price = models.IntegerField("가격")
    create_time = models.DateTimeField("도입일", auto_now_add=True)
    active = models.BooleanField("active 여부")
    subscribe = models.ForeignKey("Subscribe", on_delete=models.CASCADE)
    

    class Meta:
        db_table ='products'

class Subscribe(models.Model):
    buy_date = models.DateTimeField("구입일", auto_now_add=True)
    start_subscribe = models.DateTimeField("구독시작일")
    end_subcribe = models.DateTimeField("구독 종료일")



