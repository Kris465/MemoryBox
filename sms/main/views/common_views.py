from django.shortcuts import render
from django.views import View
from main.models import AboutPage, ContactPage


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class AboutView(View):
    def get(self, request):
        about_text = AboutPage.objects.first() or AboutPage.objects.create(
            about="Текст по умолчанию")
        return render(request, 'about.html', {'about_details': about_text})


class ContactView(View):
    def get(self, request):
        contact_text = ContactPage.objects.first() or ContactPage.objects.create(
            address="Ваш адрес",
            email="your@email.com",
            contact_num=1234567890
        )
        return render(request, 'contact.html',
                      {'contact_details': contact_text})
