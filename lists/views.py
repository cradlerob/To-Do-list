from django.shortcuts import render,redirect

from lists.models import List,Item

from lists.forms import ItemForm,EditItemForm,ListForm

from django.http import HttpResponseRedirect


def home_page(request):
    lists = List.objects.all()
    form = ListForm()
    return render(request, 'home.html', { 'lists' : lists, 'form' : form})


def view_list(request, pk):
    form = ItemForm()
    list_=List.objects.get(pk=pk)
    name=list_.name
    items = Item.objects.filter(list = list_)
    return render(request, 'list.html', {'list': items , 'tittle' : name ,'form' : form })


def new_list(request):
    status = 'Error'
    if request.method == 'POST':
        form = ListForm( data=request.POST )
        if form.is_valid():
            form.save()
            status='Guardado Con exito'
            url(r'^new$', views.new_list, name='new_list'),

    else:
        form = ListForm()
    return render(request, 'home.html', {"form": form, 'status' : status })


def edit_item_list(request,pk):
    item = Item.objects.get(pk=pk)
    if request.method=='POST':
        form=EditItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form=EditItemForm(instance=item)
    return render(request,'list.html',{'form':form , 'tittle' : item.list.name})


def delete_item_list(request,pk):
    item = Item.object.get(pk)
    list =item.list
    item.delete()
    return redirect('/lists/'+list.id+'/view')

def add_item(request,pk):
    list_ = List.objects.get(pk=pk)
    print(request.method)
    if request.method=='POST':
        print('post')

        form=ItemForm(request.POST)
        if form.is_valid():
            print('valid')
            item_text = request.POST.get('text', '')
            item= Item.objects.create(
                text=item_text,
                list=list_,
            )
            item.save()
            print ('save')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form=ItemForm()
    return render(request,'list.html',{'form':form,'tittle':list_.name})
