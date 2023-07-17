from django.core.exceptions import ValidationError
from django.utils import formats
from django.utils.translation import gettext_lazy as _ 
import os


def validate_file_size(value):
    limit_mb = 10
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError(_('File size should not exceed %(limit_mb)s MB.'),
                              params={'limit_mb': limit_mb},
                              code='file_size')

def validate_file_format(value):
    allowed_formats = ['.pdf', '.docx', '.txt', '.jpg', '.jpeg', '.png', '.csv']
    file_extension = os.path.splitext(value.name)[1].lower()
    if file_extension not in allowed_formats:
        raise ValidationError(_('Invalid file format. Allowed formats are %(allowed_formats)s.'),
                              params={'allowed_formats': ', '.join(allowed_formats)},
                              code='file_format')