from django.db import models

# Create your models here.

#model is a Class that represents a table in database
# each type of data gets its own model 

# Tables: User, Main, Filter, Cart, Profile, Login, Item

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

class Profile(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    logout = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)



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