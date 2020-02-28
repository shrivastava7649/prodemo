from django.contrib import admin
from prodemoapp.models import Employee_data,Organisations,Category,SubCategory,Task,Client,Packages,Subscription,Payment,Packages_type_Choices,Task_tracking
from rest_framework.authtoken.models import Token



admin.site.register(Employee_data)
admin.site.register(Organisations)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Task)
admin.site.register(Client)




admin.site.register(Packages)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(Task_tracking)
# Register your models here.
