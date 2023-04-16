from django.db import models
from users.models import Users
from relationships.models import Business
from django.core.validators import MinValueValidator
from datetime import timedelta

class IncomeStatement(models.Model):
    # Financial statement quality choices that are to be chosen from a drop-down menu.
    FINANCIAL_STATEMENT_QUALITY_CHOICES = [
        ('PR', 'Projections'),
        ('CP', 'Company Prepared'),
        ('TR', 'Tax Returns'),
        ('CRQ', 'CPA Reviewed - Qualified'),
        ('CRU', 'CPA Reviewed - Unqualified'),
        ('CAQ', 'CPA Audited - Qualified'),
        ('CAU', 'CPA Audited - Unqualified'),
        ('OTH', 'Other'),
    ]

    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    # Establishes relevant information for a given financial period that is to be spread.
    business = models.ForeignKey(Business, on_delete=models.CASCADE) # Populates the business name from the Business class defined within the Relationships' models.py file
    legal_entity_fiscal_year_end = models.DateField()
    period_ending_date = models.DateField()
    financial_statement_quality = models.CharField(max_length=3, choices=FINANCIAL_STATEMENT_QUALITY_CHOICES)

    # Revenue
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    returns_and_allowances = models.DecimalField(max_digits=15, decimal_places=2)

    # Cost of Goods Sold
    cost_of_goods_sold_general = models.DecimalField(max_digits=15, decimal_places=2)
    cost_of_goods_sold_depreciation = models.DecimalField(max_digits=15, decimal_places=2)

    # Operating Expenses
    salaries_and_wages = models.DecimalField(max_digits=15, decimal_places=2)
    officers_compensation = models.DecimalField(max_digits=15, decimal_places=2)
    repairs_and_maintenance = models.DecimalField(max_digits=15, decimal_places=2)
    bad_debt = models.DecimalField(max_digits=15, decimal_places=2)

    # Rent and Lease Expenses
    real_estate_rent_effects_ebitdar = models.DecimalField(max_digits=15, decimal_places=2)
    real_estate_rent_no_refinance_scenario = models.DecimalField(max_digits=15, decimal_places=2)
    operating_leases = models.DecimalField(max_digits=15, decimal_places=2)

    # Taxes, Licenses, and Insurance
    real_estate_taxes = models.DecimalField(max_digits=15, decimal_places=2)
    payroll_taxes = models.DecimalField(max_digits=15, decimal_places=2)
    liability_insurance = models.DecimalField(max_digits=15, decimal_places=2)
    other_taxes_and_licenses = models.DecimalField(max_digits=15, decimal_places=2)

    # Other fields
    depreciation_and_depletion = models.DecimalField(max_digits=15, decimal_places=2)
    amortization = models.DecimalField(max_digits=15, decimal_places=2)
    legal_and_professional_expenses = models.DecimalField(max_digits=15, decimal_places=2)
    employee_benefit_programs = models.DecimalField(max_digits=15, decimal_places=2)
    advertising = models.DecimalField(max_digits=15, decimal_places=2)

    # Other Operating Expenses
    other_operating_expenses_general = models.DecimalField(max_digits=15, decimal_places=2)

    # Other Income and Expenses
    gain_on_sale_of_asset = models.DecimalField(max_digits=15, decimal_places=2)
    loss_on_sale_of_asset = models.DecimalField(max_digits=15, decimal_places=2)
    interest_income = models.DecimalField(max_digits=15, decimal_places=2)
    interest_expense = models.DecimalField(max_digits=15, decimal_places=2)

    # Other Income or Expenses
    other_income_or_expense_general = models.DecimalField(max_digits=15, decimal_places=2)

    # Taxes
    c_corporation_taxes = models.DecimalField(max_digits=15, decimal_places=2)
    c_corporation_tax_refund = models.DecimalField(max_digits=15, decimal_places=2)

    # Other Adjustments to Cash Flow and Shareholders' Equity
    other_cash_flow_adjustment_general = models.DecimalField(max_digits=15, decimal_places=2)

    # Debt Service Coverage Analysis (Includes Other Cash Flow Adjustments)
    debt_service_obligations = models.DecimalField(max_digits=15, decimal_places=2)
    adjusted_monthly_debt_service_obligations = models.DecimalField(max_digits=15, decimal_places=2)
    adjusted_obligations_for_months_in_current_period = models.DecimalField(max_digits=15, decimal_places=2)
    historical_interest_expenses = models.DecimalField(max_digits=15, decimal_places=2)
    adjusted_debt_service_obligations = models.DecimalField(max_digits=15, decimal_places=2)
    distributions_to_shareholders = models.DecimalField(max_digits=15, decimal_places=2)



    # Auto-calculated fields (i.e., amount of months in current period, total and subtotal fields)
    @property
    def months_in_period(self):
        if self.period_ending_date and self.legal_entity_fiscal_year_end:
            fy_end_month = self.legal_entity_fiscal_year_end.month
            period_end_month = self.period_ending_date.month

            if fy_end_month == 12:
                return period_end_month
            elif period_end_month > fy_end_month:
                return period_end_month - fy_end_month
            else:
                return (12 - fy_end_month) + period_end_month
        else:
            return None

    @property
    def net_revenue(self):
        return self.revenue - self.returns_and_allowances

    @property
    def revenue_subtotal(self):
        return self.revenue

    @property
    def cost_of_goods_sold_subtotal(self):
        return self.cost_of_goods_sold_general + self.cost_of_goods_sold_depreciation

    @property
    def total_gross_profit(self):
        return self.net_revenue - self.cost_of_goods_sold_subtotal

    @property
    def rent_and_lease_expenses_subtotal(self):
        return self.real_estate_rent_effects_ebitdar + self.real_estate_rent_no_refinance_scenario + self.operating_leases

    @property
    def taxes_licenses_and_insurance_subtotal(self):
        return self.real_estate_taxes + self.payroll_taxes + self.liability_insurance + self.other_taxes_and_licenses

    @property
    def other_operating_expenses_subtotal(self):
        return self.other_operating_expenses_general

    @property
    def total_operating_expenses(self):
        return (
            self.salaries_and_wages + self.officers_compensation + self.repairs_and_maintenance + self.bad_debt +
            self.rent_and_lease_expenses_subtotal + self.taxes_licenses_and_insurance_subtotal +
            self.depreciation_and_depletion + self.amortization + self.legal_and_professional_expenses +
            self.employee_benefit_programs + self.advertising + self.other_operating_expenses_subtotal
        )

    @property
    def net_operating_income(self):
        return self.total_gross_profit - self.total_operating_expenses

    @property
    def other_income_and_expenses(self):
        return self.gain_on_sale_of_asset - self.loss_on_sale_of_asset + self.interest_income - self.interest_expense

    @property
    def other_income_or_expenses_subtotal(self):
        return self.other_income_or_expense_general

    @property
    def total_other_income_and_expenses(self):
        return self.other_income_and_expenses + self.other_income_or_expenses_subtotal

    @property
    def net_profit_loss(self):
        return self.net_operating_income + self.total_other_income_and_expenses

    @property
    def net_profit_loss_after_taxes(self):
        return self.net_profit_loss - self.c_corporation_taxes + self.c_corporation_tax_refund

    @property
    def other_cash_flow_adjustments_subtotal(self):
        return self.other_cash_flow_adjustment_general

    @property
    def total_adjusted_ebit(self):
        return (
            self.net_profit_loss_after_taxes +
            self.other_cash_flow_adjustments_subtotal +
            abs(self.c_corporation_taxes) +
            self.c_corporation_tax_refund +
            abs(self.interest_expense)
        )

    @property
    def total_adjusted_ebitda(self):
        return self.total_adjusted_ebit + self.depreciation_and_depletion + self.amortization

    @property
    def total_adjusted_ebitdar(self):
        return self.total_adjusted_ebitda + self.real_estate_rent_effects_ebitdar

    @property
    def total_adjusted_ebitdar_includes_distributions(self):
        return self.total_adjusted_ebitdar - self.distributions_to_shareholders

    def __str__(self):
        return f"Income Statement of user {self.user} for business {self.business.entity_name}"
