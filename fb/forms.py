from django import forms
from .models import Ebook, Ebook_detail, Contactbook2, Dailyrecord, Announcement


class EbookCoverForm(forms.ModelForm):

    class Meta:
        model = Ebook
        fields = ('image',  'title',)


class EbookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EbookForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['multiple'] = True

    class Meta:
        model = Ebook_detail
        fields = ('image',)


class ContactbookForm(forms.ModelForm):

    class Meta:
        model = Contactbook2
        fields = ('title',  'imagecontact', 'content', 'honor')


class DailyrecordForm(forms.ModelForm):

    class Meta:
        model = Dailyrecord
        fields = ('title', 'content', 'image', 'topic', 'studentnum',
                  'attend', 'absence', 'event', 'introspective')


class AnnounceForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = ('title', 'content', 'file', 'datetime')
