from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Article, Thema, ArticleThema
from django.forms import BaseInlineFormSet


class ArticleThemaInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = False
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                if not is_main:
                    is_main = True
                else:
                    raise ValidationError('Основная тема возможна только одна.')

            if not is_main:
                raise ValidationError('Укажите основной раздел')

        if len(self.forms) == 0:
            raise ValidationError("Не указана тема")

        return super().clean()


class ArticleThemaInline(admin.TabularInline):
    model = ArticleThema
    formset = ArticleThemaInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ArticleThemaInline]


@admin.register(Thema)
class ThemaAdmin(admin.ModelAdmin):
    list_display = ['id', 'thema']
    inlines = [ArticleThemaInline]