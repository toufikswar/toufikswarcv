from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label="Full Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", required=False)
    message = forms.CharField(label = "Say stuff here",
            widget=forms.Textarea(attrs={'row':'3'})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, email_provider = email.split("@")
        domain, extension = email_provider.split(".")
        if domain != "gmail":
            raise forms.ValidationError("You must enter a Gmail address")
        return email