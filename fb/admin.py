# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

from django.contrib.auth.models import User
# Register your models here.


class FilterUserAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(FilterUserAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        return obj.user == request.user or request.user.is_superuser


@admin.register(Schoolclass)
class SchoolclassAdmin(admin.ModelAdmin):
    pass


@admin.register(Studentinformation)
class StudentinformationAdmin(admin.ModelAdmin):
    pass


@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    pass


@admin.register(Ebook_detail)
class Ebook_detail(admin.ModelAdmin):
    pass


@admin.register(Contactbook2)
class Contactbook2Admin(admin.ModelAdmin):
    pass


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    pass
