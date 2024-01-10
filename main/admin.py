from django.contrib import admin
from main.models import *

# Register your models here.
class AdminModelSingle(admin.ModelAdmin):
    pass

admin.site.register(Category, AdminModelSingle)
admin.site.register(Tovar, AdminModelSingle)
admin.site.register(Contact, AdminModelSingle)
admin.site.register(Feedback, AdminModelSingle)
admin.site.register(Service, AdminModelSingle)
admin.site.register(Partner, AdminModelSingle)
admin.site.register(Otziv, AdminModelSingle)

