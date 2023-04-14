# Generated by Django 4.1.8 on 2023-04-10 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('loans', '0002_remove_loan_id_loan_loan_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('loan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loans.loan')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]