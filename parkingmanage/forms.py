from django import forms
from parkingmanage.models import User, Vehicle


class UserForm(forms.ModelForm):
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
                'placeholder': 'Tên nguời gửi xe'
            }
        )
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Số điện thoại nguời gửi xe'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
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
            'vehicle',] 
    def clean_code(self, *args, **kwargs):
        new_code = self.cleaned_data.get('code')
        if not new_code.isnumeric():
            raise forms.ValidationError('The code should be digit only!')
        return new_code


# class VehicleForm(forms.ModelForm):
#     code = forms.CharField(
#         label='code',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'code'
#             }
#         )
#     )
#     name = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Tên vật dụng'
#             }
#         )
#     )
#     origin = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Nơi xuất xứ'
#             }
#         )
#     )
#     status = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Tình trạng'
#             }
#         )
#     )
#     amount = forms.IntegerField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Số lượng'
#             }
#         )
#     )
#     class Meta:
#         model = Vehicle
#         fields = [
#             'code',
#             'name',
#             'origin',
#             'status',
#             'amount',
#             'catogery',] 
#     def clean_code(self, *args, **kwargs):
#         new_code = self.cleaned_data.get('code')
#         if not new_code.isnumeric():
#             raise forms.ValidationError('The code should be digit only!')
#         return new_code