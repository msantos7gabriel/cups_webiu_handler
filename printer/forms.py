# core/forms.py
from django.forms import ModelForm
from printer.models import PDFDocument

class PDFDocumentForm(ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['upload']