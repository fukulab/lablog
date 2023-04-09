import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','login.settings')
from django import setup
setup()

from loginapp.models import TemplateSelect

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "集積回路情報",
    professor = "沼",
    comment = "こっちに行っとけばよかった。",
    url = "https://ufhuehfuhsuhdfksudhfksufe"

)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "計算機工学",
    professor = "沼",
    comment = "こっちに行っとけばよかった。",
    url = "https://ufhuehfuhsuhdfksudhfksufe"
)

TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "情報通信",
    professor = "沼",
    comment = "こっちに行っとけばよかった。",
    url = "https://ufhuehfuhsuhdfksudhfksufe"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "アルゴリズム",
    professor = "沼",
    comment = "こっちに行っとけばよかった。",
    url = "https://ufhuehfuhsuhdfksudhfksufe"
)
TemplateSelect.objects.create(
    faculty = "工学部",
    department = "電気電子工学科",
    image = "",
    room = "知的学習論",
    professor = "沼",
    comment = "こっちに行っとけばよかった。",
    url = "https://ufhuehfuhsuhdfksudhfksufe"
)

# TemplateSelect.objects.create(
#     faculty = "工学部",
#     department = "情報知能工学科",
#     image = "",
#     room = "システム計画,システム計測"
# )

# TemplateSelect.objects.create(
#     faculty = "工学部",
#     department = "応用化学科",
#     image = "",
#     room = ""
# )
# TemplateSelect.objects.create(
#     faculty = "工学部",
#     department = "建築学科",
#     image = "",
#     room = ""
# )

# TemplateSelect.objects.create(
#     faculty = "工学部",
#     department = "市民工学科",
#     image = "",
#     room = ""
# )
# TemplateSelect.objects.create(
#     faculty = "工学部",
#     department = "機械工学科",
#     image = "",
#     room = ""
# )

# TemplateSelect.objects.create(
#     faculty = "農学部",
#     department = "食料環境システム学科",
#     image = "",
#     room = ""
# )

# TemplateSelect.objects.create(
#     faculty = "農学部",
#     department = "資源生命科学科",
#     image = "",
#     room = ""
# )

# TemplateSelect.objects.create(
#     faculty = "農学部",
#     department = "生命機能科学科",
#     image = "",
#     room = ""
# )