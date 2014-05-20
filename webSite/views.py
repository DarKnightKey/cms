import datetime
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import Context
from django.template.loader import get_template

# 站点的列表页面
from webSite.forms import ContactForm
from webSite.models import Site

# site列表页
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
            return render_to_response('webSite/site/list.html', {'siteList': siteList, 'siteName': siteName});
    return render_to_response('webSite/site/list.html', {'error': error});

# 感谢
def thanks(request):
    return render_to_response('webSite/common/thanks.html');

# 联系我们
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST);
    if form.is_valid():
        cd = form.cleaned_data;
        # send_mail(
        #     cd['subject'],
        #     cd['message'],
        #     cd.get('email', '240942070@qq.com'),
        #     ['240942070@qq.com'],
        # );
        return HttpResponseRedirect('webSite/thanks/');
    else:
        form = ContactForm();
    return render_to_response('webSite/common/contact.html', {'form': form})