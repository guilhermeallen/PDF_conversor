from django.shortcuts import render
from .forms import ArquivoForm
from .utils import converter_para_pdf

def upload_arquivo(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save()
            converter_para_pdf(arquivo)
            return render(request, 'conversor/sucesso.html', {'arquivo': arquivo})
    else:
        form = ArquivoForm()
    return render(request, 'conversor/upload.html', {'form': form})


# Create your views here.
