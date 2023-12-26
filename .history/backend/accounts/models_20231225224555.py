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
    # 通常ユーザーメソッド
