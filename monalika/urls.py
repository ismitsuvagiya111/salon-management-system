"""monalika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from saloon.views import *
from django.conf.urls.static import static 
from monalika import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    # --------------------------------Home page Urls--------------------------------
    path('',page),
    path('about/',about),
    path('contact/',contact),
    path('shop/',shop),
    path('shopdetail/<int:id>/',shopdetail),
    path('shopsingle/<int:id>/',shop_single),
    path('service/',service),
    path('shopdetails/',ShopDetails),
    path('shopdescription/',shopdescription),
    path('sign/',Sign),
    path('appointments/',appointments),
    path('customerlogin/',customerlogin),
    path('profile/',profile),
    path('addToCart/',addtocart),
    path('cart/',cart),
    path('packges/',packges),
    path('serapoo/<int:id>/',serapoo),
    path('packgesappo/',packgesappo),
    path('serapposave/',serapposave),
    path('order/',order),




    
    # ---------------------------Appointment Table urls-------------------------------------------------------------------
    path('appointmentlist/',appointment),
    path('appointmentadd/', Appointmentadd),
    path('appointmentsave/',Appointmentsave),
    path('appoedit/<int:id>/', appoedit), 
    path('appoupdate/<int:id>/', appoupdate), 
    path('appodel/<int:id>/',appodel),
    # ---------------------------Brand table urls-------------------------------------------------------------------
    path('brandlist/',brandlist),
    path('badd/', brandadd), 
    path('bsave/', brandsave), 
    path('bdel/<int:id>/', branddel), 
    path('bedit/<int:id>/', brandedit), 
    path('bupdate/<int:id>/', brandupdate), 
    # ---------------------------Category table urls-------------------------------------------------------------------
    path('categorylist/',categorylist),
    path('categoryadd/', categoryadd), 
    path('categorysave/', categorysave),
    path('categorydel/<int:id>/', categorydel), 
    path('categoryedit/<int:id>/', categoryedit), 
    path('categoryupdate/<int:id>/', categoryupdate),
    # ---------------------------Customer table urls-------------------------------------------------------------------
    path('customerlist/', customerlist),
    path('customeradd/', customeradd), 
    path('customersave/', customersave),
    path('customerdel/<int:id>/', customerdel), 
    path('customeredit/<int:id>/', customeredit),
    path('customerupdate/<int:id>/', custupdate),
    # ---------------------------Employee table urls-------------------------------------------------------------------
    path('emplist/', emplist),
    path('empadd/', empadd), 
    path('empsave/', empsave), 
    path('employeedel/<int:id>/', employeedel), 
    path('employeeedit/<int:id>/', empedit),
    path('empupdate/<int:id>/', empupdate),
    # --------------------------------Employee Attandance urls-------------------------------------------------------------------
    path('empattand/',empattand),
    path('empattendadd/', empattendadd),
    path('empattendsave/',empattendsave),
    path('employeeattanddel/<int:id>/', employeeattanddel), 
    path('employeeattandedit/<int:id>/', empattendedit), 
    path('empattendupdate/<int:id>/', empattendupdate), 
    # --------------------------------Employee Salary urls-------------------------------------------------------------------
    path('empsalary/',empsalary),
    path('empsalaryadd/', empsalaryadd),
    path('empsalarysave/',empsalarysave),
    path('emplsalarydel/<int:id>/', empsalarydel), 
    path('empsalaryedit/<int:id>/', empsaledit), 
    path('empsalupdate/<int:id>/', empsalupdate),
    # --------------------------------Membership urls-------------------------------------------------------------------
    path('memberlist/',membership),
    path('memadd/', memadd),
    path('memsave/',memsave),
    path('memberdel/<int:id>/', memberdel), 
    path('memberedit/<int:id>/', memedit),
    path('memupdate/<int:id>/', memupdate),
    # --------------------------------Membership Package urls-------------------------------------------------------------------
    path('mempackagelist/',mempackage),
    path('mempackadd/', mempackadd), 
    path('mempacksave/', mempacksave),
    path('mempackagedel/<int:id>/',mempackdel), #IntegrityError at /mempackagedel/1/
    path('mempackageedit/<int:id>/',mempackedit), 
    path('mempackupdate/<int:id>/', mempackupdate),
    # --------------------------------Package urls-------------------------------------------------------------------
    path('packagelist/',package),  
    path('packageadd/', packadd), 
    path('packagesave/', packsave), 
    path('packdel/<int:id>/', packdel),
    path('packedit/<int:id>/', packedit),
    path('packupdate/<int:id>/', packupdate),
    # --------------------------------Package Details urls-------------------------------------------------------------------
    path('packdetailslist/',PackDetails),
    path('packdetailadd/', packdetailadd),
    path('packdetailsave/',packdetailsave),
    path('packdetailsdel/<int:id>/', packdetailsdel),
    path('packdetailsedit/<int:id>/', packdetailedit),
    path('packdetailupdate/<int:id>/', packdetailupdate),
    # --------------------------------Product urls-------------------------------------------------------------------
    path('productlist/',products),
    path('productadd/', productsadd),
    path('productsave/',productsave),
    path('productdel/<int:id>/', productdel),
    path('productedit/<int:id>/', productedit),
    path('productupdate/<int:id>/', productupdate), 
    # --------------------------------Product Details urls-------------------------------------------------------------------
    path('productdetailslist/',pdetail),
    path('productdetailsadd/',productdetailsadd),
    path('productdetailsave/',productdetailsave),
    path('productdetailsdel/<int:id>/', productdetailsdel),
    path('productdetailsedit/<int:id>/', proddetailedit),
    path('proddetailupdate/<int:id>/', proddetailupdate), 
    # --------------------------------Purchase Order urls-------------------------------------------------------------------
    path('purchaseorderlist/',po),
    path('purchaseorderadd/', purchaseorderadd),
    path('purchaseordersave/',purchaseordersave),
    path('purchaseorderdel/<int:id>/', puchaseorderdel),
    path('purchaseorderedit/<int:id>/', purchaseorderedit),
    path('purchaseorderupdate/<int:id>/', purchaseorderupdate), 
    # --------------------------------Purchase Order Details urls-------------------------------------------------------------------
    path('purchaseorderdetailslist/',podetails),
    path('purchaseorderdetailsadd/', purchaseorderdetailsadd),
    path('purchaseorderdetailssave/',purchaseorderdetailssave),
    path('poddel/<int:id>/', podetaildel), 
    path('podedit/<int:id>/', purchaseorderdetailsedit), 
    # --------------------------------Sales Order urls-------------------------------------------------------------------
    path('salsorderlist/',salorder),
    path('salesorderadd/', salesorderadd),
    path('salesordersave/',salesordersave),
    path('sodel/<int:id>/', salesorderdel), 
    path('soedit/<int:id>/', soedit), 
    path('soupdate/<int:id>/', soupdate), 
    # --------------------------------Sales Order Details urls-------------------------------------------------------------------
    path('salsorderdetailslist/',salorderdetail),
    path('salesorderdetailsadd/', salesorderdetailsadd),
    path('salesorderdetailssave/',salesorderdetailssave),
    path('soddel/<int:id>/', salesorderdetaildel), 
    path('salesorderdetailsedit/<int:id>/', salesorderdetailsedit),
    path('salesorderdetailsupdate/<int:id>/',salesorderdetailsupdate),
    
    # --------------------------------Service urls-------------------------------------------------------------------
    path('slist/', servicelist),
    path('sadd/', serviceadd), 
    path('ssave/', servicesave), 
    path('serdel/<int:id>/', servicedel), 
    path('sedit/<int:id>/', serviceedit),
    path('supdate/<int:id>/', serviceupdate), 
    
    # --------------------------------Suplier urls-------------------------------------------------------------------
    path('supplierlist/',supplier),
    path('supplieradd/', suppadd), 
    path('suppliersave/', suppsave),
    path('supdel/<int:id>/', supdel),
    path('suppedit/<int:id>/', suppedit), 
    path('suppupdate/<int:id>/', suppupdate), 
    path('master/',master),
    path('login/',login),
    path('deshboard/',Deshboard),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


