from django.db import models


class UserRole(models.TextChoices):
    Admin = 'Admin', 'admin'
    Manager = 'Manager', 'manager'
    executive = 'Executive', 'executive'
    student = 'Student', 'student'


class UserStatus(models.TextChoices):
    Active = 'Active', 'active'
    Inactive = 'Inactive', 'inactive'
    Delete = 'Delete', 'delete'
