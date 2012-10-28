from django.db import models

class Group(models.Model):
    name = models.CharField(max_length = 200)
    chief = models.ForeignKey('student.Student', blank = True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'show_group', (self.pk,)

    @models.permalink
    def get_edit_url(self):
        return  'edit_group', (self.pk,)

    @models.permalink
    def get_delete_url(self):
        return 'delete_group', (self.pk,)