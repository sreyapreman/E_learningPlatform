from django.shortcuts import render
from django.views.generic import TemplateView

class ChatBotView(TemplateView):
    template_name="chatbot.html"
