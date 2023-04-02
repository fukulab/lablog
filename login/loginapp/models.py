from django.db import models
# ユーザー認証
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Userにも保存されている。
    #追加の部分がAccountのテーブルに保存されている。
    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self): #管理画面で見るときに役に立つ。
        return self.user.username

class TemplateSelect(models.Model):

    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_pics",blank=True)
    room = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.faculty}_{self.department}'


