from django.contrib import admin
from OpenMap import models
# Register your models here.


class WhatWeDoInLine(admin.TabularInline):
    model = models.WhatWeDo
    extra = 3


class AboutOpenMapAdmin(admin.ModelAdmin):
    inlines = [WhatWeDoInLine]





admin.site.register(models.AboutOpenMap, AboutOpenMapAdmin)
admin.site.register(models.OurProjects)
admin.site.register(models.TeamMembers)
admin.site.register(models.Phrase)
admin.site.register(models.Library)
admin.site.register(models.WhatWeDoPhrase)
admin.site.register(models.ProjectPhrase)
admin.site.register(models.TeamPhrase)
admin.site.register(models.LibraryPhrase)
admin.site.register(models.BlogPhrase)

