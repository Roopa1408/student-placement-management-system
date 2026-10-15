

from django import forms
from .models import Student, Company, Placement


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "email",
            "phone",
            "course",
            "department",
            "year",
            "cgpa",
            "skills",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter student name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }),
            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter course",
            }),
            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter department",
            }),
            "year": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter graduation year",
            }),
            "cgpa": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter CGPA",
                "step": "0.01",
            }),
            "skills": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter skills separated by commas",
                "rows": 3,
            }),
        }

    def clean_cgpa(self):
        cgpa = self.cleaned_data.get("cgpa")

        if cgpa is not None and not (0 <= cgpa <= 10):
            raise forms.ValidationError(
                "CGPA must be between 0 and 10."
            )

        return cgpa


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "email",
            "phone",
            "location",
            "website",
            "job_role",
            "package",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter company name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter company email",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }),
            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter company location",
            }),
            "website": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com",
            }),
            "job_role": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter job role",
            }),
            "package": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter annual package",
                "step": "0.01",
            }),
        }


class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = [
            "student",
            "company",
            "job_role",
            "package",
            "status",
        ]

        widgets = {
            "student": forms.Select(attrs={
                "class": "form-select",
            }),
            "company": forms.Select(attrs={
                "class": "form-select",
            }),
            "job_role": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter job role",
            }),
            "package": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter package",
                "step": "0.01",
            }),
            "status": forms.Select(attrs={
                "class": "form-select",
            }),
        }
