__author__ = 'Arpit shrivastav'
from django.contrib import admin
from django.urls import path
from prodemoapp.views import CustomAuthToken
from prodemoapp import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from prodemoapp.views import AdminUserCreationViewSet,EmployeeUserCreationViewSet,SubCategory_serializerviewset,Category_serializerviewset,Task_serializersViewset,Task_get_serializersviewset,SubCategory_get_serializerviewset,Employee_edit_serializerViewset,Employee_get_serializerViewset,Employee_otp_varifyserializersviewSet,Employee_otp_loginviewset,SendConfirmUserMailfor_otp_login,Panding_Task_get_serializersviewset,forgot_password_Organisations,new_password_forgot_password_viewset,setpassword_forgotviewset_for_org,ChangePasswordView_Orgnations,Packages_get_serializerviewset,Packages_create_serializerviewset,Client_get_serializerviewset,Client_Edit_serializervieswset,Organisation_get_serializerviewset,Subscription_get_serializervewset,Subscription_edit_serializervewset,Organisation_edit_serializerviewset,Pyment_get_serializerviewet,Pyment_create_serializerviewet,get_all_account,accounts_serializer_edit_viewset,get_task_allviewset,bar_chart_serializerviewset,Task_trackingserializerviewset,panding_amt_serializerviewset,Task_tracking_get_serializerviewset,admin_id,update_password_serializerviewset,Category_serializerpostviewset
from prodemoapp.views import *

router = DefaultRouter()
#Organisations Urls
router.register(r'all_account',get_all_account,basename='all_account')
router.register(r'edit_user',accounts_serializer_edit_viewset,basename='edit_user')
router.register(r'setpassword_forgot_org', setpassword_forgotviewset_for_org, basename='setpasswordforgot')
router.register(r'Organisations_create', AdminUserCreationViewSet, basename='New_Organisations_create')
router.register(r'Organisations_get', Organisation_get_serializerviewset, basename='Organisations_get')
router.register(r'Organisations_edit', Organisation_edit_serializerviewset,basename='Organisation_edit')
router.register(r'reset_password', forgot_password_Organisations, basename='reset_password')

router.register(r'ChangePassword', ChangePasswordView_Orgnations, basename='ChangePassword')


router.register(r'new_password', new_password_forgot_password_viewset, basename='Employeenewpassword')

#Task Url
router.register(r'task', Task_serializersViewset, basename='task')
router.register(r'taskget', Task_get_serializersviewset, basename='tskg1')
#router.register(r'taskpandingget', Panding_Task_get_serializersviewset, basename='tskg')
router.register(r'get_all_task', get_task_allviewset, basename='get_all_task')

# Category subCategory Url
router.register(r'Categorygetorg', Category_serializerviewset, basename='Category')
router.register(r'catgorycreate', Category_serializerpostviewset,basename='catgorycreate')
router.register(r'subCategorycreate', SubCategory_serializerviewset, basename='subCategorycreate')
router.register(r'subCategorygetorg', SubCategory_get_serializerviewset, basename='subg')
router.register(r'subCategoryget', SubCategory_get_serializersviewsetemp, basename='subCategoryget')
router.register(r'Category', Category_get,basename='Category')

# employee Url
router.register(r'employee_create', EmployeeUserCreationViewSet, basename='user1')
router.register(r'employee', Employee_edit_serializerViewset, basename='empedit')
router.register(r'employeeget', Employee_get_serializerViewset, basename='empget')
router.register(r'mobauth', Employee_otp_varifyserializersviewSet, basename='mobauth')
router.register(r'varify_mobile', SendConfirmUserMailfor_otp_login, basename='varify_mobile')
#router.register(r'employeeotp_varify123', SendConfirmUserMailfor_otp_login, basename='empget')
#router.register(r'users2', EmployeeUserCreationViewSet, basename='user1')
#router.register(r'admin',admin.site.urls,basename='admin')
router.register(r'get_client_list', Client_get_serializerviewset,basename='get_client_list')
router.register(r'edit_client', Client_Edit_serializervieswset,basename='edit_client')


router.register(r'Packages_get', Packages_get_serializerviewset)
router.register(r'Packages_create', Packages_create_serializerviewset,basename='Packages_create')
router.register(r'Subscription_get', Subscription_get_serializervewset,basename='Subscription_get')
router.register(r'Subscription_edit', Subscription_edit_serializervewset,basename='Subscription_edit')


router.register(r'Pyment_get', Pyment_get_serializerviewet,basename='Pyment_get')
router.register(r'Pyment_create', Pyment_create_serializerviewet,basename='Pyment_create')
router.register(r'pament2', Pyment_create_serializerviewet2,basename='pyment2')
router.register(r'bar_chart', bar_chart_serializerviewset,basename='bar_chart')
router.register(r'tracking_task', Task_trackingserializerviewset,basename='tracking_task')
router.register(r'tracking_task_get', Task_tracking_get_serializerviewset,basename='tracking_task_get')
router.register(r'amt_panding', panding_amt_serializerviewset,basename='amt_panding')
router.register(r'admin_id', admin_id,basename='admin_id')
router.register(r'update', update_password_serializerviewset,basename='update')

router.register(r'updatelogo', uploadelogoimage,basename='updatelogo')


router.register(r'updateempimage', ulpoademployeeimage,basename='updateempimage')
router.register(r'orgauth', emaillogin,basename='updateempimage')
router.register(r'admin_img', uploadadminimg,basename='admin_img')




urlpatterns = router.urls


