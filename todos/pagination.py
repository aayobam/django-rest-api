from rest_framework.pagination import PageNumberPagination



class CustomPageNUmberPagination(PageNumberPagination):
    """
    This helps to handle the amounts of todo list that can be fetched and returned
    per page.
    """
    page_size = 10
    page_size_query_param = 'count'
    max_page_size = 15
    page_query_param = 'p'
