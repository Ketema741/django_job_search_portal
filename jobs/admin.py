from django.contrib import admin
from .models import Job
from candidates.models import CandidateJobMap

#Register your models here.

class CandidateInline(admin.TabularInline):
    model = CandidateJobMap

    def get_readonly_fields(self,request,*args,**kwargs):
        model = CandidateJobMap
        if request.user.is_superuser:
            return []
        else:
            return []
       

class JobAdmin(admin.ModelAdmin):
    # exclude = ('creator')
    list_display = ('position_name','creator',)
    inlines = (CandidateInline,)

    def get_queryset(self, request,*args,**kwargs):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creator=request.user)

    def get_list_display(self,request,*args,**kwargs):
        if request.user.is_superuser:
            return  ('position_name','creator',)
        else:
            return ('position_name',)
    def save_model(self,request,obj,form,change):
        if not obj.pk:
            obj.creator = request.user
            obj.save()

admin.site.register(Job,JobAdmin)
