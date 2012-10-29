from django.core.management.base import BaseCommand
from group.models import Group

class Command(BaseCommand):

    def handle(self, *args, **options):
        groups = Group.objects.all()

        for group in groups:
            print "%s   \t%d" % (group.name, group.students.count())
        