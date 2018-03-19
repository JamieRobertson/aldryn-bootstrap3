# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.forms.widgets import RadioSelect, TextInput, Textarea

from . import constants
from .conf import settings


class Context(RadioSelect):
    template_name = 'admin/aldryn_bootstrap3/widgets/context.html'


class Size(RadioSelect):
    template_name = 'admin/aldryn_bootstrap3/widgets/size.html'


class LinkOrButton(RadioSelect):
    template_name = 'admin/aldryn_bootstrap3/widgets/link_or_button.html'


class Icon(TextInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super(Icon, self).render(name, value, attrs=attrs, **kwargs)
        if value is None:
            value = ''
        iconset = value.split('-')[0] if value and '-' in value else ''
        iconset_prefexes = [s[1] for s in settings.ALDRYN_BOOTSTRAP3_ICONSETS]
        if len(settings.ALDRYN_BOOTSTRAP3_ICONSETS) and iconset not in iconset_prefexes:
            # invalid iconset! maybe because the iconset was removed from
            # the project. set it to the first in the list.
            iconset = settings.ALDRYN_BOOTSTRAP3_ICONSETS[0][1]
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/icon.html',
            {
                'input_html': input_html,
                'value': value,
                'name': name,
                'iconset': iconset,
                'is_required': self.is_required,
                'iconsets': settings.ALDRYN_BOOTSTRAP3_ICONSETS,
            },
        )
        return rendered


class MiniTextarea(Textarea):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['cols'] = '120'
        attrs['rows'] = '1'
        super(MiniTextarea, self).__init__(attrs)


class Responsive(Textarea):
    def render(self, name, value, attrs=None):
        from django.template.loader import render_to_string
        widget_html = super(Responsive, self).render(name=name, value=value, attrs=attrs)

        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/responsive.html',
            {
                'widget_html': widget_html,
                'widget': self,
                'value': value,
                'name': name,
                'id': attrs.get('id', None),
                'attrs': attrs,
            },
        )
        return rendered


class ResponsivePrint(Textarea):
    def render(self, name, value, attrs=None):
        from django.template.loader import render_to_string
        widget_html = super(ResponsivePrint, self).render(
            name=name, value=value, attrs=attrs)

        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/responsive_print.html',
            {
                'widget_html': widget_html,
                'widget': self,
                'value': value,
                'name': name,
                'id': attrs.get('id', None),
                'attrs': attrs,
            },
        )
        return rendered
