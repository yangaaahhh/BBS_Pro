from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BBS


# Create your views here.
def index(request):
    bbs_list = BBS.objects.all()
    return render(request, 'index.html', {'bbs_list': bbs_list})


def bbs_detail(request, id):
    bbs = get_object_or_404(BBS, id=id)
    return render(request, 'bbs_detail.html', {'bbs': bbs})
