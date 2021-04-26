from django.forms.models import model_to_dict
from .models import WeeklyTimeSlot, PriorityGroup
from datetime import datetime


def get_time_slot_info():
    all_slots = list(WeeklyTimeSlot.objects.values())
    for i in range(len(all_slots)):
        all_slots[i]["start_time"] = all_slots[i]["start_time"].strftime("%H:%M:%S")
        all_slots[i]["end_time"] = all_slots[i]["end_time"].strftime("%H:%M:%S")
    return all_slots


def get_priority_group_info():
    all_groups = list(PriorityGroup.objects.values())
    # print(all_groups)
    for i in range(len(all_groups)):
        # print(all_groups[i]["eligible_date"])
        # print(type(all_groups[i]["eligible_date"]))
        all_groups[i]["eligible_date"] = all_groups[i]["eligible_date"].strftime(
            "%Y/%m/%d"
        )
    return all_groups
