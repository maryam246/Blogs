from django.contrib import admin
from .models import Category,Post

# for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_image','title','description','url','pic','add_date')
    search_fields = ('title',)

# for configuration of Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js =('https://cdn.tiny.cloud/1/1avrqcnzti489854ljs6dhrkanmkiqubuhe9l1ijbl0mu0bq/tinymce/5/tinymce.min.js','js/script.js',)
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)