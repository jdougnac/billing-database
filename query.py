import mysql.connector as mysql

db = mysql.connect(user='root', password='',
                              host='127.0.0.1',
                              database='billing')



#a simple query selecting all results from the
#given parameters
def selectAll(parameters, table):    
    request="SELECT "+parameters+" FROM "+table
    cursor=db.cursor()
    cursor.execute(request)    
    results = cursor.fetchall()
    return results

#this makes a query with a single select where
def selectWhere(parameters, table, where, amount):
    if type(amount)==int and amount >0:
        request="SELECT "+parameters+" FROM "+table+" WHERE "+where+"="+str(amount)    
        cursor=db.cursor()
        cursor.execute(request)    
        results = cursor.fetchall()    
        return results
    else:
        raise Exception('Amounts must be positive integers.')


def insert( table, columns, values):
    request="INSERT INTO " +table+" ("+columns+") VALUES "+values+";"    
    cursor=db.cursor()
    cursor.execute(request)    
    db.commit()
    print("The database has been updated")



def createInvoice(storeID,customerID,date,productInfo):
    try:
        invoiceRequest='INSERT INTO invoice(store_id,customer_id,invoice_date) VALUES '+'('+str(storeID)+', '+str(customerID)+', '+date+')'
        cursor=db.cursor()
        cursor.execute(invoiceRequest)            
        invoice_id=str(cursor.lastrowid)
        #this loops creates the insert for each product on the product detail
        for product in productInfo:            
            if type(product[0])==int and type(product[1])==int and product[0]>0 and product[1]>0:
                product_id=product[0]
                currentPriceRequest='SELECT product_name, available_stock, product_price  FROM product WHERE product_id='+str(product_id)
                cursor=db.cursor()
                cursor.execute(currentPriceRequest)
                results = cursor.fetchall()
                currentPrice=results[0][2]
                product_name=results[0][0]
                current_stock=results[0][1]
                amount_purchased=product[1]
                if current_stock >=amount_purchased:
                    detailRequest='INSERT INTO purchase_detail(invoice_id,product_id,current_price,amount_purchased) VALUES '+'('+str(invoice_id)+','+str(product_id)+','+str(currentPrice)+','+str(amount_purchased)+')'
                    cursor=db.cursor()
                    cursor.execute(detailRequest)
                    cursor=db.cursor()
                    stockAdjustmentRequest='UPDATE product SET available_stock = available_stock -' +str(amount_purchased)+ ' WHERE product_id='+' '+str(product_id)+';'
                    cursor.execute(stockAdjustmentRequest)                    
                else:
                    raise Exception('{} only has {} units left, and you requested {}, please wait for stock replenishment or adjust your order accordingly'.format(product_name,current_stock,amount_purchased)) 
            else:
                raise Exception('Product details must be positive integers.')
        db.commit()
        print('Invoice Sucessfully Created')
    except mysql.Error as error:
        print("Failed inserting record into table {}".format(error))
        db.rollback()

#this function deletes a given invoice and adds the amount purchased to
#each product's available stock        
def deleteInvoice(invoiceID):
    try:
        detailRequest='SELECT product_id FROM purchase_detail WHERE invoice_id='+str(invoiceID)
        cursor=db.cursor()
        cursor.execute(detailRequest)
        results=cursor.fetchall()
        #this loop takes the product from the invoice and, prior to its deletion, adds up the amount of
        #stock the order implied. The idea is that, if you cancel an order for 10 boxes, those 10 boxes
        #should become available again
        for item in results:
            temp=int(item[0])            
            tempRequest='SELECT amount_purchased FROM purchase_detail WHERE product_id='+str(temp)+' AND invoice_id='+str(invoiceID)          
            cursor=db.cursor()
            cursor.execute(tempRequest)
            tempResults=cursor.fetchall()            
            updateStockRequest='UPDATE product SET available_stock = available_stock +' +str(tempResults[0][0])+ ' WHERE product_id='+' '+str(temp)            
            cursor=db.cursor()
            cursor.execute(updateStockRequest)     
        deleteRequest='DELETE FROM invoice WHERE invoice_id=' + str(invoiceID)
        cursor=db.cursor()
        cursor.execute(deleteRequest)
        db.commit()
    except mysql.Error as error:
        print("Failed deleting record from table {}".format(error))
        db.rollback()    

   
deleteInvoice(49)
