from django import forms
from django.contrib.auth.models import User

from .models import Account,Review

# フォームクラス作成
#書き換える場合フィールド書けばいい。
class AccountForm(forms.ModelForm):
    # Userの上書き
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User #モデルに合わせてフォームが作成される。つまり、自分でフィールド設定しなくていいことだと思う。
        # フィールド指定 画面上に表示される
        fields = ('username','email','password')
        # フィールド名指定　
        labels = {'username':"ユーザーID",'email':"メール"}


class ReviewForm(forms.ModelForm):   
    class Meta:
        model = Review
        fields = ['score1','score2','score3','score4', 'comment']
        # フィールド名指定
        labels = {'score1':'担当教授の干渉度','score2':'先輩・後輩との関わり','score3':'研究室の設備','score4':'学会のレベル', 'comment':'コメント'}

class Select_d_f(forms.Form):
    choice_de = (

    )
    de = forms.ChoiceField()
