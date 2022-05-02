from django.utils.translation import ugettext_lazy as _

ENGLISH, SPANISH = 'en', 'es'
LANGUAJES_CHOICES = (
    (ENGLISH, _("English")),
    (SPANISH, _("Spanish"))
)

MODERN, SIMPLE = 'Modern', 'Simple'
CURRICULUM_CHOICES = (
    (MODERN, _("Modern")),
    (SIMPLE, _("Simple"))
)