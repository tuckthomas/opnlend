from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class OpnLendHomePage(Page):
    header_text = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('header_text'),
    ]
