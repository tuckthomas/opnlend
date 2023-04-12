from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('LOAN_OFFICER', 'Loan Officer'),
        ('CREDIT_ANALYST', 'Credit Analyst'),
        ('UNDERWRITER', 'Underwriter'),
        ('PORTFOLIO_MANAGER', 'Portfolio Manager'),
        ('CHIEF_CREDIT_OFFICER', 'Chief Credit Officer'),
        ('BUSINESS_DEVELOPMENT_OFFICER', 'Business Development Officer'),
        ('LOAN_OPERATIONS_SPECIALIST', 'Loan Operations Specialist'),
        ('CHIEF_FINANCIAL_OFFICER', 'Chief Financial Officer'),
        ('CHIEF_EXECUTIVE_OFFICER', 'Chief Executive Officer'),
        ('LOAN_ADMINISTRATOR', 'Loan Administrator'),
    ]

    user_type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES)
