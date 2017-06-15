# -*- coding: utf-8 -*-

from django.forms.widgets import CheckboxInput, FileInput, RadioSelect


class BootstrapFormMixin(object):

    css_class = "form-control input-sm"
    exclude_widgets = (CheckboxInput, FileInput, RadioSelect)

    def __init__(self, *args, **kwargs):
        super(BootstrapFormMixin, self).__init__(*args, **kwargs)
        self.apply_css_class()

    def apply_css_class(self):
        for field in self.fields.keys():
            css_class = self.fields[field].widget.attrs.get('class', '')
            if not isinstance(self.fields[field].widget, self.exclude_widgets) and self.css_class not in css_class:
                css_class += ' %s' % self.css_class
                self.fields[field].widget.attrs.update({'class': css_class})
