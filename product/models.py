from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Bot(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена', default=0)

    rating = models.PositiveSmallIntegerField(default=0, verbose_name='рейтинг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Image(models.Model):
    bot = models.ForeignKey('Bot', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bot/', verbose_name='Скриншот')

    class Meta:
        verbose_name = 'скриншот'
        verbose_name_plural = 'скриншоты'

    def __str__(self):
        return f'{self.bot}'
