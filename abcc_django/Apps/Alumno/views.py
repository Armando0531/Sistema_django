from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .form import AlumnoForm

# Create your views here.
def inicio(request):
    alumno = Alumno.objects.all()
    context = {
        'valumno' : alumno
    }
    return render(request, 'Alumno/inicio.html',context)

def alumno_new(request):
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST)
        if alumno_form.is_valid():
                alumno_form.save()
                return redirect('inicio')
    else:
        alumno_form = AlumnoForm()
    return render(
        request,'alumno/alumno_form.html',{
            'alumno_form':alumno_form
        }
    )

def alumno_update(request, id):
    alumno = get_object_or_404(Alumno, id= id)
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, instance = alumno)
        if alumno_form.is_valid():
                alumno_form.save()
                return redirect('inicio')
    else:
        alumno_form = AlumnoForm(instance = alumno)
    return render(
        request,'alumno/alumno_form.html',{
            'alumno_form':alumno_form
        }
    )

def alumno_delete(request, id):
    alumno = get_object_or_404(Alumno, id= id)

    if alumno:
        alumno.delete()
    return redirect('inicio')

def alumno_view(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, 'alumno/alumno_detail.html', {'alumno': alumno})