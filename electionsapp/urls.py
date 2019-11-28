from django.urls import path

from .views import IndexView, PollDetail, poll_results, vote

app_name = 'elect'
urlpatterns = [
    path('', IndexView.as_view(), name='welcome'),
    path('<int:pk>/', PollDetail.as_view(), name='detail'),
    path('<int:question_id>/vote', vote, name='vote'),
    path('<int:question_id>/results', poll_results, name='results'),
]
