from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        #Sales Roles
        ('LOAN_OFFICER', 'Loan Officer'),
        ('BUSINESS_DEVELOPMENT_OFFICER', 'Business Development Officer'),
        #Credit Administration Roles
        ('COMMERCIAL_CREDIT_ANALYST', 'Commercial Credit Analyst'),
        ('COMMERCIAL_UNDERWRITER', 'Commercial Underwriter'),
        ('COMMERCIAL_LOAN_ADMINISTRATOR', 'Commercial Loan Administrator'),
        ('COMMERCIAL_PORTFOLIO_MANAGER', 'Commercial Portfolio Manager'),
        #Loan Operations Roles
        ('LOAN_OPERATIONS_SPECIALIST', 'Loan Operations Specialist'),
        #Executive Roles
        ('CHIEF_CREDIT_OFFICER', 'Chief Credit Officer'),
        ('CHIEF_FINANCIAL_OFFICER', 'Chief Financial Officer'),
        ('CHIEF_EXECUTIVE_OFFICER', 'Chief Executive Officer'),
        ('CHIEF_LENDING_OFFICER', 'Chief Lending Officer'),
    ]

    user_type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES)
