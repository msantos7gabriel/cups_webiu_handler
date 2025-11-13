import subprocess
from django.shortcuts import render, redirect
from printer.forms import PDFDocumentForm
from printer.models import PDFDocument


def test(request):
    try:
        result = subprocess.run(
            ["lpstat", "-p"], capture_output=True, text=True, check=True)
        output = result.stdout
        if result.stdout == None:
            output = "Nenhuma impressora encontrada"

    except subprocess.CalledProcessError as e:
        output = "Erro ao verificar impressoras"

    context = {'result': output}
    return render(request, 'printer/test.html', context)

# printer/views.py


def upload_print(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)

        if form.is_valid():

            print("--- FORMULÁRIO VÁLIDO! ---")
            validated_form = form.save(commit=False)
            validated_form.title = validated_form.upload.name
            validated_form.save()

            path = validated_form.upload.path
            print(f"Arquivo salvo em: {path}")

            try:
                subprocess.run(
                    ["lp", path], check=True)
                print("Arquivo enviado para impressão com sucesso.")
            except subprocess.CalledProcessError as e:
                print("Erro ao enviar o arquivo para impressão.")

        else:
            # --- ADICIONE ESTE BLOCO 'ELSE' ---
            # SE O FORMULÁRIO FOR INVÁLIDO, ISSO VAI RODAR
            print("--- FORMULÁRIO INVÁLIDO ---")
            print(form.errors)
            print("-----------------------------")
            # --- FIM DO BLOCO NOVO ---

    else:
        form = PDFDocumentForm()

    # O 'context' precisa ser definido fora do 'if'
    context = {'form': form}
    return render(request, 'printer/upload_print.html', context)
