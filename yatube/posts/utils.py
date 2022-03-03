from django.core.paginator import Paginator

COUNTLIST = 10


def pagin(request, post_list):
    paginator = Paginator(post_list, COUNTLIST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
