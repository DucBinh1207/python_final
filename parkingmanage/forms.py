from turtle import color
from django import forms
from parkingmanage.models import ParkingLog, User, Vehicle, Manager


#############################  USER   ############################

class UserForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     users = User.objects.all()
    #     vehicles = Vehicle.objects.all()
    #     _delete = []

    #     for _user in users:
    #         _delete.append(_user.vehicle)
    #     vehicles.filter(licensePlate__in=_delete).delete()

    #     self.fields['vehicle'].queryset = vehicles   

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
        if not new_code.isnumeric():
            raise forms.ValidationError('The code should be digit only!')
        return new_code

#############################  VEHICLE   ############################


class VehicleForm(forms.ModelForm):

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


#############################  PARKING LOG   ############################


class LogForm(forms.ModelForm):

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
            'timeIn': forms.DateTimeInput(),
            'timeOut': forms.DateTimeInput(),
        }

    
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
        super(ManagerForm, self).__init__(*args, **kwargs)
        print(self.usertype)
        if self.usertype == 'Manager':
            self.fields['role'].choices = (
                ('Staff', 'Staff'),
            )
        elif self.usertype == 'Administrator':
            self.fields['role'].choices = (
                ('Manager', 'Manager'),
                ('Staff', 'Staff'),
            )

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Email không hợp lệ')
        return email

    