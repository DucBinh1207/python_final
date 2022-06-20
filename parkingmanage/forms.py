from django import forms
from parkingmanage.models import ParkingLog, User, Vehicle


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

    