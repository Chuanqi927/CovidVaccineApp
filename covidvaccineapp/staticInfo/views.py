from django.http import HttpResponse
from django.shortcuts import render
from .utils import get_time_slot_info, get_priority_group_info


# Create your views here.
def index(request):
    return HttpResponse("This is static info index page")


def show_time_slots(request):
    all_time_slots_info = get_time_slot_info()
    # print(all_time_slots_info)
    parameter_dict = {
        "all_time_slots": all_time_slots_info,
    }
    return render(request, "show_time_slots.html", parameter_dict)


def show_priority_groups(request):
    all_priority_groups_info = get_priority_group_info()
    # print(all_priority_groups_info)
    parameter_dict = {
        "all_priority_groups": all_priority_groups_info,
    }
    return render(request, "show_priority_groups.html", parameter_dict)
