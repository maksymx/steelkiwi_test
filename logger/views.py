from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404
from student.models import Student
from group.models import Group
from forms import YesNoForm
# Create your views here.
@login_required(login_url='/login/')
def delete_instance(request, instance_id, instance_type):
    if instance_type == 1:
        instance = get_object_or_404(Student, pk=instance_id)
    elif instance_type == 2:
        instance = get_object_or_404(Group, pk=instance_id)
    else:
        raise Http404
    if request.method == 'POST':
        form = YesNoForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            if choice:
                instance.delete()
            return redirect('index')
    else:
        form = YesNoForm()
    data = dict(form=form, instance_id=instance_id, instance=instance, instance_type=instance_type)
    return render_to_response('deletion.html', data, context_instance=RequestContext(request))