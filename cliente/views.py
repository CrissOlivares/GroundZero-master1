from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario,Genero
# Create your views here.
def index(request):
    cliente=usuario.objetcs.all()
    context={"usuario":usuario}
    return render(request,'index.html',context)

TEMPLATE_DIRS=(
    'os.path.join(BASE_DIR, "templates"),'
)
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

def GroundZeropPQ(request):
    return render(request,'GroundZeroInicio.html')

def GroundZeropPQ(request):
    return render(request,'index.html')