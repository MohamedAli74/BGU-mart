from persistence import *

def print_table(name, rows):
    print(name)
    for row in rows:
        print(row)

def main():
    print_table("Activities", repo.activities.find_all())
    print_table("Branches", repo.branches.find_all())
    print_table("Employees", repo.employees.find_all())
    print_table("Products", repo.products.find_all())
    print_table("Suppliers", repo.suppliers.find_all())

    # Detailed employees report
    employees = repo.employees.find_all()
    activities = repo.activities.find_all()
    sales_income = {e.id: 0 for e in employees}
    for activity in activities:
        if activity.quantity < 0:
            product = repo.products.find(id=activity.product_id)[0]
            sales_income[activity.activator_id] += -activity.quantity * product.price

    print("Employees Report")
    for employee in sorted(employees, key=lambda e: e.name):
        branche = repo.branches.find(id=employee.branche)[0].location
        print(f"{employee.name} {employee.salary} {branche} {sales_income[employee.id]}")

    # Detailed activity report
    print("Activities Report")
    for activity in sorted(activities, key=lambda a: a.date):
        product = repo.products.find(id=activity.product_id)[0]
        if activity.quantity > 0:
            supplier = repo.suppliers.find(id=activity.activator_id)[0]
            print(f"('{activity.date}', '{product.description}', {activity.quantity}, None, '{supplier.name}')")
        else:
            employee = repo.employees.find(id=activity.activator_id)[0]
            print(f"('{activity.date}', '{product.description}', {activity.quantity}, '{employee.name}', None)")

if __name__ == '__main__':
    main()
