import subprocess
from django.shortcuts import render


def test(request):
    try:
        result = subprocess.run(["lpstat", "-p"], capture_output=True, text=True, check=True)
        output = result.stdout
        if result.stdout:
            output = "Nenhuma impressora encontrada"

    except subprocess.CalledProcessError as e:
        output = "Erro ao verificar impressoras"

    context = {'result': output}
    return render(request, 'printer/test.html', context)
