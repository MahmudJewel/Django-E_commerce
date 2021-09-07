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
	return render(request, 'admn/admin-customer-side.html')