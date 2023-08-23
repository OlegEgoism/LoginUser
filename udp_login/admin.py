from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilterBuilder
from .models import UserInfo
from .resources import UserInfoResource
from django import forms

admin.site.site_header = 'Информация о пользователях портала'


class UserInfoAdminForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'

    user_name = forms.CharField(widget=forms.TextInput(attrs={'size': '100'}), label='Пользователь')
    note = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}), label='Примечание')


@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin):
    """Информация о пользователях"""
    form = UserInfoAdminForm
    resource_class = UserInfoResource
    list_display = 'user_name', 'login_user', 'password_user', 'note', 'is_active', 'date_created', 'date_updated',
    list_editable = 'note', 'is_active',
    list_filter = ("date_created", DateRangeFilterBuilder()), ("date_updated", DateRangeFilterBuilder()), 'is_active', 'note',
    search_fields = 'user_name', 'note', 'login_user',
    search_help_text = 'Поиск по пользователю, логину и примечанию'
    list_per_page = 20
