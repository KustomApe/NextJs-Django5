from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from hashids import Hashids

# カスタムユーザーマネージャークラス
class UserManager(BaseUserManager):
    # 通常ユーザー作成メソッド
    def create_user(self, email, password=None, **extra_fields):
        # Check email
        if not email:
            raise ValueError('メールアドレスは必須です')
        # メールアドレスの正規化
        email = self.normalize_email(email)
        email = email.lower()

        # ユーザーオブジェクトの作成と保存
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    # スーパーユーザー作成メソッド
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

# カスタムユーザーアカウントモデル
class UserAbstract(AbstractBaseUser, PermissionsMixin):
    uid = models.CharField('uid', max_length=30, unique=True)
    email = models.EmailField('メールアドレス', max_length=255, unique=True)
    name = models.CharField('名前', max_length=255)
