from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm


def news_list(request):
    # news_list=News.published.all()
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)


# Create your views here.
def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context)


# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:5]
#     local_one = News.published.filter(category__name="Mahalliy").order_by('-publish_time')[:1]
#     local_news = News.published.all().filter(category__name="Mahalliy").order_by('-publish_time')[1:6]
#     context = {
#         'news_list': news_list,
#         "categories": categories,
#         "local_one": local_one,
#         "local_news": local_news
#     }
#
#     return render(request, 'news/home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['mahalliy_xabarlar'] = News.published.all().filter(category__name="Mahalliy").order_by('-publish_time')[:5]
        context['xorij_xabarlari'] = News.published.all().filter(category__name="Xorij").order_by('-publish_time')[:5]
        context['sport_xabarlari'] = News.published.all().filter(category__name="Sport").order_by('-publish_time')[:5]
        context['texnologiya_xabarlari'] = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[:5]
        return context


class ContactsPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            HttpResponse("<h1> Biz bilan boglaningiz uchun rahmat </h1>")
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news


class ForeignNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news

class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = 'texnologiya_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news