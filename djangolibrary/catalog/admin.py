from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Author
from .models import Genre
from .models import Language
from .models import BookInstance


class BooksInLine(admin.TabularInline):
    model = Book


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInLine]


admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

    list_display = ('book', 'status', 'borrower', 'due_back')


# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)
