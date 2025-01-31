from django import forms

class RegistroUsuariosForm(forms.Form):
    nombre_usuario=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    email=forms.EmailField( widget=forms.EmailInput(attrs={'autocomplete': 'off'}))
    contrasena=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    contrasena_confirmar=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))

    def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data.get('nombre_usuario')
        if len(nombre_usuario) < 3:
            raise forms.ValidationError("El nombre de usuario debe tener al menos 3 caracteres")
        return nombre_usuario.strip()  # Se devuelve sin espacios extra

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email == "existe@gmail.com":
            raise forms.ValidationError("Este correo ya existe")
        return email
    
    def clean_contrasena(self):
        contrasena=self.cleaned_data.get('contrasena')
        if len(contrasena)<8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres")
        return contrasena
        
    def clean_contrasena_confirmar(self):
        contrasena=self.cleaned_data.get('contrasena')
        contrasena_confirmar=self.cleaned_data.get('contrasena_confirmar')

        if contrasena != contrasena_confirmar:
            raise forms.ValidationError("Las contraseñas no son iguales")
        return contrasena_confirmar