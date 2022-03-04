import os
import sys

from django.core.paginator import Paginator

sys.path.append(os.path.abspath('..'))

from yatube.settings import COUNTLIST # noqa: E402


def pagin(request, post_list):
    paginator = Paginator(post_list, COUNTLIST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
