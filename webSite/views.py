import datetime
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import Context
from django.template.loader import get_template

# 站点的列表页面
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
    errors = [];
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e‐mail address.')
    if not errors:
        # 发送反馈邮件
        # send_mail(
        #     request.POST['subject'],
        #     request.POST['message'],
        #     request.POST.get('email', '240942070@qq.com'),
        #     ['240942070@qq.com'],
        # )
        return HttpResponseRedirect('/webSite/thanks')
    return render_to_response('webSite/common/contact.html',{'errors': errors})