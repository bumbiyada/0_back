from django.urls import path

from .views import ListCustomUsersView, ListDepartmentViewN3, ListDepartmentViewN4, ListDepartmentViewN5, ListDepartmentViewN6

from .views import ListDepartmentViewN9, ListDepartmentViewN10, ListDepartmentViewN13

from .views import ListCustomStageNameView, ListCustomDocNameView, ListCustomDocTypeView, ListCustomFoivView
urlpatterns = [
    path('custom-users', ListCustomUsersView.as_view()),
    path('custom-foiv', ListCustomFoivView.as_view()),
    path('custom-doc-type', ListCustomDocTypeView.as_view()),
    path('custom-doc-name', ListCustomDocNameView.as_view()),
    path('custom-stage-name', ListCustomStageNameView.as_view()),
    path('dep-3', ListDepartmentViewN3.as_view()),
    path('dep-4', ListDepartmentViewN4.as_view()),
    path('dep-5', ListDepartmentViewN5.as_view()),
    path('dep-6', ListDepartmentViewN6.as_view()),
    path('dep-9', ListDepartmentViewN9.as_view()),
    path('dep-10', ListDepartmentViewN10.as_view()),
    path('dep-13', ListDepartmentViewN13.as_view()),
]
