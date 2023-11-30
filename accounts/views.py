# p380
from django.views.generic import CreateView, TemplateView, ListView
from .forms import CustomUserCreationForm, StrategyForm
from django.urls import reverse_lazy
from .models import StrategyModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, DeleteView
from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)


class IndexView(ListView):
    template_name = 'index_ac.html'
    queryset = StrategyModel.objects.order_by('-posted_at')
    paginate_by = 9


class PostView(TemplateView):
    template_name = 'post.html'


class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"


class PostSuccessView(TemplateView):
    template_name = 'post_success.html'


class MypageView(ListView):
    template_name = 'mypage.html'
    context_object_name = 'orderby_records'
    queryset = StrategyModel.objects.order_by('posted_at')


@method_decorator(login_required, name='dispatch')
class CreateStrategyView(CreateView):
    form_class = StrategyForm
    template_name = "post.html"
    success_url = reverse_lazy('accounts:post_done')

    def form_valid(self, form):
        postdate = form.save(commit=False)
        postdate.user = self.request.user
        postdate.save()
        return super().form_valid(form)


class CategoryView(ListView):
    template_name = 'index_ac.html'
    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = StrategyModel.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories


class DetailView(DetailView):
    template_name = 'detail.html'
    model = StrategyModel


class PhotoDeleteView(DeleteView):
    model = StrategyModel
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('accounts:mypage')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        title = request.POST.get('title', '')
        message_body = request.POST.get('message', '')

        try:
            # メールの送信ロジック
            email_subject = f'お問い合わせ: {title}'
            email_body = f'送信者: {name}\nメールアドレス: {email}\n\n{message_body}'
            email = EmailMessage(email_subject, email_body,
                                 to=['mit2371152@stu.o-hara.ac.jp'])
            email.send()

            # 送信成功時のメッセージ
            success_message = 'お問い合わせは正常に送信されました。'
            return render(request, 'contact_success.html', {'success_message': success_message})

        except Exception as e:
            # 送信失敗時のメッセージ
            error_message = 'お問い合わせの送信中にエラーが発生しました。'
            return render(request, 'contact_false.html', {'error_message': error_message})

    return render(request, 'contact.html')
