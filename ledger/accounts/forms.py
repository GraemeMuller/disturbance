from django import forms

from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ValidationError

from .models import Address, Profile, EmailUser


class FirstTimeForm(forms.Form):
    redirect_url = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField(input_formats=['%d/%m/%Y'])


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['line1', 'line2', 'line3', 'locality', 'state', 'country', 'postcode']
        widgets = {'country': CountrySelectWidget()}


class ProfileForm(forms.ModelForm):
    #auth_identity = forms.BooleanField(required=False)
    class Meta:
        model = Profile
        fields = ['name', 'email', 'institution']

    def clean(self): 
        super(ProfileForm,self).clean();
        #always create a email identity for profile email
        self.cleaned_data["auth_identity"] = True

    def clean_auth_identity(self):
        if not self.cleaned_data.get("auth_identity",False):
            if self.instance.user and self.instance.user.email == self.cleaned_data["email"]:
                #the profile's email is the same as the user account email, it must be an email identity;
                return True;
        return self.cleaned_data.get("auth_identity")

    def __init__(self, *args, **kwargs):
        initial_display_name = kwargs.pop('initial_display_name', None)
        initial_email = kwargs.pop('initial_email', None)

        super(ProfileForm, self).__init__(*args, **kwargs)

        """
        instance = kwargs.get("instance")
        if instance and instance.pk:
            self.fields['auth_identity'].initial = kwargs["instance"].auth_identity
            if instance.user and instance.user.email == instance.email:
                #the profile's email is the same as the user account email, it must be an email identity;
                self.fields['auth_identity'].widget.attrs['disabled'] = True
        """

        if initial_display_name is not None:
            self.fields['name'].initial = initial_display_name

        if initial_email is not None:
            self.fields['email'].initial = initial_email