from django.contrib import admin

from pepysdiary.common.admin import YearmonthListFilter
from pepysdiary.diary.models import Entry, Summary


class DiaryDateYearmonthListFilter(YearmonthListFilter):
    filter_field = "diary_date"


class EntryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "diary_date",
        "comment_count",
    )
    list_filter = (DiaryDateYearmonthListFilter,)
    search_fields = [
        "title",
        "text",
        "footnotes",
    ]
    readonly_fields = (
        "date_created",
        "date_modified",
        "last_comment_time",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "diary_date",
                    "text",
                    "footnotes",
                    "allow_comments",
                ),
            },
        ),
        (
            None,
            {
                "fields": (
                    "date_created",
                    "date_modified",
                    "comment_count",
                    "last_comment_time",
                ),
            },
        ),
    )


admin.site.register(Entry, EntryAdmin)


class SummaryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = [
        "title",
        "text",
    ]
    readonly_fields = (
        "date_created",
        "date_modified",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "summary_date",
                    "text",
                )
            },
        ),
        (
            None,
            {
                "fields": (
                    "date_created",
                    "date_modified",
                )
            },
        ),
    )


admin.site.register(Summary, SummaryAdmin)
