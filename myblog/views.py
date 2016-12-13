from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #posts = Post.objects.all()
    return render(request, 'myblog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', { 'post': post })

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('myblog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'myblog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('myblog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myblog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'myblog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')



# class RegisterFormView(FormView):
#     form_class = UserCreationForm

#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "/login/"

#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "myblog/register.html"

#     def form_valid(self, form):
#         # Создаём пользователя, если данные в форму были введены корректно.
#         form.save()

#         # Вызываем метод базового класса
#         return super(RegisterFormView, self).form_valid(form)



# from django.contrib.auth.forms import AuthenticationForm

# # Функция для установки сессионного ключа.
# # По нему django будет определять, выполнил ли вход пользователь.
# from django.contrib.auth import login

# class LoginFormView(FormView):
#     form_class = AuthenticationForm

#     # Аналогично регистрации, только используем шаблон аутентификации.
#     template_name = "myblog/login.html"

#     # В случае успеха перенаправим на главную.
#     success_url = "/"

#     def form_valid(self, form):
#         # Получаем объект пользователя на основе введённых в форму данных.
#         self.user = form.get_user()

#         # Выполняем аутентификацию пользователя.
#         login(self.request, self.user)
#         return super(LoginFormView, self).form_valid(form)


# from django.http import HttpResponseRedirect
# from django.views.generic.base import View
# from django.contrib.auth import logout

# class LogoutView(View):
#     def get(self, request):
#         # Выполняем выход для пользователя, запросившего данное представление.
#         logout(request)

#         # После чего, перенаправляем пользователя на главную страницу.
#         return HttpResponseRedirect("/")
