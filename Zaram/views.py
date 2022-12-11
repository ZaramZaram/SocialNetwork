from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from Zaram.models import Post


class HomePage(View):
    def get(self, request):
       return render(request, 'Zaram/index.html')

class PostDetailView(View):
     def dispatch(self, request, *args, **kwargs):
        print('aaaa')
        render(request, 'Zaram/index.html')

     def get(self, request):
         print('aaaa')
         if request.user.is_authenticated:
             posts = Post.objects.filter(user_id=request.user.id)

             for p in posts:
                 print(p.postimage_set.values())

             render(request, 'Zaram/post_detail.html', {"posts": posts})
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
