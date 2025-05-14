from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from blogs.models import Blog
from store.models import Product
from django.core.mail import send_mail
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by('-date')[:3]
        context['products'] = Product.objects.all().order_by('-date')[:4]
        return context


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = '✅ Ваше сообщение успешно отправлено!'

    def form_valid(self, form):
        contact = form.save()

        # إرسال الإيميل
        subject = f"Сообщение от{form.cleaned_data['name']}"
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        full_message = f"{message}\n\nномер телефона: {phone}\n\nПочта: {from_email}"

        send_mail(
            subject,
            full_message,
            from_email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return super().form_valid(form)