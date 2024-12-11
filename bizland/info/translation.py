from modeltranslation.translator import translator,register,TranslationOptions
from .models import *


@register(TeamMember)
class SliderTranslationOptions(TranslationOptions):
    fields = ('name','position')


@register(Service)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title','description')


@register(ServiceDetail)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title','description')


@register(PortfolioItem)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title','description')


@register(FAQ)
class SliderTranslationOptions(TranslationOptions):
    fields = ('question','answer')


