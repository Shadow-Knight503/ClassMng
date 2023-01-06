from django.contrib import admin
from .models import UserProf, CodeProb, Code, Status

# Register your models here.
admin.site.register(UserProf)
admin.site.register(CodeProb)
admin.site.register(Code)
admin.site.register(Status)
