from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipt
from django.contrib.auth.decorators import login_required
from .forms import NewReceiptForm, EditReceiptForm

## CRUD Operations views ##
@login_required
def new(request):
    if request.method == 'POST':
        form = NewReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            Receipt = form.save(commit=False)
            Receipt.created_by = request.user
            Receipt.save()
            return redirect('receipts:detail', pk=Receipt.id)
    else:
        form = NewReceiptForm()

    return render(request, 'receipts/form.html', {
        'form':form,
        'title':'New Receipt',
    })

@login_required
def edit(request,pk):
    receipt = get_object_or_404(Receipt, pk=pk, created_by = request.user)
    if request.method == 'POST':
        form = EditReceiptForm(request.POST, request.FILES, instance=receipt)
        if form.is_valid():
            receipt.save()
            return redirect('receipts:detail', pk=receipt.id)
    else:
        form = EditReceiptForm(instance=receipt)

    return render(request, 'receipts/form.html', {
        'form':form,
        'title':'Edit Receipt',
    })

@login_required
def delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk, created_by = request.user)
    receipt.delete()

    return redirect('receipts:list')

## READ views ##
@login_required
def ListReceipts(request):
    receipts = Receipt.objects.filter(created_by=request.user)

    return render(request, 'receipts/index.html', {'receipts': receipts})

@login_required
def DetailReceipt(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)

    return render(request, 'receipts/detail.html', {'receipt': receipt})

