from types import NoneType
from django.shortcuts import render , redirect
from biblioteca.forms import Libros , BuscarLibro, Prestamos
from biblioteca.models import Libro , Cliente , Prestamo
from django.db.models import Q
import datetime
# Create your views here.
def inicio(request):
    Libros = Libro.objects.all()
    context = { 'libros': Libros }
    return render(request, 'inicio.html' , context)

def buscar(request):
    if request.method == 'POST':
        buscador = BuscarLibro(request.POST)
        if buscador.is_valid():
            buscarLibro = buscador.cleaned_data
            context = {'libro': NoneType , 'buscador': buscador}
            if buscarLibro['anioo'] == None:
                libros = Libro.objects.filter(Q(titulo= buscarLibro['nombre']) | Q(autor=buscarLibro['nombre'])).distinct()
            elif buscarLibro['nombre'] == '':
                libros = Libro.objects.filter(anioPublicacion=buscarLibro['anioo'])
            elif buscarLibro['anioo'] != None and buscarLibro['nombre'] != '':
                libros = Libro.objects.filter(Q(titulo= buscarLibro['nombre']) | Q(autor=buscarLibro['nombre'])).filter(anioPublicacion=buscarLibro['anioo']).distinct()
            context = { 'libro': libros , 'buscador': buscador }
            return render(request, 'buscar.html' , context)    
        
    else:
        buscador= BuscarLibro()
    return render(request, 'buscar.html' , {'buscador': buscador })

def eliminar(request, idlibro):
    libro = Libro.objects.get(idLibro=idlibro)
    libro.delete()
    return redirect('inicio')

def editar(request , idlibro):
    libro = Libro.objects.get(idLibro=idlibro)
    if request.method == 'POST':
        form = Libros(request.POST)
        if form.is_valid():
            editarLibro = form.cleaned_data
            libro.titulo = editarLibro['nombre']
            libro.autor = editarLibro['autor']
            libro.anioPublicacion = editarLibro['anioPublicacion']
            libro.stock = editarLibro['stock']
            libro.save()
            return redirect('inicio')
    else:
        form = Libros(initial={'nombre': libro.titulo, 'autor': libro.autor, 'anioPublicacion': libro.anioPublicacion, 'stock': libro.stock})
    return render(request, 'editar.html' , {'form': form , 'libro': libro})

def registrarP(request):
    todoslibro = Libro.objects.all()
    todosClientes = Cliente.objects.all()
    dia = datetime.date.today()
    context = {'libros': todoslibro , 'clientes': todosClientes , 'dia': dia}
    if request.method == 'POST':
        idLibro = request.POST['idlib']
        libro = Libro.objects.get(idLibro=idLibro)
        idCliente = request.POST.get('idCliente')
        cliente = Cliente.objects.get(idCliente=idCliente)
        fechaP = request.POST['fechaPrestamo']
        fechaD = request.POST['fechaDevolucion']
        prestamo = Prestamo.objects.create(
            idLibro=libro, 
            idCliente=cliente, 
            fechaPrestamo=fechaP, 
            fechaDevolucion=fechaD)
        prestamo.save()
        libro.stock = libro.stock - 1
        libro.save()
        return redirect('inicio')

    return render(request, 'registrarP.html' , context)

def devolverP(request):
    prestamos = Prestamo.objects.all()
    libros = Libro.objects.all()
    cliente = Cliente.objects.all()
    context = {'prestamos': prestamos , 'libros': libros , 'clientes': cliente}
    return render(request, 'devolver.html' , context)
    
def registrar(request):
    if request.method == 'POST':
        form = Libros(request.POST)
        if form.is_valid():
            registrarLibro = form.cleaned_data
            registroLib =  Libro.objects.create(titulo = registrarLibro['nombre'], 
                   autor= registrarLibro['autor'], 
                   anioPublicacion = registrarLibro['anioPublicacion'], 
                   stock = registrarLibro['stock'], 
                   status = registrarLibro['status'])
            registroLib.save()
                
            return redirect('inicio')
    else:
        form= Libros()

    return render(request, 'registrar.html' , {'form': form})

def editarP(request , idprestamo):
    prestamo = Prestamo.objects.get(idPrestamo=idprestamo)
    libro = Libro.objects.get(idLibro=prestamo.idLibro.idLibro)
    cliente = Cliente.objects.get(idCliente=prestamo.idCliente.idCliente)
    dia = datetime.date.today()
    if request.method == 'POST':
        form = Prestamos(request.POST)
        if form.is_valid():
            editarPrestamo = form.cleaned_data
            prestamo.fechaDevolucion = editarPrestamo['prestamoDevolucion']     
            prestamo.status = editarPrestamo['status'] 
            prestamo.save()
            return redirect('devolver')
    else:
        form = Prestamos(initial={'fechaDevolucion' : prestamo.fechaDevolucion , 'status' : prestamo.status})
    return render(request, 'editarP.html' , {'form': form , 'prestamo':prestamo , 'libro': libro , 'cliente': cliente , 'dia': dia})