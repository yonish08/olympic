from django import forms
from django.forms import fields, widgets
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from core.models import *


# about olympic form
class AboutFunOlympicForm(forms.ModelForm):
    class Meta:
        model = AboutFunOlympic
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter title',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter something about page',
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Enter address',
            }),
            'logo': forms.ClearableFileInput(attrs={
                'placeholder': 'Select logo',
            }),
            'fb_link': forms.TextInput(attrs={
                'placeholder': 'Enter facebook link',
            }),
            'instagram_link': forms.TextInput(attrs={
                'placeholder': 'Enter instagram link',
            }),
            'youtube_link': forms.TextInput(attrs={
                'placeholder': 'Enter youtube link',
            }),
        }


# New form
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title',
            }),
            'content': SummernoteWidget(attrs={
                'class': 'form-control',
				'summernote': {
					'class': 'w-100',
					'placeholder': 'News description',
					'height': '350px',
                    }
			}),
            'featured': forms.CheckboxInput(attrs={
                'class': 'form-control',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            })
        } 



# Country form
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'country': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select country',
            }),
        } 



# Standing form
class StandingForm(forms.ModelForm):
    class Meta:
        model = Standing
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title',
            }),
        } 



# Sport form
class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title',
            }),
            'display_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select image',
            })
        } 



# Player form
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'sport_category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select category',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select image',
            }),
            'standing': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select standing rank',
            }),
            'country': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select country',
            })
        } 



# Highlight form
class HighlightForm(forms.ModelForm):
    class Meta:
        model = Highlight
        fields = '__all__'
        widgets = {
            'sport_category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select category',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title',
            }),
            'description': SummernoteWidget(attrs={
                'class': 'form-control',
				'summernote': {
					'class': 'w-100',
					'placeholder': 'News description',
					'height': '350px',
                    }
			}),
            'video': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter video url',
            }),
            'country': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Select country',
            })
        }



# LiveMatch form
class LiveMatchForm(forms.ModelForm):
    class Meta:
        model = LiveMatch
        fields = '__all__'
        widgets = {
            'sport_category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select category',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title',
            }),
            'description': SummernoteWidget(attrs={
                'class': 'form-control',
				'summernote': {
					'class': 'w-100',
					'placeholder': 'News description',
					'height': '350px',
                    }
			}),
            'video_url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter video url',
            }),
            'venue_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter venue name',
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select country',
            })
        } 



# Fixture form
class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = '__all__'
        widgets = {
            'first_participant': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first participant name',
            }),
            'second_participant': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter second participant name',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
            }),
            'sport_category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select category',
            }),
            'venue_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter venue name',
            }),
        } 