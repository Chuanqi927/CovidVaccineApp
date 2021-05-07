from django.contrib import admin

# Register your models here.

from .models import (
    WeeklyTimeSlot,
    PriorityGroup,
)


admin.site.register(WeeklyTimeSlot)
admin.site.register(PriorityGroup)

