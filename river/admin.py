from django.contrib import admin

from river.models import Choice, Logic, Condition, ApproveNode

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "pub_date"]
class LogicAdmin(admin.ModelAdmin):
    list_display = ["name", "pub_date"]
class ConditionAdmin(admin.ModelAdmin):
    list_display = ["choice", "logic", "val", "pub_date"]
class ApproveNodeAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "pub_date"]

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Logic, LogicAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(ApproveNode, ApproveNodeAdmin)