from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.urls import reverse
from . import models as boards_models
from . import forms as boards_forms
from django.views.generic import DetailView,FormView,ListView,UpdateView


def home(request):
    return render(request,'home.html',{})

class BoardListView(ListView):
    model = boards_models.Board
    paginate_by = 5  # 페이지당 8개
    paginate_orphans = 3 # 마지막 페이지에 3개 이하가 남겨져 있으면 앞페이지로 당겨짐 마지막 페이지에는 (8 + 3이하)개의 게시물이 있음
    template_name: str = 'boards/board_list.html'
    def get_queryset(self):
        boards = boards_models.Board.objects.order_by('-created_at')
        return boards
    def get_context_data(self, **kwargs):
        context = super(BoardListView, self).get_context_data()
        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        context['pagelist'] = pagelist
        return context

class BoardDetailView(DetailView):
    model = boards_models.Board
    template_name: str = 'boards/board_detail.html'
    def get_object(self):
        board = get_object_or_404(boards_models.Board, pk=self.kwargs["pk"])
        return board


class BoardCreateView(FormView):
    template_name = "boards/board_create.html"
    form_class = boards_forms.BoardCreateForm
    queryset = boards_models.Board
    def form_valid(self, form):
        board = form.save()
        board.writer = self.request.user
        board.save()
        form.save_m2m()
        return redirect(reverse("board:board_detail", kwargs={"pk": board.pk}))
    
class BoardUpdateView(UpdateView):
    model = boards_models.Board
    template_name = "boards/board_edit.html"
    fields = (
        "title",
        "content",
        "tag",
    )
    def get_success_url(self):
        board_pk = self.kwargs.get("board_pk")
        return reverse(
            "board:board_detail",
            kwargs={
                "pk": board_pk,
            },
        )
    def get_object(self):
        board = get_object_or_404(boards_models.Board, pk=self.kwargs["board_pk"])

        return board


def board_delete(request, board_pk):
    board = boards_models.Board.objects.get(pk=board_pk)
    board.delete()
    return redirect("board:board_list")


def TagSearchView(request):
    if request.method == "GET":
        form=boards_forms.TagSearchForm()
    else:
        form = boards_forms.TagSearchForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data.get('name')
            tag = get_object_or_404(tags)
            boards_list = boards_models.Board.objects.filter(tag__name__icontains=tag).order_by('-pk')
            page = request.GET.get('page','1')
            paginator = Paginator(boards_list,per_page=5,orphans=3) # 페이지당 5개
            page_obj = paginator.get_page(page)
            return render(request,'tag/tag_search.html',{'form':form,'boards_list':boards_list,'page_obj':page_obj,"tag":tag})
    return render(request,'tag/tag_search.html',{'form':form})
