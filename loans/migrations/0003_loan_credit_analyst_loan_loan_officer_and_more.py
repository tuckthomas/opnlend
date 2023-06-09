# Generated by Django 4.1.8 on 2023-04-14 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('loans', '0002_remove_loan_id_loan_loan_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='credit_analyst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loans_credit_analyst', to='users.user'),
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_officer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loans_loan_officer', to='users.user'),
        ),
        migrations.AddField(
            model_name='loan',
            name='portfolio_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loans_portfolio_manager', to='users.user'),
        ),
        migrations.AddField(
            model_name='loan',
            name='underwriter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loans_underwriter', to='users.user'),
        ),
    ]
