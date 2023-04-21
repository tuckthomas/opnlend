from django.db import models
from users.models import User
from relationships.models import Business
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models import F
from spreading.models import GlobalStatement
from datetime import timedelta

# Custom model for fields that the Balance Sheet model requires to
# be reflected as negative values. This approach will keep the
# conversion logic within the model iteself. Those field within
# the BalanceSheet model will then reference the NegativeDecimalField.
# Please note that the conversion to a negative value will not
# automatically be reflected in the form until saved, unless
# client-side JavaScript code is included to handle this
# negative conversion in real-time.
class NegativeDecimalField(models.DecimalField):
    def to_python(self, value):
        value = super(NegativeDecimalField, self).to_python(value)
        if value is not None and value > 0:
            value = -value
        return value

# Balance Sheet model.
class BalanceSheet(models.Model):
    # Global Statement ID for Financial Statement Set
    global_statement = models.ForeignKey(GlobalStatement, on_delete=models.CASCADE, related_name='income_statements')
    # Business Name
    business_name = models.ForeignKey(Business, on_delete=models.CASCADE)
    
    uuid = models.UUIDField(primary_key=True, unique=True)
    entity_name = models.CharField(max_length=100)

    # Asset fields
    
    # Current Assets
    # Cash (subtotal)
    cash_subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Cash Accounts (cascade)
    cash_at_financial_institution = models.DecimalField(max_digits=15, decimal_places=2)
    cash_at_other_financial_institution = models.DecimalField(max_digits=15, decimal_places=2)
    unclassified_cash_account = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Accounts Receivable (net)
    accounts_receivable_net = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    accounts_receivable = models.DecimalField(max_digits=15, decimal_places=2)
    bad_debt_allowance = NegativeDecimalField(max_digits=15, decimal_places=2)

    # Inventory (subtotal)
    inventory_subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    raw_material = models.DecimalField(max_digits=15, decimal_places=2)
    work_in_progress = models.DecimalField(max_digits=15, decimal_places=2)
    finished_goods = models.DecimalField(max_digits=15, decimal_places=2)
    unclassified_inventory = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Other Current Assets
    prepaid_expenses_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_current_assets_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_current_assets_udf1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_current_assets_udf2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_current_assets_udf3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Total Current Assets
    total_current_assets = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    # Gross Plant and Equipment (excludes land)
    gross_fixed_assets_subtotal) = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fixed_assets_generic = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    machinery_and_equipment = models.DecimalField(max_digits=15, decimal_places=2)
    computers_and_office_equipment = models.DecimalField(max_digits=15, decimal_places=2)
    furniture_and_fixtures = models.DecimalField(max_digits=15, decimal_places=2)
    leasehold_improvements = models.DecimalField(max_digits=15, decimal_places=2)
    construction_in_progress = models.DecimalField(max_digits=15, decimal_places=2)
    building = models.DecimalField(max_digits=15, decimal_places=2)
    other_fixed_assets_udf1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_fixed_assets_udf2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_fixed_assets_udf3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Accumulated Depreciation
    accumulated_depreciation = NegativeDecimalField(max_digits=15, decimal_places=2)
    # Net Plan and Equipemnt (excludes land); = Gross Plan and Equipment (subtotal) + Accumulated Depreciation (summed due to accumualted depreciation required to be entered as a negative amount)
    net_fixed_assets = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Land; listed separately to more easily differentiate non-depreciable assets
    land = models.DecimalField(max_digits=15, decimal_places=2)

    # Gross Intangible Assets
    goodwill = models.DecimalField(max_digits=15, decimal_places=2)
    trademarks_and_licenses = models.DecimalField(max_digits=15, decimal_places=2)
    financing_costs = models.DecimalField(max_digits=15, decimal_places=2)
    other_intangible_assets_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_intangible_assets_udf2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_intangible_assets_udf3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Accumulated Amortization
    accumulated_amortization = NegativeDecimalField(max_digits=15, decimal_places=2)
    # Net Intangible Assets
    net_intangible_assets = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Other Long Term Assets
    due_from_related_parties_generic = models.DecimalField(max_digits=15, decimal_places=2)
    due_from_shareholders_generic = models.DecimalField(max_digits=15, decimal_places=2)
    # Other Long Term Assets (subtotal)
    other_long_term_assets_subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    # Other Long Term Assets (cascade)
    other_long_term_assets_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_assets_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_assets_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_assets_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_assets_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    # Total Long Term Assets
    total_long_term_assets = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Total Assets; = Total Current Assets + Total Long Term Assets
    total_assets = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Liability Fields
    
    # Current Liabilities
    # Accounts Payable (subtotal)
    accounts_payable_subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Accounts Payable (cascade)
    trade_accounts_payable = models.DecimalField(max_digits=15, decimal_places=2)
    other_accounts_payable = models.DecimalField(max_digits=15, decimal_places=2)
    # Current Portion of Long Term Debt (subtotal)
    current_portion_of_long_term_debt_subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    # Current Portion of Long Term Debt (cascade)
    current_portion_of_long_term_debt_generic = models.DecimalField(max_digits=15, decimal_places=2)
    current_portion_of_long_term_debt_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    current_portion_of_long_term_debt_udf2 = models.DecimalField(max_digits=15, decimal_places=2)
    current_portion_of_long_term_debt_udf3 = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Short-Term Revolving Lines; Note: This is separated out to allow for easier exclusion of short-term notes payble from debt service coverage analysis, as occasionally accountants will sum current portion of long term debts (principal and interest payments) with revolving lines (interest only payments)
    # Revolving Lines (subtotal)
    revolving_lines_subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    # Revolving Lines (cascade)
    revolving_lines_generic = models.DecimalField(max_digits=15, decimal_places=2)
    credit_cards_payable = models.DecimalField(max_digits=15, decimal_places=2)
    revolving_lines_of_credit_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_revolving_line_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_revolving_line_udf2 = models.DecimalField(max_digits=15, decimal_places=2)
    other_revolving_line_udf3 = models.DecimalField(max_digits=15, decimal_places=2)
    other_revolving_line_udf4 = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Accruals; seperated for clearer distinction in UCA Cash Flow Analysis
    # Accruals (subtotal)
    accruals_subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    # Accruals (cascade)
    other_accruals_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_accruals_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_accruals_udf2 = models.DecimalField(max_digits=15, decimal_places=2)
    other_accruals_udf3 = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Other Current Liabilities
    taxes_payable = models.DecimalField(max_digits=15, decimal_places=2)
    customer_advances = models.DecimalField(max_digits=15, decimal_places=2)
    payroll_liabilities = models.DecimalField(max_digits=15, decimal_places=2)
    # Other Current Liabilities (subtotal)
    other_current_liabilities_subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    # Other Current Liabilities (cascade)
    other_current_liabilities_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_current_liabilities_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_current_liabilities_udf2 = models.DecimalField(max_digits=15, decimal_places=2)
    other_current_liabilities_udf3 = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Total Current Liabilities; = Accounts Payable (subtotal) + Current Portion of Long Term Debt (subtotal) +
    # Revolving Lines (subtotal) + Accruals (subtotal) + Taxes Payable + Customer Advances +
    # Payroll Liabilities + Other Current Liabilities (subtotal)
    total_current_liabilities = models.DecimalField(max_digits=15, decimal_places=2)

    # Long Term Liabilities
    # Long-Term Debt to be Refinanced; Note: This is seperated out for clearer distinction for SBA loan requests due to the SBA requiring debts being refinanced by an SBA loan be itemized on the balance sheet.
    # Refinanced Debt (subtotal)
    refinanced_long_term_debt_subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    # Refinanced Debt (cascade)
    refianced_long_term_debt_generic = models.DecimalField(max_digits=15, decimal_places=2)
    refianced_long_term_debt_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    refianced_long_term_debt_udf2 = models.DecimalField(max_digits=15, decimal_places=2)
    refianced_long_term_debt_udf3 = models.DecimalField(max_digits=15, decimal_places=2)
    refianced_long_term_debt_udf4 = models.DecimalField(max_digits=15, decimal_places=2)
    refianced_long_term_debt_udf5 = models.DecimalField(max_digits=15, decimal_places=2)
    refianced_long_term_debt_udf6 = models.DecimalField(max_digits=15, decimal_places=2)
    refianced_long_term_debt_udf7 = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Long Term Notes Payable (other) (subtotal)
    long_term_notes_payable_generic = models.DecimalField(max_digits=15, decimal_places=2)
    # Long Term Notes Payable (other) (cascade)
    long_term_notes_payable_generic = models.DecimalField(max_digits=15, decimal_places=2)
    long_term_notes_payable_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    long_term_notes_payable_udf2 = models.DecimalField(max_digits=15, decimal_places=2)
    long_term_notes_payable_udf3 = models.DecimalField(max_digits=15, decimal_places=2)
    long_term_notes_payable_udf4 = models.DecimalField(max_digits=15, decimal_places=2)
    # Total Notes Payable; = Refinanced Long-Term Debt Subtotal + Long-Term Notes Payable Subtotal
    total_notes_payable = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Other Long Term Debt
    # Other Long Term Debt (subtotal)
    other_long_term_debt_subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    #Other Long Term Debt (cascade)
    due_to_related_parties_generic = models.DecimalField(max_digits=15, decimal_places=2)
    due_to_shareholders_generic = models.DecimalField(max_digits=15, decimal_places=2)
    # Other Long Term Debt (subtotal)
    other_long_term_liabilities_generic = models.DecimalField(max_digits=15, decimal_places=2)
    # Other Long Term Debt (cascade)
    other_long_term_liabilities_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_liabilities_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_liabilities_udf2 = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_liabilities_udf3 = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_liabilities_udf4 = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Shareholders' Equity Fields
    paid_in_capital = models.DecimalField(max_digits=15, decimal_places=2)
    beginning_retained_earnings = models.DecimalField(max_digits=15, decimal_places=2)
    current_period_retained_earnings = models.DecimalField(max_digits=15, decimal_places=2)
    current_period_distributions = models.DecimalField(max_digits=15, decimal_places=2)
    # Other Equity (subtotal)
    other_equity_subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    # Other Equity (cascade)
    other_equity_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_equity_udf1 = models.DecimalField(max_digits=15, decimal_places=2)
    other_equity_udf2 = models.DecimalField(max_digits=15, decimal_places=2)
    other_equity_udf3 = models.DecimalField(max_digits=15, decimal_places=2)
    other_equity_udf4 = models.DecimalField(max_digits=15, decimal_places=2)
    # Total Shareholde's Equity
    total_shareholders_equity = models.DecimalField(max_digits=15, decimal_places=2)
    # Total Shareholder's Equity and Liabilities
    
    # Current Unbalanced Amount; Note: This is to be a dynamically updated field (requires javascript) that will continue to report any unbalanced amount to assist in reconciliation.
    unbalanced_amount = models.DecimalField(max_digits=15, decimal_places=2)
    # Note: At a later date, I'd like to add in some custom logic based on the offage amount.
    # For example, if the offage is a significant percentage (say, +- 30%) of total assets,
    # it may suggest a "slide error". Or, the offage is within a small percentage of an
    # single account type, it may suggest to review that account.
    
    
    
    # Sub-Total Fields
    @property
    def total_current_assets(self):
        return self.cash_subtotal + self.net_accounts_receivable_subtotal + self.inventory_subtotal + \
               self.prepaid_expenses_generic + self.other_current_assets_generic

    @property
    def total_long_term_assets(self):
        return self.total_fixed_assets + self.total_other_long_term_assets

    @property
    def total_assets(self):
        return self.total_current_assets + self.total_long_term_assets

    @property
    def accounts_payable_subtotal(self):
        return self.trade_accounts + self.other_accounts

    @property
    def current_portion_of_long_term_debt_subtotal(self):
        return self.current_portion_of_long_term_debt_generic  # Add user-defined fields related to current portion of long-term debt

    @property
    def credit_cards_and_other_lines_of_credit_subtotal(self):
        return self.revolving_lines_of_credit_generic  # Add user-defined fields related to credit cards and other lines of credit

    @property
    def accruals_subtotal(self):
        return self.customer_advances + self.other_accruals

    @property
    def other_current_liabilities_subtotal(self):
        return self.payroll_liabilities + self.taxes_payable + self.other_current_assets_generic

    @property
    def total_current_liabilities(self):
        return self.accounts_payable_subtotal + self.current_portion_of_long_term_debt_subtotal + \
               self.credit_cards_and_other_lines_of_credit_subtotal + self.accruals_subtotal + \
               self.other_current_liabilities_subtotal

    @property
    def notes_to_be_refinanced_subtotal(self):
        return 0  # Add user-defined fields related to notes to be refinanced

    @property
    def other_long_term_notes_payable_subtotal(self):
        return self.long_term_notes_payable_generic  # Add user-defined fields related to other long-term notes payable

    @property
    def due_to_related_party_subtotal(self):
        return self.due_to_related_parties_generic  # Add user-defined fields related to due to related party

    @property
    def due_to_shareholders_subtotal(self):
        return self.due_to_shareholders_generic  # Add user-defined fields related to due to shareholders

    @property
    def other_long_term_liabilities_subtotal(self):
        return self.other_long_term_liabilities_generic  # Add user-defined fields related to other long-term liabilities

    @property
    def total_long_term_liabilities(self):
        return self.notes_to_be_refinanced_subtotal + self.other_long_term_notes_payable_subtotal + \
               self.due_to_related_party_subtotal + self.due_to_shareholders_subtotal + \
               self.other_long_term_liabilities_subtotal

    @property
    def total_liabilities(self):
        return self.total_current_liabilities + self.total_long_term_liabilities

    @property
    def retained_earnings_subtotal(self):
        return self.beginning_retained_earnings + self.current_periods_net_income_after_tax - \
               self.current_periods_distributions

    @property
    def other_adjustments_to_equity_subtotal(self):
        return 0  # Add user-defined fields related to other adjustments to equity

    @property
    def total_shareholders_equity(self):
        return self.paid_in_capital + self.retained_earnings_subtotal + self.other_adjustments_to_equity_subtotal

    @property
    def total_shareholders_equity_and_liabilities(self):
        return self.total_liabilities + self.total_shareholders_equity
