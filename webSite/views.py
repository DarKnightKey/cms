import datetime
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import Context
from django.template.loader import get_template

# 站点的列表页面
def siteList(request):
    # now = datetime.datetime.now();
    # t = get_template('webSite/list.html');
    # html = t.render(Context({'siteName': 'my site', 'current_date' : now}));
    # return HttpResponse(html);

    siteName = 'my site';
    current_date = datetime.datetime.now();
    return render_to_response('webSite/site/list.html', locals());