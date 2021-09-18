from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from customer import models as CMODEL
#from customer import forms as CFORM

# Create your views here.

def dashboard_view(request):
	context={
    #'total_customer':CMODEL.Customer.objects.all().count(),
    #'total_teacher':TMODEL.Teacher.objects.all().filter(status=True).count(),
    #'total_course':models.Course.objects.all().count(),
    #'total_question':models.Question.objects.all().count(),
    }
	return render(request, 'admn/admin_dashboard.html', context)


#======================= Start Admin-Customer ===============================
def admin_customer_side_var(request):
	context={
		'total_customer':CMODEL.Customer.objects.all().count(),
	}
	return render(request, 'admn/admin-customer-side.html',context)



def customer_list_view(request):
	customers=CMODEL.Customer.objects.all()
	context={
		'customers': customers
	}
	return render(request, 'admn/customer-list.html',context)


def update_customer_view(request, pk):
	'''
	customer=CMODEL.Customer.objects.get(id=pk)
	user=CMODEL.User.objects.get(id=customer.user_id)
	#print('user is: ', user)
	#print('password: ', user.first_name, user.password)
	userForm = CFORM.UserForm(instance=user)
	customerForm = CFORM.CustomerForm(instance=customer)
	if request.method == 'POST':
		userForm = CFORM.UserForm(request.POST, instance=user)
		customerForm = CFORM.CustomerForm(request.POST,request.FILES, instance=customer)
		if customerForm.is_valid:
			userForm.save()
			user.set_password(user.password)
			user.save()
			customerForm.save()
			return redirect('customer-list')
	context={
		'userForm' : userForm,
		'customerForm': customerForm,
		'customer':customer,
		'user' : user,
	}
	'''
	return render(request,'admn/update-customer.html',context)



def delete_customer_view(request, pk):
	return render(request,'admn/update-customer.html')

#======================= End Admin-Customer ===============================
