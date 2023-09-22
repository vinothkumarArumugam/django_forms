from django import forms   ----# you have to create on own (forms.py file) 
                                # this is collecting information from the user,like name,age,email,numbers,my project mainly depend on this
class Employee(forms.Form):
    name=forms.CharField(max_length=100)  ---# these are the form fields not model fields in database ,you have to create db fields in models.py file
    age=forms.IntegerField()
    salary=forms.IntegerField()
