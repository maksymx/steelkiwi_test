from django.template import RequestContext
from django.shortcuts import render_to_response
from group.models import Group

def studentlist(request):
    groups = Group.objects.all()
    data = dict(groups=groups)
    return render_to_response('student/student.html',
                              data,
                              context_instance=RequestContext(request))