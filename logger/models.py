from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from student.models import Student
from group.models import Group
# Create your models here.
TYPES = (
    ('C', 'Created'),
    ('M', 'Modified'),
    ('D', 'Deleted')
)

class Logger(models.Model):
    create_date = models.DateTimeField('Date', auto_now=True)
    type = models.CharField('Type', choices=TYPES, max_length=1)
    model = models.CharField('Class', max_length=200)
    log = models.CharField('Log', max_length=250)
    def __unicode__(self):
        return "%s: %s" % (self.create_date.strftime("%d.%m.%Y %H:%M"), self.log)

@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Group)
def model_save_signal(sender, instance, signal, *args, **kwargs):
    h = Logger()
    h.model = str(sender)
    try:
        sender.objects.get(pk=instance.pk)
        h.type = 'M'
        h.log = 'modified'
    except sender.DoesNotExist:
        h.type = 'C'
        h.log = 'created'
    h.log = 'Object <%s> ' % instance + h.log
    h.save()


@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def model_delete_signal(sender, instance, signal, *args, **kwargs):
    h = Logger()
    h.model = str(sender)
    h.type = 'D'
    h.log = 'Object <%s> was deleted' % instance
    h.save()