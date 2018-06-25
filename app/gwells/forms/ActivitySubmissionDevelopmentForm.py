"""
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, Hidden, HTML, Field
from crispy_forms.bootstrap import FormActions, AppendedText, InlineRadios

from gwells.models import ActivitySubmission


class ActivitySubmissionDevelopmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Fieldset(
                'Well Development',
                Div(
                    Div('development_method', css_class='col-md-3'),
                    css_class='row',
                ),
                Div(
                    Div(AppendedText('development_hours', 'hrs'), css_class='col-md-3'),
                    css_class='row',
                ),
                Div(
                    Div('development_notes', css_class='col-md-6'),
                    css_class='row',
                ),
            )
        )
        super(ActivitySubmissionDevelopmentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ActivitySubmission
        fields = ['development_method', 'development_hours', 'development_notes']
