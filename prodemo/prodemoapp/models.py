from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)






''''
class subscription_packages(models.Model):
    Package_Name=models.CharField(max_length=25,blank=True,null=True)
    Package_Amount=models.CharField(max_length=45,blank=True,null=True)
    Package_Duration=models.CharField(max_length=25,blank=True,null=True)
    is_active = models.BooleanField(default=False,blank=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

class Buy_subscription_packages(models.Model):

    User_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Package_id=models.ForeignKey(subscription_packages,on_delete=models.CASCADE)
    Amount_Status=models.ForeignKey(subscription_packages,on_delete=models.CASCADE,related_name='Amount')
    Activation_Start_date=models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False,blank=True)
    Activation_Expired_date=models.DateField()
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='created_By')
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
'''










class Organisations(models.Model):
    Organisations_name=models.CharField(max_length=25,blank=True,null=True)
    Organisations_email=models.EmailField()
    Logo_Image=models.ImageField(upload_to='media/Logo_Image/', blank=True,null=True)
    Admin_img=models.ImageField(upload_to='media/Admin_img/', blank=True,null=True)
    Contact_pesion_First_name=models.CharField(max_length=25,blank=True,null=True)
    Contact_pesion_Last_name=models.CharField(max_length=25,blank=True,null=True)
    Organisation_mobile_number=models.CharField(max_length=25,blank=True,null=True)
    Organisations_Uniqe_id=models.CharField(max_length=25,blank=True,null=True)
    Org_address=models.CharField(max_length=150,blank=True,null=True)
    #Organisationsp_no=models.CharField(max_length=25)
    which_user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True,related_name='Organisations_user',)
    #Organisations_Created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_active = models.BooleanField(default=False,blank=True,null=True)
    is_email_verify=models.BooleanField(default=False,blank=True,null=True)
    is_mobile_verify=models.BooleanField(default=False,blank=True,null=True)
    is_subscribe=models.BooleanField(default=False,blank=True,null=True)
    otp=models.CharField(max_length=15,blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    otp_forgot_password=models.CharField(max_length=25,blank=True,null=True)
    org_uni_id=models.CharField(max_length=25,blank=True,null=True)


    '''
    def __str__(self):
        x=self.Organisations_email
        for i in x:
            if i.isalpha()==False:
                p=x.index(i)
                break
            else:
                pass

        return self.Organisations_email[0:int(p)]
        '''
class Employee_data(models.Model):
    Employee_First_Name=models.CharField(max_length=15,blank=True,null=True)
    Employee_Last_Name=models.CharField(max_length=15,blank=True,null=True)
    Employee_Addres=models.TextField(null=True,blank=True)
    Zip_Code=models.CharField(max_length=15,blank=True,null=True)
    Employee_email=models.EmailField(null=True,blank=True)
    Employee_Uniqe_id=models.CharField(max_length=25,blank=True,null=True)
    Employee_image=models.ImageField(upload_to='media/employee_images/', blank=True,null=True)
    Employee_otp=models.CharField(max_length=15,blank=True,null=True)
    Employee_mobile_number=models.CharField(max_length=25)
    Employee_DOB=models.DateField(blank=True,null=True)
    Employee_DOJ=models.DateField(blank=True,null=True)
    Employee_Create=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Employee_Update=models.DateTimeField(auto_now=True)
    Supervisor=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='Supervisor')
    IS_ACCOUNTENT=models.BooleanField(default=False)
    which_user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Employee_user',blank=True,null=True)
    which_Organisations=models.ForeignKey(Organisations,on_delete=models.CASCADE,related_name='Employee_user',blank=True,null=True)
    is_active = models.BooleanField(default=False,blank=True,null=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

class Client(models.Model):
    Client_name=models.CharField(max_length=50,blank=True,null=True)
    Client_email=models.EmailField(unique=True,null=True,blank=True)
    Client_mobile_number=models.CharField(max_length=25)
    #Type_Of_Client=models
    Client_Create=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Client_Update=models.DateTimeField(auto_now=True)
    Client_Firm_Registration_number=models.CharField(max_length=50,blank=True,null=True)
    Client_Firm_Gst_number=models.CharField(max_length=50,blank=True,null=True)
    Client_Firm_TIN_number=models.CharField(max_length=50,blank=True,null=True)
    Client_PAN_number=models.CharField(max_length=12,blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    which_Organisations=models.ForeignKey(Organisations,on_delete=models.CASCADE,blank=True,null=True)






class Category(models.Model):
    Category_name=models.CharField(max_length=50,unique=True)
    Category_Created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    which_Organisations = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)


class SubCategory(models.Model):
    SubCategory_name=models.CharField(max_length=50,unique=True)
    SubCategory_Created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Category=models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    #which_Organisations = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)


class attachments(models.Model):
    img=models.FileField(blank=True, null=True,upload_to='media/attachments/')

Task_Statu = (
    ("New", "New"),
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("Complete", "Complete"),
    ("Cancel", "Cancel"),
    ("Invoice Paid", "Invoice Paid"))
class Task(models.Model):
    Task_Title=models.CharField(max_length=50)
    Task_Category_name=models.ForeignKey('Category',on_delete=models.CASCADE)
    Task_SubCategory_name=models.ForeignKey('SubCategory',on_delete=models.CASCADE)
    Task_Status = models.CharField( max_length = 30, choices = Task_Statu, default = 'New')
    #Mobile_number_client=models.ForeignKey('Client',on_delete=models.CASCADE,blank=True,null=True,related_name='Client_Mobile_number')
    Task_Client_name=models.ForeignKey('Client',on_delete=models.CASCADE,blank=True,null=True,related_name='Client_name_task')
    Task_Amount= models.CharField(max_length=50,blank=True,null=True)
    is_paid=models.BooleanField(default=False)
    Task_Created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Task_assignment_to=models.ManyToManyField(User,related_name='assignment_of_task')
    Task_Comment=models.TextField(blank=True,null=True)
    Task_attchments=models.ManyToManyField(attachments,blank=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    which_manager=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='manager')
    which_organisation=models.ForeignKey(Organisations,on_delete=models.CASCADE,null=True,blank=True)

    Due_date=models.DateField(blank=True,null=True)


#class Clients(models.Model):


@receiver(post_save, sender=Task)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Task_tracking.objects.create(Task_id=instance)



Task_Statu = (
    ("New", "New"),
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("Complete", "Complete"),
    ("InvoicePaid", "InvoicePaid"))


class Task_tracking(models.Model):
    Task_id=models.ForeignKey(Task,on_delete=models.CASCADE)
    Task_Status = models.CharField( max_length = 30, choices = Task_Statu, default = 'New')
    date=models.DateField(auto_now_add=True)
    Task_Comment=models.TextField(null=True,blank=True)
    create_date=models.DateField(auto_now_add=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)



class Notification(models.Model):
    Title=models.TextField()
    Sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='sender')
    View=models.BooleanField(default=False)
    Task_id=models.ForeignKey(Task,on_delete=models.CASCADE,null=True,blank=True)
    Receiver_emp=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='Receiver_emp')
    Img=models.ForeignKey(Employee_data,on_delete=models.CASCADE,null=True,blank=True)
    Description=models.TextField()
    Create_date=models.DateField()
    CreatedBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='createdBy')



Packages_Choices = (
    ("N", "None"),
    ("B", "Basic"),
    ("P", "Premium"),
    ("Pro", "Professional"))

class Packages_type_Choices(models.Model):
    Package_typs_name=models.CharField(max_length=40,blank=True,null=True)
    def __str__(self):
        return self.Package_typs_name

#monthly quarterly half yearly yearly
Package_Durations = (
    ("30","Monthly" ),
    ("90","Quarterly"),
    ("180","Half_yearly"),
    ("365","Yearly"))


class Packages(models.Model):
    Package_Type = models.CharField(max_length=150,null=True,blank=True)
    Package_price=models.IntegerField(null=True,blank=True)
    currency =models.CharField(max_length=15,null=True,blank=True)
    Package_Duration=models.CharField( max_length = 30, choices = Package_Durations, default = 'Monthly')
    Package_Benefits=models.TextField()
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)


class Payment(models.Model):
    Response=models.TextField(null=True,blank=True)
    package_name=models.ForeignKey(Packages,on_delete=models.CASCADE,null=True,blank=True)
    Organisation_name=models.ForeignKey(Organisations,on_delete=models.CASCADE)
    Ordr_ID=models.CharField(max_length=100,null=True,blank=True,unique=True)
    Payment_Method=models.CharField( max_length = 100,null=True,blank=True)
    Amount=models.CharField(max_length=40,null=True,blank=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)



class Subscription(models.Model):
    Organisation_id=models.ForeignKey(Organisations,on_delete=models.CASCADE,null=True,blank=True)
    Package_name=models.ForeignKey(Packages,on_delete=models.CASCADE,null=True,blank=True)
    Subscription_start_date=models.DateField(auto_now_add=True, blank=True, null=True)
    Remaining_days=models.IntegerField(blank=True, null=True)
    Subscription_End_date=models.DateField(blank=True, null=True)
    Payment_ID=models.ForeignKey(Payment,on_delete=models.CASCADE,blank=True, null=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)









































