from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'judul': 'Halaman Beranda',
        'menu': 'home',
    }
    return render(request, 'data/dashboard.html', context)


def pendaftaran(request):
    context = {
        'judul': 'Halaman Pendaftaran',
        'menu': 'pendaftaran',
    }
    return render(request, 'data/pendaftaran.html', context)


def datasambang(request):
    context = {
        'judul': 'Halaman Data Sambang Santri',
        'menu': 'datasambang',
    }
    return render(request, 'data/datasambang.html', context)


def dataquota(request):
    context = {
        'judul': 'Halaman Data Quota',
        'menu': 'dataquota',
    }
    return render(request, 'data/dataquota.html', context)
