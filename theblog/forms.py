from django import forms
from .models import Post, Category, Ingredient

# food_category_choices = [('dessert',), ('pasta'), ('pizza'), ('salad')] -> choices comes first from the attrs
food_category_choices = Category.objects.all().values_list(
    'name', 'name')  # query to get the names of category model
ingredient_category_choices = Ingredient.objects.all().values_list(
    'name', 'name')  # query to get the names of ingredient model

foods = []
for food in food_category_choices:
    foods.append(food)

ingredients = []
for ingredient in ingredients:
    ingredients.append(ingredient)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'body', 'image', 'ingredients')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'post_author_id', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=foods, attrs={'class': 'form-control'}),
            'ingredients': forms.SelectMultiple(choices=ingredients, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Put your post in here..'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'ingredients': forms.SelectMultiple(choices=ingredients, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'PostBody'})
        }
