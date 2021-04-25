from django.contrib import admin

# Register your models here.
from .models import (
    User,
    Patient,
    Provider,
)

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Provider)
