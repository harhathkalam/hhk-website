from django.shortcuts import render
from django.core.mail import EmailMessage

def homepage(request):
	return render(request,'index.html')

def stories_of_hope(request):
	return render(request,'stories-of-hope.html')

def our_programs(request):
	return render(request,'our-programs.html')

def about_us(request):
	return render(request,'about-us.html')
	
def connect_with_us(request):
	return render(request,'connect-with-us.html')

def contact(request):
	print("inside contact")
	if request.method == "POST":
		data=[request.POST["email"],request.POST["name"],request.POST["mobile"],request.POST["comment"]]
		send_mail_A(data)
		return render(request,'contact.html',{"data":1})
	return render(request,'contact.html',{"data":0})

def our_team(request):
	return render(request,'our-team.html')

def donation(request):
	return render(request,'donation.html')

def send_mail_A(data):
    print("Sending mail")
    msg = EmailMessage("Website Form Data",f"Someone Filled the online form \n Name:{data[1]} \n Email:{data[0]}, \n Phone No:{data[2]}, \n Comment:{data[3]}","Website Form",["info@harhathkalam.org"])
    msg.send()
    print("mail sent")
# Create your views here.
