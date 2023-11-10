from django import template
from home.models import Contact

register = template.Library()

@register.simple_tag
def total_contacts():
    return Contact.objects.count()

@register.inclusion_tag('contacts_list.html')
def contact_list():
    contacts = Contact.objects.all()
    return {'contacts': contacts}