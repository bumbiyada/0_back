from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import ListAll
from .serializers import ListAllSerializer, ListWithoutDataSerializer
# Create your views here.


class ListCustomUsersView(ListAPIView):
    queryset = ListAll.objects.values('Stage_user').distinct()
    serializer_class = ListWithoutDataSerializer
    # permission_classes = (permissions.IsAuthenticated,)  # affects only backend part (locale 8000)


class ListCustomFoivView(ListAPIView):
    queryset = ListAll.objects.values('Foiv').distinct()
    serializer_class = ListWithoutDataSerializer


class ListCustomDocTypeView(ListAPIView):
    queryset = ListAll.objects.values('Document_type').distinct()
    serializer_class = ListWithoutDataSerializer


class ListCustomDocNameView(ListAPIView):
    queryset = ListAll.objects.values('Document_number').distinct()
    serializer_class = ListWithoutDataSerializer


class ListCustomStageNameView(ListAPIView):
    queryset = ListAll.objects.values('Stage_name').distinct()
    serializer_class = ListWithoutDataSerializer


class ListDepartmentViewN3(ListAPIView):
    queryset = ListAll.objects.filter(
        User_department__startswith='3'
    )
    serializer_class = ListAllSerializer


class ListDepartmentViewN4(ListAPIView):
    queryset = ListAll.objects.filter(
        User_department__startswith='4'
    )
    serializer_class = ListAllSerializer


class ListDepartmentViewN5(ListAPIView):
    queryset = ListAll.objects.filter(
        User_department__startswith='5'
    )
    serializer_class = ListAllSerializer


class ListDepartmentViewN6(ListAPIView):
    queryset = ListAll.objects.filter(
        User_department__startswith='6'
    )
    serializer_class = ListAllSerializer


class ListDepartmentViewN9(ListAPIView):
    queryset = ListAll.objects.filter(
        User_department__startswith='9'
    )
    serializer_class = ListAllSerializer


class ListDepartmentViewN10(ListAPIView):
    queryset = ListAll.objects.filter(
        User_department__startswith='1'
    )
    serializer_class = ListAllSerializer


class ListDepartmentViewN13(ListAPIView):
    queryset = ListAll.objects.filter(
        User_department__startswith='2'
    )
    serializer_class = ListAllSerializer


def get_users():
    pass


class ListCustomDash(ListAPIView):
    queryset = ListAll.objects.values('Stage_user').distinct('Stage_user')
    serializer_class = ListAllSerializer
