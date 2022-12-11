from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


class UserRegistrationView(View):
    form_class = UserRegistrationForm
    # before running the get and post
    # sometime you can send a param to UI through this way
    def dispatch(self, request, *args, **kwargs):
        if (request.user.is_authenticated):
            return render(request, 'Zaram/post_detail.html')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        user_from = self.form_class()

        return render(request, 'usr_account/user_registration.html', {'form': user_from})

    def post(self, request):
          form = self.form_class(request.POST)
          if form.is_valid():
              cl = form.cleaned_data
              User.objects.create_user(cl['username'], cl['email'], cl['password'])
              messages.success(request, 'registration successfully', 'success')
              return render(request, 'Zaram/post_detail.html')
          return render(request, 'usr_account/user_registration.html', {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'usr_account/user_login.html'
    def get(self, request):
        if (request.user.is_authenticated):
            logout(request)
        user_form = self.form_class()
        return render(request, self.template_name, {'form': user_form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cl = form.cleaned_data
            user = authenticate(username=cl['username'], password=cl['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you login successfuly', 'success')
                return render(request, 'Zaram/post_detail.html')
            messages.error(request, 'username or password is wrong', 'warning')
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})

class UserProfile(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return render(request, 'usr_account/user_profile.html', {'user': user})
