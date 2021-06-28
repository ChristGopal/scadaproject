from django.shortcuts import render
from .models import Datalog
import datetime


# Create your views here.


def index(request):
    start_date = datetime.date(2021, 6, 26)
    end_date = datetime.date(2021, 6, 27)
    data = Datalog.objects.filter(opc_iot_flow_timestamp__range=(start_date, end_date))
    # data = round(data, 2)
    context = {'arr_users': data}
    return render(request, 'index.html', context)
