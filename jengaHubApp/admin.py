from django.contrib import admin
from jengaHubApp.models import Professional,Message, Project, Feedback, News

# Register your models here.
admin.site.register(Professional)
admin.site.register(Project)
admin.site.register(Feedback)
admin.site.register(Message)
admin.site.register(News)