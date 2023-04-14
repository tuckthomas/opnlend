# Generated by Django 2.2.28 on 2023-04-09 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('relationships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_program', models.CharField(choices=[('CONSUMER', 'Consumer'), ('COMMERCIAL', 'Commercial'), ('SBA', 'SBA'), ('USDA', 'USDA')], max_length=10)),
                ('loan_type', models.CharField(choices=[('TERM', 'Term Loan'), ('REVOLVING', 'Revolving Lines of Credit'), ('NONREVOLVING', 'Non-Revolving Line of Credit'), ('CONSTRUCTION', 'Construction Loan'), ('MASTER', 'Master Line of Credit')], max_length=15)),
                ('loan_delivery_method', models.CharField(blank=True, choices=[('7A', '7(a)'), ('504', '504')], max_length=4, null=True)),
                ('jobs_created', models.PositiveIntegerField(blank=True, null=True)),
                ('jobs_retained', models.PositiveIntegerField(blank=True, null=True)),
                ('conversion_type', models.CharField(blank=True, choices=[('PERMANENT', 'Permanent Conversion'), ('DUE_UPON_MATURITY', 'Due Upon Maturity')], max_length=20, null=True)),
                ('borrower_type', models.CharField(choices=[('PRIMARY', 'Primary Borrower'), ('CO_BORROWER', 'Co-Borrower')], max_length=15)),
                ('guarantor_amount_type', models.CharField(choices=[('LIMITED', 'Limited Guarantor'), ('UNLIMITED', 'Unlimited')], max_length=10)),
                ('guarantor_security_type', models.CharField(choices=[('UNSECURED', 'Unsecured'), ('SECURED', 'Secured')], max_length=10)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('loan_purpose', models.CharField(max_length=255)),
                ('loan_term', models.PositiveIntegerField(verbose_name='Loan Term (months)')),
                ('loan_amortization', models.PositiveIntegerField(verbose_name='Loan Amortization (months)')),
                ('period_1_interest_rate_type', models.CharField(choices=[('VARIABLE', 'Variable'), ('FIXED', 'Fixed')], max_length=10)),
                ('period_1_interest_rate_applied', models.CharField(choices=[('FULL', 'Full'), ('GUARANTEED', 'Guaranteed'), ('UN_GUARANTEED', 'Un-Guaranteed')], max_length=15)),
                ('period_1_base_rate', models.CharField(choices=[('WSJ_PRIME', 'Wall Street Journal Prime'), ('SBA_PEG', 'SBA Peg Rate'), ('FIXED_RATE', 'Fixed Rate'), ('OTHER', 'Other')], max_length=15)),
                ('period_1_base_rate_other', models.CharField(blank=True, max_length=255, null=True)),
                ('period_1_interest_rate_spread', models.DecimalField(decimal_places=4, max_digits=7)),
                ('period_1_full_rate', models.DecimalField(decimal_places=4, max_digits=7)),
                ('period_2_interest_rate_type', models.CharField(blank=True, choices=[('VARIABLE', 'Variable'), ('FIXED', 'Fixed')], max_length=10, null=True)),
                ('period_2_interest_rate_applied', models.CharField(blank=True, choices=[('FULL', 'Full'), ('GUARANTEED', 'Guaranteed'), ('UN_GUARANTEED', 'Un-Guaranteed')], max_length=15, null=True)),
                ('period_2_base_rate', models.CharField(blank=True, choices=[('WSJ_PRIME', 'Wall Street Journal Prime'), ('SBA_PEG', 'SBA Peg Rate'), ('FIXED_RATE', 'Fixed Rate'), ('OTHER', 'Other')], max_length=15, null=True)),
                ('period_2_base_rate_other', models.CharField(blank=True, max_length=255, null=True)),
                ('period_2_interest_rate_spread', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('period_2_full_rate', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('interest_rate_repricing_frequency', models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('BI_WEEKLY', 'Bi-Weekly'), ('MONTHLY', 'Monthly'), ('QUARTERLY', 'Quarterly'), ('SEMI_ANNUALLY', 'Semi-Annually'), ('ANNUALLY', 'Annually'), ('CUSTOM', 'Custom')], max_length=15)),
                ('interest_rate_repricing_frequency_custom', models.CharField(blank=True, max_length=255, null=True)),
                ('first_interest_rate_adjustment_date', models.DateField()),
                ('repayment_frequency', models.CharField(choices=[('WEEKLY', 'Weekly'), ('BI_WEEKLY', 'Bi-Weekly'), ('MONTHLY', 'Monthly'), ('SEMI_MONTHLY', 'Semi-Monthly'), ('QUARTERLY', 'Quarterly'), ('SEMI_ANNUAL', 'Semi-Annual'), ('ANNUAL', 'Annual'), ('CUSTOM', 'Custom')], max_length=15)),
                ('repayment_frequency_custom', models.CharField(blank=True, max_length=255, null=True)),
                ('repayment_type', models.CharField(choices=[('INTEREST_ONLY', 'Interest Only'), ('PRINCIPAL_AND_INTEREST', 'Principal and Interest'), ('MODIFIED', 'Modified')], max_length=20)),
                ('repayment_type_modified', models.CharField(blank=True, max_length=255, null=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower_loans', to='relationships.Affiliate')),
                ('guarantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guarantor_loans', to='relationships.Affiliate')),
            ],
        ),
    ]