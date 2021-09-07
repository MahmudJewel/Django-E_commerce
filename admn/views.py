from django.shortcuts import render

from customer import models as CMODEL

# Create your views here.

def dashboard_view(request):
	context={
    'total_customer':CMODEL.Customer.objects.all().count(),
    #'total_teacher':TMODEL.Teacher.objects.all().filter(status=True).count(),
    #'total_course':models.Course.objects.all().count(),
    #'total_question':models.Question.objects.all().count(),
    }
	return render(request, 'admn/admin_dashboard.html', context)


def admin_customer_side_var(request):
	customers=CMODEL.Customer.objects.all()
	context={
		'customers': customers
	}
	return render(request, 'admn/admin-customer-side.html',context)

def update_customer_view(request, pk):
	return render(request,'admn/update-customer.html')

def delete_customer_view(request, pk):
	return render(request,'admn/update-customer.html')