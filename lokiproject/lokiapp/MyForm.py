from django import forms
 
# creating a form
class InputForm(forms.Form):   #  form class must be inherited from 'Form' class
                                # 'form' is a key to your class 'InputForm'
 
    pname = forms.CharField(max_length = 200)
    price = forms.FloatField()
    quantity=forms.FloatField()