from django import forms


class LogInForm(forms.Form):
    username = forms.CharField(max_length=200, required=True, error_messages={"required": "Veuillez saisir un nom d'utilisateur"})
    password = forms.CharField(required=True, error_messages={"required": "Veuillez saisir un mot de passe"})
