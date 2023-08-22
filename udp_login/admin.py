from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilterBuilder
from .models import UserInfo
from .resources import UserInfoResource

admin.site.site_header = 'Информация о пользователях портала'


@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin):
    """Информация о пользователях"""
    resource_class = UserInfoResource
    list_display = 'user_name', 'login_user', 'password_user', 'note', 'is_active', 'date_created', 'date_updated',
    list_editable = 'note', 'is_active',
    list_filter = ("date_created", DateRangeFilterBuilder()), ("date_updated", DateRangeFilterBuilder()), 'is_active', 'note',
    search_fields = 'user_name', 'note', 'login_user',
    search_help_text = 'Поиск по пользователю, логину и примечанию'
    list_per_page = 20
