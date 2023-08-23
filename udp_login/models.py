from django.core.exceptions import ValidationError
from django.db import models
import random
import string


def validate_login_user(value):
    """Проверка на наличие пробелов в поле login_user"""
    if ' ' in value:
        raise ValidationError("Логин не должен содержать пробелы")


class UserInfo(models.Model):
    """Информация о пользователях"""
    user_name = models.CharField(verbose_name='Пользователь', max_length=500)
    login_user = models.CharField(verbose_name='Логин', max_length=50, unique=True, validators=[validate_login_user],
                                  help_text='При создании Логина учесть приставки: k - Мониторинг кадров, inv_ - Мониторинг инвестпроектов')
    password_user = models.CharField(verbose_name='Пароль', max_length=50, null=True, blank=True,
                                     help_text='Пароль автоматически сгенерируется при сохранении, если вы не придумали свой')
    note = models.CharField(verbose_name='Примечание', max_length=100, null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True,help_text='Если пользователь активный то ставим галочку')
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Информация о пользователях'
        verbose_name_plural = 'Информация о пользователях'
        ordering = '-date_updated',

    def __str__(self):
        return self.user_name

    def generate_random_password(self):
        """Генератор пароля для поля password_user"""
        length = random.randint(3, 8)  # Генерация случайной длины от 3 до 8
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def save(self, *args, **kwargs):
        """Сохранением сгенерированный пароль в поле password_user"""
        if not self.password_user:
            self.password_user = self.generate_random_password()
        super().save(*args, **kwargs)
        """Преобразование поля note в заглавные буквы перед сохранением"""
        if self.note:
            self.note = self.note.title()
        super(UserInfo, self).save(*args, **kwargs)
