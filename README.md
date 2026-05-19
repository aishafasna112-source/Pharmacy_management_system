# Pharmacy_management_system
This project consists of three main modules:Admin Module, Pharmacist Module, Inventory Manager Module.. By integrating the Admin, Pharmacist, and Inventory Manager modules, the system ensures smooth workflow, efficient inventory control, accurate billing, and secure management of pharmacy data.

Developed as a beginner/intermediate Python database project for learning pharmacy inventory and sales management systems.main purpose is to help manage pharmacy operations such as,User authentication,Medicine inventory,Sales tracking,
Role-based access.
The database module consists of  some activities like Connects to the SQLite database,Creates tables if they do not exist and Stores all application data.it is the foundation module of the project.

Authendication module named as auth.py it handles user registration and login.When a user enters system asks username and password and their role for registration.and this data stores in users table.After that they matching the username and password with previously stored data then get access to the login.if it fails then shows that login failed message.

The system manages pharmacy stock through the medicines table.Each medicine stores:Name,Quantity and Price.The inventory section can:
Add medicines,Update stock quantity,View available medicines,Manage prices.This helps pharmacists track available stock inside the pharmacy.

The sales system records medicine purchases.when a sale occures, there will take palce some actions ie,medicine is selected and the quantity of sold will be entered then its total price will calculate and everything will store in sales table.

the project built in a role based access so the admin getting full access fo the system and the pharmacist handles sales and medicines then the inventory manager focuses on the inventory area.

the workflow of this project shown below..

Start Program
      ↓
Create Database Tables
      ↓
Register or Login
      ↓
Authenticate User
      ↓
Access Features Based on Role
      ↓
Manage Medicines / Sales
      ↓
Store Data in SQLite Database



Summary:
This Pharmacy Management System is a small database-driven application that simulates real pharmacy operations.
It allows users to:
Register and log in
Manage medicine inventory
Record medicine sales
Store and retrieve data using SQLite.




















