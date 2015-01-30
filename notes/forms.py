from django import forms

class UpdateNoteForm(forms.Form):
    guid = forms.IntegerField(widget=forms.HiddenInput)
    # guid = forms.HiddenInput()
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     num_words = len(message.split())
    #     if num_words < 4:
    #         raise forms.ValidationError("Not enough words!")
    #     return message