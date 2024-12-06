from django.db import models

# Create your models here.

#model is a Class that represents a table in database
# each type of data gets its own model 

# Tables: User, Main, Filter, Cart, Profile, Login, Item


from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    logout = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cloth = models.BooleanField(default=False)
    equip = models.BooleanField(default=False)
    text = models.BooleanField(default=False)
    condition = models.CharField(max_length=100, choices=[('New', 'New'), ('Used', 'Used')])
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Item {self.itemID}: {self.description[:20]}"


class Filter(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='filter')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cloth = models.BooleanField(default=False)
    equip = models.BooleanField(default=False)
    condition = models.CharField(max_length=100, choices=[('New', 'New'), ('Used', 'Used')])

    def __str__(self):
        return f"Filter for Item {self.item.itemID}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cart_entries')
    image = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=255, choices=[('Completed', 'Completed'), ('NoPayment', 'NoPayment')])

    def __str__(self):
        return f"Cart Entry: User {self.user.username} - Item {self.item.itemID}"


class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='login')
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"Login for {self.user.username}"


'''
-- Table for User
CREATE TABLE User (
    userID SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Table for Profile
CREATE TABLE Profile (
    userID INT,
    logout BOOLEAN,
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255),
    FOREIGN KEY (userID) REFERENCES User(userID)
);

-- Table for Item
CREATE TABLE Item (
    itemID SERIAL PRIMARY KEY,
    description TEXT,
    price DECIMAL(10, 2),
    cloth BOOLEAN,
    equip BOOLEAN,
    text BOOLEAN,
    condition VARCHAR(100),
    image TEXT
);

-- Table for Cart
CREATE TABLE Cart (
    userID INT,
    itemID INT,
    image TEXT,
    price DECIMAL(10, 2),
    payment VARCHAR(255),
    FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID)
);

-- Table for Filter
CREATE TABLE Filter (
    itemID INT,
    price DECIMAL(10, 2),
    cloth BOOLEAN,
    equip BOOLEAN,
    condition VARCHAR(100),
    FOREIGN KEY (itemID) REFERENCES Item(itemID)
);

-- Table for Login
CREATE TABLE Login (
    userID INT,
    email VARCHAR(255),
    password VARCHAR(255),
    FOREIGN KEY (userID) REFERENCES User(userID)
);
'''