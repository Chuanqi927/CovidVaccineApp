from django.shortcuts import render
from django.http import HttpResponse
from staticInfo.models import PriorityGroup
from staticInfo.utils import get_priority_group_info


# def homepage(request):
#     return render(request, "homepage.html")


def index(request):
    return render(request, "index.html")
#
#
# def index2(request):
#     return render(request, "pulseadmin/index.html")
#
#
# def base(request):
#     return render(request, "base.html")


def home(request):

    all_priority_groups_info = get_priority_group_info()
    # print(all_priority_groups_info)
    context = {
        "all_priority_groups": all_priority_groups_info,
    }

    return render(request, "home.html", context)
