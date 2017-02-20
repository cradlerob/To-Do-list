from django.shortcuts import render,redirect

from lists.models import List,Item

from lists.forms import ItemForm,EditItemForm,ListForm

from django.http import HttpResponseRedirect


def home_page(request):
    lists = List.objects.all()
    form = ListForm()
    return render(request, 'home.html', { 'lists' : lists, 'form' : form})


def view_list(request, pk):
    list_=List.objects.get(pk=pk)
    items = Item.objects.filter(list = list_).order_by('id')
    return render(request, 'list.html', {'lists': items , 'tittle' : list_.name , 'primary' : list_.id })


def new_list(request):
    status = 'Error'
    if request.method == 'POST':
        form = ListForm( data=request.POST )
        if form.is_valid():
            form.save()
            status='Guardado Con exito'
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        form = ListForm()
    return render(request, 'home.html', {"form": form, 'status' : status })


def edit_item_list(request,pk):
    item = Item.objects.get(pk=pk)
    list=item.list
    if request.method=='POST':
        form=EditItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/lists/' + str(list.id) + '/view/')
    else:
        form=EditItemForm(instance=item)
    return render(request,'additem.html',{'form':form , 'function' : 'Edit'})


def delete_item_list(request,pk):
    item = Item.objects.get(pk=pk)
    list =item.list
    item.delete()
    return redirect('/lists/'+str(list.id)+'/view/')

def add_item(request,pk):
    list_ = List.objects.get(pk=pk)
    if request.method=='POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            item = Item(list=list_)
            item.save()
            item.text_item=form.cleaned_data['text_item']
            #item= Item.objects.create(
             #   text=form.cleaned_data['text'],
              #  list=list_,
            #)
            item.save()
            return redirect('/lists/'+pk+'/view/')
    else:
        print('else')
        form=ItemForm()
    return render(request, 'addItem.html', {'form': form, 'function': 'Add'})


def delete_list(request,pk):

    list = List.objects.get(pk=pk)
    list.delete()

    return redirect('/')

