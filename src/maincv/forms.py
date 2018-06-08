from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label="Full Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone (optional)", required=False)
    message = forms.CharField(label = "Your message",
            widget=forms.Textarea(attrs={'rows':'8'})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@" not in email:
            raise forms.ValidationError("Please enter a valid email address.")
        return email