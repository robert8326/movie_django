from django.shortcuts import render
from django.views.generic import CreateView

from contact.forms import ContactForm
from contact.models import Contact
from movies.service import send


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'movies/movie_list.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        print(form)
        print(form.instance.email)
        return super().form_valid(form)
