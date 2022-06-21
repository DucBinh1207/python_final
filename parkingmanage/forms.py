from distutils.log import Log
from django import forms
from parkingmanage.models import ParkingLog, User, Vehicle


#############################  USER   ############################

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None : 
                self.isUpdate = True 
        else :
                self.isUpdate = False

    code = forms.CharField(
        label='code',
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
                'placeholder': 'Số điện thoại'
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
        elif Users.exists() and not self.isUpdate : 
            raise forms.ValidationError('The code already exist!')
        else :  
            if self.instance.code == new_code : 
                return new_code
            else :
                raise forms.ValidationError('The code already exist!')
    
    def clean_phone(self, *args, **kwargs):
        new_phone = self.cleaned_data.get('phone')
        Users = User.objects.filter(phone=new_phone)
        if not new_phone.isnumeric():
            raise forms.ValidationError('The phone number should be digit only!')
        elif Users.exists() and not self.isUpdate : 
            raise forms.ValidationError('The phone number already exist!')
        else :  
            if self.instance.phone == new_phone : 
                return new_phone
            else :
                raise forms.ValidationError('The email already exist!')

    def clean_email(self, *args, **kwargs):
        new_email = self.cleaned_data.get('email')
        Users = User.objects.filter(email=new_email)
        if Users.exists() and not self.isUpdate : 
            raise forms.ValidationError('The email already exist!')
        else :  
            if self.instance.email == new_email : 
                return new_email
            else :
                raise forms.ValidationError('The email already exist!')

            


#############################  VEHICLE   ############################


class VehicleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None : 
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
        if Vehicles.exists() and not self.isUpdate : 
            raise forms.ValidationError('The License Plate already exist!')
        else :  
            if self.instance.licensePlate == new_licensePlate : 
                return new_licensePlate
            else :
                raise forms.ValidationError('The License Plate already exist!')


#############################  PARKING LOG   ############################


class LogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None : 
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
        elif Logs.exists() and not self.isUpdate : 
            raise forms.ValidationError('The logId already exist!')
        else :  
            if self.instance.logId == new_logId : 
                return new_logId
            else :
                raise forms.ValidationError('The logId already exist!')

    