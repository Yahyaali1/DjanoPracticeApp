from django import forms


class Feedback(forms.Form):
    name = forms.CharField(label="name", max_length=255, strip=True)
    feedback = forms.CharField(label="feedback", max_length=500, strip=True)
