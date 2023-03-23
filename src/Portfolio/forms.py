from django import forms


class EmailForm(forms.Form):
    email_from = forms.EmailField(required=True, error_messages={"required": "Veuillez saisir une adresse mail"})
    subject = forms.CharField(max_length=100, required=True, error_messages={"required": "Veuillez saisir un sujet"})
    # attachments = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea, required=True, error_messages={"required": "Veuillez saisir un message"})
