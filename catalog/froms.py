from django.forms import ModelForm, BooleanField
from .models import Product
from django.core.exceptions import ValidationError


ban_words = ['криптовалюта', 'крипта', 'бесплатно', 'радар', 'полиция', 'дешево', 'обман', 'биржа']

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'



class ProductsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("names", "description", "price", "group", "image")

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('names')
        description = cleaned_data.get('description')

        if any(word in name.lower() for word in ban_words) or any(
                word in description.lower() for word in ban_words):
            raise ValidationError('Слово это запрещено тута!')

        return cleaned_data


    def clean_price(self):

        cleaned_data = super().clean()
        price = cleaned_data.get('price')

        if price < 1:
           raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_photo(self):
        image = self.cleaned_data.get('image')


        if image:
            if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
                raise ValidationError('Только JPEG или PNG.')


            if image.size > 5 * 1024 * 1024:  # 5 МБ
                raise ValidationError('Размер файла не выше 5 МБ.')

        return image



class ProductsModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("status_publication", )

