from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.loginView, name="loginView"),
    path("logout", views.logoutView, name="logoutView"),
    path("portal/home", views.index, name="index"),
    path("portal/examinations", views.examinationsView, name="exams"),
    path("portal/fees", views.feesView, name="fees"),
    path("portal/clearance", views.clearanceView, name="clearance"),
    path("portal/news", views.newsView, name="news"),
    path("portal/reporting", views.reportingView, name="reporting"),
    path("portal/units", views.unitsView, name="units"),
    path("portal/hostel", views.hostelView, name="hostel"),
    path("portal/messages", views.messagesView, name="messages"),
    path("portal/profile", views.profileView, name="profile"),
]