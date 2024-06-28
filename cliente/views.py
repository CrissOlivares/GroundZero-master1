from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if remember:
                request.session.set_expiry(2592000)  # 30 dias en Segundos
            return redirect('pagina_principal')  # Redirige a la página principal
        else:
            # Retorna a Credenciales Invalidas
            return render(request, 'mi_template.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'mi_template.html')
