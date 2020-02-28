from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core import signing
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from prodemoapp.serializer import Organisations_serializers,Employee_data_serializers,UserSerializer,Task_serializers,Category_serializer,SubCategory_serializer,Employee_edit_serializer,Employee_get_serializer,Employee_otp_varifyserializers,Employee_otp_loginserializer,SubCategory_get_serializers,Panding_Task_get_serializers,Organisations_passwords_serializer,New_passwordresetserializer,ChangePasswordSerializer_for_Organisations,Packages_get_serializer,Packages_create_serializer,Client_get_serializer,Client_Edit_serializer,Organisation_get_serializer,Subscription_get_serializer,Organisation_edit_serializer,Pyment_create_serializer,Pyment_get_serializer,Subscription_edit_serializer,accounts_serializer,accounts_serializer_edit,Task_get_serializers,get_task_all_serializer,bar_chart_serializer,xyzserializer,Task_trackingserializer,admin_id_serializers,update_password_serializer,ImageSerializer,Imageuploademployee,orgloginserializer,Imageuploademployee_admin


from rest_framework import viewsets

from prodemoapp.models import Organisations,Employee_data,Task,Category,SubCategory,Payment,Packages,Subscription,Client,Task_tracking
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from django.template.loader import render_to_string, get_template


from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view








class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    #pass

    def has_object_permission(self, request, view, obj):
        print('here')
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return obj.createdBy == request.user or obj.which_user==request.user
        print(obj.createdBy)
        print(request.user)

        return obj.createdBy == request.user or obj.which_user==request.user



class subscriptionpermissions(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        print('here')
        print('request.method',request.method)
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        org=request.user
        x=Organisations.objects.get(which_user=org)
        if request.method in permissions.SAFE_METHODS:
            print(obj.is_subscribe)
            print(request.user)
            return x.is_subscribe == True

        print(request.method)
        if request.method =='post' or request.method =='POST':
            print(obj.is_subscribe)
            print(request.user)

            return x.is_subscribe == True


        return x.is_subscribe == True
    def has_permission(self, request, view):
        return True
















class IsOwnerOrReadOnlyemp(permissions.BasePermission):
    pass
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        print('here')
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return obj.createdBy == request.user or obj.which_user==request.user
        print(obj.createdBy)
        print(request.user)

        return obj.createdBy == request.user or obj.which_user==request.user




class ChangePasswordView_Orgnations(viewsets.ViewSet):

    def create(self,request):
        serializer=ChangePasswordSerializer_for_Organisations(data=request.data)
        if serializer.is_valid():
            userid=serializer.data['which_user']
            old_password=serializer.data['old_password']
            new_password=serializer.data['new_password']
            try:
                x=User.objects.get(id=int(userid))
                #x.check_password('arpit764933')
            except:
                return Response({'User id not valid',}, status=status.HTTP_400_BAD_REQUEST)
            if x.check_password(old_password) == True:
                x.set_password(new_password)
                x.save()
                return Response({'Success': 'Password updated successfully',}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'Old Pasword is incorrect',}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








'''
class setpassword_forgotviewset_for_org(viewsets.ViewSet):
    #this view set will change the passwrd affter sendng OTP
    def create(self,request):
        email=request.data['Enter_Your_Email']
        otp=request.data['Enter_Your_OTP']
        new_password=request.data['Enter_new_password']
        conform_password=request.data['Confrom_password']
        serializer=New_passwordresetserializer(data=request.data)
        if serializer.is_valid():
            try:
                x=User.objects.get(username=email)
                y=Organisations.objects.get(which_user =x.id)
            except:
                return Response({'Email Not Valid',}, status=status.HTTP_400_BAD_REQUEST)
            if new_password != conform_password:
                return Response({'Password Dose Not Match',}, status=status.HTTP_400_BAD_REQUEST)
            else:
                pass
            if y.otp_forgot_password !=otp:
                return Response({'Invalid Otp',}, status=status.HTTP_400_BAD_REQUEST)
            else:
                x=User.objects.get(username=email)
                x.set_password(new_password)
                x.save()
                return Response({'Success': 'Successfully completed the  process',}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        p,e,o=None,0,0
        org=0
        org_logo=None
        which_Organisations=None
        IS_ACCOUNTENT=None
        flg=0
        try:
            usernm=request.data['username']
        except:
            return Response('Pls enter username ')
        try:
            request.data['password']
        except:
            return Response('Pls enter password ')


        def check_org():
            #org1=None
            password=0
            print('====================dfsll')

            try:
                print('usernm',usernm)
                user1=User.objects.get(username=usernm)
                print('212............',user1)
                password=request.data['password']

            except:
                return Response('invalid username ')

            if user1.check_password(password)==False:
                return Response('invalid password')
            else:
                pass
            try:
                org1=Organisations.objects.get(which_user=user1.id)
                if org1.is_email_verify==False:
                    return Response('first you have to verify your account by  the given link on email then you are abel to log in ')

            except:
                pass
            if org1.is_subscribe==False:
                return Response('Your subscription has been expired!')
            try:
                x = User.objects.get(username=request.data['username'],is_active=True)
            except:
                return Response('your account is suspended or inactive please contact admin')
            return 1
        #print('usernmusernmusernmusernmusernmusernm ',usernm)
        if usernm[0:4]=='FIRM':
            #print('=====================240',usernm)
            flg=check_org()
            if flg!=1:
                return flg
            else:
                pass
        else:
            pass

        #print('d32222222222',flg)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']













        try:
            token = Token.objects.get(user=user).delete()
        except:
            pass
        token, created = Token.objects.get_or_create(user=user)
        try:
            employee=Employee_data.objects.get(which_user=user.pk,)
            e=1
        except:
            try:
                org=Organisations.objects.get(which_user=user.id)
                o=1
            except:
                return Response("No such User ")
        super_user=user.is_superuser


        if super_user == True:
            return Response({
            'token': token.key,
            'user_name':user.username,
            'user_id': user.pk,
            'email': user.email,
            'type':user.is_superuser,
            'First Name':user.first_name,'Last_Name':user.last_name})
        else:
            if e==1:
                employee=Employee_data.objects.get(which_user=user.pk,)
                try:
                    org=Organisations.objects.get(id=employee.which_Organisations.id)
                    org_name=org.Organisations_name
                    org_logo=org.Logo_Image.url
                    p=employee.Employee_image.url
                    which_Organisations=employee.which_Organisations.id

                    IS_ACCOUNTENT=employee.IS_ACCOUNTENT
                    #
                except:
                    pass


                Emp_id=employee.id
                which_Organisations=employee.which_Organisations.id


                IS_ACCOUNTENT=employee.IS_ACCOUNTENT
                Fname=employee.Employee_First_Name
                Lname=employee.Employee_Last_Name
                print('org name ',org_name)
                print('org name ',org_logo)




            try:
                #x=employee.Employee_image

                #token, created = Token.objects.get_or_create(which_user=user)
                return Response({
            'token': token.key,
            'user_name':user.username,
            'user_id': user.pk,
            'email': user.email,'First_Name':Fname,'Last_Name':Lname,'pic':p,'emp_id':Emp_id,'org_id':which_Organisations,'IS_ACCOUNTENT':IS_ACCOUNTENT,'org_name':org_name,'logo':org_logo})

            except:
                pass
            if o==1:

                org=Organisations.objects.get(which_user=user.pk,)
                name=org.Organisations_name
                org_id=org.id
                try:

                    limg=org.Logo_Image.url
                    img_admin=org.Admin_img.url
                except:
                    limg=None
                    img_admin=None

                return Response({
            'token': token.key,
            'user_name':user.username,
            'user_id': user.pk,
            'email': user.email,'First_Name':org.Contact_pesion_First_name,'Last_Name':org.Contact_pesion_Last_name,'org_name':name,'org_id':org_id,'logo':limg,'pic':img_admin,'Active':org.is_active})
            else:
                    return Response({'Error':'user is not superuser ....... !!'}, status=status.HTTP_401_UNAUTHORIZED)

        #else:
        return Response({'Error':'user is not superuser ....... !!'}, status=status.HTTP_401_UNAUTHORIZED)


class new_password_forgot_password_viewset(viewsets.ViewSet):
    def post(self,request):
        serializer=Employee_otp_loginserializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class setpassword_forgotviewset_for_org(viewsets.ViewSet):
    #this view set will change the passwrd affter sendng OTP
    def create(self,request):
        print(request.data)
        #email=request.data['Enter_Your_Email']
        #otp=request.data['Enter_Your_OTP']
        #new_password=request.data['Enter_new_password']
        #conform_password=request.data['Confrom_password']
        serializer=New_passwordresetserializer(data=request.data)
        if serializer.is_valid():
            email=serializer.data['Enter_Your_Email']
            otp=serializer.data['Enter_Your_OTP']
            new_password=serializer.data['Enter_new_password']
            conform_password=serializer.data['Confrom_password']
            try:
                x=User.objects.filter(email=email)
                x=x[1]
                y=Organisations.objects.get(which_user=x.id)
            except:
                return Response({'Email Not Valid',}, status=status.HTTP_400_BAD_REQUEST)
            if new_password != conform_password:
                return Response({'Password Dose Not Match',}, status=status.HTTP_400_BAD_REQUEST)
            else:
                pass
            print('y.otp_forgot_password',y.otp_forgot_password)
            print('y.otp_forgot_password',otp)
            if y.otp_forgot_password !=otp:
                return Response({'Invalid Otp',}, status=status.HTTP_400_BAD_REQUEST)
            else:
                x=User.objects.filter(email=email)
                x=x[1]
                x.set_password(new_password)
                x.save()
                y.is_active=True
                y.is_email_verify=True
                y.save()
                return Response({'Success': 'Successfully completed the  process',}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SendConfirmUserMail(APIView):
    def get(self, request, *args, **kwargs):
        try:
            username = signing.loads(kwargs['hash'])[0]
            print('username ===============',username)
            x=username.split(':')
            print('username ===============228',x[0])
            usrorgid=x[0]
            l=['mob','web']
            for i in l:
                username=str(usrorgid+':'+i)

                user = get_object_or_404(User.objects.all(),username=username)
                user.is_active = True
                print('username ',username)
                emil=user.email



                user.save()
                x=User.objects.filter(email=emil)
            try:
                x=User.objects.get(username=username)
                y=Organisations.objects.get(which_user=x.id)
                y.is_email_verify=True
                y.is_active=True
                y.save()

            except:
                return Response({'Error':'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({
			    'Success': 'Successfully completed the registration process',
			}, status=status.HTTP_200_OK)
        except:
            return Response({'Error':'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)



class SendConfirmUserMailfor_otp_login(viewsets.ViewSet):
    global otp
    def create(self, request):
        #print(request.data)
        serializer=Employee_otp_loginserializer(data=request.data)
        #print(request.data)
        if serializer.is_valid():
            otp=request.data['Enter_your_otp']
            h=request.data['hash']

            eui=h.split(':')
            eui=eui[0]
            try:
                print('eui ===========',eui)
                Employee_data.objects.get(Employee_Uniqe_id=eui)
            except:
                h='FIRM-'+h


            #h=h.strip()
            #print(h)
            #print('len of hash ',len(h))

            #print(h)
            if h[0:4]!='FIRM':


                try:
                    name =h
                    #print(username)
                    p=str(name)
                    print('name =============================',name)
                    #print('try .............................',name)
                    y=p.split(':')
                    y=y[0]
                    print('try .............................',y)

                    qry=Employee_data.objects.get(Employee_Uniqe_id=y)

                    oottp=qry.Employee_otp
                    user = get_object_or_404(User.objects.all(),username=name)

                    otp=otp.strip()
                    print(otp)


                    if oottp==str(otp):
                        try:

                            token = Token.objects.get(user=user).delete()
                        except:
                            pass
                        token, created = Token.objects.get_or_create(user=user)
                        print('==================================================================== h =312 id ur',user.id,user)

                        qry.Employee_otp=None
                        WID=qry.which_user_id
                        qry.save()

                        print('================================')
                        return Response({
                        'token': token.key,
                        'user_id':WID,
                        'Emp_ID':qry.id,
                        'IS_ACCOUNTENT':qry.IS_ACCOUNTENT,
                        'org_id':qry.which_Organisations.id,



                }, status=status.HTTP_200_OK)
                    else:
                        return Response({'Error':'OTP is wrong'}, status=status.HTTP_400_BAD_REQUEST)

                except:
                    return Response({'Error':'Invalid Username'}, status=status.HTTP_400_BAD_REQUEST)

            else:

                try:
                    name =h
                    #print(username)
                    p=str(name)
                    print('name =============================',name)
                    #print('try .............................',name)
                    y=p.split(':')
                    y=y[0]
                    #print('try .............................',y)
                    #print(y)
                    print('otp.......................')

                    qry=Organisations.objects.get(org_uni_id=y)

                    oottp=qry.otp

                    user = get_object_or_404(User.objects.all(),username=name)

                    otp=otp.strip()
                    print(otp)


                    if oottp==str(otp):
                        try:

                            token = Token.objects.get(user=user).delete()
                        except:
                            pass
                        token, created = Token.objects.get_or_create(user=user)
                        print('==================================================================== h =312 id ur',user.id,user)

                        qry.otp=None
                        WID=qry.which_user_id
                        qry.save()

                        print('================================')
                        return Response({
                        'token': token.key,
                        'user_id':WID,
                        'org_id':qry.id,





                }, status=status.HTTP_200_OK)
                    else:
                        return Response({'Error':'OTP is wrong'}, status=status.HTTP_400_BAD_REQUEST)

                except:
                    return Response({'Error':'Invalid Username'}, status=status.HTTP_400_BAD_REQUEST)


        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
            global otp
    def list(self, request):
        serializer=Employee_otp_loginserializer(data=request.data)
        if serializer.is_valid():
            otp=request.data['Enter_your_otp']

            data_dict = {'status':'ok'}
            return Response(data_dict)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''




class AdminUserCreationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = Organisations_serializers(data=request.data)
        if serializer.is_valid():
            this_user = serializer.save()
            now = UserSerializer(this_user)
            #data_dict = {'status':'ok'}
            data_dict = now.data
            return Response(data_dict)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Organisation_get_serializerviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user=self.request.user
        user=user.username
        user=user.split(':')

        user=user[0]
        user=user+':web'
        user=User.objects.get(username=user)
        print('line 617 ============',user)
        queryset = Organisations.objects.all().filter(which_user=user.id)
        return queryset
    serializer_class = Organisation_get_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['which_user']

    http_method_names = ['get','head','option']

class Organisation_edit_serializerviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Organisations.objects.all()
    serializer_class = Organisation_edit_serializer
    http_method_names =  ['head','option','patch','put']






class forgot_password_Organisations(viewsets.ViewSet):
    def create(self,request):
        serializer = Organisations_passwords_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """


    def post(self, request, format=None):
        serializer = Organisations_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def xyz(request):
    send_mail('subject', 's', 'bitcoinora@gmail.com', ['arpitshrivastava654@gmail.com',])
    # send_mail('Subject here','Here is the message.','arpit.s@flitwebs.com',['arpit.s@flitwebs.com'],fail_silently=False,)
    return HttpResponse('<h1>hii</h1>')

class Employee_otp_loginviewset(viewsets.ViewSet):
    global otp
    def list(self, request):
        serializer=Employee_otp_loginserializer(data=request.data)
        if serializer.is_valid():
            otp=request.data['Enter_your_otp']

            data_dict = {'status':'ok'}
            return Response(data_dict)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeUserCreationViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def create(self, request):
        user=self.request.user
        user=user.username.split(':')
        user=user[0]+str(':web')
        usr=User.objects.get(username=user)



        #usr=request.user
        x=Organisations.objects.get(which_user=usr)
        if x.is_subscribe==False:
            return Response('you have not purchased any subscription or may be your subscription is expired')
        else:
            pass

        serializer = Employee_data_serializers(data=request.data,context={'request':request})
        #print('===========================',request.data)
        if serializer.is_valid():
            this_user = serializer.save()
            #now = UserSerializer(this_user)
            data_dict = {'status':'ok'}
            #data_dict = now.data
            return Response(data_dict)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        serializer = Employee_data_serializers(data=request.data)
        pass

class Packages_create_serializerviewset(viewsets.ModelViewSet):
   # print('cfvbgjhnjcdfvbghnjdcfvgbhjnkertfvbgynhjmkcfvbghnjkdfsssssssssssssssss')
    queryset = Packages.objects.all()
    serializer_class = Packages_create_serializer
    http_method_names = ['get','patch','put','post']
    '''def create(self,request):
        serializer=Packages_create_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        else:
            return Response("Error ")
            '''

class Employee_otp_varifyserializersviewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = Employee_otp_varifyserializers(data=request.data)

        if serializer.is_valid():
            emp_code=request.data['Employee_code']
            #print(emp_code)
            serializer.save()

             #xy=validated_data['Employee_code']
            eui=emp_code.split(':')
            eui=eui[0]
            try:
                print('eui ===========',eui)
                Employee_data.objects.get(Employee_Uniqe_id=eui)
            except:
                emp_code='FIRM-'+emp_code
                #print('hiiiiiiiiiiiiiii')
            #print('xy==',xy[0:4])
            if emp_code[0:4]!='FIRM':
                x=User.objects.get(username=emp_code)
                eui=x.username
                eui=eui.split(':')
                eui=eui[0]
                y=Employee_data.objects.get(Employee_Uniqe_id=eui)

                lnm=y.Employee_Last_Name
                fnm=y.Employee_First_Name
                if lnm==None:
                    lnm=''
                elif fnm==None:
                    fnm=''


                #try:
                 #
                #except:
                  #  fnm=' '
                print('680 =========',lnm)
                print('681 =========',fnm)


                name=fnm +' '+lnm
                z=Organisations.objects.get(id=y.which_Organisations_id)
                encp=y.Employee_mobile_number
                len(encp)
                mob=str()
                l=[]
                for i in range(len(encp)):
                    if i==0:
                        l.append(encp[i])
                    elif i==(len(encp)-1):
                        l.append(encp[i])
                    elif i==(len(encp)-2):
                        l.append(encp[i])
                    else:
                        l.append('x')
                for i in l:
                    mob=mob+str(i)
                    try:
                        img=str(y.Employee_image.url)
                    except:
                        img =None
                data_dict = {'ID':y.id,'Image':img,'Mobile_Number':mob,'Name':name,'Organisations_Name':z.Organisations_name,'Employee_code':y.Employee_Uniqe_id}
                return Response (data_dict)
            else:
                print('line no 724...........',emp_code)

                x=User.objects.get(username=emp_code)
                print('line no 724...........')
                eui=x.username
                eui=eui.split(':')
                eui=eui[0]
                y=Organisations.objects.get(org_uni_id=eui)

                lnm=y.Contact_pesion_First_name
                fnm=y.Contact_pesion_Last_name
                z=y.Organisations_name
                if lnm==None:
                    lnm=''
                elif fnm==None:
                    fnm=''

                name=fnm +' '+lnm
                #z=Organisations.objects.get(id=y.which_Organisations_id)
                encp=y.Organisation_mobile_number
                len(encp)
                mob=str()
                l=[]
                for i in range(len(encp)):
                    if i==0:
                        l.append(encp[i])
                    elif i==(len(encp)-1):
                        l.append(encp[i])
                    elif i==(len(encp)-2):
                        l.append(encp[i])
                    else:
                        l.append('x')
                for i in l:
                    mob=mob+str(i)
                    try:
                        img=str(y.Admin_img.url)
                    except:
                        img =None
                data_dict = {'ID':y.id,'Image':img,'Mobile_Number':mob,'Name':name,'Organisations_Name':z,'Employee_code':y.org_uni_id}
                return Response (data_dict)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Employee_edit_serializerViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Employee_data.objects.all()
    serializer_class = Employee_edit_serializer
    http_method_names = ['patch','put','option','head','delete']


class Employee_get_serializerViewset(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['createdBy','which_Organisations','Employee_Uniqe_id']
    def get_queryset(self):
        user=self.request.user
        user=user.username.split(':')
        user=user[0]+str(':web')
        print('===================714',user)
        usr=User.objects.get(username=user)
        un=usr.username
        print(un[0:4])
        if un[0:4]=='FIRM':
            queryset = Employee_data.objects.all().filter(createdBy=usr)

        else:
            x=Employee_data.objects.get(which_user=usr)
            print(x.which_Organisations)

            queryset = Employee_data.objects.all().filter(which_Organisations=x.which_Organisations)
            pass



        return queryset
    serializer_class = Employee_get_serializer
    http_method_names = ['get','head','option']







class Task_serializersViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,IsOwnerOrReadOnly)
    permission_classes = (IsAuthenticated,)

    queryset = Task.objects.all()
    serializer_class = Task_serializers

    http_method_names = ['get','patch','put','option','head','post','delete']

class Category_serializerviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        org=0
        user=self.request.user
        user=user.username.split(':')
        user=user[0]+str(':web')
        usr=User.objects.get(username=user)

        #print('user 666', us)
        #usr=User.objects.get()
        #usr=self.request.user
        print('user id ',usr.id)
        x=Organisations.objects.get(which_user=usr.id)
        if usr.username == x.which_user.username:
            #org=2
            queryset=Category.objects.all().filter(which_Organisations=usr.id)
            return queryset
        else:
            queryset=None
            return queryset

        #return queryset
    serializer_class = Category_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['which_Organisations']

    http_method_names = ['get','option','head']

'''class SubCategory_serializerviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset =  SubCategory.objects.all().filter(is_active=True)
    serializer_class = SubCategory_serializer
    http_method_names = ['patch','put','option','head','post','delete']
'''

class SubCategory_get_serializerviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    #queryset =  SubCategory.objects.all()
    serializer_class = SubCategory_get_serializers
    def get_queryset(self):
        org=0
        user=self.request.user
        user=user.username.split(':')
        user=user[0]+str(':web')
        x=User.objects.get(username=user)
        org=Organisations.objects.get(which_user=x.id)
        if org.is_subscribe ==False:
            return Response('you have not any purchased any subscription or may be your subscription is expired')
        else:
            pass
        if x.username ==org.which_user.username:
            queryset=SubCategory.objects.all()
            return queryset

        else:
            queryset=None
        return queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['Category__Category_name','Category__id']

    http_method_names = ['get','head','option']

class Task_get_serializersviewset(viewsets.ModelViewSet):
    #print('vcvsycvysvyasvcysvcasvcjsvjc')
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
#    filter_backends = [DjangoFilterBackend]
 #   filterset_fields=['Task_Status','Task_assignment_to','createdBy']
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user=self.request.user
        user=user.username
        user=user.split(':')
        user=user[0]
        user=user+':web'
        user=User.objects.get(username=user)
        print('user======826',user)
        resultquery = ((Q(Task_assignment_to=user.id) | Q(createdBy=user.id))|Q(which_manager=user.id))
        queryset=Task.objects.filter(resultquery)

        return queryset
    serializer_class= Task_get_serializers

    http_method_names = ['get','head','option']

class Panding_Task_get_serializersviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset=Task.objects.all()
    serializer_class = Panding_Task_get_serializers
    #print('====================================',serializer_class.data)
    http_method_names =  ['get','head','option']
#client viewsets
class Client_get_serializerviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = Client_get_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['createdBy']
    http_method_names =  ['get','head','option']
#createdBy

class Client_Edit_serializervieswset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = Client_Edit_serializer
    http_method_names =  ['get','post','head','option','patch','put']




'''
class UpdateUserMainInfoViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UpdateUserMainInfoSerializer
    http_method_names = ['get','patch','put']
    '''


class Packages_get_serializerviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Packages.objects.all()
    serializer_class = Packages_get_serializer
    http_method_names = ['get','put','head','option']





class Subscription_get_serializervewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user=self.request.user
        queryset = Subscription.objects.all().filter(createdBy=user.id)
        return queryset

    filter_backends = [DjangoFilterBackend]
    filterset_fields=['createdBy','Organisation_id','Subscription_End_date','Subscription_start_date']
    serializer_class = Subscription_get_serializer
    http_method_names = ['get']





class Subscription_edit_serializervewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    def create(self,request):
        usr=self.request.user
        org=Organisations.objects.get(which_user=usr.id)
        #Organisation_name=org.id
        serializer = Subscription_edit_serializer(data=request.data)

        if serializer.is_valid():
            oid=org.id
            print('=======================',oid)
            oidi=Organisations.objects.get(id=oid)

            xy=User.objects.filter(email=oidi.Organisations_email)
            Package_name=serializer.data['Package_name']
            pkgid=Packages.objects.get(id=Package_name)
            Payment_ID=serializer.data['Payment_ID']

            payment_dur=Packages.objects.get(id=Package_name)
            payment_dur=payment_dur.Package_Duration
            x=Organisations.objects.get(id=oid)
            '''for i in xy:
                print('===========================',i.username)
                i.is_active=True
                i.save()

            '''
            #emp_id=Employee_data.objects.get(Employee_email=x.Organisations_email)
            #emp_id=str(emp_id.Employee_Uniqe_id+':web')
            end_date=datetime.datetime.now()+timedelta(days=int(payment_dur))
            usr=User.objects.get(username=x.which_user)

            #dict={'Payment_ID':Payment_ID,'Organisation_ID':oid,'Package_name':Package_name,'Employee_id':emp_id,'Remaining_days':payment_dur,'end':end_date}
            Payment_ID1=Payment.objects.get(id=Payment_ID)

            Subscription.objects.create(Organisation_id=oidi,Package_name=pkgid,Payment_ID=Payment_ID1,Remaining_days=payment_dur,createdBy=usr,Subscription_End_date=end_date)
            x.is_subscribe=True
            x.save()

            #print('oid===========================================\n\n\n',oid)
            #serializer.save()
            return Response('done')
        else:
            return Response(serializer.errors)








'''
class Subscription_edit_serializervewset(viewsets.ModelViewSet):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    queryset = Subscription.objects.all()
    serializer_class = Subscription_edit_serializer

    http_method_names = ['get','put','post','patch']
    '''




    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    #
    #def get_queryset(self):
     #   print(self.request.Subscription_start_date)
      #  return self.request.user.accounts.all()
    #filterset_fields=['createdBy','Organisation_id','Subscription_End_date','Subscription_start_date']
    #
    #serializer_class = Subscription_get_serializer
    #http_method_names = ['get','put','post','patch']


class Pyment_create_serializerviewet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        usr=self.request.user
        org=Organisations.objects.get(which_user=usr.id)

        #longitude = self.request.query_params.get('Organisation_name')

        queryset = Payment.objects.all().filter(Organisation_name=org.id)
        #Organisation_name=org

        return queryset
    #serializer=Pyment_create_serializer
    serializer_class =Pyment_create_serializer
    http_method_names = ['get','patch','head','option']

class Pyment_create_serializerviewet2(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        serializer=Pyment_create_serializer(data=request.data)
        usr=self.request.user
        org=Organisations.objects.get(which_user=usr.id)
        Organisation_name=org.id

        if serializer.is_valid():
            #serializer.save()
            #serializer.data['Organisation_name']=org.id
            x=serializer.data

            Organisation_name=org
            createdBy=usr
            Response1=serializer.data['Response']

            Ordr_ID=serializer.data['Ordr_ID']
            Payment_Method=serializer.data['Payment_Method']
            Amount=serializer.data['Amount']
            is_active=serializer.data['is_active']
            package_name=serializer.data['package_name']
            pkg=Packages.objects.get(id=package_name)
            x=Payment.objects.create(Organisation_name=Organisation_name,Response=Response1,Ordr_ID=Ordr_ID,Payment_Method=Payment_Method,Amount=Amount,is_active=is_active,package_name=pkg,createdBy=createdBy)
            return Response({'id':x.id,'package_name':package_name})

        else:
            return Response('vchsvhdvc')




















class Pyment_get_serializerviewet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class =Pyment_get_serializer
    http_method_names = ['get','head','option']

class get_all_account(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def list(self,request):
        serializer=accounts_serializer(data=request.data)
        if serializer.is_valid():
            emali=serializer.data['Enter_emil']
            y=User.objects.filter(email=emali)
            l=[]
            for i in y:
                l.append(i.username)
            return Response(l)
        else:
            return Response(serializer.errors)

class accounts_serializer_edit_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = accounts_serializer_edit
    http_method_names = ['get','put','patch','head','option']






class get_task_allviewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def create(self,request):
        serializer=get_task_all_serializer(data=request.data)
        N,P,Com,I,CA,=0,0,0,0,0
        ttl=0
        flg=0


        if serializer.is_valid():
            id=serializer.data['User_ID']
            usernm=User.objects.get(id=id).username

            #print('id = =============================',id)
            if usernm[0:4]=='FIRM':
                flg=1
                #print('==================1075',usernm)
            else:
                pass
#            x=Employee_data.objects.get(which_user=id)
            print()

            if flg==1:
                tsk=Task.objects.filter(createdBy=id)
            else:
                tsk=Task.objects.filter(Task_assignment_to=id)
                #F=Task_assignment_to.id



            #tsk2=Task.objects.filter(Task_Created_at=datetime.datetime.now())

            for i in tsk:
                ttl=ttl+1
                if i.Task_Status=='New':
                    N=N+1
                elif i.Task_Status=='Pending':
                    P=P+1
                elif i.Task_Status=='In Progress':
                    I=I+1
                elif i.Task_Status=='Complete':
                    Com=Com+1
                elif i.Task_Status=='Cancel':
                    CA=CA+1
                else:
                    pass
            #dict={'Total':ttl,'New':N,'Pending':P,'in_progress':I,'Complete':Com,'Cancel':CA}
            dict={'total': ttl, 'complete': Com, 'new':N, 'pending': P, 'in_progress': I, 'cancel':CA}





            return Response(dict)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class bar_chart_serializerviewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def create(self,request):
        serializer=bar_chart_serializer(data=request.data)
        date=datetime.date.today()
        flg=0
        l=[]
        countl=[]
        weeklyd=set()
        tsk2=Task.objects.all()
        for i in tsk2:
            l.append(i.Task_Created_at.date())
        print(l)

            #Task.objects.filter(Task_Created_at__in=[],Task_Created_at__lte=).count()
        if serializer.is_valid():
            User_ID=serializer.data['User_ID']
            try:
                Task_Status=serializer.data['Task_Status']
            except:
                Task_Status='Pending'
            print('Task_Status',Task_Status)
            try:
                Task_Statusl=['Pending','New','In Progress','Complete','Cancel','Invoice Paid']
                if Task_Status not in Task_Statusl:
                    return Response('invalid Task Status')
                else:
                    pass
            except:
                pass

            x=User.objects.get(id=User_ID)
            p=x.username
            if p[0:4]=='FIRM':
                flg=11
            else:
                flg=1

            try:
                if flg==11:
                    x=1
                    l.clear()
                    x12=User.objects.get(id=User_ID)
                    org=Organisations.objects.get(which_user=x12)


                    lmn=Task.objects.filter(which_organisation=org.id)

                    for i in lmn:
                        if i.Task_Status==Task_Status:
                            l.append(i.Task_Created_at.date())
                        else:
                            pass
                    print('l================',l)
                else:
                    print('line =============12else ')
                    x=Employee_data.objects.get(which_user=User_ID)
                    x=1
                    l.clear()
                    lmn=Task.objects.filter(Task_assignment_to=User_ID)

                    for i in lmn:
                        if i.Task_Status==Task_Status:
                            l.append(i.Task_Created_at.date())
                        else:
                            pass

            except:

                return Response('you are not the employee ')

            Choices=serializer.data['Choices']
            if x==1:

                for i2 in l:
                    if Choices=='today':
                        if ((date-i2).days) ==0:
                            weeklyd.add(i2)
                            #today=today
                        else:
                            pass
                    if Choices=='weekly':
                        if((date-i2).days) <=7:
                            weeklyd.add(i2)
                    if Choices=='monthly':
                        if((date-i2).days) <=30:
                            weeklyd.add(i2)
                    if Choices=='yearly':
                        if((date-i2).days) <=365:
                            weeklyd.add(i2)

                    if Choices=='half yearly':
                        if((date-i2).days) <=180:
                            weeklyd.add(i2)
                for i in weeklyd:
                    countl.append(l.count(i))
                dict={'dates':weeklyd,'count':countl}
                return Response(dict)


            return Response('you are not Admin ')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





'''
class xyzserializerviewset(viewsets.ViewSet):
    def create(self,):
        pass
        '''

    #filter_backends = [DjangoFilterBackend]
    #filterset_fields=['createdBy','Organisation_id','Subscription_End_date','Subscription_start_date']



class Task_tracking_get_serializerviewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task_tracking.objects.all()
    serializer_class = Task_trackingserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['Task_id','Task_Status','createdBy']
    http_method_names = ['get','post']







class Task_trackingserializerviewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        serializer=Task_trackingserializer(data=request.data)
        if serializer.is_valid():

            return Response([serializer.data])
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def create(self,request):
        serializer=Task_trackingserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            d=serializer.data['date']
            c=serializer.data['Task_Comment']
            cd=serializer.data['create_date']
            cb=serializer.data['createdBy']

            x=serializer.data['Task_id']
            y=serializer.data['Task_Status']
            p=Task.objects.get(id=x)
            p.Task_Status=y

            p.save()


            x1=serializer.data['id']
            dict={'id':x1,'Task_Status':y,'date':d,'Task_Comment':c,'create_date':cd,'Task_id':x,'createdBy':cb}
            return Response(dict)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class panding_amt_serializerviewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def create(self,request):
        user=request.user
        try:
            org=Organisations.objects.get(which_user=user.id)
        except:
            org=Employee_data.objects.get(which_Organisations=user.id)
        print('user============1471..',user)
        x=Task.objects.filter(is_paid=False,which_organisation=org)
        s=set()
        b=0
        cut=0
        count=[]
        count1=[]
        name=[]
        amt=[]
        k=[]
        m=[]
        for i in x:
            s.add(i.Task_Client_name_id)
            count.append(i.Task_Client_name_id)

            #p=Client.objects.get(id=i.Task_Client_name_id)
            #name.append(p.Client_name)

            amt.append(i.Task_Amount)





            #Client.objects.filter(id=i.Task_Client_name_id)
        try:
            print('line no ......1459')
            s.remove(None)
            print('line no ......1461')
        except:
            pass

        for i in s:
            name.append(Client.objects.get(id=i).Client_name)
        for i in s:
            p=Task.objects.filter(Task_Client_name=i)
            for i2 in p:
                b=b+int(i2.Task_Amount)
            m.append(b)
            k.append(m)
            m=[]
            b=0
        for i in s:
            count1.append(count.count(i))






        dict={'ID':s,'Name':name,'Amount':k,'Count':count1}

        return Response(dict)







#(viewsets.ModelViewSet):



'''
$url = "http://flitsms.in/api/sendhttp.php?authkey=150365AXdLl3PJwG59b3d280&mobiles=".$mobile."&message=".$message."&sender=FLTEAM&route=4&country=0";
'''
   #     @simplexml_load_file($url);

class admin_id(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def create(self,request):
        serializer=admin_id_serializers(data=request.data)
        l=set()
        if serializer.is_valid():
            oid=serializer.data['org_id']
            x=Subscription.objects.filter()
            for i in x:
                l.add(i.Organisation_id_id)
            print('Organisation_id=============',l)
            try:
                if int(oid) in l:
                    y=Organisations.objects.get(id=oid)
                else:
                    return Response('No Subscription ')
            except:
                return Response('No Subscription ')
            emp=Employee_data.objects.get(which_Organisations=y)
            empuni=emp.Employee_Uniqe_id
            dict={'unique_id':empuni}


            return Response(dict)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class update_password_serializerviewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def create(self,request):
        serializer=update_password_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #token=serializer.data['Token']
            #username=serializer.data['uniqueid']
            #password1=serializer.data['password']
            #confirm_password1=serializer.data['confirm_password']



            return Response('Success')
        else:
            return Response(serializer.errors)




class Category_serializerpostviewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def create(self,request):
        serializer=Category_serializer(data=request.data)
        user=self.request.user
        user=user.username.split(':')
        user=user[0]+str(':web')
        x=User.objects.get(username=user)

        #x=self.request.user
        org=Organisations.objects.get(which_user=x.id)

        #print('x.username',x.username)
        #print('org.which_user',org.which_user)
        if org.is_subscribe ==False:
            return Response('you have not any purchased any subscription or may be your subscription is expired')
        else:
            pass


        if x.username ==org.which_user.username:
            if serializer.is_valid():
                name=serializer.data['Category_name']

                Category.objects.create(Category_name=name,which_Organisations=x)

                #serializer.save()
                return Response('done')
            else:
                return Response(serializer.errors)
        else:
            return Response('you are not Admin')
    def partial_update(self,request,pk=None):
        try:
            instance = Category.objects.get(id=pk)
            print('instance =============================',instance)
            serializer=Category_serializer(instance,data=request.data,partial=True)
        except:
            pass
        x=self.request.user
        org=Organisations.objects.get(which_user=x.id)



        if x.username ==instance.which_Organisations.username:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response('you are not authorized to access this Action ')






        #    serializer.save()




class SubCategory_serializerviewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def create(self,request):
        serializer=SubCategory_serializer(data=request.data)
        user=self.request.user
        user=user.username.split(':')
        user=user[0]+str(':web')
        x=User.objects.get(username=user)
        org=Organisations.objects.get(which_user=x.id)

        if org.is_subscribe ==False:
            return Response('you have not any purchased any subscription or may be your subscription is expired')
        else:
            pass

        if x.username ==org.which_user.username:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response('you are not Admin')
    def partial_update(self,request,pk=None):
        instance = SubCategory.objects.get(id=pk)
        serializer=SubCategory_serializer(instance,data=request.data,partial=True)
        x=self.request.user
        user=self.request.user
        user=user.username.split(':')
        user=user[0]+str(':web')
        x=User.objects.get(username=user)
        org=Organisations.objects.get(which_user=x.id)
        if x.username ==org.which_user.username:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response('you are not Admin')


class Category_get(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Category_serializer
    def get_queryset(self):
        org=0
        usr=self.request.user
        name=usr.username
        name=name.split(':')
        unique=name[0]
        try:
            x=Employee_data.objects.get(Employee_Uniqe_id=unique)
            org=x.which_Organisations_id
            p=Organisations.objects.get(id=org)
            u=User.objects.get(id=p.which_user_id)
            queryset=Category.objects.all().filter(is_active=True).filter(which_Organisations=u.id)
        except:
            queryset=None

        return queryset



    http_method_names = ['get','option','head']



class SubCategory_get_serializersviewsetemp(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        org=0
        usr=self.request.user
        name=usr.username
        name=name.split(':')
        unique=name[0]
        try:
            x=Employee_data.objects.get(Employee_Uniqe_id=unique)


            org=x.which_Organisations_id
            p=Organisations.objects.get(id=org)

            u=User.objects.get(id=p.which_user_id)


            queryset=SubCategory.objects.all().filter(is_active=True)
        except:
            queryset=None

        return queryset


    filter_backends = [DjangoFilterBackend]
    filterset_fields=['Category__Category_name','Category__id']
    #filterset_fields=['createdBy','Organisation_id','Subscription_End_date','Subscription_start_date']
    serializer_class = SubCategory_get_serializers
    http_method_names = ['get','option','head']



class uploadelogoimage(viewsets.ModelViewSet):
    queryset = Organisations.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['get','patch']



class ulpoademployeeimage(viewsets.ModelViewSet):
    queryset =Employee_data.objects.all()
    serializer_class = Imageuploademployee
    http_method_names = ['get','patch']

class uploadadminimg(viewsets.ModelViewSet):
    queryset = Organisations.objects.all()
    serializer_class = Imageuploademployee_admin
    http_method_names = ['get','patch']



class emaillogin(viewsets.ViewSet):
    def create(self, request):
        serializer=orgloginserializer(data=request.data)

        def org_check(user):
            try:
                xy=User.objects.get(username=user)
                org1=Organisations.objects.get(which_user=xy.id)
            except:
                return Response('error')
            if org1.is_email_verify==False:
                return Response('Please verify your Email address to go through the sent Email.')
            if x.is_active==False:
                return Response('Your account has been suspended! Please contact administrator')
            else:
                pass


            return 1



        if serializer.is_valid():
            email=serializer.data['email']
            password=serializer.data['password']
            try:
                x=User.objects.filter(email=email)

                x=x[1]
                print('x==============',x)

                #for i in x:
                 #   x=i
            except:
                return Response('This Email is not registered with us')
            if x.check_password(password)==False:

                return Response('Incorrect Password ')
            else:
                flg=org_check(user=x.username)
                if flg==1:
                    try:

                        token = Token.objects.get(user=x).delete()
                        print('delete==========')
                    except:
                        pass
                    token, created = Token.objects.get_or_create(user=x)
                else:
                    return flg
            frm=x.username
            print('frm========',frm[0:3])
            if frm[0:4]=='FIRM':

                org1=Organisations.objects.get(which_user=x.id)
                try:
                    logo=org1.Logo_Image.url
                except:
                    logo=None
                try:
                    pic=org1.Admin_img.url
                except:
                    pic=None


                return Response({
            'token': token.key,
            'user_name':x.username,
            'user_id': x.pk,

            'email': x.email,'First_Name':org1.Contact_pesion_First_name,'Last_Name':org1.Contact_pesion_Last_name,'org_name':org1.Organisations_name,'org_id':org1.id,'logo':logo,'pic':pic,'Active':org1.is_active})

            else:
                return Response('You are not Firm')
        else:
            return Response(serializer.errors)




'''
        if super_user == True:


















'''






            #if flg==1:



