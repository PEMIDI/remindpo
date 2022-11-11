from django.contrib.auth import get_user_model
from django.db import models
from utils.basemodel import BaseModel
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Reminder(BaseModel):
    title = models.CharField(max_length=32, verbose_name=_('title'))
    message = models.CharField(max_length=500, verbose_name=_('message'), blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('created by'))
    scheduled_at = models.DateTimeField(verbose_name=_('scheduled at'))
    alert_time = models.DateTimeField(verbose_name=_('alert time'))
    category = models.ForeignKey('Category', verbose_name='category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('reminder')
        verbose_name_plural = _('reminders')
        db_table = 'reminder'

    def __str__(self):
        return f"{self.title}, at {self.scheduled_at}"


class Category(BaseModel):
    title = models.CharField(max_length=32, verbose_name=_('title'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'category'

    def __str__(self):
        return self.title
