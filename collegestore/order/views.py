from django.contrib import messages
from django.shortcuts import render

from order.models import Order



from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import OrderCreationForm
from .models import Order
from a3h1collegestore.models import Course


def order_create_view(request):
    form = OrderCreationForm()
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "order created successfully")
            return redirect('order:order_create')
    return render(request, 'shop.html', {'form': form})



# # AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

