import datetime
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import Context
from django.template.loader import get_template

# 站点的列表页面
from webSite.models import Site


def siteList(request):
    # now = datetime.datetime.now();
    # t = get_template('webSite/list.html');
    # html = t.render(Context({'siteName': 'my site', 'current_date' : now}));
    # return HttpResponse(html);

    error = False;
    if 'siteName' in request.GET:
        siteName = request.GET['siteName']
        if not siteName:
            error = True
        else:
            siteList = Site.objects.filter(name__icontains = siteName)
        return render_to_response('search_results.html', {'siteList': siteList, 'siteName': siteName});
    return render_to_response('search_form.html', {'error': error});