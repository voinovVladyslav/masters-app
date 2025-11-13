from rest_framework import pagination


class DefaultPagination(pagination.PageNumberPagination):
    max_page_size = 100
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'page_size'
