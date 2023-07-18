from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )

from autoslug import AutoSlugField

from .choice import (
    UserRole,
    UserStatus,
)

from .utils import(
    get_document_slug,
    get_document_share_slug,
)
from .helpers import(
    validate_file_size,
    validate_file_format,
)

import logging
import uuid

logger = logging.getLogger(__name__)


class CustomUserManager(BaseUserManager):
    def create_user(self,
                    username,
                    password=None,
                    **extra_fields):
        if not username:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            username=self.normalize_email(username),
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,
                         username,
                         password=None,
                         **extra_fields):
        extra_fields.setdefault('role', 'Admin')
        if extra_fields.get('role') != 'Admin':
            raise ValueError('Superuser must have role of Global Admin')

        user = self.create_user(
            username=self.normalize_email(username),
            password=password, **extra_fields
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return 
       

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=False,
        verbose_name='user email address',
        max_length=255,
        blank=True,
        null=True,
    )
    username = models.EmailField(max_length=255,
                                 unique=True,
                                 verbose_name='Email')
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        db_index=True,
        default=UserRole.student,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        db_index=True,
        default=UserStatus.Active
    )
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def save(self, *args, **kwargs):
        self.email = self.username
        return super().save(*args, **kwargs)

    
class BaseModel(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=15,
        choices=UserStatus.choices,
        default=UserStatus.Active
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="User_who_created",
        verbose_name="Created Person"
        )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="The_User_who_Updated",
        verbose_name="Updated Person"
    )


class Document(BaseModel):
    title = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from=get_document_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    description = models.TextField(max_length=None,
                                   blank=True,
                                   null=True)
    file = models.FileField(upload_to='documents/',
                            validators=[validate_file_size, validate_file_format])

    def __str__(self):
        return self.title 


class DocumentShare(BaseModel):
    document = models.ManyToManyField(Document, related_name="document_share_info", blank=True, null=True)
    slug = AutoSlugField(populate_from=get_document_share_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    share_person = models.ManyToManyField(User, related_name="person_share_info", blank=True, null=True)

    def __str__(self):
        return self.slug

class DocumentConvertor(BaseModel):
    docx_file = models.FileField(blank=True, null=True)
    pdf_file = models.FileField(blank=True, null=True)
