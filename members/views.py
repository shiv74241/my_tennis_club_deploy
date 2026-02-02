from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member  # at the time "display data-Prep Template and view. (student table )"
from .models import student
#from django.shortcuts import render # for home page formula
from django.db.models import Q  # only for "OR" FILTER COMMAND
from .models import ContactMessage  # for form details filled by customer
from django.core.paginator import Paginator


#def members(request):
 #   return HttpResponse("Hello world!")
def abouts(request):
    return HttpResponse("Hello world!2")

def members2(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

#def main(request):
 # template = loader.get_template('main.html')
  #return HttpResponse(template.render())

def home(request):
    return render(request, "main.html")


def testing(request):
  template = loader.get_template('template.html')
  mymembers = Member.objects.all().values()
  mydata = Member.objects.all()
  mydata2 = Member.objects.all()
  firstcolumnlists= Member.objects.values_list()
  firstcolumnlists1= Member.objects.values_list('firstname')
  filterlist= Member.objects.filter(firstname ='Emil').values()
  filterlist2= Member.objects.filter(firstname ='Emil', id=1).values()
  mymembers3 = Member.objects.all().values()
  filterlist3= Member.objects.filter(firstname = 'Emil').values() | Member.objects.filter(firstname = 'Linus').values()
  filterlist4= Member.objects.filter(Q(firstname = 'Emil') | Q(firstname = 'Linus')).values()
  mymembers6 = Member.objects.filter(firstname__startswith='L').values()
  orderby1 = Member.objects.all().order_by('firstname').values()
  orderby2 = Member.objects.all().order_by('-firstname').values()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'], 
    'firstname' : 'ShivKumarChauhan',
    'mymembers':mymembers,
    'greeting' : 1,
    'greetings' : 2,
    'day' : 'monday',
    'greetingss' : 6,
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
    'cars': [
      {'brand': 'Ford','model': 'Mustang','year': 1964,},
      {'brand': 'Ford','model': 'Bronco','year': 1970,},
      {'brand': 'Volvo','model':'P1800','year': 1964}
      ],
     'mydata' : mydata,
    'emptytestobject': [],
    'columns': firstcolumnlists,
    'columns1': firstcolumnlists1,
    'filterlist' : filterlist,
    'filterlist2' : filterlist2,
    'mydata2' : mydata2,
    'mymembers3' : mymembers3,
    'filterlist3' : filterlist3,
    'filterlist4' : filterlist4,
    'mymembers6' : mymembers6,
    'orderby1': orderby1,
    'orderby2': orderby2,

  }
  return HttpResponse(template.render(context, request))



def handle_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return HttpResponse("✅ Your message has been saved successfully!")
    
    return render(request, 'main.html')  


#def student_list(request):
 #   students = student.objects.all()
  #  messagess = ContactMessage.objects.all()
   # return render(request, "student_list.html", {
   #"students": students,
   #"messagess": messagess
   #})


def student_list(request):
    students = student.objects.all()
    messagess = ContactMessage.objects.all()
    messagess2 = ContactMessage.objects.all()

    # pagination for ContactMessage by 1-5Row Convertinto One page
    paginator1 = Paginator(messagess2, 5)   # ← now 5 records per page
    page_number = request.GET.get("page")
    page_obj1 = paginator1.get_page(page_number)


    return render(request, "student_list.html", {
        "students": students,
        "messagess": messagess,
        "page_obj1": page_obj1,   # send only one message
    })


def vest_products(request):
    return render(request, 'vest_products.html')

def payment_cod(request):
    product = request.GET.get('product')
    return render(request, 'payment_cod.html', {'product': product})

def payment_bank(request):
    product = request.GET.get('product')
    return render(request, 'payment_bank.html', {'product': product})


def upi_payment(request):
    return render(request, "pay.html")    
