import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE','login.settings')
setup()

from loginapp.models import TemplateSelect
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room1 = "集積回路情報,計算機工学,知的学習論,	情報通信,アルゴリズム"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "情報知能工学科",
    image = "",
    room = "システム計画,システム計測"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "応用化学科",
    image = "",
    room = ""
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "建築学科",
    image = "",
    room = ""
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "市民工学科",
    image = "",
    room = ""
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "機械工学科",
    image = "",
    room = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "食料環境システム学科",
    image = "",
    room = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "資源生命科学科",
    image = "",
    room = ""
)

TemplateSelect.objects.create(
    faculty = "農学部",
    department = "生命機能科学科",
    image = "",
    room = ""
)