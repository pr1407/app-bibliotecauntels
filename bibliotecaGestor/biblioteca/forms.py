from pickle import TRUE
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class Libros(forms.Form):
    nombre = forms.CharField(label = "Nombre del Libro" , widget=forms.TextInput(attrs={'class':'form-control'}))
    autor = forms.CharField(label = "Autor" , widget=forms.TextInput(attrs={'class':'form-control'}))
    anioPublicacion = forms.DateField(label= "Año de Publicacion" ,widget=DateInput(attrs={'class':'form-control'}))
    stock = forms.IntegerField(label = "Stock" , widget=forms.NumberInput(attrs={'class':'form-control'}))
    status = forms.ChoiceField(label = "Status" , choices = [(True,'Disponible'),(False,'No Disponible')], widget=forms.Select(attrs={'class':'form-select' , 'aria-label':'Default select example'}))

class Prestamos(forms.Form):
    status = forms.ChoiceField(label = "Cambiar Status" , choices = [(True,'Devuelto'),(False,'No Devuelto')], widget=forms.Select(attrs={'class':'form-select' , 'aria-label':'Default select example'}))
    prestamoDevolucion = forms.DateField(label= "Cambiar Fecha Prestamo" ,widget=DateInput(attrs={'class':'form-control'}))

class RegistrarPrestamo(forms.Form):
    idCliente = forms.ChoiceField(label = "Cliente")
    idLibro = forms.ChoiceField(label = "Libro")
    fechaPrestamo = forms.DateField(label = "Fecha de Prestamo", widget=DateInput(attrs={'class':'form-control'}))
    fechaDevolucion = forms.DateField(label = "Fecha de Devolucion", widget=DateInput(attrs={'class':'form-control'}))

class BuscarLibro(forms.Form):
    nombre = forms.CharField(label = "Buscador Libro / Autor" , widget=forms.TextInput(attrs={'class':'form-control'}))
    anioo = forms.DateField(label = "Buscador por Publicacion" , widget=DateInput(attrs={'class':'form-control' }) )
    def __init__(self, *args, **kwargs):
        super(BuscarLibro, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = False
        self.fields['anioo'].required = False

