import random
#from rest_framework import Base64ImageField
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from prodemo.settings import base_url
from django.contrib.auth.models import User
from django.core import signing
from rest_framework import serializers
import requests
from prodemoapp.models import Employee_data,Organisations,Category,SubCategory,Task,Client,Packages,Subscription,Payment,attachments,Packages_type_Choices,Task_tracking
from django.template.loader import render_to_string, get_template
from rest_framework.validators import UniqueValidator
from django.core.mail import send_mail
from drf_extra_fields.fields import Base64ImageField
#from drf_extra_fields.fields import Base64ImageField


'''
class WhichUserSerializer(serializers.ModelSerializer):
	class Meta:
		model =  User
		fields = '__all__'
		'''


class accounts_serializer(serializers.Serializer):
    Enter_emil=serializers.EmailField()


class accounts_serializer_edit(serializers.ModelSerializer):
    class Meta:
            model = User
            fields =['id','username','is_active','date_joined']



class ChangePasswordSerializer_for_Organisations(serializers.Serializer):

    which_user=serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class New_passwordresetserializer(serializers.Serializer):
    Enter_Your_Email=serializers.EmailField()
    Enter_Your_OTP =serializers.CharField()
    Enter_new_password =serializers.CharField()
    Confrom_password =serializers.CharField()




class Organisations_passwords_serializer(serializers.ModelSerializer):
    Enter_your_user_name=serializers.CharField(allow_blank=False, write_only=True)

    def validate(self, data):
        try:
            x=User.objects.get(username=data['Enter_your_user_name'])
        except:
            raise serializers.ValidationError("username is not valid")
        return data
    def create(self, validated_data):
        '''

        l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '#', '$', '%', '&', '*', '?', '(', ')', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        s=set()
        while True:
            s.add(random.choice(l))
            if len(s)==10:
                break
        otpf=str()
        for i in s:

            otpf=str(otpf+str(i))
            '''
        x=User.objects.get(username=validated_data['Enter_your_user_name'])
        y=Organisations.objects.get(which_user =x.id)


        otpf=random.randint(111111,999999)
        y.otp_forgot_password=str(otpf)
        y.save()



        username=validated_data['Enter_your_user_name']
        x=User.objects.get(username=validated_data['Enter_your_user_name'])
        try:
            value = signing.dumps((x.username,))
            email_body = render_to_string('forgotpassword.html',{'otp':otpf,'base_url':(base_url).strip()})

            send_mail(' Click on Button To change Password '+str(otpf), (base_url).strip()+'reset_password/   '+value+' ', 'youflip@publicdomain.co.in', [x.email,],html_message=email_body)

        except:
            pass
        return x

    class Meta:
        model = User
        fields = ['Enter_your_user_name']


class Organisations_serializers(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False,validators=[UniqueValidator(queryset=User.objects.values_list('username', flat=True))])
    confirm_password = serializers.CharField(style={'input_type': 'password'}, allow_blank=False, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, allow_blank=False,)
    phonenumber = serializers.CharField(allow_blank=False, write_only=True)
    Organisation_Name =serializers.CharField(style={'input_type': 'password'}, allow_blank=False,)
    Organisation_Logo =serializers.ImageField(required=False)


    Contact_person_first_name=serializers.CharField(allow_blank=False, write_only=True)
    Contact_person_last_name=serializers.CharField(allow_blank=False, write_only=True)
    Contact_person_img=serializers.ImageField(required=False)


    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        #Organisationemls = [x.Organisations_email for x in Organisations.objects.all()]
        return data
    def create(self, validated_data):
        Employee_name=validated_data['Contact_person_first_name']
        Employee_name=Employee_name+str( validated_data['Contact_person_last_name'])
        First_name=validated_data['Contact_person_first_name']
        Last_Name=validated_data['Contact_person_last_name']
        Email=validated_data['email']
        validated_data.pop('Contact_person_first_name',None)
        validated_data.pop('Contact_person_last_name',None)
        try:
            img=validated_data['Contact_person_img']
            validated_data.pop('Contact_person_img',None)
        except:
            img=None

        try:
            org_img=validated_data['Organisation_Logo']
        except:
            org_img=None
        validated_data.pop('Organisation_Logo',None)

        #password = validated_data.pop('password', None)
        email=self.validated_data['email']
        mob=self.validated_data['phonenumber']
        validated_data.pop('phonenumber',None)
        #validated_data.pop('phonenumber', None)
        name = (validated_data['email'])
        password = validated_data['password']
        validated_data.pop('password', None)
        phonenumber=validated_data.pop('phonenumber',None)
        unique_id_of_org=(validated_data['Organisation_Name'])
        nameorg=(validated_data['Organisation_Name'])
        Organisations_name=validated_data['Organisation_Name']
        validated_data.pop('Organisation_Name',None)
        print('========================================================',type(unique_id_of_org))
        unique_id_of_org=unique_id_of_org.upper()
        p=unique_id_of_org.split()
        length_of_name=len(p)
        if length_of_name ==4:
            f=str()
            print('we are from if 4 ===================== ===============================================================')
            for i in p:
                f=f+i[0]
            final_name=str(f[0:2]+'0')

            user_last_name=[x.last_name for x in User.objects.all()]
            for i in user_last_name:
                if final_name == i:
                    len_of_old=len(final_name)
                    remain=int(final_name[len_of_old-1])
                    remain=remain+1
                    final_name=str(final_name[0:2]+str(remain))
            #final_name=final_name+'0'+str(random.randint(1111,9999))
            #print(final_name)
        elif length_of_name >=5:
            f=str()
            for i in p:
                f=f+i[0]
            final_name=f[0:3]+'0'
            #final_name=final_name+str(random.randint(11111,99999))
            user_last_name=[x.last_name for x in User.objects.all()]
            for i in user_last_name:
                if final_name == i:
                    #final_name=final_name+0

                    len_of_old=len(final_name)
                    remain=int(final_name[len_of_old-1])
                    remain=remain+1
                    final_name=str(final_name[0:3]+str(remain))
            print(final_name)
        else:
            final_name=p[0]
            final_name=str(final_name[0:3]+'0')
            user_last_name=[x.last_name for x in User.objects.all()]
            print('we are from if else  ===================== ===============================================================')
            for i in user_last_name:
                if final_name == i:
                    print('we are from second if   ===================== ===============================================================')
                    len_of_old=len(final_name)
                    remain=int(final_name[len_of_old-1])
                    remain=remain+1
                    final_name=str(final_name[0:3]+str(remain))
            else:
                pass
                #final_name=p[0]
                #final_name=str(final_name[0:3]+'0')
                #final_name=final_name+str(random.randint(11111,99999))
                #print(final_name)

        name=str('firm-'+final_name+str(random.randint(11111,99999)))
        p=10
        n=0
        def idcreate():
            try:
                n=name
                Organisations.objects.get(org_uni_id=n)
                p=0
            except:
                pass

            return n
        n=idcreate()
        if p==0:
            n=idcreate()
        else:
            idcreate()


        l=['mob','web']
        for i in l:
            #org user creaing
            print('================================= 235 i=',unique_id_of_org)
            user = self.Meta.model(**validated_data)
            user.is_active = False
            user.username=str(n+':'+str(i))
            print('==================================================================line no 100',name)
            user.first_name=unique_id_of_org#validated_data['First_name']
            user.last_name=final_name
            user.set_password(password)
            user.email=email
            user.save()
        uso=user
        x=Organisations.objects.create(Organisations_email=email,Organisation_mobile_number=mob,which_user=user,Organisations_Uniqe_id=final_name,Organisations_name=nameorg,Logo_Image=org_img,Contact_pesion_First_name=First_name,Contact_pesion_Last_name=Last_Name,Admin_img=img,org_uni_id=n)

        # working in the Organisations Serializer

        #try:
        value = signing.dumps((user.username,))


#<a href="(base_url).strip()+'/verify-account/'+value+'/'"</a>
#<a href="'+FRONTEND_BASE_URL+'/email-verification/?token='+str(token)+'">'+FRONTEND_BASE_URL+'/email-verification/?token='+str(token)+'</a>
        email_body = render_to_string('email-confirmation.html',{'confirmation_token':value,'base_url':(base_url).strip()})
        send_mail('Confirmation Email By the Flit_Webs for  CA firm  account', (base_url).strip()+'/verify-account/'+value+'/', 'youflip@publicdomain.co.in', [user.email,],html_message=email_body,)
        #except:
         #   pass
        org_id=x.Organisations_Uniqe_id
        validated_data.pop('email',None)

        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++ line 112',org_id)
        oid=Organisations.objects.get(id=x.id)
        print('================================================= oid == from line 114',oid)
        def check():
            p=1

            Employee_Uniqe_idf=str(org_id+str(random.randint(11111,99999)))
            try :
                Employee_data.objects.get(Employee_Uniqe_id=Employee_Uniqe_idf)
                p=10
            except:
                pass
            if p==10:
                #print('=========================================================== value of --------p ',p)
                check()
            else:
                print('=========================================================== inside the fuction body line 128 ')
                return Employee_Uniqe_idf


                #
        Employee_Uniqe_idf=check()
        #print('=========================================================== Employee_Uniqe_idf line 135 ',Employee_Uniqe_idf)
        l=[]
        for i in l:
            user = self.Meta.model(**validated_data)

            user.first_name=Employee_name
            user.is_active = False
            final_nam=str(Employee_Uniqe_idf)+':'+str(i)
            #Organisationemls = [x.username for x in User.objects.all()]
            #print(Organisationemls)
            #try:
                #pass

            user.username=final_nam
            user.set_password(password)
            user.email=Email
            user.save()
            #x=Organisations.objects.get(id=Organisations_name)

        #Employee_data.objects.create(Employee_mobile_number=mob,which_user=user,Employee_Uniqe_id=Employee_Uniqe_idf,which_Organisations=oid,Employee_First_Name=First_name,Employee_Last_Name=Last_Name,Employee_email=Email,IS_ACCOUNTENT=True)



        return uso

    class Meta:
        model = User
        fields = ( 'password', 'confirm_password','email','phonenumber','Organisation_Name','Contact_person_first_name','Contact_person_last_name','Organisation_Logo','Contact_person_img')




class Organisation_get_serializer(serializers.ModelSerializer):
    class Meta:
        model = Organisations
        fields =('id','Organisations_name','Organisations_email','Contact_pesion_First_name','Contact_pesion_Last_name','Organisation_mobile_number','Organisations_Uniqe_id','is_active','createdAt','updatedAt','which_user','Logo_Image')

class Organisation_edit_serializer(serializers.ModelSerializer):
    class Meta:
        model = Organisations
        #fields='__all__'
        fields =('Organisations_name','Organisations_email','Organisation_mobile_number','Organisations_Uniqe_id','is_active','createdAt','updatedAt','which_user','Logo_Image','Contact_pesion_First_name','Contact_pesion_Last_name')





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username','email','is_active','date_joined')

class Employee_data_serializers(serializers.ModelSerializer):
    Employee_First_name =serializers.CharField( allow_blank=False, write_only=True)
    Employee_Last_name=serializers.CharField(allow_blank=False, write_only=True)
    #Employee_addres=serializers.CharField(allow_blank=False, write_only=True)
    #Employee_Zip_Code=serializers.CharField(allow_blank=False, write_only=True)
    createdBy=serializers.IntegerField(required=False)

    Employee_DOB=serializers.DateField(required=False)
    email=serializers.EmailField()
    password=serializers.CharField(style={'input_type': 'password'}, allow_blank=False, write_only=True)
    password_confirmation=serializers.CharField(style={'input_type': 'password'}, allow_blank=False, write_only=True)
    Employee_mobile_number=serializers.CharField(allow_blank=False, write_only=True)
    Employee_DOJ=serializers.DateField(required=False)
    IS_ACCOUNTENT=serializers.BooleanField(default=False)
    which_Organisations=serializers.IntegerField()
    #Employee_image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    def validate(self, data):

        if data['password'] != data.pop('password_confirmation'):
            raise serializers.ValidationError("Passwords do not match")

        try:
            p=data['which_Organisations']
            x=Organisations.objects.get(pk=p)
            which_Organisations=x.Organisations_email

        except:
            raise serializers.ValidationError(" Id not match")
        #which_Organisations=x.Organisations_email

        return data
    def create(self, validated_data):
        #Employee_DOJ1=None
        #EmployeeDOB1=None
        First_name=validated_data['Employee_First_name']
        Last_name=validated_data['Employee_Last_name']
        #Addres=validated_data['Employee_addres']
        #validated_data.pop('Employee_addres',None)
        #zip_code=validated_data['Employee_Zip_Code']
        #validated_data.pop('Employee_Zip_Code',None)
        try:
            cb=validated_data['createdBy']
        except:
            cb=None

        print('cb==========',cb)
        validated_data.pop('createdBy',None)
        password = validated_data['password']
        validated_data.pop('password', None)

        Employee_name=validated_data['Employee_First_name']
        Employee_name=Employee_name+'  '+str(validated_data['Employee_Last_name'])

        p=validated_data['which_Organisations']
        x=Organisations.objects.get(pk=p)
        which_Organisations=x.Organisations_email
        org_id=x.Organisations_Uniqe_id
        #print('===========================================================org id ',org_id)

        def check():
            p=1
         #   print('=========================================================== inside the fuction body ')
            Employee_Uniqe_idf=str(org_id+str(random.randint(11111,99999)))
            try :
                Employee_data.objects.get(Employee_Uniqe_id=Employee_Uniqe_idf)
                p=10
            except:
                pass
            if p==10:
                #print('=========================================================== value of --------p ',p)
                check()
            else:
                return Employee_Uniqe_idf

                #
        Employee_Uniqe_idf=check()
        #validated_data.pop()

        #print('creatiing data............................',p)
        #print('creatiing data............................',type(p))


        email=self.validated_data['email']
        mob=self.validated_data['Employee_mobile_number']
        #validated_data.pop('phonenumber', None)
        name = (validated_data['email'])
        name2=which_Organisations#validated_data['which_Organisations']
        final_name=str(name+':'+name2)

        phonenumber=validated_data.pop('Employee_mobile_number',None)
        isacc=validated_data.pop('IS_ACCOUNTENT',None)
        try:
            EmployeeDOB1=validated_data['Employee_DOB']
        except:
            EmployeeDOB1=None
        try:
            EmployeeDOJ1=validated_data['Employee_DOJ']
        except:
            EmployeeDOJ1=None
        Organisations_name=int(validated_data['which_Organisations'])
        oid=Organisations.objects.get(id=Organisations_name)
        print('========================================',Organisations_name)
        print('========================================',type(Organisations_name))
        #imgemp=validated_data['Employee_image']
        #validated_data.pop('Employee_image',None)
        validated_data.pop('which_Organisations',None)
        validated_data.pop('Employee_First_name',None)
        validated_data.pop('Employee_Last_name',None)
        validated_data.pop('Employee_DOB',None)
        validated_data.pop('Employee_DOJ',None)
        # createing the user in the Employee Serializer
        l=['mob','web']
        for i in l:
            user = self.Meta.model(**validated_data)

            user.first_name=Employee_name
            user.is_active = True
            final_nam=Employee_Uniqe_idf+':'+str(i)
            #Organisationemls = [x.username for x in User.objects.all()]
            #print(Organisationemls)
            #try:
                #pass

            user.username=final_nam
            print('psssword = ..........................................')
            user.set_password(password)
            user.save()
            #except:
             #       pass
                #return 0
        try:

            cbx=User.objects.get(id=int(cb))
        except:
            cbx=None

        print('EmployeeDOB1===========================',EmployeeDOB1)

        Employee_data.objects.create(Employee_email=email,Employee_mobile_number=mob,which_user=user,Employee_Uniqe_id=Employee_Uniqe_idf,which_Organisations=oid,Employee_First_Name=First_name,Employee_Last_Name=Last_name,createdBy=cbx,Employee_DOB=EmployeeDOB1,Employee_DOJ=EmployeeDOJ1)
        return user

    class Meta:
        model = User
        fields = ( 'password', 'which_Organisations','password_confirmation','email','Employee_mobile_number','IS_ACCOUNTENT','Employee_First_name','Employee_Last_name','createdBy','Employee_DOB','Employee_DOJ')



class Employee_otp_varifyserializers(serializers.ModelSerializer):
    Employee_code=serializers.CharField( allow_blank=False, write_only=True)
    def validate(self, data):
        try:

            x=User.objects.get(username=data['Employee_code'])

        except:
            raise serializers.ValidationError("Id not found  ")

        return data
    def create(self, validated_data):
        mob=0
        email=''
        x=User.objects.get(username=validated_data['Employee_code'])
        p=str(x.username)
        y=p.split(':')
        print('=======================',y)
        y=str(y[0])
        otp=str(random.randint(111111,999999))
        #x.last_name=otp
        #x.save()
        #print(data['Emter_your_Employee_code'])
        #print('y====================================',y)
        Employee_data.objects.filter(Employee_Uniqe_id=y).update(Employee_otp=otp)

        mobl=Employee_data.objects.filter(Employee_Uniqe_id=y)
        print('mobl ===============',mobl)
        for i in mobl:
            mob=i.Employee_mobile_number
            email=i.Employee_email
        #mob=mobl.Employee_mobile_number
        print('mob = ',mob)
        print('emil =',email)
        massage='''Your otp is {} for CAFIRM login'''.format(str(otp))
        senders='CAFIRM'
        url="""http://flitsms.in/api/sendhttp.php?authkey=150365AXdLl3PJwG59b3d280&mobiles={}&message={}&sender={}&route=4&country=91""".format(mob,massage,senders)
        print('=====',url)




        try:
            #value = signing.dumps((x.username,))
            value=x.username
            x=requests.get(url)
            print('====================================================== status code',x.status_code)
            send_mail('your OTP       '+otp, (base_url).strip()+'app/employeeotp_varify123/   '+value+'/', 'bitcoinora@gmail.com', [email])
        #value=x.username
        except:
            pass

        return 'Done '
    class Meta:
            model = User
            fields = ['Employee_code']





class Employee_otp_loginserializer(serializers.Serializer):
    Enter_your_otp=serializers.CharField()
    hash=serializers.CharField()




    #global username

    '''
    def __init__(self, *args, **kwargs):
        username = signing.loads(kwargs['hash'])[0]
        user = get_object_or_404(User.objects.all(),username=username)
        '''








'''
def validate(self, data):
        try:
            print(data['Emter_your_otp'])
            x=User.objects.get(username=data['Emter_your_otp'])

        except:
            raise serializers.ValidationError('Error  wrong OTP')

        return data
'''

'''
class Employee_otp_login(serializers.Serializer):
    Emter_your_otp=serializers.CharField( allow_blank=False, write_only=True)
    def validate(self, data):
        '''
class Employee_edit_serializer(serializers.ModelSerializer):

    class Meta:
        model=Employee_data
        fields='__all__'

class Employee_get_serializer(serializers.ModelSerializer):
    Supervisor=Employee_edit_serializer(many=True)
    which_user=UserSerializer()
    createdBy=accounts_serializer_edit()
    class Meta:
        model=Employee_data
        fields='__all__'
#class

class Task_serializers(serializers.ModelSerializer):
    #Task_assignment_to=UserSerializer()

    class Meta:
        model=Task
        fields = '__all__'
class attachments_serializers(serializers.ModelSerializer):
    class Meta:

        model=attachments
        fields = '__all__'



class Panding_Task_get_serializers(serializers.ModelSerializer):
    global l,m,o,p,q

    Pending=serializers.SerializerMethodField(read_only=True)
    Total=serializers.SerializerMethodField(read_only=True)
    #Complete_task=serializers.SerializerMethodField(read_only=True)
    In_progres=serializers.SerializerMethodField(read_only=True)
    New=serializers.SerializerMethodField(read_only=True)
    Cancel=serializers.SerializerMethodField(read_only=True)
    Complate=serializers.SerializerMethodField(read_only=True)
    def get_New(self,obj):

        x=obj.Task_Status
        if x=='New':
            l.append(x)
        else:
            pass
        return len(l)

    def get_Pending(self,obj):
        m=[]
        y=obj.Task_Status
        if y=='Pending':
            m.append(y)
        else:
            pass
        return len(m)
    #p=get_Total_panding_task()
    def get_Total(self,obj):
        n=[]
        z=obj.Task_Status
        n.append(z)
        return len(n)
    def get_Complate(self,obj):
        o=[]
        a=obj.Task_Status

        if a=='Complete':
            o.append(a)
        else:
            pass
        return len(o)
    def get_In_progres(self,obj):
        p=[]
        b=obj.Task_Status
        if b=='In Progress':
            p.append(b)
        else:
            pass
        return len(p)
    def get_Cancel(self,obj):
        q=[]
        c=obj.Task_Status
        if c=='Cancel':
            q.append(c)
        else:
            pass
        return len(q)

    class Meta:
        model=Task
        fields = ['Pending','Total','Cancel','New','In_progres','Complate']




class Category_serializer(serializers.ModelSerializer):
    #SubCategory=serializers.SerializerMethodField(read_only=True)
   # which_Organisations=serializers.IntegerField()

    class Meta:
        model=Category
        fields = ['id','Category_name','is_active','which_Organisations']

class SubCategory_serializer(serializers.ModelSerializer):
   # Category=serializers.IntegerField()


    class Meta:
        model=SubCategory
        fields = '__all__'#['SubCategory_name','Category']
class SubCategory_get_serializers(serializers.ModelSerializer):
    Category=Category_serializer()
    class Meta:
        model=SubCategory
        fields = '__all__'
class get_task_of_emp:

    pass


'''
    def validate(self, data):
        try:
            id=data['Package_Type']
            Packages_type_Choices.objects.get(pk=id)
        except:
             raise serializers.ValidationError(" Package_Type do not match")



    def create(self, validated_data):
        id=validated_data['Package_Type']
        Packages_type_Choices.objects.get(pk=id)
        return id
        '''

class Packages_create_serializer(serializers.ModelSerializer):
    class Meta:
            model=Packages
            fields='__all__'


class Packages_get_serializer(serializers.ModelSerializer):
    class Meta:
        model=Packages
        fields='__all__'


class Subscription_get_serializer(serializers.ModelSerializer):
    Package_name=Packages_get_serializer()
    class Meta:
        model=Subscription
        fields='__all__'

class Pyment_create_serializer(serializers.ModelSerializer):

    Organisation_name=serializers.CharField(required=False)
    class Meta:
            model=Payment
            fields='__all__'


class Pyment_get_serializer(serializers.ModelSerializer):
    class Meta:
            model=Payment
            fields='__all__'


class Client_get_serializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'
class Client_Edit_serializer(serializers.ModelSerializer):

    class Meta:
        model=Client
        fields='__all__'
class Subscription_edit_serializer(serializers.ModelSerializer):
    #Package_name=Packages_get_serializer()
    #Payment_ID=Pyment_get_serializer()
    #Organisation_id=Organisation_get_serializer()
    #Subscription_start_date=serializers.CharField()
    Package_name=serializers.IntegerField()
    Organisation_id=serializers.CharField(required=False)
    Payment_ID=serializers.IntegerField()

    class Meta:
        model=Subscription
        fields='__all__'



#class get_total_task(serializers.ModelSerializer)










'''
class Subscription_edit_serializer(serializers.Serializer):
    #Subscription_start_date=serializers.CharField()
    Package_name=serializers.IntegerField()
    Organisation_id=serializers.IntegerField()
    Payment_ID=serializers.IntegerField()



    class Meta:
        model=Subscription
        fields=['Package_name','Organisation_id','Payment_ID']
        '''




'''
class Employee_otp_varifyserializers(serializers.ModelSerializer):
    Emter_your_Employee_code=serializers.CharField( allow_blank=False, write_only=True)
    def validate(self, data):
        try:
            print(data['Emter_your_Employee_code'])
            x=User.objects.get(username=data['Emter_your_Employee_code'])

        except:
            raise serializers.ValidationError("Id not found ")

        return data
    def create(self, validated_data):
        x=User.objects.get(username=validated_data['Emter_your_Employee_code'])
        p=str(x)
        y=p.split(':')
        y=y[0]
        otp=str(random.randint(111111,999999))
        x.last_name=otp
        x.save()
        y=Employee_data.objects.filter(Employee_Uniqe_id=y).update(Employee_otp=otp)
        try:
            #value = signing.dumps((x.username,))
            value=x.username
            send_mail('your OTP       '+otp, (base_url).strip()+'app/employeeotp_varify123/   '+value+'/', 'bitcoinora@gmail.com', [x.email])
        #value=x.username
        except:
            pass

        return 'Done '
    class Meta:
            model = User
            fields = ['Emter_your_Employee_code']

            '''

class get_task_all_serializer(serializers.Serializer):
    User_ID=serializers.IntegerField()
    #class Meta:
     #   model=Task


class Task_get_serializers(serializers.ModelSerializer):
    Name=serializers.SerializerMethodField(read_only=True)
    def get_Name(self,obj):
        first=''
        last=''

        x=obj.Task_assignment_to
        #print('x===============',x.id)
        p=Employee_data.objects.filter(which_user=x)
        for i in p:
            first=i.Employee_First_Name
            last=i.Employee_Last_Name

        #first=p.Employee_First_Name
        #last=p.Employee_Last_Name
        name=first+' '+last
        return name


    Task_assignment_to=UserSerializer()
    Task_Category_name=Category_serializer()
    Task_SubCategory_name=SubCategory_get_serializers()
    #Task_attchments=attachments_serializers(many=True)
    #Task_assignment_to=accounts_serializer_edit()
    #createdBy=UserSerializer()

    class Meta:
        model=Task
        fields = '__all__'

class bar_chart_serializer(serializers.Serializer):
    User_ID=serializers.IntegerField()
    Choices=serializers.CharField()

class xyzserializer(serializers.ModelSerializer):
    date =serializers.DateField(datetime.datetime.now(),required=False)

class Task_trackingserializer(serializers.ModelSerializer):
    Task_Status= serializers.CharField(required=False)
    class Meta:
        model=Task_tracking
        fields = '__all__'



class panding_amt_serializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields = '__all__'

class admin_id_serializers(serializers.Serializer):
    org_id=serializers.CharField(required=True)
    class Meta:
        model=Subscription
        fields = '__all__'

class update_password_serializer(serializers.Serializer):
    Token=serializers.CharField(required=True)
    uniqueid=serializers.CharField(required=True)
    password=serializers.CharField(style={'input_type': 'password'}, allow_blank=False, write_only=True)
    confirm_password=serializers.CharField(style={'input_type': 'password'}, allow_blank=False, write_only=True)
    def validate(self, data):
        try:
            token1=data['Token']
            #print('token==================',token1)
            #data.pop['Token']

            x=Token.objects.get(key=str(token1))
           # print('token==================',token1)
            orgu=User.objects.get(id=x.user_id)
            org=Organisations.objects.get(which_user=orgu.id)
        except:
            raise serializers.ValidationError("Token Not Valid")

        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        try:
            uid=data['uniqueid']
            y=Employee_data.objects.get(Employee_Uniqe_id=uid)
            #print('uid===========================',uid)
            #print('org===========================',org.id)
            #print('y.which_Organisations_id==========================',y.which_Organisations_id)
            if y.which_Organisations_id !=org.id:
                raise serializers.ValidationError("employee is not from current org line 854")
            else:
                pass


        except:
            raise serializers.ValidationError("employee is not from current org 860")
        return data
    def create(self, validated_data):
        token1=validated_data['Token']
        uid=validated_data['uniqueid']
        password=validated_data['password']
        #org1=validated_data['org']
        x=Token.objects.get(key=str(token1))
        orgu=User.objects.get(id=x.user_id)
        uid=uid+':'+'web'
        p=User.objects.get(username=uid)
        p.set_password(password)
        p.save()

        return validated_data
        #Organisationemls = [x.Organisations_email for x in Organisations.objects.all()]
        return data
    #def create(self, validated_data):



class ImageSerializer(serializers.ModelSerializer):
    Logo_Image = Base64ImageField(max_length=None, use_url=True,)
    # Base64ImageField(max_length=None, use_url=True,)

    class Meta:
        model = Organisations
        fields = ['Logo_Image']

class Imageuploademployee(serializers.ModelSerializer):
    Employee_image=Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model=Employee_data
        fields = ['Employee_image']


