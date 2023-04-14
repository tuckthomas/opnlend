from django.urls import path
from .views import LoanDetailView, LoanListView, LoanCreateView, LoanUpdateView, LoanDeleteView

app_name = 'loan'

urlpatterns = [
    path('', LoanListView.as_view(), name='list'),
    path('create/', LoanCreateView.as_view(), name='create'),
    path('<int:pk>/', LoanDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', LoanUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', LoanDeleteView.as_view(), name='delete'),
]
