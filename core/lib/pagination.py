from django.conf import settings

from rest_framework.pagination import PageNumberPagination


class ListPagination(PageNumberPagination):
    page_size = settings.DEFAULT_PAGE_ORDERS
