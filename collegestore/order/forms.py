
from django import forms

from credentials.models import Material
from order.models import Order
from a3h1collegestore.models import Course

class DateInput(forms.DateInput):
    input_type = 'date'


class RadioSelect(forms.RadioSelect):
    input_type = 'radio'

class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    input_type = 'checkbox'


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','DOB','age','gender','phone_number','mail_id','address','department','course','purpose','materials']
        materials = forms.ModelMultipleChoiceField(
            queryset=Material.objects.all(),
        )
        widgets = {
            'DOB': DateInput(),
            'gender': RadioSelect(),
            'materials':CheckboxSelectMultiple()
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')

