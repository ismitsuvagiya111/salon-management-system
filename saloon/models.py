from django.db import models

# Create your models here.
class Admin(models.Model):
    a_id = models.AutoField(db_column='A_id', primary_key=True)  # Field name made lowercase.
    a_email = models.CharField(db_column='A_email', max_length=25)  # Field name made lowercase.
    a_password = models.CharField(db_column='A_password', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Appointment(models.Model):
    a_id = models.AutoField(db_column='A_id', primary_key=True)  # Field name made lowercase.
    a_datetime = models.DateTimeField(db_column='A_datetime')  # Field name made lowercase.
    c = models.ForeignKey('Customer', models.DO_NOTHING, db_column='C_id')  # Field name made lowercase.
    s = models.ForeignKey('Service', models.DO_NOTHING, db_column='S_id')  # Field name made lowercase.
    pkg = models.ForeignKey('Package', models.DO_NOTHING, db_column='PKG_id')  # Field name made lowercase.
    a_rate = models.IntegerField(db_column='A_rate')  # Field name made lowercase.
    a_status = models.CharField(db_column='A_status', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appointment'

class Brand(models.Model):
    b_id = models.AutoField(db_column='B_id', primary_key=True)  # Field name made lowercase.
    b_name = models.CharField(db_column='B_name', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.b_name
    class Meta:
        managed = False
        db_table = 'brand'
        




class Category(models.Model):
    c_id = models.AutoField(db_column='C_id', primary_key=True)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_name', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.c_name
    class Meta:
        managed = False
        db_table = 'category'


class Customer(models.Model):
    c_id = models.AutoField(db_column='C_id', primary_key=True)  # Field name made lowercase.
    c_name = models.CharField(db_column='C_name', max_length=25)  # Field name made lowercase.
    c_age = models.CharField(db_column='C_age', max_length=8)  # Field name made lowercase.
    c_contact = models.IntegerField(db_column='C_contact')  # Field name made lowercase.
    c_gender = models.CharField(db_column='C_gender', max_length=8)  # Field name made lowercase.
    c_email = models.CharField(db_column='C_email', max_length=25)  # Field name made lowercase.
    c_password = models.CharField(db_column='C_password', max_length=15)  # Field name made lowercase.
    c_address = models.CharField(db_column='C_address', max_length=50)  # Field name made lowercase.
    c_image = models.CharField(db_column='C_image', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.c_name
    class Meta:
        managed = False
        db_table = 'customer'


class Cart(models.Model):
    cart_id = models.AutoField(db_column='Cart_id', primary_key=True)  # Field name made lowercase.
    c = models.ForeignKey('Customer', models.DO_NOTHING, db_column='C_id')  # Field name made lowercase.
    pd = models.ForeignKey('ProductDetails', models.DO_NOTHING, db_column='PD_id')  # Field name made lowercase.
    cart_quntity = models.IntegerField(db_column='Cart_quntity')  # Field name made lowercase.
    cart_rate = models.IntegerField(db_column='Cart_rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'

class Employee(models.Model):
    e_id = models.AutoField(db_column='E_id', primary_key=True)  # Field name made lowercase.
    e_name = models.CharField(db_column='E_name', max_length=25)  # Field name made lowercase.
    e_gender = models.CharField(db_column='E_gender', max_length=8)  # Field name made lowercase.
    e_contact = models.IntegerField(db_column='E_contact')  # Field name made lowercase.
    e_eamil = models.CharField(db_column='E_eamil', max_length=25)  # Field name made lowercase.
    e_password = models.CharField(db_column='E_password', max_length=15)  # Field name made lowercase.
    e_address = models.CharField(db_column='E_address', max_length=50)  # Field name made lowercase.
    e_salary = models.IntegerField(db_column='E_salary')  # Field name made lowercase.
    e_image = models.CharField(db_column='E_image', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.e_name
    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeAttandance(models.Model):
    ea_id = models.AutoField(db_column='EA_id', primary_key=True)  # Field name made lowercase.
    e = models.ForeignKey(Employee, models.DO_NOTHING, db_column='E_id')  # Field name made lowercase.
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee_attandance'


class EmployeeSalary(models.Model):
    es_id = models.AutoField(db_column='ES_id', primary_key=True)  # Field name made lowercase.
    e = models.ForeignKey(Employee, models.DO_NOTHING, db_column='E_id')  # Field name made lowercase.
    es_month = models.CharField(db_column='ES_month', max_length=10)  # Field name made lowercase.
    es_year = models.CharField(db_column='ES_year', max_length=15)  # Field name made lowercase.
    es_date = models.DateField(db_column='ES_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee_salary'


class Membership(models.Model):
    m_id = models.AutoField(db_column='M_id', primary_key=True)  # Field name made lowercase.
    c = models.ForeignKey(Customer, models.DO_NOTHING, db_column='C_id')  # Field name made lowercase.
    mp = models.ForeignKey('MembershipPackage', models.DO_NOTHING, db_column='MP_id')  # Field name made lowercase.
    start_date = models.DateField()
    def __str__(self):
        return self.mp
    class Meta:
        managed = False
        db_table = 'membership'


class MembershipPackage(models.Model):
    mp_id = models.AutoField(db_column='MP_id', primary_key=True)  # Field name made lowercase.
    mp_name = models.CharField(db_column='MP_name', max_length=50)  # Field name made lowercase.
    mp_discount = models.IntegerField(db_column='MP_discount')  # Field name made lowercase.
    mp_amount = models.IntegerField(db_column='MP_amount')  # Field name made lowercase.
    mp_duration = models.DateTimeField(db_column='MP_duration')  # Field name made lowercase.
    def __str__(self):
        return self.mp_name
    class Meta:
        managed = False
        db_table = 'membership_package'


class Package(models.Model):
    pkg_id = models.AutoField(db_column='PKG_id', primary_key=True)  # Field name made lowercase.
    pkg_name = models.CharField(db_column='PKG_name', max_length=15)  # Field name made lowercase.
    pkg_price = models.IntegerField(db_column='PKG_price')  # Field name made lowercase.
    pkg_decription = models.CharField(db_column='PKG_decription', max_length=500)  # Field name made lowercase.
    def __str__(self):
        return self.pkg_name
    class Meta:
        managed = False
        db_table = 'package'


class PackageDetails(models.Model):
    pkd_id = models.AutoField(db_column='PKD_id', primary_key=True)  # Field name made lowercase.
    s = models.ForeignKey('Service', models.DO_NOTHING, db_column='S_id')  # Field name made lowercase.
    pkg = models.ForeignKey(Package, models.DO_NOTHING, db_column='PKG_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'package_details'


class Payment(models.Model):
    pm_id = models.AutoField(db_column='PM_id', primary_key=True)  # Field name made lowercase.
    pm_type = models.CharField(db_column='PM_type', max_length=25)  # Field name made lowercase.
    a = models.ForeignKey(Appointment, models.DO_NOTHING, db_column='A_id')  # Field name made lowercase.
    so = models.ForeignKey('SalesOrder', models.DO_NOTHING, db_column='SO_id')  # Field name made lowercase.
    pm_amount = models.IntegerField(db_column='PM_amount')  # Field name made lowercase.
    pm_date = models.DateField(db_column='PM_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    p_id = models.AutoField(db_column='P_id', primary_key=True)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_name', max_length=50)  # Field name made lowercase.
    b = models.ForeignKey(Brand, models.DO_NOTHING, db_column='B_id')  # Field name made lowercase.
    c = models.ForeignKey(Category, models.DO_NOTHING, db_column='C_id')  # Field name made lowercase.
    p_description = models.CharField(db_column='P_description', max_length=50)  # Field name made lowercase.
    p_price = models.IntegerField(db_column='P_price')  # Field name made lowercase.
    p_image = models.CharField(db_column='P_image', max_length=50)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'product'


class ProductDetails(models.Model):
    pd_id = models.AutoField(db_column='PD_id', primary_key=True)  # Field name made lowercase.
    p = models.ForeignKey(Product, models.DO_NOTHING, db_column='P_id')  # Field name made lowercase.
    pd_image = models.CharField(db_column='PD_image', max_length=100)  # Field name made lowercase.
    pd_size = models.CharField(db_column='PD_size', max_length=20)  # Field name made lowercase.
    pd_price = models.IntegerField(db_column='PD_price')  # Field name made lowercase.
    current_stock = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_details'


class PurchaseOrder(models.Model):
    po_id = models.AutoField(db_column='PO_id', primary_key=True)  # Field name made lowercase.
    po_date = models.DateField(db_column='PO_date')  # Field name made lowercase.
    sup = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SUP_id')  # Field name made lowercase.
    po_total = models.IntegerField(db_column='PO_total')  # Field name made lowercase.
    po_status = models.CharField(db_column='PO_status', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase_order'

class PurchaseOrderDetails(models.Model):
    pod_id = models.AutoField(db_column='POD_id', primary_key=True)  # Field name made lowercase.
    po = models.ForeignKey(PurchaseOrder, models.DO_NOTHING, db_column='PO_id')  # Field name made lowercase.
    pd = models.ForeignKey(ProductDetails, models.DO_NOTHING, db_column='PD_id')  # Field name made lowercase.
    pod_quantity = models.IntegerField(db_column='POD_quantity')  # Field name made lowercase.
    pod_date = models.DateField(db_column='POD_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase_order_details'


class SalesOrder(models.Model):
    so_id = models.AutoField(db_column='SO_id', primary_key=True)  # Field name made lowercase.
    c = models.ForeignKey(Customer, models.DO_NOTHING, db_column='C_id')  # Field name made lowercase.
    so_date = models.DateField(db_column='SO_date')  # Field name made lowercase.
    so_total = models.IntegerField(db_column='SO_total')  # Field name made lowercase.
    so_discount = models.IntegerField(db_column='SO_discount')  # Field name made lowercase.
    so_amount = models.IntegerField(db_column='SO_amount')  # Field name made lowercase.
    so_status = models.CharField(db_column='SO_status', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales_order'


class SalesOrderDetails(models.Model):
    sod_id = models.AutoField(db_column='SOD_id', primary_key=True)  # Field name made lowercase.
    so = models.ForeignKey(SalesOrder, models.DO_NOTHING, db_column='SO_id')  # Field name made lowercase.
    pd = models.ForeignKey(ProductDetails, models.DO_NOTHING, db_column='PD_id')  # Field name made lowercase.
    sod_quntity = models.IntegerField(db_column='SOD_quntity')  # Field name made lowercase.
    sod_date = models.DateField(db_column='SOD_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales_order_details'


class Service(models.Model):
    s_id = models.AutoField(db_column='S_id', primary_key=True)  # Field name made lowercase.
    s_name = models.CharField(db_column='S_name', max_length=25)  # Field name made lowercase.
    s_price = models.IntegerField(db_column='S_price')  # Field name made lowercase.
    s_image = models.CharField(db_column='S_image', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.s_name
    class Meta:
        managed = False
        db_table = 'service'


class Supplier(models.Model):
    sup_id = models.AutoField(db_column='SUP_id', primary_key=True)  # Field name made lowercase.
    sup_name = models.CharField(db_column='SUP_name', max_length=25)  # Field name made lowercase.
    sup_address = models.CharField(db_column='SUP_address', max_length=25)  # Field name made lowercase.
    sup_contact = models.IntegerField(db_column='SUP_contact')  # Field name made lowercase.
    sup_email = models.CharField(db_column='SUP_email', max_length=25)  # Field name made lowercase.
    def __str__(self):
        return self.sup_name
    
    class Meta:
        managed = False
        db_table = 'supplier'
