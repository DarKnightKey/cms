from django.contrib import admin

# Register your models here.
from webSite.models import Site, Category, Content

# class UserAdmin(admin.ModelAdmin):
#     # 列表页中展示的元素
#     list_display = ('sort', 'createTime', 'name');
#     # 列表页中用于建立过滤规则
#     list_filter = ('createTime',);

class SiteAdmin(admin.ModelAdmin):
    # 列表页中展示的元素
    list_display = ('sort', 'createTime', 'name');
    # 列表页中用于建立过滤规则
    list_filter = ('createTime',);
    # 用于按日期进行详细过滤
    date_hierarchy = 'createTime';
    # 用于根据某个字段属性进行排序
    # ordering = ('‐createTime',);

class CategoryAdmin(admin.ModelAdmin):
    # 列表页中展示的元素
    list_display = ('sort', 'createTime', 'name');
    # 列表页中用于搜索的元素
    search_fields = ('sort', 'createTime', 'name');
    # 列表页中用于建立过滤规则
    list_filter = ('createTime',);

class ContentAdmin(admin.ModelAdmin):
    # 列表页中展示的元素
    list_display = ('sort', 'createTime', 'title');
    # 列表页中用于建立过滤规则
    list_filter = ('createTime',);

# admin.site.register(User);
admin.site.register(Site, SiteAdmin);
admin.site.register(Category, CategoryAdmin);
admin.site.register(Content, ContentAdmin);