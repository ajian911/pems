from django.shortcuts import render
from django.core.paginator import Paginator

def pageBar(request, objects, pageIndex, template = 'control/pageBar.html'):
    pageIndex = int(pageIndex)
    _paginator = Paginator(objects, 5)
    return render(request, template, {
        'request' :  request,
        'pagiator' :  _paginator,
        'has_pages' :  _paginator.num_pages > 1,
        'has_next' :  _paginator.page(pageIndex).has_next(),
        'has_prev' : _paginator.page(pageIndex).has_previous(),
        'page_index' : pageIndex,
        'page_next' : pageIndex + 1,
        'page_prev' : pageIndex - 1,
        'page_count' : _paginator.num_pages,
        'row_count' : _paginator.count,
        'page_nums' : range(_paginator.num_pages + 1)[1:],
    }
    )