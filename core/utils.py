from uuid import uuid4
from io import BytesIO
from docx2pdf import convert
import logging

logger = logging.getLogger(__name__)


def get_document_slug(instance):
    return (f"{instance.title}{str(instance.uid).split('-')[0]}")


def get_document_share_slug(instance):
    return (f"{'share'}{str(instance.uid).split('-')[0]}")

def convert_docx_to_pdf(docx_file):
    # Convert docx to pdf 
    docx_bytes = docx_file.read()
    docx_stream = BytesIO(docx_bytes)
    pdf_stream = BytesIO()

    convert(docx_stream, pdf_stream)

    pdf_bytes = pdf_stream.getvalue()
    return pdf_bytes


