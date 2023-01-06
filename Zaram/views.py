from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from Zaram.models import Post
from Zaram.forms import PostUpdateForm, CommentCreateForm


class HomePage(View):
    def get(self, request):
        if request.user.is_authenticated:
            posts = Post.objects.filter(user_id=request.user.id)
            return render(request, 'Zaram/post_detail.html', {"posts": posts})
        return render(request, 'Zaram/index.html')

class PostDetailView(View):
     # def dispatch(self, request, *args, **kwargs):
     #    print('aaaa')
     #    render(request, 'Zaram/index.html')

     def get(self, request):
         frm_class = CommentCreateForm
         if request.user.is_authenticated:
             posts = Post.objects.filter(user_id=request.user.id)

             return render(request, 'Zaram/post_detail.html', {"posts": posts,'form': self.frm_class})
         return render(request, 'Zaram/index.html')

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if post.user.id == request.user.id:
           post.delete()
           messages.success(request, 'post deleted')
        else:
            messages.error(request, 'you can not delete this post')
        return redirect('Zaram/post_detail.html')

class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostUpdateForm
    def setup(self, request, *args, **kwargs):
        post_instance = Post.objects.get(pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)
    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(request, 'you cannot update this post')
            return redirect('Zaram/index.html')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, 'Zaram/update.html', {'form': form})
    def post(self, request):
        post = self.post_instance
        form = self.form_class(instance=post)