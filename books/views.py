from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBookForm, EditBookForm, AddComment
from django.views.generic import TemplateView
from .models import Books, BookCheckout
from django.utils import timezone
import datetime


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

        #template_name = 'users/homepage.html'
        CB_form = CreateBookForm(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if CB_form.is_valid():
            create_book = CB_form.save(commit=False)
            create_book.owner = request.user            
            CB_form.save()
            return redirect('users:homepage')
        else:
            return redirect('users:homepage')

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

            UB_form = EditBookForm(request.POST, request.FILES, instance=book_data, initial=initial_data)
            context = {
                'book_data': book_data,
                'UB_form': UB_form,
                'pk': kwargs.get('pk'),
            }

            if UB_form.is_valid():
                update_book = UB_form.save(commit=False)
                update_book.save()
                return render(request, template_name, context)
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


class BookCommentView(TemplateView):

    def post(request, *args, **kwargs):

        CC_form = AddComment(request.POST)
        # import pdb; pdb.set_trace()
        if CC_form.is_valid():
            book_data = get_object_or_404(Books, pk=kwargs.get('pk'))        
            create_comment = CC_form.save(commit=False)
            create_comment.user = request.user
            create_comment.book_comment = book_data
            create_comment.save()
            return redirect('users:homepage')
        else:
            return redirect('users:homepage')


class BookCheckoutViews(TemplateView):

    def post(request, *args, **kwargs):
                    
            # import pdb; pdb.set_trace()                    
            book_data = Books.objects.get(pk=kwargs.get('pk'))
            book_data.status = 'checkedout'
            checkout = BookCheckout.objects.create(book_checkout=book_data, borrower=request.user)              
            book_data.save()
            checkout.save()
            return redirect('users:homepage')


class ReturnBookView(TemplateView):

    def post(request, *args, **kwargs):

        import pdb; pdb.set_trace()
        book_data = Books.objects.get(pk=kwargs.get('pk'))        
        book_data.status = 'available'
        checkout = BookCheckout.objects.get(book_checkout=book_data, borrower=request.user)                                
        checkout.return_date = datetime.datetime.now(tz=timezone.utc)
        checkout.is_returned = 'True'
        book_data.save()
        checkout.save()
        return redirect('users:borrowedbooks', request.user.id)


class SearchBookView(TemplateView):

    def post(request, *args, **kwargs):

        if request.user.is_authenticated:
            query = request.POST.get('bookSearch')
            search = Books.objects.filter(title__icontains=query)
            return render(request, 'books/search.html', {'search': search})
        else:
            return redirect('users:login')
        

