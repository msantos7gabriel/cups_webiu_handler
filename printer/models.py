from django.db import models
from django.core.validators import FileExtensionValidator


class PDFDocument(models.Model):
    title = models.CharField(max_length=200, blank=True)
    upload = models.FileField(upload_to='pdfs/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])
    ], help_text="Somente arquivos PDF são permitidos.")

    def __str__(self):
        return self.title
