from django.contrib import admin

# Register your models here.

from .models import mypost

# class mypostModelAdmin(admin.ModelAdmin):
#
#     list_display = ["tittle","updated","timestamp"]
#     list_display_links = ["updated"]
#     list_editable = ["tittle"]
#     list_filter = ["tittle","content"]
#     search_fields = ["tittle","content"]
#    # admin_order_field = ["tittle"]
#
#     class Meta:
#         module = mypost


admin.site.register(mypost)