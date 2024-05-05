from django.contrib import admin

from app.models import JobPost, author,location, skills

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','date','description','salary')
    list_filter=('date','salary')
    search_fields = ('title',)
    search_help_text="Write in title of job"
    # fields = (('title','salary'),'description')#to make first two appear in single line either fields or fieldsets must be specified
    fieldsets=(
        (
            'Basic Information',{
                'fields':('title','description')
            }
        ),
        (
            'More Information',{
                'classes':('collapse','wide'),
                'fields':('expiry','salary','slug','location',)
            }
        ),
    )
    pass

class locationAdmin(admin.ModelAdmin):
    list_display=('street','city','state','country','zip')

class authorAdmin(admin.ModelAdmin):
    pass
class skillsAdmin(admin.ModelAdmin):
    pass
# Register your models here.
# admin.site.register(JobPost, JobAdmin)
admin.site.register(JobPost, )
admin.site.register(location,locationAdmin)
admin.site.register(author,authorAdmin)
admin.site.register(skills,skillsAdmin)