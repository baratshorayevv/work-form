from django.shortcuts import render
from online_shop import views
from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

# Create your views here.


def product_list(request):
    return render(request, template_name= 'online_shop/home.html')


from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user  # Agar foydalanuvchi modelidan foydalanayotgan bo'lsangiz
            order.save()
            return redirect('order_success')  # Yangi buyurtma qo'shilgandan keyin qayerga yo'naltirish
    else:
        form = OrderForm()

    return render(request, 'online_shop/add_order.html', {'form': form})
