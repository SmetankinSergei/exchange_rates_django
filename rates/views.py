from datetime import datetime

from django.shortcuts import render
from pycbrf import ExchangeRates

from rates import utils


def home(request):
    return render(request, 'rates/home.html')


def get_current_usd(request):
    data = {'wait_process': False}
    if request.GET.get('get_rates'):
        data['wait_process'] = True
        time_now = datetime.now()
        rates = ExchangeRates(str(time_now)[:10])
        for rate in rates.rates:
            if rate.code == 'USD':
                rub_rate = rate.value
                utils.write_rates_data(time_now, rub_rate)
    return render(request, 'rates/home.html', data)
