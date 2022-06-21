from distutils.log import Log
from turtle import color
from django import forms
from parkingmanage.models import ParkingLog, User, Vehicle, Manager


#############################  USER   ############################

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.inst = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if self.inst is not None : 
            self.isUpdate = True 
        else :
            self.isUpdate = False

    code = forms.CharField(
        label='Code',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'code'
            }
        )
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tên người gửi xe'
            }
        )
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Số điện thoại',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'example : abc123@gmail.com'
            }
        )
    )
    address = forms.CharField(
        initial='Viet Nam',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5',
                'cols': '10'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'code',
            'name',
            'phone',
            'email',
            'address',
            ] 

    def clean_code(self, *args, **kwargs):
        new_code = self.cleaned_data.get('code')
        Users = User.objects.filter(code=new_code)
        if not new_code.isnumeric():
            raise forms.ValidationError('The code should be digit only!')
        elif not self.isUpdate : # Create
            if Users.exists() : 
                raise forms.ValidationError('The code already exist!')
            else :
                return new_code
        else :  # Update
            if self.instance.code == new_code : 
                return new_code
            elif Users.exists() :
                raise forms.ValidationError('The code already exist!')
            else : 
                return new_code

    def clean_phone(self, *args, **kwargs):
        new_phone = self.cleaned_data.get('phone')
        Users = User.objects.filter(phone=new_phone)
        if not new_phone.isnumeric():
            raise forms.ValidationError('The phone number should be digit only!')
        elif not self.isUpdate : # Create
            if Users.exists() : 
                raise forms.ValidationError('The phone number already exist!')
            else :
                return new_phone
        else :  # Update
            if self.instance.phone == new_phone : 
                return new_phone
            elif Users.exists() :
                raise forms.ValidationError('The phone number already exist!')
            else : 
                return new_phone

    def clean_email(self, *args, **kwargs):
        new_email = self.cleaned_data.get('email')
        Users = User.objects.filter(email=new_email)
        if not self.isUpdate : # Create
            if Users.exists() :
                raise forms.ValidationError('The email already exist!')
            else :
                return new_email
        else :  # Update
            if self.instance.email == new_email : 
                return new_email
            elif Users.exists() :
                raise forms.ValidationError('The email already exist!')
            else :
                return new_email

            


#############################  VEHICLE   ############################


class VehicleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.inst = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if self.inst is not None : 
            self.isUpdate = True 
        else :
            self.isUpdate = False

    licensePlate = forms.CharField(
        label='License Plate',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Biển số xe'
            }
        )
    )
    color = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Màu xe'
            }
        )
    )
    type = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Loại xe'
            }
        )
    )
    brand = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Thương hiệu xe'
            }
        )
    )

    class Meta:
        model = Vehicle
        fields = [
            'licensePlate',
            'color',
            'type',
            'brand',
            'user'
            ] 
    
    def clean_licensePlate(self, *args, **kwargs):
        new_licensePlate = self.cleaned_data.get('licensePlate')
        Vehicles = Vehicle.objects.filter(licensePlate=new_licensePlate)
        if not self.isUpdate : # Create
            if Vehicles.exists() : # Biển số xe đã tồn tại
                raise forms.ValidationError('The License Plate already exist! Create')
            else : # Biển số xe chưa tồn tại
                return new_licensePlate
        else :  # Update
            if self.instance.licensePlate == new_licensePlate : # Không đổi biển sỗ xe
                return new_licensePlate
            elif Vehicles.exists() : # Đổi biển số xe trùng với biển số xe tồn tài
                raise forms.ValidationError('The License Plate already exist! Update')
            else : # Đổi biển số xe trùng với biển số xe tồn tài
                return new_licensePlate

#############################  PARKING LOG   ############################


class LogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.inst = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if self.inst is not None : 
            self.isUpdate = True 
        else :
            self.isUpdate = False

    logId = forms.CharField(
        label='Log ID',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mã Log'
            }
        )
    )



    class Meta:
        model = ParkingLog
        fields = [
            'logId',
            'timeIn',
            'timeOut',
            'vehicle'
            ]  
        widgets = {
            'timeIn': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH-MM-SS','size': '25'}),
            'timeOut': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH-MM-SS','size': '25'}),
        }

    def clean_logId(self, *args, **kwargs):
        new_logId = self.cleaned_data.get('logId')
        Logs = Log.objects.filter(logId=new_logId)
        if not new_logId.isnumeric():
            raise forms.ValidationError('The logId should be digit only!')
        elif not self.isUpdate : # Create
            if Logs.exists() : 
                raise forms.ValidationError('The logId already exist!')
            else :
                return new_logId
        else :  # Update
            if self.instance.logId == new_logId : 
                return new_logId
            elif Logs.exists() :
                raise forms.ValidationError('The logId already exist!')
            else : 
                return new_logId
#############################  Manager  ############################

class ManagerForm(forms.ModelForm):

    code = forms.CharField(
        label='Mã nhân viên',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mã nhân viên'
            }
        )
    )

    role = forms.ChoiceField(
        label='Quyền hạn',
        required=True,
        
    )

    username = forms.CharField(
        label='Tên tài khoản',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tên tài khoản'
            }
        )
    )

    password = forms.CharField(
        label='Mật khẩu',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mật khẩu'
            }
        )
    )

    name = forms.CharField(
        label='Tên nhân viên',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tên nhân viên'
            }
        )
    )

    address = forms.CharField(
        label='Địa chỉ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Địa chỉ'
            }
        )
    )

    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Số điện thoại'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )

    class Meta:
        model = Manager
        fields = [
            'code',
            'username',
            'password',
            'role',
            'name',
            'address',
            'phone',
            'email',
            ] 

    def __init__(self, *args, **kwargs):
        self.usertype = kwargs.pop('role', None)
        self.inst = kwargs.pop('instance', None)
        super(ManagerForm, self).__init__(*args, **kwargs)
        if self.usertype == 'Manager':
            self.fields['role'].choices = (
                ('Staff', 'Staff'),
            )
        elif self.usertype == 'Administrator':
            self.fields['role'].choices = (
                ('Manager', 'Manager'),
                ('Staff', 'Staff'),
            )
        if self.inst is not None:
            self.isUpdate = True
            self.fields['code'].widget.attrs['readonly'] = True
        else:
            self.isUpdate = False
            print("Create")
            self.fields['code'].widget.attrs['readonly'] = False

    def clean_code(self):
        code = self.cleaned_data.get('code')
        manager = Manager.objects.filter(code=code)
        if not self.isUpdate : # Create
            if manager.exists() : 
                raise forms.ValidationError('The code already exist!')
            else :
                return code
        else :  # Update
            if self.instance.code == code : 
                return code
            elif manager.exists() :
                raise forms.ValidationError('The code already exist!')
            else : 
                return code

    def clean_username(self):
        username = self.cleaned_data.get('username')
        manager = Manager.objects.filter(username=username)
        if not self.isUpdate : # Create
            if manager.exists() : 
                raise forms.ValidationError('The username already exist!')
            else :
                return username
        else :  # Update
            if self.instance.username == username : 
                return username
            elif manager.exists() :
                raise forms.ValidationError('The username already exist!')
            else : 
                return username
        

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        manager = Manager.objects.filter(phone=phone)
        if not self.isUpdate : # Create
            if manager.exists() : 
                raise forms.ValidationError('The phone already exist!')
            else :
                return phone
        else :  # Update
            if self.instance.phone == phone : 
                return phone
            elif manager.exists() :
                raise forms.ValidationError('The phone already exist!')
            else : 
                return phone

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Email không hợp lệ')
        return email

    