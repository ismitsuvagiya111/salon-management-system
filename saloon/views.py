from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.
# --------------------------------Login Page--------------------------------
def login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pas=request.POST.get('password')
        admins=Admin.objects.filter(a_email=un,a_password=pas)
        cnt=0
        for a in admins:
            cnt=cnt+1
            request.session['admin']=a.a_email
            return redirect('/master/')            
    return render(request,'index.html')
# --------------------------------Home Page--------------------------------
def page(request):
    return render(request,'Homepage/index.html')
def about(request):
    return render(request,'Homepage/about.html')
def contact(request):
    return render(request,'Homepage/contact.html')
def shop(request):
    prod=Product.objects.all()
    return render(request,'Homepage/shop.html',{'products':prod})
def shopdetail(request,id):
    proddetail=ProductDetails.objects.filter(p=id)
    return render(request,'Homepage/shopdetails.html',{'products':proddetail})
def cart(request):
    if request.session.has_key('customer'):
        pass
    else:
        return redirect('/customerlogin/')
    cid=request.session.get('customer')
    customer=Customer.objects.get(c_id=cid)
    cart=Cart.objects.filter(c=customer)
    return render(request,'Homepage/cart.html',{'products':cart})

def ShopDetails(request):
    prod=ProductDetails.objects.all()
    return render(request,'Homepage/ShopDetails.html',{'products':prod})

def shopdescription(request):
    return render(request,'Homepage/ShopDescription.html')
def Sign(request):
    if request.session.has_key('customer'):
        pass
    else:
        return redirect('/customerlogin/')
    return render(request,'Homepage/signup.html')
def appointments(request):
    service=Service.objects.all()
    package=Package.objects.all()
    return render(request,'Homepage/appointment.html',{'services':service,'packs':package})


def shop_single(request,id):    
    prod=ProductDetails.objects.get(pd_id=id)
    return render(request,'Homepage/shop-single.html',{'product':prod})

def service(request):
    srv=Service.objects.all()
    return render(request,'Homepage/service.html',{'service':srv})
def Deshboard(request):
    if request.session.has_key('customer'):
        pass
    else:
            return redirect('/customerlogin/')
    return render(request,'Deshboard.html')
def customerlogin(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pas=request.POST.get('password')
        customers=Customer.objects.filter(c_email=un,c_password=pas)
        cnt=0
        for a in customers:
            cnt=cnt+1
            request.session['customer']=a.c_id
            return redirect('/')            
    return render(request,'Homepage/CustmerLogin.html')
def profile(request):
    if request.session.has_key('customer'):
        pass
    else:
        return redirect('/customerlogin/')
    cid=request.session.get('customer')#aama session mathi id lai ne aavi gaya
    customer=Customer.objects.get(c_id=cid)
    return render(request,"Homepage/profile.html",{'customer':customer})
def addtocart(request):
    if request.session.has_key('customer'):
        pass
    else:
        return redirect('/customerlogin/')
    cid=request.session.get('customer')
    customer=Customer.objects.get(c_id=cid)
    
    podid=request.POST.get('productid')
    pod=ProductDetails.objects.get(pd_id=podid)
    qty=request.POST.get('qty')
    rate=request.POST.get('rate')
    save=Cart(c=customer,pd=pod,cart_quntity=qty,cart_rate=rate) 
    save.save()
    return redirect('/cart/')   
def packges(request):
    pack=Package.objects.all()
    return render(request , 'Homepage/Package.html',{"packs":pack})
def serapoo(request,id):
    service=Service.objects.get(s_id=id)
    return render(request , 'Homepage/SerAppo.html',{"services":service})
def packgesappo(request):
    pack=Package.objects.all()
    return render(request , 'Homepage/PackAppo.html',{"packs":pack})
def serapposave(request):
    date=request.POST.get('date')
    price=request.POST.get('price')
    cid=request.session.get('customer')
    serviceid=request.POST.get('serviceid')
    cust=Customer.objects.get(c_id=cid)
    sers=Service.objects.get(s_id=serviceid)
    
    save=Appointment(c=cust,s=sers,a_rate=sers.s_price,a_datetime=date,a_status='Pending ')
    save.save()
    return redirect('/shop/')

def order(request):
    order=SalesOrder.objects.all()
    return render(request,'Homepage/order.html',{'sales':order})
        
# --------------------------------Appointment Table--------------------------------
def appointment(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    appos=Appointment.objects.all()
    return render(request,'Appointment/Appointmentlist.html',{'appointments':appos})
def Appointmentadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    customers=Customer.objects.all()
    service=Service.objects.all()
    package=Package.objects.all()
    return render(request,'Appointment/AppointmentAdd.html',{'customers':customers,'services':service,'packs':package})
def Appointmentsave(request):
    adatetime=request.POST.get('adatetime')
    arate=request.POST.get('arate')
    adisc=request.POST.get('adisc')
    astat=request.POST.get('astat')
    cid=request.POST.get('cid')
    cust=Customer.objects.get(c_id=cid)
    sid=request.POST.get('sid')
    sers=Service.objects.get(s_id=sid)
    pckid=request.POST.get('pckid')
    pack=Package.objects.get(pkg_id=pckid)
    service=Appointment(a_datetime=adatetime,a_rate=arate,a_discount=adisc,a_status=astat,c=cust,s=sers,pkg=pack)
    service.save()
    return redirect('/appointmentlist/')
def appodel(request,id):
    appo=Appointment.objects.get(a_id=id)
    appo.delete()
    return redirect('/appointmentlist/')
def appoedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    customers=Customer.objects.all()
    service=Service.objects.all()
    package=Package.objects.all()
    appo=Appointment.objects.get(a_id=id)
    return render(request,'Appointment/AppointmentEdit.html/',{'appointment':appo,'customers':customers,'services':service,'packs':package})
def appoupdate(request,id):
    adatetime=request.POST.get('adatetime')
    arate=request.POST.get('arate')
    adisc=request.POST.get('adisc')
    astat=request.POST.get('astat')
    cid=request.POST.get('cid')
    cust=Customer.objects.get(c_id=cid)
    sid=request.POST.get('sid')
    sers=Service.objects.get(s_id=sid)
    pckid=request.POST.get('pckid')
    pack=Package.objects.get(pkg_id=pckid)
    service=Appointment(a_id=id,a_datetime=adatetime,a_rate=arate,a_discount=adisc,a_status=astat,c=cust,s=sers,pkg=pack)
    service.save()
    
    return redirect('/appointmentlist/')

# --------------------------------Brand Table-------------------------------------------------------------------
def brandlist(request):
    if request.session.has_key('admin'):
        pass
    else:
            return redirect('/login/')
    sers=Brand.objects.all()
    return render(request,'brand/brandlist.html',{'brands':sers})
def brandadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request,'brand/brandadd.html')
def brandsave(request):
    sname=request.POST.get('sname')
    service=Brand(b_name=sname,)
    service.save()
    return redirect('/brandlist/')
def branddel(request,id):
    brand=Brand.objects.get(b_id=id)
    brand.delete()
    return redirect('/brandlist/')
def brandedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    brand=Brand.objects.get(b_id=id)
    return render(request,'brand/brandedit.html',{'brand':brand})
def brandupdate(request,id):
    sname=request.POST.get('sname')
    brand=Brand.objects.get(b_id=id)
    brand.b_name=sname
    brand.save()
    return redirect('/brandlist/')

# --------------------------------Category Table-------------------------------------------------------------------
def categorylist(request):
    if request.session.has_key('admin'):
        pass
    else:
            return redirect('/login/')
    categorys=Category.objects.all()
    return render(request,'category/categorylist.html',{'categorys':categorys})
def categoryadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request,'category/categotyadd.html')
def categorysave(request):
    cname=request.POST.get('cname')
    category=Category(c_name=cname,)
    category.save()
    return redirect('/categorylist/')
def categorydel(request,id):
    category=Category.objects.get(c_id=id)
    category.delete()
    return redirect('/categorylist/')
def categoryedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    category=Category.objects.get(c_id=id)
    return render(request,'category/categoryedit.html',{'category':category})
def categoryupdate(request,id):
    cname=request.POST.get('cname')
    category=Category.objects.get(c_id=id)
    category.c_name=cname
    category.save()
    return redirect('/categorylist/')

# --------------------------------Customer Table-------------------------------------------------------------------
def customerlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    customers=Customer.objects.all()
    return render(request,'customer/customerlist.html',{'customers':customers})
def customeradd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request,'customer/customeradd.html')
def customersave(request):
    cname=request.POST.get('cname')
    cage=request.POST.get('cage')
    ccontect=request.POST.get('ccontect')
    cgen=request.POST.get('cgen')
    cemail=request.POST.get('cemail')
    cpass=request.POST.get('cpass')
    caddress=request.POST.get('caddress')

    pimage=request.FILES['cimage']
    fss=FileSystemStorage()
    file=fss.save(pimage.name,pimage)
    file_url=fss.url(file)

    cust=Customer(c_name=cname,c_age=cage,c_contact=ccontect,c_gender=cgen,c_email=cemail,c_password=cpass,c_address=caddress,c_image=file_url)
    cust.save()
    return redirect('/customerlist/')
def customerdel(request,id):
    cust=Customer.objects.get(c_id=id)
    cust.delete()
    return redirect('/customerlist/')
def customeredit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    customer=Customer.objects.get(c_id=id)
    return render(request,'customer/customeredit.html',{'customer':customer})
def custupdate(request,id):
    cname=request.POST.get('cname')
    cage=request.POST.get('cage')
    ccon=request.POST.get('ccontect')
    cgen=request.POST.get('cgen')
    cemail=request.POST.get('cemail')
    cpass=request.POST.get('cpass')
    cadd=request.POST.get('caddress')
    
    if len(request.FILES)>0:
        pimage=request.FILES['cimage']
        fss=FileSystemStorage()
        file=fss.save(pimage.name,pimage)
        file_url=fss.url(file)
    else:
        file_url=request.POST.get('oldimage')
    
    cust=Customer(c_id=id,c_name=cname,c_age=cage,c_contact=ccon,c_gender=cgen,c_email=cemail,c_password=cpass,c_address=cadd,c_image=file_url)
    cust.save()
    return redirect('/customerlist/')


# --------------------------------Employee Table-------------------------------------------------------------------
def emplist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    emps=Employee.objects.all()
    return render(request,'employee/employeelist.html',{'employees':emps})
def empadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request,'employee/employeeAdd.html')
def empsave(request):
    ename=request.POST.get('ename')
    egen=request.POST.get('egen')
    econtect=request.POST.get('econtect')
    eemail=request.POST.get('email')
    epass=request.POST.get('epass')
    eaddress=request.POST.get('eaddress')
    esalary=request.POST.get('esalary') 

    pimage=request.FILES['eimage']
    fss=FileSystemStorage()
    file=fss.save(pimage.name,pimage)
    file_url=fss.url(file)

    emp=Employee(e_name=ename,e_gender=egen,e_contact=econtect,e_eamil=eemail,e_password=epass,e_address=eaddress,e_salary=esalary,e_image=file_url)
    emp.save()
    return redirect('/emplist/')
def employeedel(request,id):
    emp=Employee.objects.get(e_id=id)
    emp.delete()
    return redirect('/emplist/')
def empedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    
    employee=Employee.objects.get(e_id=id)
    return render(request,'employee/employeeedit.html',{'employee':employee})
def empupdate(request,id):
    ename=request.POST.get('ename')
    egen=request.POST.get('egen')
    econ=request.POST.get('econtect')
    eemail=request.POST.get('eemail')
    epass=request.POST.get('epass')
    eadd=request.POST.get('eaddress')
    esal=request.POST.get('esal')
    
    if len(request.FILES)>0:
        eimage=request.FILES['eimage']
        fss=FileSystemStorage()
        file=fss.save(eimage.name,eimage)
        file_url=fss.url(file)
    else:
        file_url=request.POST.get('oldimage')
    
    emp=Employee(e_id=id,e_name=ename,e_gender=egen,e_contact=econ,e_eamil=eemail,e_password=epass,e_address=eadd,e_salary=esal,e_image=file_url) 
    emp.save()
    return redirect('/emplist/')

# --------------------------------Employee Attandance Table-------------------------------------------------------------------
def empattand(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    attand=EmployeeAttandance.objects.all()
    return render(request,'EmployeeAttandance/EmpAttandanceList.html',{'attandance':attand})
def empattendadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    attand=Employee.objects.all() 
    return render(request,'EmployeeAttandance/AttandanceAdd.html',{'employees':attand})
def empattendsave(request):
    stime=request.POST.get('stime')
    etime=request.POST.get('etime')
    eid=request.POST.get('eid')
    empl=Employee.objects.get(e_id=eid)
    attand=EmployeeAttandance(e=empl,start_time=stime,end_time=etime)
    attand.save()
    return redirect('/empattand/')
def employeeattanddel(request,id):
    empattand=EmployeeAttandance.objects.get(ea_id=id)
    empattand.delete()
    return redirect('/empattand/')
def empattendedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    employee=Employee.objects.all() 
    empattend=EmployeeAttandance.objects.get(ea_id=id)
    return render(request,'EmployeeAttandance/AttandanceEdit.html/',{'employees':employee,'attand':empattend})
def empattendupdate(request,id):
    stime=request.POST.get('stime')
    etime=request.POST.get('etime')
    eid=request.POST.get('eid')
    empl=Employee.objects.get(e_id=eid)
    service=EmployeeAttandance(ea_id=id,e=empl,start_time=stime,end_time=etime)
    service.save()
    return redirect('/empattand/')

# --------------------------------Employee Salary Table-------------------------------------------------------------------
def empsalary(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    salary=EmployeeSalary.objects.all()
    return render(request,'EmployeeSalary/EmployeeSalaryList.html',{'profit':salary})
def empsalaryadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    salaryadd=Employee.objects.all() 
    return render(request,'EmployeeSalary/EmployeeSalaryAdd.html',{'employees':salaryadd})
def empsalarysave(request):
    month=request.POST.get('month')
    year=request.POST.get('year')
    date=request.POST.get('date')
    eid=request.POST.get('eid')
    empl=Employee.objects.get(e_id=eid)
    salarysave=EmployeeSalary(es_month=month,es_year=year,es_date=date,e=empl)
    salarysave.save()
    return redirect('/empsalary/')
def empsalarydel(request,id):
    salarydel=EmployeeSalary.objects.get(es_id=id)
    salarydel.delete()
    return redirect('/empsalary/')
def empsaledit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    employee=Employee.objects.all() 
    empsal=EmployeeSalary.objects.get(es_id=id)
    return render(request,'EmployeeSalary/EmployeeSalaryEdit.html',{'salarys':empsal,'employees':employee})
def empsalupdate(request,id):
    month=request.POST.get('month')
    year=request.POST.get('year')
    date=request.POST.get('date')
    eid=request.POST.get('eid')
    empl=Employee.objects.get(e_id=eid)
    empsal=EmployeeSalary(es_id=id,e=empl,es_month=month,es_year=year,es_date=date)
    empsal.save()
    return redirect('/empsalary/')

# --------------------------------Membership Table-------------------------------------------------------------------
def membership(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    mem=Membership.objects.all()
    return render(request,'Membership/menbershipList.html',{'memberships':mem})
def memadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    cust=Customer.objects.all()
    mempack=MembershipPackage.objects.all() 
    return render(request,'Membership/MembershipAdd.html',{'customers':cust,'packages':mempack})
def memsave(request):   
    date=request.POST.get('date')
    cid=request.POST.get('cid')
    customer=Customer.objects.get(c_id=cid)
    mid=request.POST.get('mid')
    mpk=MembershipPackage.objects.get(mp_id=mid)  
    mem=Membership(c=customer,mp=mpk,start_date=date)
    mem.save()
    return redirect('/memberlist/')
def memberdel(request,id):
    memdel=Membership.objects.get(m_id=id)
    memdel.delete()
    return redirect('/memberlist/')
def memedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    cust=Customer.objects.all()
    mempack=MembershipPackage.objects.all() 
    mem=Membership.objects.get(m_id=id)
    return render(request,'Membership/MembershipEdit.html',{'customers':cust,'packages':mempack,'membership':mem})
def memupdate(request,id):   
    date=request.POST.get('date')
    cid=request.POST.get('cid')
    customer=Customer.objects.get(c_id=cid)
    mid=request.POST.get('mid')
    mpk=MembershipPackage.objects.get(mp_id=mid)  
    service=Membership(m_id=id,c=customer,mp=mpk,start_date=date)
    service.save()
    return redirect('/memberlist/')

# --------------------------------Membership Package Table-------------------------------------------------------------------
def mempackage(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    mpack=MembershipPackage.objects.all()
    return render(request,'MembershipPackage/PackageList.html',{'packages':mpack})
def mempackadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request,'MembershipPackage/MemPackageAdd.html')
def mempacksave(request):
    cname=request.POST.get('cname')
    cdis=request.POST.get('cdis')
    camount=request.POST.get('camount')
    cduration=request.POST.get('cduration')
    mpacksave=MembershipPackage(mp_name=cname,mp_discount=cdis,mp_amount=camount,mp_duration=cduration)
    mpacksave.save()
    return redirect('/mempackagelist/')
def mempackdel(request,id):
    mempackdel=MembershipPackage.objects.get(mp_id=id)
    mempackdel.delete()
    return redirect('/mempackagelist/')
def mempackedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    mpk=MembershipPackage.objects.get(mp_id=id)
    return render(request,'MembershipPackage/MemPackageEdit.html',{'package':mpk})
def mempackupdate(request,id):
    mpname=request.POST.get('mpname')
    mpdisc=request.POST.get('mpdisc')
    mpamount=request.POST.get('mpamount')
    mpdu=request.POST.get('mpdu')
    mpk=MembershipPackage.objects.get(mp_id=id)
    mpk.mp_name=mpname
    mpk.mp_discount=mpdisc
    mpk.mp_amount=mpamount
    mpk.mp_duration=mpdu
    mpk.save()
    return redirect('/mempackagelist/')

# --------------------------------Package Table-------------------------------------------------------------------
def package(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pack=Package.objects.all()
    return render(request,'Package/PackageList.html',{'packs':pack})
def packadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request,'Package/PackageAdd.html')
def packsave(request):
    pname=request.POST.get('pname')
    pdes=request.POST.get('pdes')
    pprice=request.POST.get('pprice')
    package=Package(pkg_name=pname,pkg_decription=pdes,pkg_price=pprice)
    package.save()
    return redirect('/packagelist/')
def packdel(request,id):
    packagedel=Package.objects.get(pkg_id=id)
    packagedel.delete()
    return redirect('/packagelist/')
def packedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pk=Package.objects.get(pkg_id=id)
    return render(request,'Package/PackageEdit.html',{'pack':pk})
def packupdate(request,id):
    pname=request.POST.get('pname')
    pdis=request.POST.get('pdes')
    pprice=request.POST.get('pprice')
    pk=Package.objects.get(pkg_id=id)
    pk.pkg_name=pname
    pk.pkg_decription=pdis
    pk.pkg_price=pprice
    pk.save()
    return redirect('/packagelist/')

# --------------------------------Package Details Table-------------------------------------------------------------------
def PackDetails(request):
    # packdeteil=PackageDetails.objects.all()
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    packdeteil=PackageDetails.objects.all()
    return render(request,'PackageDetails/PackageDetailsList.html',{'packsdetails':packdeteil})
def packdetailadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pkg=Package.objects.all()
    sres=Service.objects.all() 
    return render(request,'PackageDetails/PackageDetailsAdd.html',{'packs':pkg,'services':sres})
def packdetailsave(request):   
    pid=request.POST.get('pid')
    pkg=Package.objects.get(pkg_id=pid)
    sid=request.POST.get('sid')
    sres=Service.objects.get(s_id=sid)
    service=PackageDetails(pkg=pkg,s=sres)
    service.save()
    return redirect('/packdetailslist/')
def packdetailsdel(request,id):
    dele=PackageDetails.objects.get(pkd_id=id)
    dele.delete()
    return redirect('/packdetailslist/')
def packdetailedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pkg=Package.objects.all()
    sres=Service.objects.all() 
    pkd=PackageDetails.objects.get(pkd_id=id)
    return render(request,'PackageDetails/PackageDetailsEdit.html',{'packs':pkg,'services':sres,'packdetails':pkd})
def packdetailupdate(request,id):   
    pid=request.POST.get('pid')
    pkg=Package.objects.get(pkg_id=pid)
    sid=request.POST.get('sid')
    sres=Service.objects.get(s_id=sid)
    pkd=PackageDetails(pkd_id=id,pkg=pkg,s=sres)
    pkd.save()
    return redirect('/packdetailslist/')

# --------------------------------Product Table-------------------------------------------------------------------
def products(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pro=Product.objects.all()
    return render(request,'Product/ProductList.html',{'products':pro})
def productsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    brands=Brand.objects.all()
    categories=Category.objects.all()
    return render(request,'Product/ProductAdd.html',{'brands':brands,'categories':categories})
def productsave(request):
    pname=request.POST.get('pname')
    pdes=request.POST.get('pdes')
    price=request.POST.get('price')

    pimage=request.FILES['pimage']
    fss=FileSystemStorage()
    file=fss.save(pimage.name,pimage)
    file_url=fss.url(file)
    
    bid=request.POST.get('bid')
    brand=Brand.objects.get(b_id=bid)
    cid=request.POST.get('cid')
    cat=Category.objects.get(c_id=cid)
    prod=Product(p_name=pname,b=brand,c=cat,p_description=pdes,p_price=price,p_image=file_url)
    prod.save()
    return redirect('/productlist/')
def productdel(request,id):
    prodel=Product.objects.get(p_id=id)
    prodel.delete()
    return redirect('/productlist/')
def productedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    brands=Brand.objects.all()
    categories=Category.objects.all()
    prod=Product.objects.get(p_id=id)
    return render(request,'Product/ProductEdit.html',{'brands':brands,'categories':categories,'prod':prod})
def productupdate(request,id):
    pname=request.POST.get('pname')
    pdes=request.POST.get('pdes')
    price=request.POST.get('price')
    bid=request.POST.get('bid')
    brand=Brand.objects.get(b_id=bid)
    cid=request.POST.get('cid')
    cat=Category.objects.get(c_id=cid)
    if len(request.FILES)>0:
        pimage=request.FILES['pimage']
        fss=FileSystemStorage()
        file=fss.save(pimage.name,pimage)
        file_url=fss.url(file)
    else:
        file_url=request.POST.get('oldimage')
    
    service=Product(p_id=id,p_name=pname,b=brand,c=cat,p_price=price,p_description=pdes,p_image=file_url)
    service.save()
    
    return redirect('/productlist/')

# --------------------------------Product Details Table-------------------------------------------------------------------
def pdetail(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    prodet=ProductDetails.objects.all()
    return render(request,'ProductDetails/ProductDetailsList.html',{'pdetails':prodet})
def productdetailsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    prod=Product.objects.all()
    return render(request,'ProductDetails/ProductDetailsAdd.html',{'products':prod})
def productdetailsave(request):
    psize=request.POST.get('psize')
    pprice=request.POST.get('pprice')
    stock=request.POST.get('stock')
    
    pimage=request.FILES['pimage']
    fss=FileSystemStorage()
    file=fss.save(pimage.name,pimage)
    file_url=fss.url(file)
    
    
    pid=request.POST.get('pid')
    prod=Product.objects.get(p_id=pid)
    prodetsave=ProductDetails(pd_size=psize,pd_price=pprice,current_stock=stock,p=prod,pd_image=file_url)
    prodetsave.save()
    return redirect('/productdetailslist/')
def productdetailsdel(request,id):
    prodetdel=ProductDetails.objects.get(pd_id=id)
    prodetdel.delete()
    return redirect('/productdetailslist/')
def proddetailedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    prod=Product.objects.all()
    product=ProductDetails.objects.get(pd_id=id)
    return render(request,'ProductDetails/ProductDetailsEdit.html',{'products':prod,'pdetail':product})
def proddetailupdate(request,id):
    psize=request.POST.get('psize')
    pprice=request.POST.get('pprice')
    stock=request.POST.get('stock')
    pid=request.POST.get('pid')
    
    if len(request.FILES)>0:
        pdimage=request.FILES['pdimage']
        fss=FileSystemStorage()
        file=fss.save(pdimage.name,pdimage)
        file_url=fss.url(file)
    else:
        file_url=request.POST.get('oldimage')
    
    prod=Product.objects.get(p_id=pid)
    service=ProductDetails(pd_id=id,pd_size=psize,pd_price=pprice,current_stock=stock,p=prod,pd_image=file_url)
    service.save()
    return redirect('/productdetailslist/')

# --------------------------------Purchase Order Table-------------------------------------------------------------------
def po(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sers=PurchaseOrder.objects.all()
    return render(request,'PurchaseOrder/Purchaseorderlist.html',{'purchaseorder':sers})
def purchaseorderadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    supp=Supplier.objects.all()
    return render(request,'PurchaseOrder/PurchaseOrderAdd.html',{'sups':supp})
def purchaseordersave(request):
    poid=request.POST.get('po_id')
    podate=request.POST.get('podate')
    pototal=request.POST.get('pototal')
    postatus=request.POST.get('postatus')
    sid=request.POST.get('sid')
    supp=Supplier.objects.get(sup_id=sid)
    service=PurchaseOrder(po_id=poid,po_date=podate,po_total=pototal,po_status=postatus,sup=supp)
    service.save()
    return redirect('/purchaseorderlist/')
def puchaseorderdel(request,id):
    purdel=PurchaseOrder.objects.get(po_id=id)
    purdel.delete()
    return redirect('/purchaseorderlist/')
def purchaseorderedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    supp=Supplier.objects.all()
    po=PurchaseOrder.objects.get(po_id=id)
    return render(request,'PurchaseOrder/PurchaseOrderEdit.html',{'sups':supp,'purchase':po})
def purchaseorderupdate(request,id):
    podate=request.POST.get('podate')
    pototal=request.POST.get('pototal')
    postatus=request.POST.get('postatus')
    sid=request.POST.get('sid')
    supp=Supplier.objects.get(sup_id=sid)
    service=PurchaseOrder(po_id=id,po_date=podate,po_total=pototal,po_status=postatus,sup=supp)
    service.save()
    
    return redirect('/purchaseorderlist/')


# --------------------------------Purchase Order Details Table-------------------------------------------------------------------
def podetails(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pods=PurchaseOrderDetails.objects.all()
    return render(request,'PurchaseOrderDetails/PurchaseOrderDetailsList.html',{'pods':pods})
def purchaseorderdetailsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    po=PurchaseOrder.objects.all()
    pd=ProductDetails.objects.all()
    return render(request,'PurchaseOrderDetails/PurchaseOrderDetailsAdd.html',{'purchaseorder':po,'pdetails':pd})
def purchaseorderdetailssave(request):
    podqunt=request.POST.get('podqunt')
    poddate=request.POST.get('poddate')
    poid=request.POST.get('poid')
    po=PurchaseOrder.objects.get(po_id=poid)
    pdid=request.POST.get('pdid')
    pd=ProductDetails.objects.get(pd_id=pdid)
    service=PurchaseOrderDetails(pod_quantity=podqunt,pod_date=poddate,po=po,pd=pd)
    service.save()
    return redirect('/purchaseorderdetailslist/')
def podetaildel(request,id):
    podetail=PurchaseOrderDetails.objects.get(pod_id=id)
    podetail.delete()
    return redirect('/purchaseorderdetailslist/')
def purchaseorderdetailsedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    po=PurchaseOrder.objects.all()
    pd=ProductDetails.objects.all()
    pod=PurchaseOrderDetails.objects.get(pod_id=id)
    return render(request,'PurchaseOrderDetails/PurchaseOrderDetailsedit.html',{'purchaseorder':po,'pdetails':pd,'pod':pod})

# --------------------------------Sale Order Table-------------------------------------------------------------------
def salorder(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sers=SalesOrder.objects.all()
    return render(request,'SalesOrder/SalesOrderList.html',{'sos':sers})
def salesorderadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    cust=Customer.objects.all()
    return render(request,'SalesOrder/SalesOrderAdd.html',{'customers':cust})
def salesordersave(request):
    sodate=request.POST.get('sodate')
    sototal=request.POST.get('sototal')
    sodisc=request.POST.get('sodisc')
    soamount=request.POST.get('soamount')
    sostatus=request.POST.get('sostatus')
    cid=request.POST.get('cid')
    cust=Customer.objects.get(c_id=cid)
    service=SalesOrder(so_date=sodate,so_total=sototal,so_discount=sodisc,so_amount=soamount,so_status=sostatus,c=cust)
    service.save()
    return redirect('/salsorderlist/')
def salesorderdel(request,id):
    so=SalesOrder.objects.get(so_id=id)
    so.delete()
    return redirect('/salsorderlist/')
def soedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    cust=Customer.objects.all()
    so=SalesOrder.objects.get(so_id=id)
    return render(request,'SalesOrder/SalesOrderEdit.html',{'customers':cust,'so':so})
def soupdate(request,id):
    sodate=request.POST.get('sodate')
    sototal=request.POST.get('sototal')
    sodisc=request.POST.get('sodisc')
    soamount=request.POST.get('soamount')
    sostatus=request.POST.get('sostatus')
    cid=request.POST.get('cid')
    cust=Customer.objects.get(c_id=cid)
    service=SalesOrder(so_id=id,so_date=sodate,so_total=sototal,so_discount=sodisc,so_amount=soamount,so_status=sostatus,c=cust)
    service.save()
    return redirect('/salsorderlist/')

# --------------------------------Sales Order Details Table-------------------------------------------------------------------
def salorderdetail(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sers=SalesOrderDetails.objects.all()
    return render(request,'SalesOrderDetails/list.html',{'sods':sers})
def salesorderdetailsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    saleso=SalesOrder.objects.all()
    pd=ProductDetails.objects.all()
    return render(request,'SalesOrderDetails/add.html',{'sos':saleso,'pdetails':pd})
def salesorderdetailssave(request):
    quen=request.POST.get('quen')
    date=request.POST.get('date')
    soid=request.POST.get('soid')
    sales=SalesOrder.objects.get(so_id=soid)
    pdid=request.POST.get('pdid')
    pd=ProductDetails.objects.get(pd_id=pdid)
    service=SalesOrderDetails(sod_quntity=quen,sod_date=date,so=sales,pd=pd)
    service.save()
    
    return redirect('/salsorderdetailslist/')
def salesorderdetaildel(request,id):
    sod=SalesOrderDetails.objects.get(sod_id=id)
    sod.delete()
    return redirect('/salsorderdetailslist/')
def salesorderdetailsedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    saleso=SalesOrder.objects.all()
    pd=ProductDetails.objects.all()
    sod=SalesOrderDetails.objects.get(sod_id=id)
    return render(request,'SalesOrderDetails/edit.html',{'sos':saleso,'pdetails':pd,'sod':sod})
def salesorderdetailsupdate(request,id):
    quen=request.POST.get('quen')
    date=request.POST.get('date')
    soid=request.POST.get('soid')
    sales=SalesOrder.objects.get(so_id=soid)
    pdid=request.POST.get('pdid')
    pd=ProductDetails.objects.get(pd_id=pdid)
    service=SalesOrderDetails(sod_id=id,sod_quntity=quen,sod_date=date,so=sales,pd=pd)
    service.save()
    
    return redirect('/salsorderdetailslist/')
# --------------------------------Service Table-------------------------------------------------------------------
def servicelist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sers=Service.objects.all()
    return render(request,'Service/ServiceList.html',{'services':sers})
def serviceadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request,'Service/ServiceAdd.html')
def servicesave(request):
    sname=request.POST.get('sname')
    spr=request.POST.get('sprice')
    
    pimage=request.FILES['simage']
    fss=FileSystemStorage()
    file=fss.save(pimage.name,pimage)
    file_url=fss.url(file)
    
    service=Service(s_name=sname,s_price=spr,s_image=file_url)
    service.save()  
    return redirect('/slist/')
def servicedel(request,id):
    Servi=Service.objects.get(s_id=id)
    Servi.delete()
    return redirect('/slist/')
def serviceedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    service=Service.objects.get(s_id=id)
    
    return render(request,'Service/ServiceEdit.html',{'service':service})
def serviceupdate(request,id):
    sname=request.POST.get('sname')
    sprice=request.POST.get('sprice') 
       
    if len(request.FILES)>0:
        pimage=request.FILES['simage']
        fss=FileSystemStorage()
        file=fss.save(pimage.name,pimage)
        file_url=fss.url(file)
    else:
        file_url=request.POST.get('oldimage')
    
    service=Service(s_id=id,s_name=sname,s_price=sprice,s_image=file_url)
    service.save()
    return redirect('/slist/')


# --------------------------------Suplier Table-------------------------------------------------------------------
def supplier(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sers=Supplier.objects.all()
    return render(request,'Suplier/SuplierList.html',{'sups':sers})
def suppadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request,'Suplier/SupplierAdd.html')
def suppsave(request):
    sname=request.POST.get('sname')
    sadd=request.POST.get('sadd')
    scontect=request.POST.get('scontect')
    semail=request.POST.get('semail')
    service=Supplier(sup_name=sname,sup_address=sadd,sup_contact=scontect,sup_email=semail)
    service.save()
    return redirect('/supplierlist/')
def supdel(request,id):
    supdel=Supplier(sup_id=id)
    supdel.delete()
    return redirect('/supplierlist/')
def suppedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    supp=Supplier.objects.get(sup_id=id)
    return render(request,'Suplier/Supplieredit.html',{'sup':supp})
def suppupdate(request,id):
    sname=request.POST.get('sname')
    sadd=request.POST.get('sadd')
    scon=request.POST.get('scon')
    semail=request.POST.get('semail')
    
    sup=Supplier.objects.get(sup_id=id)
    sup.sup_name=sname
    sup.sup_address=sadd
    sup.sup_contact=scon
    sup.sup_email=semail
    sup.save()
    return redirect('/supplierlist/')


def master(request):
    return render(request,'master.html')