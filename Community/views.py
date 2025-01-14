from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
from django.views.generic import View
from django.http import HttpResponseRedirect
from Community.models import Comment

class CommentCreateView(View):
    comment_form_class = CommentForm
    template_name: str = "Community/community_home.html"
    success_url = reverse_lazy("Community:comment-list")
    next_page = "Community/community_comment_list.html"
    def get(self, request):
        comment_form=self.comment_form_class()
        return render(
            request,
            self.template_name,
            {"comment_form": comment_form},
        )
    def post(self, request):
        comment_form = self.comment_form_class(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user.email
            comment.save()
            return HttpResponseRedirect(self.success_url)
        return render(
            request,
            self.template_name,
            {"comment_form":comment_form,},
        )


class CommentListView(View):
    comments = Comment.objects.all()
    template_name = "Community/community_comment_list.html"
    def get(self,request):
        return render(
            request,
            self.template_name,
            {"comment_query_set":self.comments}            
        )