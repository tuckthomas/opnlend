from django.db import models
from relationships.models import Affiliate

class Loan(models.Model):
    LOAN_PROGRAM_CHOICES = [
        ('CONSUMER', 'Consumer'),
        ('COMMERCIAL', 'Commercial'),
        ('SBA', 'SBA'),
        ('USDA', 'USDA')
    ]

    LOAN_TYPE_CHOICES = [
        ('TERM', 'Term Loan'),
        ('REVOLVING', 'Revolving Lines of Credit'),
        ('NONREVOLVING', 'Non-Revolving Line of Credit'),
        ('CONSTRUCTION', 'Construction Loan'),
        ('MASTER', 'Master Line of Credit')
    ]

    CONVERSION_CHOICES = [
        ('PERMANENT', 'Permanent Conversion'),
        ('DUE_UPON_MATURITY', 'Due Upon Maturity')
    ]

    PERIOD_1_INTEREST_RATE_TYPE_CHOICES = [
        ('VARIABLE', 'Variable'),
        ('FIXED', 'Fixed'),
    ]

    PERIOD_1_INTEREST_RATE_APPLIED_CHOICES = [
        ('FULL', 'Full'),
        ('GUARANTEED', 'Guaranteed'),
        ('UN_GUARANTEED', 'Un-Guaranteed'),
    ]

    PERIOD_1_BASE_RATE_CHOICES = [
        ('WSJ_PRIME', 'Wall Street Journal Prime'),
        ('SBA_PEG', 'SBA Peg Rate'),
        ('FIXED_RATE', 'Fixed Rate'),
        ('OTHER', 'Other'),
    ]

    PERIOD_2_INTEREST_RATE_TYPE_CHOICES = [
        ('VARIABLE', 'Variable'),
        ('FIXED', 'Fixed'),
    ]

    PERIOD_2_INTEREST_RATE_APPLIED_CHOICES = [
        ('FULL', 'Full'),
        ('GUARANTEED', 'Guaranteed'),
        ('UN_GUARANTEED', 'Un-Guaranteed'),
    ]

    PERIOD_2_BASE_RATE_CHOICES = [
        ('WSJ_PRIME', 'Wall Street Journal Prime'),
        ('SBA_PEG', 'SBA Peg Rate'),
        ('FIXED_RATE', 'Fixed Rate'),
        ('OTHER', 'Other'),
    ]

    REPRICING_FREQUENCY_CHOICES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('BI_WEEKLY', 'Bi-Weekly'),
        ('MONTHLY', 'Monthly'),
        ('QUARTERLY', 'Quarterly'),
        ('SEMI_ANNUALLY', 'Semi-Annually'),
        ('ANNUALLY', 'Annually'),
        ('CUSTOM', 'Custom'),
    ]

    REPAYMENT_FREQUENCY_CHOICES = [
        ('WEEKLY', 'Weekly'),
        ('BI_WEEKLY', 'Bi-Weekly'),
        ('MONTHLY', 'Monthly'),
        ('SEMI_MONTHLY', 'Semi-Monthly'),
        ('QUARTERLY', 'Quarterly'),
        ('SEMI_ANNUAL', 'Semi-Annual'),
        ('ANNUAL', 'Annual'),
        ('CUSTOM', 'Custom'),
    ]

    REPAYMENT_TYPE_CHOICES = [
        ('INTEREST_ONLY', 'Interest Only'),
        ('PRINCIPAL_AND_INTEREST', 'Principal and Interest'),
        ('MODIFIED', 'Modified'),
    ]

    loan_number = models.CharField(max_length=50, primary_key=True, default='')
    loan_program = models.CharField(max_length=10, choices=LOAN_PROGRAM_CHOICES)
    loan_type = models.CharField(max_length=15, choices=LOAN_TYPE_CHOICES)

    loan_delivery_method = models.CharField(max_length=4, choices=[('7A', '7(a)'), ('504', '504')], blank=True, null=True)
    jobs_created = models.PositiveIntegerField(blank=True, null=True)
    jobs_retained = models.PositiveIntegerField(blank=True, null=True)

    conversion_type = models.CharField(max_length=20, choices=CONVERSION_CHOICES, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.loan_program == 'SBA':
            if not self.loan_delivery_method:
                raise ValueError('Loan Delivery Method is required for SBA loans.')
            if self.jobs_created is None or self.jobs_retained is None:
                raise ValueError('Jobs Created and Jobs Retained are required for SBA loans.')
        else:
            self.loan_delivery_method = None
            self.jobs_created = None
            self.jobs_retained = None

        if self.loan_type in ['NONREVOLVING', 'CONSTRUCTION']:
            if not self.conversion_type:
                raise ValueError('Conversion Type is required for Non-Revolving Line of Credit and Construction Loan types.')
        else:
            self.conversion_type = None

        super().save(*args, **kwargs)

    borrower = models.ForeignKey(Affiliate, on_delete=models.CASCADE, related_name='borrower_loans')
    borrower_type = models.CharField(
        max_length=15,
        choices=[
            ('PRIMARY', 'Primary Borrower'),
            ('CO_BORROWER', 'Co-Borrower'),
        ]
    )
    guarantor = models.ForeignKey(Affiliate, on_delete=models.CASCADE, related_name='guarantor_loans')
    guarantor_amount_type = models.CharField(
        max_length=10,
        choices=[
            ('LIMITED', 'Limited Guarantor'),
            ('UNLIMITED', 'Unlimited'),
        ]
    )
    guarantor_security_type = models.CharField(
        max_length=10,
        choices=[
            ('UNSECURED', 'Unsecured'),
            ('SECURED', 'Secured'),
        ]
    )

    loan_amount = models.DecimalField(max_digits=15, decimal_places=2)
    loan_purpose = models.CharField(max_length=255)
    loan_term = models.PositiveIntegerField(verbose_name="Loan Term (months)")
    loan_amortization = models.PositiveIntegerField(verbose_name="Loan Amortization (months)")

    period_1_interest_rate_type = models.CharField(max_length=10, choices=PERIOD_1_INTEREST_RATE_TYPE_CHOICES)
    period_1_interest_rate_applied = models.CharField(max_length=15, choices=PERIOD_1_INTEREST_RATE_APPLIED_CHOICES)
    period_1_base_rate = models.CharField(max_length=15, choices=PERIOD_1_BASE_RATE_CHOICES)
    period_1_base_rate_other = models.CharField(max_length=255, blank=True, null=True)
    period_1_interest_rate_spread = models.DecimalField(max_digits=7, decimal_places=4)
    period_1_full_rate = models.DecimalField(max_digits=7, decimal_places=4)

    period_2_interest_rate_type = models.CharField(max_length=10, choices=PERIOD_2_INTEREST_RATE_TYPE_CHOICES, blank=True, null=True)
    period_2_interest_rate_applied = models.CharField(max_length=15, choices=PERIOD_2_INTEREST_RATE_APPLIED_CHOICES, blank=True, null=True)
    period_2_base_rate = models.CharField(max_length=15, choices=PERIOD_2_BASE_RATE_CHOICES, blank=True, null=True)
    period_2_base_rate_other = models.CharField(max_length=255, blank=True, null=True)
    period_2_interest_rate_spread = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    period_2_full_rate = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)

    interest_rate_repricing_frequency = models.CharField(max_length=15, choices=REPRICING_FREQUENCY_CHOICES)
    interest_rate_repricing_frequency_custom = models.CharField(max_length=255, blank=True, null=True)
    first_interest_rate_adjustment_date = models.DateField()

    repayment_frequency = models.CharField(max_length=15, choices=REPAYMENT_FREQUENCY_CHOICES)
    repayment_frequency_custom = models.CharField(max_length=255, blank=True, null=True)
    repayment_type = models.CharField(max_length=22, choices=REPAYMENT_TYPE_CHOICES)
    repayment_type_modified = models.CharField(max_length=255, blank=True, null=True)

