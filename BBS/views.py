from django.shortcuts import render, get_object_or_404, redirect
from .models import BBS


# Create your views here.
def index(request):
    bbs_list = BBS.objects.all()
    return render(request, 'index.html', {'bbs_list': bbs_list})


def bbs_detail(request, bbs_id):
    bbs = get_object_or_404(BBS, id=bbs_id)

    if request.method == 'POST':
        return redirect(bbs)
    else:
        return render(request, 'bbs_detail.html', {'bbs': bbs})
