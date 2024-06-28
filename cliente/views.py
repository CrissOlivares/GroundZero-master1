from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario,Genero
# Create your views here.


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


