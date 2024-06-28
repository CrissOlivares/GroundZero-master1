from django.http import HttpResponse
from .models import usuario,Genero
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm, ClienteUpdateForm

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/agregar_cliente.html', {'form': form})

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteUpdateForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista_clientes')
    else:
        form = ClienteUpdateForm(instance=cliente)
    return render(request, 'clientes/actualizar_cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:lista_clientes')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})







TEMPLATE_DIRS=(
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    usuarios=usuario.objects.all()
    context={"Usuarios":usuarios}
    return render(request,'index.html',context)

def crud_generos(request):
    generos=Genero.objetcs.all()
    context={'generos': generos}
    print("enviando datos de generos_list")
    return render(request, "index_genero.html",context)

def GroundZeroInicio(request):
    return render(request,'GroundZeroInicio.html')

def GorundZeroCompra(request):
    return render(request,'GorundZeroCompra.html')

def GroundZeroArtistas(request):
    return render(request,'GroundZeroArtistas.html')

def GroundZeroCuadros(request):
    return render(request,'GroundZeroCuadros.html')

def GroundZeroEsculturas(request):
    return render (request,'GroundZeroEsculturas.html')

def GroundZeroOrfebreria(request):
    return render (request,'GroundZeroOrfebreria.html')

def GroundZeroLogin(request):
    return render (request,'GroundZeroLogin.html')

def GroundZeroRegister(request):
    return render (request,"GroundZeroRegister.html")

def GroundZeroPaises(request):
    return render(request,"GroundZeroPaises.html")

def GroundZeropPQ(request):
    return render(request,'GroundZeropPQ.html')


