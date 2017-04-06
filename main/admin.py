from django.contrib import admin
from main.models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'email', 'wechat_openid')
	list_filter = ('username', )
	list_select_related = ('username', )
	search_fields = ['username', 'email']

class ResumeAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')
	search_fields = ['filename']

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'coname', 'email', 'login_num')
	search_fields = ['coname','email']

class JobAdmin(admin.ModelAdmin):
	list_display = ('id', 'company', 'position')
	list_filter = ('company',)
	list_select_related = ('company',)
	search_fields = ('company__coname','position')

class TopicAdmin(admin.ModelAdmin):
	list_display = ('id', 'content')

class ApplicationAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'job', 'status')
	list_filter = ('user', )
	list_select_related = ('user', )
	search_fields = ['user__username',]

class VideoAdmin(admin.ModelAdmin):
	list_display = ('id', 'application', 'topic')

class WorkExperienceAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'company', 'position')

class LogAdmin(admin.ModelAdmin):
	list_display = ('id', 'userid','usertype','url','time','timestamps')

class DataReportAdmin(admin.ModelAdmin):
	list_display = ('id', 'datetime')

class DailyRecordAdmin(admin.ModelAdmin):
	list_display = ('id', 'datetime')

class ArticleInfoAdmin(admin.ModelAdmin):
	class Media:
		js=("/static/js/article/jquery-1.8.0.min.js",
			"/static/tinymce/js/tinymce/jquery.tinymce.min.js",
			"/static/tinymce/js/tinymce/tinymce.min.js",
			"/static/js/article/tinymce.js")
	
	list_display = ('id', 'title')

class ImageInfoAdmin(admin.ModelAdmin):
	list_display = ('id',)

class LogintimeAdmin(admin.ModelAdmin):
	list_display = ('user', 'company', 'time')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id','ment_companyid','ucomment','ccomment','comments','comm_time','position','quote_who','anonymous','delete')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Log, LogAdmin)
# admin.site.register(DataReport, DataReportAdmin)
# admin.site.register(DailyRecord, DailyRecordAdmin)
admin.site.register(Article, ArticleInfoAdmin)
admin.site.register(Image,ImageInfoAdmin)
admin.site.register(logintime, LogintimeAdmin)
admin.site.register(Comment,CommentAdmin)

#admin.site.register(Comment,CommentAdmin)