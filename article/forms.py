from django import forms

class ArticleForm(forms.Form):
    title  = forms.CharField(label="Title",max_length=100)
    content = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    comment_text = forms.CharField(label = "Enter",max_length=10000)
    comment_article = forms.HiddenInput()

