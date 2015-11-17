# -*- coding: utf-8 -*-

"""
This module can serialize various django fields to json
with all the rules applied

    >>> from django.db.models import CharField
    >>> name = CharField(max_length=64, null=True)

    >>> FieldSerializer(name).to_dict()
    {
        "help_text": "30 characters or fewer. Letters, digits and @/./+/-/_ only.",
        attrs: {
            "maxlength": 64,
            "class": "vTextField",
        },
        "is_required": False,
    }
"""

class FieldSerializer(object):

    def __init__(self, field):
        self._field = field

    def to_dict(self):
        widget = self._field.widget
        return {
            "label": unicode(self._field.label),
            "is_required": self._field.required,
            "attrs": widget.attrs,
            "help_text": unicode(self._field.help_text),
        }

