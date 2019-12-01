from django.contrib import admin
from dialog.models import Member


class MemberAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Member, MemberAdmin)
