from django import forms

class MovieSearchForm(forms.Form):
    imdb_rating = forms.DecimalField(min_value=0.1, max_value=9.9,
                                     required=True, label='Minimum IMDB Rating')
    release_year = forms.IntegerField(required=True)
