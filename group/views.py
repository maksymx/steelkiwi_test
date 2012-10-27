# Create your views here.
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import Group

def group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = group.students.all()
    data = dict(group=group, students=students)
    return render_to_response('group/group.html',
                              data,
                              context_instance=RequestContext(request))