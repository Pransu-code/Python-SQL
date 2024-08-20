import mysql.connector


def get_all_products():

    cnx = mysql.connector.connect(user='root', password='4707',
                                host='127.0.0.1',
                                database='gstore')


    cursor = cnx.cursor()
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uomcol FROM products INNER JOIN uom ON products.uom_id = uom.uom_id")
    cursor.execute(query)

    response = []

    for(product_id, name, uom_id, price_per_unit, uomcol) in cursor:
        response.append({
            'product_id': product_id, 
            'name': name, 
            'uom_id': uom_id,
            'price_per_unit': price_per_unit, 
            'uomcol': uomcol
        })


    cnx.close()

    return response
if __name__ == '__main__':
    print(get_all_products())