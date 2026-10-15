from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("students/", views.student_list, name='student_list'),
    path("students/add/", views.add_student, name='add_student'),
    path("edit/<int:id>/", views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('students/<int:id>/', views.student_detail, name='student_detail'),
    path("companies/", views.company_list, name='company_list'),
    path("companies/add/", views.add_company, name='add_company'),
    path("companies/edit/<int:id>/", views.edit_company, name='edit_company'),
    path("companies/delete/<int:id>/", views.delete_company, name='delete_company'),
    path("placements/", views.placement_list, name='placement_list'),
    path("placements/add/", views.add_placement, name='add_placement'),
    path("placements/edit/<int:id>/", views.edit_placement, name='edit_placement'),
    path("placements/delete/<int:id>/", views.delete_placement, name='delete_placement'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
]