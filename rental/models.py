from django.db import models

# Create your models here.
class VehicleDb(models.Model):
    vehicle_name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    vehicle_type=models.CharField(max_length=100)
    registration_number=models.CharField(max_length=50,unique=True)
    rent_per_day=models.DecimalField(max_digit=10,decimal_places=2)
    is_avaialable=models.BooleanField(default=True)

    def ___str__(self):
        return self.vehicle_name

class CustomerDb(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    license_number=models.CharField(max_length=30,unique=True)
    address=models.TextField()

    def __str__(self):
        return self.name

class BookingDb(models.Model):
    customer=models.ForeignKey(CustomerDb,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(VehicleDb,on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)
    start_date=models.DateField()
    end_date=models.DateField()
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    booking_status=models.CharField(max_length=20,choices=[
        ("Pending","Pending"),
        ("Confirmed","Confirmed"),
        ("Completed","Completed"),
        ("cancelled","Cancelled")
    ],default="Pending")
    def __str__(self):
        return f"{self.customer.name}-{self.vehicle_name}"

class PaymentDb(models.Model):
    booking=models.ForeignKey(BookingDb,on_delete=models.CASCADE)
    payment_date=models.DateField(auto_now_add=True)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_method=models.CharField(max_length=20,choices=[
        ("Cash","Cash"),
        ("UPI","UPI"),
        ("Card","Card")
    ])
    payement_status=models.CharField(
        max_length=20,choices=[
            ("Pending","Pending"),
            ("Paid","Paid"),
            ("Failed","Failed")
        ],default="Pending"
    )

    def __str__(self):
        return f"Payment{self.id}"
