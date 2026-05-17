from django import forms
from app.models import AnomalyDetection

class AnomalyDetectForm(forms.ModelForm):

    class Meta:
        model = AnomalyDetection
        fields = ['video']

    
    # For beautification of form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['video'].widget.attrs.update({'class':'form-control'})