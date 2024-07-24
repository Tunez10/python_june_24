'''
create a product object 
name, description, brand, model, price
return Discount

calculate the total number of object price
'''



class Products():

    def __init__(self, name, description, brand, model, price):
        self.name = name
        self.description = description
        self.brand = brand
        self.model = model
        self.price = price

    
    def promo(self):
        if self.brand.casefold() == 'iphone':
            price = self.price
            discountPrice = 10/100 * price 
            discount = price - discountPrice
            return f'former price - {price} discount - {discount} 10% off'
        
        elif self.brand.casefold() == 'Samsung':
            price = self.price
            discountPrice = 15/100 * price 
            discount = price - discountPrice
            return f'former price - {price} discount - {discount} 15% off'
        
        elif self.brand.casefold() == 'infinix':
            price = self.price
            discountPrice = 20/100 * price 
            discount = price - discountPrice
            return f'former price - {price} discount - {discount} 20% off'
        
        elif self.brand.casefold() == 'tecno':
            price = self.price
            discountPrice = 20/100 * price 
            discount = price - discountPrice
            return f'former price - {price} discount - {discount} 20% off'
        
        else:
            return f'{self.brand} cannot be found'
    
    def total(self):
        price1 = self
        

                

                
    

phone1 = Products(
    name = 'phone',
    description = 'sleek and derable, runs on IOS operating system',
    brand = 'Iphone',
    model = 'Iphone 14',
    price = 500000
)
phone2 = Products(
    name = 'Phone',
    description = 'High resolution touchscreen display with vibrant colors and contrast',
    brand = 'Samsung',
    model = 'Samsung Galaxy A22',
    price = 550000
)
phone3 = Products(
    name = 'Phone',
    description = 'sleek and slim design with a 6.7-inch AMOLED display with an Andriod 11 operating system' ,
    brand = 'infinix',
    model = 'infinix note 12',
    price = 350000
)
phone4 = Products(
    name = 'Phone',
    description = 'sleek design, HiOS 8.6 custom skin with a triple camera setup', 
    brand = 'Tecno',
    model = 'Tecno Camon 19',
    price = 200000
)
phone5 = Products(
    name = 'phone',
    description = 'sleek and derable, runs on IOS operating system',
    brand = 'Iphone',
    model = 'Iphone x',
    price = 250000
)
