from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import MyCustomPage

class MyCustomPageModelAdmin(ModelAdmin):
    model = opnlendPage
    menu_label = "opnlend"
    menu_icon = "pilcrow"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    search_fields = ("title",)

modeladmin_register(MyCustomPageModelAdmin)
