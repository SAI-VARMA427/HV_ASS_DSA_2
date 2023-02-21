# Question 2 - 
# Create a program that allows users to enter customer data.
# The customer data should include the following information:

# Customer Id
# Customer Name
# Purchase date(dd/mm/yy)
# Bill amount

# Store this information in a linked list. The program should provide three options for viewing information:

# View all customer data in sorted order based on bill amount
# View the total purchase amount for a specific year
# View details of a specific customer based on name


class Customer:
    def _init_(self, id, name, purchase_date, bill_amount):
        self.id = id
        self.name = name
        self.purchase_date = purchase_date
        self.bill_amount = bill_amount
        self.next = None

class CustomerDatabase:
    def _init_(self):
        self.head = None

    def add_customer(self, id, name, purchase_date, bill_amount):
        new_customer = Customer(id, name, purchase_date, bill_amount)
        if not self.head:
            self.head = new_customer
        else:
            current = self.head
            while current.next and current.next.bill_amount < bill_amount:
                current = current.next
            new_customer.next = current.next
            current.next = new_customer

    def view_all_customers(self):
        current = self.head
        while current:
            print(f"ID: {current.id}, Name: {current.name}, Purchase Date: {current.purchase_date}, Bill Amount: {current.bill_amount}")
            current = current.next

    def view_total_purchase_amount_for_year(self, year):
        total_purchase_amount = 0
        current = self.head
        while current:
            if current.purchase_date[-2:] == year:
                total_purchase_amount += current.bill_amount
            current = current.next
        print(f"Total purchase amount for {year}: {total_purchase_amount}")

    def view_customer_details_by_name(self, name):
        current = self.head