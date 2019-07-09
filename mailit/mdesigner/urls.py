from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path("login/", views.login_user, name="login_user"),
  path("signup/", views.signup_user, name="signup_user"),
  path("dashboard/",views.dashboard_view, name="dashboard_view"),
  path("designer/",views.designer_view, name="designer_view"),
  path("newproject/",views.project_new_view, name="project_new_view"),
  path("dashboardrev/",views.dashboard_reviewer_view, name="dashboard_reviewer_view"),
  path("dashboardadmin/",views.dashboard_admin_view, name="dashboard_admin_view"),
  path("designer/",views.designer_view, name="designer_view"),
  path("designerrev/",views.designer_reviewer_view, name="designer_reviewer_view"),
  path("designeradmin/",views.designer_admin_view, name="designer_admin_view"),
  path("profile/",views.profile_view, name="profile_view"),
]
