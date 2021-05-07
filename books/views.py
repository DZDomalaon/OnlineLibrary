from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBookForm, EditBookForm
from django.views.generic import TemplateView
from .models import Books


class BookView(TemplateView):
    
    def get(request, *args, **kwargs):

        if request.user.is_authenticated:
            book_page = get_object_or_404(Books, pk=kwargs.get('pk'))
            context = {
                    #'form': form, 
                    'book_page': book_page, 
                    #'post_comment': post_comment,
            }
            return render(request, "books/book_page.html",  context)
        else:
            return render(request, "books/book_page.html",  context)

    def post(request, *args, **kwargs):

        template_name = 'books/create_book.html'
        CB_form = CreateBookForm(request.POST, request.FILES)
        if CB_form.is_valid():
            create_book = CB_form.save(commit=False)
            create_book.owner = request.user            
            CB_form.save()
            return redirect('users:homepage')
        else:
            return render(request, template_name, {'CB_form':CB_form})

    def update_book(request, *args, **kwargs):

        template_name = 'books/edit_book.html'

        if request.user.is_authenticated:
            book_data = get_object_or_404(Books, pk=kwargs.get('pk'))

            initial_data = {
                'title' : book_data.title,
                'author': book_data.author,
                'location': book_data.location,
                'book_image': book_data.book_image,
                'is_digital': book_data.is_digital,
            }
            UB_form = EditBookForm(request.POST or None, request.FILES, instance=book_data, initial=initial_data)
            context = {
                'book_data': book_data,
                'UB_form': UB_form,
            }
            if UB_form.is_valid():
                update_book = UB_form.save(commit=False)
                update_book.save()
                return redirect('books:bookpage', kwargs.get('pk'))
            else:
                UB_form = EditBookForm(request.POST, initial=initial_data)
                return render(request, template_name, context)
        else:
            redirect('users:login')

    def delete(request, *args, **kwargs):

        if request.user.is_authenticated:
            book = get_object_or_404(Books, pk=kwargs.get('pk'))
            if request.user == book.owner:
                book.delete()
                return redirect('users:homepage')
        else:
            return redirect('users:login')

