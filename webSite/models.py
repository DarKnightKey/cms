from django.db import models

# Create your models here.
# 权限对象
# class User(models.Model):
#     # 通用属性
#     createTime = models.DateTimeField();
#     sort = models.IntegerField(max_length=10);
#
#     # 自定义属性
#     # 登录账号
#     accountName = models.CharField(max_length=20);
#     # 用户昵称
#     callingName = models.CharField(max_length=20);
#     # 密码
#     passWord = models.CharField(max_length=10);
#     # e-mail
#     userMail = models.EmailField();
#
#     #模型的默认排序规则实现
#     class Meta:
#         ordering = ['-sort']
#
#     #对象的toString()方法实现
#     def __unicode__(self):
#         return u'用户账户: %s;  用户昵称: %s' % (self.accountName, self.callingName);

# CMS基本对象
class Site(models.Model):
    # 通用属性
    createTime = models.DateTimeField();
    sort = models.IntegerField(max_length=10);
    actFlag = models.CharField(max_length=5);

    # 自定义属性
    # 站点名称
    name = models.CharField(max_length=30);
    # 访问地址
    webUrl = models.URLField();

    # # 创建人
    # founder = models.ForeignKey(User);
    # # 管理者
    # manager = models.ManyToManyField(User);

    #模型的默认排序规则实现
    class Meta:
        ordering = ['-sort']

    #对象的toString()方法实现
    def __unicode__(self):
        return self.name

class Category(models.Model):
    # 通用属性
    createTime = models.DateTimeField();
    sort = models.IntegerField(max_length=10);
    actFlag = models.CharField(max_length=5);

    # 自定义属性
    # 栏目名称
    name = models.CharField(max_length=30);

    # # 创建人
    # founder = models.ForeignKey(User);
    # # 管理者
    # manager = models.ManyToManyField(User);
    # 所属站点
    site = models.ForeignKey(Site);

    #模型的默认排序规则实现
    class Meta:
        ordering = ['-sort']

    #对象的toString()方法实现
    def __unicode__(self):
        return self.name

class Content(models.Model):
    # 通用属性
    createTime = models.DateTimeField();
    sort = models.IntegerField(max_length=10);
    actFlag = models.CharField(max_length=5);

    # 自定义属性
    # 标题
    title = models.CharField(max_length=30);
    # 内容
    textBody = models.TextField(max_length=100);

    # # 创建人
    # founder = models.ForeignKey(User);
    # # 管理者
    # manager = models.ManyToManyField(User);
    # 所属栏目
    category = models.ForeignKey(Category);

    #模型的默认排序规则实现
    class Meta:
        ordering = ['-sort']

    #对象的toString()方法实现
    def __unicode__(self):
        return self.title

