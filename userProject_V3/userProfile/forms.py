from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password1', 'password2')

        

# edit user form
class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200,)
    class Meta:
        model = User
        fields  = ('username','first_name', 'last_name','email')

    def __init__(self, *arg, **kwrg):
        super(UserForm, self).__init__(*arg, **kwrg)
        self.fields["username"].widget.attrs.update({'class':'form-control','readonly':'readonly'})
        self.fields["first_name"].widget.attrs.update({'class':'form-control','placeholder':'Enter first name'})
        self.fields["last_name"].widget.attrs.update({'class':'form-control','placeholder':'Enter last name'})
        self.fields["email"].widget.attrs.update({'class':'form-control','placeholder':'Enter your email'})
        

        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image','role','nid_number','gender',)

    def __init__(self, *arg, **kwrg):
        super(UserProfileForm, self).__init__(*arg, **kwrg)
        self.fields["image"].widget.attrs.update({'class':'form-control',})
        self.fields["nid_number"].widget.attrs.update({'class':'form-control','placeholder':'Enter Your National ID','min':'0'})
        
        self.fields["role"].widget.attrs.update({'class':'form-control',})
        self.fields['role'].required = False
        self.fields["gender"].widget.attrs.update({'class':'form-control',})
        self.fields['gender'].required = False
        # self.fields['gender'].label = "Gender"
