from persistence import *
import sys

def main(args: list[str]):
    inputfilename: str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(", ")
            product_id, quantity, activator_id, date = splittedline
            quantity = int(quantity)
            product = repo.products.find(id=product_id)[0]
            if quantity < 0 and product.quantity + quantity < 0:
                continue
            repo.activities.insert(Activitie(product_id, quantity, activator_id, date))
            product.quantity += quantity
            repo.products.update(product)  # Update the product

if __name__ == '__main__':
    main(sys.argv)
