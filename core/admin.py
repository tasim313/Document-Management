from django.contrib import admin

from django.contrib import messages
from import_export.admin import ImportExportModelAdmin

from .models import(
    User,
    Document,
    DocumentShare,
    DocumentConvertor,
)

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'username',
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
        )
    list_filter = ('username', 'role',)
    search_fields = ("username", 'role','is_active')

    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
  
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active = 1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")
  
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active = 0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
  
    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")

admin.site.register(User, UserAdmin)


class DocumentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'title',
        'description',
        'file',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('title', 'status',)
    search_fields = ("title", 'user_created','user_updated')

admin.site.register(Document, DocumentAdmin)

class DocumentShareAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('status',)
    search_fields = ('user_created','user_updated')

admin.site.register(DocumentShare, DocumentShareAdmin)



class DocumentConvertorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('status',)
    search_fields = ('user_created','user_updated')

admin.site.register(DocumentConvertor, DocumentConvertorAdmin)