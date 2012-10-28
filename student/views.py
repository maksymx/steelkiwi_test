from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from group.models import Group
from models import Student
from django.contrib.auth.decorators import login_required
from forms import StudForm

def studentlist(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = group.students.all()
    data = dict(group=group, students=students)
    return render_to_response('student/student.html',
                              data,
                              context_instance=RequestContext(request))
    
@login_required(login_url='/login/')
def manage_student(request, student_id=None, group_id=None):
    if student_id:
        student = get_object_or_404(Student, pk=student_id)
    else:
        student = None

    if group_id:
        group = get_object_or_404(Group, pk=group_id)
    else:
        group = None
        
    if request.method == 'POST':
        if student:
            form = StudForm(request.POST, instance=student)
        else:
            form = StudForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        if student:
            form = StudForm(instance=student)
        else:
            form = StudForm(initial={'student_group': group})
            
    data = dict(form=form, student_id=student_id)
    return render_to_response('student/add_student.html',
                              data,
                              context_instance=RequestContext(request))