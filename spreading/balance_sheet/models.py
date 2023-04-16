from django.db import models

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
    uuid = models.UUIDField(primary_key=True, unique=True)
    entity_name = models.CharField(max_length=100)

    # Asset fields
    cash_at_financial_institution = models.DecimalField(max_digits=15, decimal_places=2)
    cash_at_other_financial_institution = models.DecimalField(max_digits=15, decimal_places=2)
    unclassified_cash_account = models.DecimalField(max_digits=15, decimal_places=2)

    accounts_receivable = models.DecimalField(max_digits=15, decimal_places=2)
    bad_debt_allowance = NegativeDecimalField(max_digits=15, decimal_places=2)

    raw_material = models.DecimalField(max_digits=15, decimal_places=2)
    work_in_progress = models.DecimalField(max_digits=15, decimal_places=2)
    finished_goods = models.DecimalField(max_digits=15, decimal_places=2)
    unclassified_inventory = models.DecimalField(max_digits=15, decimal_places=2)

    prepaid_expenses_generic = models.DecimalField(max_digits=15, decimal_places=2)

    other_current_assets_generic = models.DecimalField(max_digits=15, decimal_places=2)

    machinery_and_equipment = models.DecimalField(max_digits=15, decimal_places=2)
    computers_and_office_equipment = models.DecimalField(max_digits=15, decimal_places=2)
    furniture_and_fixtures = models.DecimalField(max_digits=15, decimal_places=2)
    leasehold_improvements = models.DecimalField(max_digits=15, decimal_places=2)
    construction_in_progress = models.DecimalField(max_digits=15, decimal_places=2)
    building = models.DecimalField(max_digits=15, decimal_places=2)
    other_fixed_asset = models.DecimalField(max_digits=15, decimal_places=2)
    accumulated_depreciation = NegativeDecimalField(max_digits=15, decimal_places=2)

    land = models.DecimalField(max_digits=15, decimal_places=2)

    goodwill = models.DecimalField(max_digits=15, decimal_places=2)
    trademarks_and_licenses = models.DecimalField(max_digits=15, decimal_places=2)
    financing_costs = models.DecimalField(max_digits=15, decimal_places=2)
    other_intangible_assets = models.DecimalField(max_digits=15, decimal_places=2)
    accumulated_amortization = NegativeDecimalField(max_digits=15, decimal_places=2)

    due_from_related_parties_generic = models.DecimalField(max_digits=15, decimal_places=2)
    due_from_shareholders_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_assets_generic = models.DecimalField(max_digits=15, decimal_places=2)

    # Liability fields
    trade_accounts = models.DecimalField(max_digits=15, decimal_places=2)
    other_accounts = models.DecimalField(max_digits=15, decimal_places=2)
    current_portion_of_long_term_debt_generic = models.DecimalField(max_digits=15, decimal_places=2)
    revolving_lines_of_credit_generic = models.DecimalField(max_digits=15, decimal_places=2)

    customer_advances = models.DecimalField(max_digits=15, decimal_places=2)
    other_accruals = models.DecimalField(max_digits=15, decimal_places=2)

    payroll_liabilities = models.DecimalField(max_digits=15, decimal_places=2)
    taxes_payable = models.DecimalField(max_digits=15, decimal_places=2)

    long_term_notes_payable_generic = models.DecimalField(max_digits=15, decimal_places=2)
    due_to_related_parties_generic = models.DecimalField(max_digits=15, decimal_places=2)
    due_to_shareholders_generic = models.DecimalField(max_digits=15, decimal_places=2)
    other_long_term_liabilities_generic = models.DecimalField(max_digits=15, decimal_places=2)

    # Shareholders' Equity fields
    paid_in_capital = models.DecimalField(max_digits=15, decimal_places=2)
    beginning_retained_earnings = models.DecimalField(max_digits=15, decimal_places=2)
    current_periods_net_income_after_tax = models.DecimalField(max_digits=15, decimal_places=2)
    current_periods_distributions = models.DecimalField(max_digits=15, decimal_places=2)

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

# This separate model will help you store User Defined Fields specific to a given entity's uuid,
# and you can then query the User Defined Fields for a specific BalanceSheet instance by
# filtering on the balance_sheet ForeignKey.
class UserDefinedField(models.Model):
    field_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    balance_sheet = models.ForeignKey(BalanceSheet, on_delete=models.CASCADE)
