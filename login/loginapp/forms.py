from django import forms
from django.contrib.auth.models import User
from .models import Account
#ModelFromは簡単に作れる。また、簡単にデータベースに入力できる。
# フォームクラス作成
#書き換える場合フィールド書けばいい。
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User #モデルに合わせてフォームが作成される。つまり、自分でフィールド設定しなくていいことだと思う。
        # フィールド指定 画面上に表示される
        fields = ('username','email','password')
        # フィールド名指定　
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name','account_image',)
        labels = {'last_name':"苗字",'first_name':"名前",'account_image':"写真アップロード",}

class Select_d_f(forms.Form):
    choice_de = (

    )
    de = forms.ChoiceField()