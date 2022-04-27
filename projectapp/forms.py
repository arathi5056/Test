from django import forms
import numpy as np 

import pandas as pd 

df = pd.read_csv('https://github.com/arathi5056/datasets/blob/master/owid-covid-data.csv?raw=true')
lt=df.columns.values
lt=lt[4:]

d1=zip(lt,lt)
csvc=dict(d1)
d1=dict(enumerate(lt))

GEEKS_CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

CHOICES=[('select1','select 1'),
         ('select2','select 2')]
# creating a form
class InputForm(forms.Form):
 
    Usercsv = forms.FileField (label='Select a file')
    xvalue_csv = forms.CharField(max_length = 200)
    yvalue_csv = forms.CharField(max_length = 200)
    #roll_number = forms.IntegerField(
     #                help_text = "Enter 6 digit roll number"
      #               )
    #password = forms.CharField(widget = forms.PasswordInput())
    

class MyForm(forms.Form):
  
  #radio = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  #Usercsv = forms.FileField (label='Select a file')
  geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)
  xcsv = forms.ChoiceField(choices=[(x, x) for x in lt])
  ycsv = forms.ChoiceField(choices=[(x, x) for x in lt])
  #name = forms.CharField(label='Enter your name', max_length=100)
  #email = forms.EmailField(label='Enter your email', max_length=100)
  #feedback = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))
  