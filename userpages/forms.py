from django import forms
from django.forms import ModelForm
from jobs.models import Choice,Job

class CategoryForm(ModelForm):
      class Meta:
            model = Choice
            fields =['category']

            labels={
                  'category':'',
            }

            widgets ={
                  'category':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add category name'})
            }


class JobForm(ModelForm):
      class Meta:
            model = Job
            fields =['title', 'category','location', 'company', 'body', 'publish', 'expire']

            labels={
                  'title':'','category':'', 'company':'', 'location':'', 'body':'', 'publish':'', 'expire':''
            }

            widgets ={
                  'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add title name'}),
                  'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add job location name'}),
                  'category':forms.Select(attrs={'class':'form-control', 'placeholder':'Add category name'}),
                  'company':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add company name'}),
                  'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add body information'}),
                  'publish':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Add publication','type':'date'}),
                  'expire':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Add expiration date','type':'date'})
            }


