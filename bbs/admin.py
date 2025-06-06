from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article # models.pyからArticleクラスをインポート

admin.site.register(Article)    # DjangoAdminにArticleクラスを登録