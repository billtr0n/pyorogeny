# python imports
import json

# django imports
from django import forms
from django.forms import ModelForm

# user defines imports
from .models import Simulation, Simulation_Input, Simulation_Output, Parameters, Rupture_Parameters, OnePoint
from .models import Figure
class SimulationForm(ModelForm):
    class Meta:
        model = Simulation
        exclude = ['comments','upload_date']

class SimulationOutputForm(ModelForm):
    class Meta:
        model = Simulation_Output 
        exclude = ['simulation']

class SimulationInputForm(ModelForm):
    class Meta:
        model = Simulation_Input
        exclude = ['simulation']

class ParametersForm(ModelForm):
    class Meta:
        model = Parameters
        exclude = ['simulation']

    def __unicode__(self):
        return 'parameters model'

class RuptureParametersForm(ModelForm):
    class Meta:
        model = Rupture_Parameters
        exclude = ['simulation']

    def __unicode__(self):
        return 'rupture parameters model'

class OnePointForm(ModelForm):
    class Meta:
        model = OnePoint
        exclude = ['simulation']

    def __unicode__(self):
        return 'one point statistics'

class FigureForm(ModelForm):
    class Meta:
        model = Figure
        exclude = ['simulation']

    def __unicode__(self):
        return "figure product"

class ActivateFigureForm(ModelForm):
    class Meta:
        model = Figure
        fields = ('active',)

    def __unicode__(self):
        return 'activate/deactive figure form'




class UploadFileForm( forms.Form ):
    file = forms.FileField()

    # handle file parsing here.
    def clean_file(self):
        data = self.cleaned_data['file']
        files = self.parse_file(data)

        # form = SimulationModelForm(data=data_dict)
        # if form.is_valid():
        #     self.instance = form.save(commit=False)
        # else:
        #     raise forms.ValidationError(u'The file contains invalid data.')
        return data


    def save(self):
        instance = getattr(self, "instance", None)
        if instance:
            instance.save()
        return instance

    # custom for SORD parameters.json file
    def parse_file(self, data):
        # data_dict={}
        # columns = [val.name for val in Simulation._meta.get_fields()]
        # json_data = json.loads(''.join(data.readlines()))
        # for key, val in json_data.iteritems():
        #     if key in columns:
        #         data_dict[key]=val
        try:
            files = [item.strip() or None for item in data]
            self.cleaned_data['files'] = files
        except Exception as e:
            print "unable to read upload file. make sure there is one directory per line."
        return files
