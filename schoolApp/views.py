from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from . models import *



#Index views

def indexView(request):
    context = {
        'sitters_count': Sitter.objects.count(),
        'babies_count': Baby.objects.count(),
        'products_count': Product.objects.count(),
        'transactions_count': Transaction.objects.count(),
        'babies': Baby.objects.all(),        
        'products': Product.objects.all(),

    }
    return render(request, 'index.html', context)

def landingView(request):
    return render(request, 'registrations/landing.html')


#Sitter views

def addSitter(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        nin_number = request.POST['nin_number']
        religion = request.POST['religion']
        education_level = request.POST['education_level']
        sitter_number = request.POST['sitter_number']
        contact = request.POST['contact']
        is_active = request.POST['is_active']
        new_sitter = Sitter.objects.create(
            name = name,
            location = location,
            date_of_birth = date_of_birth,
            gender = gender,
            nin_no = nin_number,
            religion = religion,
            education_level = education_level,
            sitter_number = sitter_number,
            is_active = is_active,
            contact = contact
        )
        new_sitter.save()
        return redirect(reverse('list_sitters'))
    else:
        return render(request, 'sitters/addSitter.html', {'sitter': Sitter})



def editSitter(request, id):
    sitter = Sitter.objects.get(id=id)
    if request.method == 'POST':
        sitter.name = request.POST.get('name')
        sitter.location = request.POST.get('location')
        sitter.date_of_birth = request.POST.get('date_of_birth')
        sitter.gender = request.POST.get('gender')
        sitter.nin_no = request.POST.get('nin_no')
        sitter.religion = request.POST.get('religion')
        sitter.education_level = request.POST.get('education_level')
        sitter.sitter_number = request.POST.get('sitter_number')
        sitter.contact = request.POST.get('contact')
        sitter.save()
        return redirect(reverse('list_sitters'))
    else:
        sitter = Sitter.objects.get(id=id)
        return render(request, 'sitters/editSitter.html', {'sitter': sitter})


def listSitters(request):
    sitters = Sitter.objects.all()
    return render(request, 'sitters/listSitters.html', {'sitters': sitters})


def viewSitter(request, id):
    sitter = Sitter.objects.get(id=id)
    return render(request, 'sitters/viewSitter.html', {'sitter': sitter}) 



def deleteSitter(request, id):
    sitter = Sitter.objects.get(id=id)
    sitter.delete()
    return redirect(reverse('listSitters'))

#Baby views

def addBaby(request):
    if request.method == 'POST':
        sitter_id = request.POST['sitter']
        sitter = Sitter.objects.get(id=sitter_id)      

        new_baby = Baby.objects.create(
            name=request.POST['name'],
            gender=request.POST['gender'],
            dob=request.POST['dob'],
            location=request.POST['location'],
            parent_name=request.POST['parent_name'],        
            baby_number=request.POST['baby_number'],
            sitter=sitter

        )

        new_baby.save()
        messages.success(request, 'Baby added successfully.')
        return redirect(reverse('list_babies'))

    else:
        sitters = Sitter.objects.all()
        return render(request, 'baby/addBaby.html', {'sitters': sitters})





def editBaby(request, id):
    baby = Baby.objects.get(id=id)
    sitters = Sitter.objects.all()
    if request.method == 'POST':
        baby.name = request.POST.get('name')
        baby.gender = request.POST.get('gender')
        baby.dob = request.POST.get('dob')
        baby.location = request.POST.get('location')
        baby.parent_name = request.POST.get('parent_name')        
        baby.baby_number = request.POST.get('baby_number')
        baby.sitter_id = request.POST.get('sitter')
        baby.save()
        return redirect(reverse('list_babies'))
    else:
        baby = Baby.objects.get(id=id)
        return render(request, 'baby/editBaby.html', {'baby': baby, 'sitters': sitters})


def listBabies(request):
    babies = Baby.objects.all()
    return render(request, 'baby/listBabies.html', {'babies': babies})

def viewBaby(request, id):
    baby = Baby.objects.get(id=id)
    return render(request, 'baby/viewBaby.html', {'baby': baby})

def deleteBaby(request, id):
    baby = Baby.objects.get(id=id)
    baby.delete()
    return redirect(request, 'baby/listBabies.html')


#Attendance views

def addAttendance(request):
    babies = Baby.objects.all()
    if request.method == 'POST':
        baby_id = request.POST['baby']
        baby = Baby.objects.get(id=baby_id)        
        
        new_attendance = Attendance.objects.create(
            Baby= baby,
            brought_by = request.POST['brought_by'],
            fee_amount = request.POST['fee_amount'],
            period_of_stay = request.POST['period_of_stay'],
            date = request.POST['date'],
            
        )
        new_attendance.save()
        return redirect(reverse('list_attendance'))
    else:
        return render(request, 'attendance/addAttendance.html', {'babies': babies})
        
    

def listAttendances(request):
    all_attendances = Attendance.objects.all()
    context = {
        'all_attendances': all_attendances
    }
    return render(request, 'attendance/attendancelist.html', context)

def deleteAttendance(request, id):
    Attendance.objects.get(id=id).delete()
    return redirect(reverse('list_attendance'))
    


#Product views
def addProduct(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        unit_price = request.POST['unit_price']

        new_product = Product.objects.create(
            name = name,
            description = description,
            unit_price = unit_price
        )
        return redirect(reverse('list_products'))
    else:
        return render(request, 'Products/addProduct.html')


def listProducts(request):
    products = Product.objects.all()
    products_count = Product.objects.all().count
    context = {
        'products': products,
        'products_count': products_count

    }
    return render(request, 'Products/listProducts.html', context)



def deleteProduct(request,id ):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(reverse('list_products'))

#Transaction views

def addTransaction(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        baby_id = request.POST['baby']
        quantity = request.POST['quantity']
        unit_price = request.POST['unit_price']
        total_price = request.POST['total_price']
        kind = request.POST['kind']
        date = request.POST['date']

        product = Product.objects.get(id=product_id)
        baby = Baby.objects.get(id=baby_id)

        total_price = product.unit_price * quantity

        #Vat calculation
        vat_rate = 0.18
        vat_amount = total_price * vat_rate

        #Discount calculation
        discount_amount = 10.0

        #Profit calculation
        profit_margin = total_price - (product.unit_price * quantity)

        #Net profit calculation
        net_profit = total_price - vat_amount - discount_amount

        #Number of transactions
        transaction_count = Transaction.objects.count()

        new_transaction = Transaction.objects.create(
            product=product,
            baby=baby,
            quantity=quantity,
            unit_price=unit_price,
            total_price=total_price,
            kind=kind,
            date=date,
            vat_amount=vat_amount,
            discount_amount=discount_amount,
            profit_margin=profit_margin,
            net_profit=net_profit,
            transaction_count=transaction_count
        )
        new_transaction.save()
        return redirect(reverse('list_transactions'))
    else:
        return render(request, 'transactions/addTransaction.html', {'products': Product.objects.all(), 'babies': Baby.objects.all()})



def listTransactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/listTransactions.html', {'transactions': transactions})


def deleteTransaction(request, id):
    transaction = Transaction.objects.get(id=id)
    transaction.delete()
    return redirect(reverse('list_transactions'))


# Admin Registration view

def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect(reverse('register'))

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect(reverse('register'))
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect(reverse('logon'))

    else:
        return render(request, 'registrations/register.html')

# 

#Administrator Login view
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect(reverse('logon'))

    return render(request, 'registrations/logon.html')


# Administrator Logout
def logoutView(request):
    logout(request)
    return redirect('/')

# Report views

def reports(request):
    return render(request, 'reports/report.html')

def sign_in(request):
    return render(request, 'registrations/sign_in.html')

