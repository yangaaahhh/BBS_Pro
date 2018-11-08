from django.contrib import admin
from BBS import models


# Register your models here.
class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'signature', 'view_count', 'created_at')
    list_filter = ('created_at',)  # 过滤
    search_fields = ('author__user__username',)  # 搜索，作者字段，首先外键到BBS_user，再外键到User

    def signature(self, obj):  # 通过自定义，展示不是本表的字段
        return obj.author.signature


admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
