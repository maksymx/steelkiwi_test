from django.forms import BooleanField, Form, RadioSelect

YES_OR_NO = (
    (True, 'Yes'),
    (False, 'No')
)
class YesNoForm(Form):
    choice = BooleanField(
        widget=RadioSelect(choices=YES_OR_NO),
        initial=False,
        required=False,
        label='Really delete?')