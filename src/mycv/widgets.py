from django import forms

class HtmlEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(HtmlEditor, self).__init__(*args, **kwargs)
        self.attrs['class'] = 'html-editor'

    class Media:
        css = {
            'all': (
                '/static/vendor/codemirror-5.37.0/lib/codemirror.css',
            )
        }
        js = (
            '/static/vendor/codemirror-5.37.0/lib/codemirror.js',
            '/static/vendor/codemirror-5.37.0/init.js',
        )
        
        