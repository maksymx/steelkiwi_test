# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from models import Group
from django.contrib.auth.decorators import login_required
from forms import GroupForm

def grouplist(request):
    groups = Group.objects.all()
    data = dict(groups=groups)
    return render_to_response('group/group.html',
                              data,
                              context_instance=RequestContext(request))
    
@login_required(login_url='/login/')
def edit_group(request, group_id=None):

    if group_id:
        group = get_object_or_404(Group, pk=group_id)
    else:
        group = None

    if request.method == 'POST':
        if group:
            form = GroupForm(request.POST, instance=group)
        else:
            form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        if group:
            form = GroupForm(instance=group)
        else:
            form = GroupForm()

    data = dict(form=form, group_id=group_id)
    return render_to_response('group/add_group.html',
                              data,
                              context_instance=RequestContext(request))