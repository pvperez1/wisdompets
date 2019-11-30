from django.contrib import admin
from .models import Pet, Vaccine
# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ('name','breed','submission_date')
    list_filter = ('sex','submission_date')
    list_editable = ('breed',)
    search_fields = ('name',)
    list_per_page = 5

admin.site.register(Pet, PetAdmin)
admin.site.register(Vaccine)
