from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Loan

class LoanListView(ListView):
    model = Loan
    template_name = 'loan_list.html'
    context_object_name = 'loans'

class LoanDetailView(DetailView):
    model = Loan
    template_name = 'loan_detail.html'
    context_object_name = 'loan'

class LoanCreateView(CreateView):
    model = Loan
    template_name = 'loan_form.html'
    fields = '__all__'

class LoanUpdateView(UpdateView):
    model = Loan
    template_name = 'loan_form.html'
    fields = '__all__'

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'loan_confirm_delete.html'
    success_url = reverse_lazy('loan_list')
