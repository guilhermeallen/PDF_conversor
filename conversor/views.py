from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfMerger
from io import BytesIO

def converter_view(request):
    if request.method == 'POST':
        arquivos = request.FILES.getlist('arquivos')
        
        if not arquivos:
            return render(request, 'conversor/upload.html', {'erro': 'Envie pelo menos um arquivo.'})

        merger = PdfMerger()

        for arquivo in arquivos:
            merger.append(arquivo)

        buffer = BytesIO()
        merger.write(buffer)
        merger.close()
        buffer.seek(0)

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resultado.pdf"'
        return response

    return render(request, 'conversor/upload.html')
