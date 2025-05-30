from django import forms
from .models import Transaccion, Categoria

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['tipo', 'categoria', 'monto', 'descripcion', 'fecha']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].required = False
        
        # Filtrar categorías según el tipo seleccionado
        if 'tipo' in self.data:
            tipo = self.data.get('tipo')
            self.fields['categoria'].queryset = Categoria.objects.filter(tipo=tipo)
        elif self.instance.pk:
            self.fields['categoria'].queryset = Categoria.objects.filter(tipo=self.instance.tipo)
        else:
            self.fields['categoria'].queryset = Categoria.objects.none()

class IngresoForm(TransaccionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].initial = 'ingreso'
        self.fields['tipo'].widget = forms.HiddenInput()
        self.fields['categoria'].queryset = Categoria.objects.filter(tipo='ingreso')

class GastoForm(TransaccionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].initial = 'gasto'
        self.fields['tipo'].widget = forms.HiddenInput()
        self.fields['categoria'].queryset = Categoria.objects.filter(tipo='gasto') 