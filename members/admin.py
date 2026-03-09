from django.contrib import admin

from .models import Member   # for "member"table create in admin as user
from .models import student
from .models import ContactMessage # for table- "contactmessage"


# ListDisplay your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

class MemberAdmin2(admin.ModelAdmin):
  list_display = ("firstname", "lastname",)


class MemberAdmin3(admin.ModelAdmin):
  list_display = ("name", "email", "message",)


# Register your models here.
admin.site.register(Member,MemberAdmin)
admin.site.register(student,MemberAdmin2)
admin.site.register(ContactMessage,MemberAdmin3)
