from django.http import HttpResponse
from django.shortcuts import render , redirect
from miapp.models import Articulo

# Create your views here.

layout = """
<h1> Ptoyecto Web (LP3) | Carlos Ruiz Montero </h1>
<hr>
<ul>
    <li>
    <a href="/inicio"> Inicio</a>
    </li>
    <li>
    <a href="/saludo"> Mensaje de saludo</a>
    </li>
    <li>
    <a href="/rango"> Mostrar Nùmeros [a,b]</a>
    </li>
    <li>
    <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
    </li>
</ul>
"""


def index(request):
    #menssage="""
    #    <h1>Inicio</h1>
    #"""
    #return HttpResponse(menssage)
    estudiantes = ['Carlos Ruiz','Jordy Quispe','Oscar Reyes','Antony Vasquez']
    #estudiantes = []
    return render(request,'index.html',{
        'titulo':'Inicio',
        'mensaje':'Proyecto Web con DJango (Desde el View)',
        'estudiantes': estudiantes
    })


def saludo(request):
    #mensaje = """
    #<h1>Bienvenidos</h1>
    #<h2>Carlos Ruiz</h2>
    #<h2>Python</h2>
    #"""
    #return HttpResponse(mensaje)
    return render(request, "saludo.html",{
        'titulo':'Saludo',
        'nombre_autor':'Carlos Ruiz',
        'mensaje':'Proyecto Web con DJango (Desde el View)'
    })


def rango(request):
    a = 10
    b= 20
    rango_numeros = range(a,b+1)
    return render(request, 'rango.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros': rango_numeros
    })
    resultado = f"""
             <h2> Numeros de [{a},{b}] </h2>
             resultado: <br>
             <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado +="</ul>"
    rango = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    return render(request, "rango.html",{
        'titulo':'Rango',
        'rango': rango
    })


def rango2(request, a=10, b=15):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado = f"""
        <h2> Numeros de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
        """
    while a<=b:
          resultado += f"<li> {a} </li>"
          a+=1
    resultado +="</ul>"
    return HttpResponse(layout + resultado)

def crear_articulo(request):
    articulo = Articulo(
        titulo = "Tendencias Covid con Power BI",
        contenido = "El articulo muestra información de....",
        publicado = True
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=1000)
        resultado = f"""Articulo: 
                        <br> <strong>ID:</strong> {articulo.id} 
                        <br> <strong>Título:</strong> {articulo.titulo} 
                        <br> <strong>Contenido:</strong> {articulo.contenido}
                        """
    except:
        resultado = "<h1> Artículo No Encontrado </h1>"
    return HttpResponse(resultado)