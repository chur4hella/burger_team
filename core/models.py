from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'

    name = models.CharField(
        _('Название'),
        max_length=250
    )

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'

    name = models.CharField(
        _('Название'),
        max_length=250
    )
    salary = models.PositiveSmallIntegerField(
        _('Заработная плата'),
        default=0
    )
    responsibilities = models.TextField(
        _('Обязанности')
    )
    benefits = models.TextField(
        _('Преимущества'),
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name=_('Город')
    )
    phone = models.CharField(
        _('Телефон'),
        max_length=50
    )
    is_active = models.BooleanField(
        _('Активна'),
        default=True
    )
    img = models.ImageField(
        upload_to='media/uploads/%Y/%m/%d/',
        verbose_name=_('Изображение для вакансии'),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def count_applying(self):
        return self.applying_set.count()


class Applying(models.Model):
    class Meta:
        verbose_name = 'Отклики'
        verbose_name_plural = 'Отклики'

    name = models.CharField(
        _('Имя'),
        max_length=50,
    )
    date_applying = models.DateTimeField(
        _('Дата и время отклика'),
        auto_now_add=True
    )
    birthday = models.CharField(
        _('День рождения'),
        max_length=15,
        default=''
    )
    email = models.EmailField(
        _('Email'),
    )
    phone = models.CharField(
        _('Телефон'),
        max_length=50
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        verbose_name=_('Вакансия')
    )
    cv = models.FileField(
        _('Резюме'),
        upload_to='applying/%Y/%m/%d/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['pdf', 'csv', 'doc', 'docx', 'xlsx'])]
    )

    def __str__(self):
        return self.name

