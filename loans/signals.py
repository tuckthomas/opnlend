from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Loan, CustomField, LoanCustomFieldValue

@receiver(post_save, sender=Loan)
def create_loan_custom_fields(sender, instance, created, **kwargs):
    if created:
        custom_fields = CustomField.objects.all()
        for custom_field in custom_fields:
            LoanCustomFieldValue.objects.create(loan=instance, custom_field=custom_field)

@receiver(post_save, sender=CustomField)
def create_custom_field_for_loans(sender, instance, created, **kwargs):
    if created:
        loans = Loan.objects.all()
        for loan in loans:
            LoanCustomFieldValue.objects.create(loan=loan, custom_field=instance)

@receiver(post_delete, sender=CustomField)
def delete_custom_field_values(sender, instance, **kwargs):
    LoanCustomFieldValue.objects.filter(custom_field=instance).delete()
