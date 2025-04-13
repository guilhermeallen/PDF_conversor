from PIL import Image
from reportlab.pdfgen import canvas
from django.core.files.base import ContentFile
import os
import io

def converter_para_pdf(arquivo_model):
    arquivo = arquivo_model.arquivo
    nome_arquivo = os.path.basename(arquivo.name)
    ext = nome_arquivo.split('.')[-1].lower()

    output = io.BytesIO()

    if ext in ['jpg', 'jpeg', 'png']:
        image = Image.open(arquivo)
        image = image.convert('RGB')
        image.save(output, format='PDF')
    elif ext in ['txt']:
        text = arquivo.read().decode('utf-8')
        pdf = canvas.Canvas(output)
        pdf.drawString(100, 750, text[:500])  # Simples, só uma parte do texto
        pdf.save()
    else:
        return None

    output.seek(0)
    arquivo_model.arquivo.save(nome_arquivo.split('.')[0] + '.pdf', ContentFile(output.read()))
    arquivo_model.save()