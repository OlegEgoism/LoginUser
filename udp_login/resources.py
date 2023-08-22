from import_export import resources
from import_export.fields import Field
from .models import UserInfo


class UserInfoResource(resources.ModelResource):
    user_name = Field(column_name='Пользователь', attribute='user_name')
    login_user = Field(column_name='Логин', attribute='login_user')
    password_user = Field(column_name='Пароль', attribute='password_user')
    note = Field(column_name='Примечание', attribute='note')

    class Meta:
        model = UserInfo
        fields = 'user_name', 'login_user', 'password_user', 'note',  # 'status', # 'date_created', 'date_updated'
        export_order = 'user_name', 'login_user', 'password_user', 'note',  # 'status', # 'date_created', 'date_updated'  # порядок экспорта полей
        import_id_fields = 'login_user',  # поля для определения идентификатора
        exclude = 'id',  # исключить поле
