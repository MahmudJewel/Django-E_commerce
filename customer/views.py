from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages

from customer import forms as CFORM
from customer import models as CMODEL

# Create your views here.
def customerSignup(request):
	RegisterForm = CFORM.RegisterForm()
	if request.method == 'POST':
		RegisterForm = CFORM.RegisterForm(request.POST)
		if RegisterForm.is_valid():
			customer=RegisterForm.save()
			customer_group=Group.objects.get_or_create(name='CUSTOMER')
			customer_group[0].user_set.add(customer)
			username=RegisterForm.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}")
			return redirect('login')
		#return redirect('login')
			
	context={
		'RegisterForm': RegisterForm,
	}
	return render(request, 'customer/signup.html',context)

def upadate_profile_view(request, pk):
	'''
	user=CMODEL.User.objects.get(id=pk)
	customer=CMODEL.Customer.objects.get(id=pk)
	userForm=CFORM.EditForm(instance=user)
	customerForm = CFORM.customerForm(instance=customer)
	'''
	
	userForm=CFORM.EditForm(instance = request.user)
	customerForm = CFORM.customerForm(instance=request.user.profile)

	if request.method == 'POST':
		userForm=CFORM.EditForm(request.POST, instance=request.user)
		customerForm = CFORM.customerForm(request.POST, request.FILES, instance=request.user.profile) #profile is onetoonefield name
		#print(f"user id ={request.user.id} and profile id={request.user.profile.id}")
		#print(f"user ={request.user} and profile ={request.user.profile}")
		if userForm.is_valid() and customerForm.is_valid():
			userForm.save()
			customerForm.save()
			messages.success(request, f"Account has been updated")
			return redirect('/')
	context={
		'userForm':userForm,
		'customerForm':customerForm
	}

	return render(request,'customer/profile.html', context)