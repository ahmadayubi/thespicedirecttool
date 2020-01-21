from django import forms


class UserForm(forms.Form):
    post = forms.IntegerField(max_value=99, min_value=0)
    # post = forms.IntegerField(widget=forms.TextInput(
    #   attrs={
    #        'class': 'form-control',
    #        'aria-describedby': 'basic-addon1 GFG_Button'
    #    }
    # ))
