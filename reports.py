import query
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics import renderPDF
from reportlab.lib.units import cm


def detail_invoice(invoiceNumber):
    #this query fetches all products for a given invoice
    firstQuery=query.selectWhere('*','invoice','invoice_id',invoiceNumber)    
    queryInvoiceStoreCityID=query.selectWhere('city_id','store','store_id',firstQuery[0][1])
    queryInvoiceStoreCity=query.selectWhere('city_name','city','city_id',queryInvoiceStoreCityID[0][0]) #name of the store's city
    queryInvoiceStoreCountyID=query.selectWhere('county_id','city','city_id',queryInvoiceStoreCityID[0][0])
    queryInvoiceStoreStateID=query.selectWhere('state_id','county','county_id',queryInvoiceStoreCountyID[0][0])
    queryInvoiceStoreState=query.selectWhere('state_name','state','state_id',queryInvoiceStoreStateID[0][0]) #name of the store's State

    detail=''
    rawDetail=[[]]
    rawDetail[0].append(queryInvoiceStoreCity[0][0]) #
    rawDetail[0].append(queryInvoiceStoreState[0][0]) #   
    invoiceDate=firstQuery[0][3]
    invoiceDate = datetime.datetime.strptime(str(invoiceDate), '%Y-%m-%d')
    invoiceDate=invoiceDate.strftime('%b %d,%Y')
    total=0
    detail+='Invoice Number: '+str(invoiceNumber)+'\n'
    rawDetail.append(str(invoiceNumber)) #Invoice Number
    detail+='Date: '+str(invoiceDate)+'\n'
    rawDetail.append(str(invoiceDate)) #Invoice Date
    rawDetail.append([])#rawDetail[3] has the products, each as a list
    queryInvoiceCustomerID= firstQuery[0][2]
    queryInvoiceCustomer= query.selectWhere('*','customer','customer_id',queryInvoiceCustomerID)
    queryInvoiceCustomerCity = query.selectWhere('*','city','city_id',queryInvoiceCustomer[0][1])
    queryInvoiceCustomerCounty = query.selectWhere('*','county','county_id',queryInvoiceCustomerCity[0][1])
    queryInvoiceCustomerState = query.selectWhere('*','state','state_id',queryInvoiceCustomerCounty[0][1])    
    rawDetail.append(queryInvoiceCustomer)
    rawDetail.append(queryInvoiceCustomerCity)
    rawDetail.append(queryInvoiceCustomerCounty)
    rawDetail.append(queryInvoiceCustomerState)
    queryInvoice=query.selectWhere('*','purchase_detail','invoice_id',invoiceNumber)
    #this loop fetches and prints the detail of each product: ID number, price, and amount purchased
    for x in queryInvoice:
        rawDetail[3].append([])
        queryProduct=query.selectWhere('*','product','product_id',int(x[1]))
        rawDetail[3][-1].append(str(x[1])) #code
        rawDetail[3][-1].append(str(queryProduct[0][1])) #product name
        rawDetail[3][-1].append(str(x[2])) # price
        rawDetail[3][-1].append(str(x[3])) #amount
        rawDetail[3][-1].append(str(x[2]*x[3])) #sub total
        detail+="Code: "+str(x[1])+". Product: "+ str(queryProduct[0][1])+". Price: "+str(x[2])+". Amount: "+str(x[3])+". Subtotal: "+str(x[2]*x[3])+"\n"        
        total+=x[2]*x[3]
    rawDetail.append(str(total))
    detail+="Total: "+str(total)+"\n"
    #this looks for the customer's details in order to add them to the invoice
    queryCustomer=query.selectWhere('customer_id','invoice','invoice_id',invoiceNumber  )  
    queryCustomerDetails = query.selectWhere('*','customer','customer_id',queryCustomer[0][0])
    queryCity = query.selectWhere('city_name','city','city_id',queryCustomerDetails[0][1])
    detail+="Client: "+str(queryCustomerDetails[0][6])+" "+str(queryCustomerDetails[0][7])+" ID: "+str(queryCustomerDetails[0][0])+" Address: "+str(queryCustomerDetails[0][8])+" "+str(queryCustomerDetails[0][9])+str(queryCustomerDetails[0][10])+","+queryCity[0][0]+"\n"
    return(detail, rawDetail)



def detail_product(productNumber):
    #this query fetches the information available on any given product
    queryProduct=query.selectWhere('*','product','product_id',productNumber)    
    product_detail="ID: "+str(queryProduct[0][0])+" Product: "+queryProduct[0][1]+" Available Stock: "+str(queryProduct[0][2])+" Current Price: "+str(queryProduct[0][3])
    product_rawDetail=[]
    product_rawDetail.append(queryProduct[0][1])
    product_rawDetail.append(queryProduct[0][3])
    product_rawDetail.append(queryProduct[0][2])
    
    return(product_detail, product_rawDetail)


def detail_customer(customerNumber):
    #this query fetches the information available on any given customer
    queryCustomer= query.selectWhere('*','customer','customer_id',customerNumber)
    queryCity = query.selectWhere('*','city','city_id',queryCustomer[0][1])
    queryCounty = query.selectWhere('*','county','county_id',queryCity[0][1])
    queryState = query.selectWhere('*','state','state_id',queryCounty[0][1])
    queryGender=query.selectWhere('*','gender','gender_id',queryCustomer[0][3])
    queryCustomerType=query.selectWhere('*','customer_type','customer_type_id',queryCustomer[0][2])
    customer_rawDetail=[]
    
    customer_rawDetail.append(queryCustomer[0][0])    #system ID
    customer_rawDetail.append(queryCustomer[0][6])    #first name
    customer_rawDetail.append(queryCustomer[0][7])    #last name
    customer_rawDetail.append(queryCustomer[0][5])    #state ID
    customer_rawDetail.append(queryCustomer[0][4])    #age
    customer_rawDetail.append(queryGender[0][1])      #gender
    customer_rawDetail.append(queryCustomerType[0][1])#customer type
    customer_rawDetail.append(queryCustomer[0][11])   #phone number
    customer_rawDetail.append(queryCustomer[0][8])    #street
    customer_rawDetail.append(queryCustomer[0][9])    #street number
    customer_rawDetail.append(queryCustomer[0][10])   #address detail
    customer_rawDetail.append(queryCity[0][2])        #city
    customer_rawDetail.append(queryCounty[0][2])      #county
    customer_rawDetail.append(queryState[0][1])       #state
    
    customer_detail=" System ID: "+str(queryCustomer[0][0])+" Name: "+queryCustomer[0][6]+" "+str(queryCustomer[0][7])+" Age: "+str(queryCustomer[0][4])+" ID No "+str(queryCustomer[0][5])+" Phone Number: "+ str(queryCustomer[0][11])+"\n"+"Address: "+str(queryCustomer[0][8])+" "+str(queryCustomer[0][9])+", "+str(queryCity[0][2])+", "+str(queryCounty[0][2])+", "+str(queryState[0][1])
    return(customer_detail, customer_rawDetail)
detail_customer(1)
def invoiceReport():
    #this makes a report in PDF with all the invoices
    c=canvas.Canvas('Invoice Report.pdf')
    w, h = A4
    invoiceQuery=query.selectAll('invoice_id','invoice')
    invoiceQuery=sorted(invoiceQuery)
    firstList=[]
    finalList=[]
    #these two loops clean the list we got by invoiceQuery
    #in order for it to be good for using on the third loop
    for item in invoiceQuery:
        f=str(item)
        firstList.append(f[1:-2])
    for iitem in firstList:
        finalList.append(int(iitem))
    #this loop adds the barcode and the details to the PDF document
    for invoice in finalList:
        barcode_value ="111"+"0"*(9-(len(str(invoice))))+str(invoice)    
        baarcode = eanbc.Ean13BarcodeWidget(barcode_value,barHeight=.5*cm,barWidth = 1.2)
        d = Drawing()  
        d.add(baarcode)
        renderPDF.draw(d, c, 150, h-65)        
        text = c.beginText(50, h-55)
        text.setFont("Times-Roman", 12)
        prelimInvoice=detail_invoice(invoice).split('\n')        
        for segment in prelimInvoice:
            text.textLine(segment)        
        c.drawText(text)
        h-=100
        if h <= 150:
            c.showPage()
            h=741.8897637795277        
    c.save()


def detail_store(storeNumber):
    #this query fetches the information available on any given store
    queryStore=query.selectWhere('*','store','store_id',storeNumber)    
    queryStoreCityID=query.selectWhere('city_id','store','store_id',queryStore[0][0])
    queryStoreCity=query.selectWhere('city_name','city','city_id',queryStoreCityID[0][0]) #name of the store's city
    queryStoreCountyID=query.selectWhere('county_id','city','city_id',queryStoreCityID[0][0])
    queryStoreCounty=query.selectWhere('county_name','county','county_id',queryStoreCountyID[0][0])#name of the store's county
    queryStoreStateID=query.selectWhere('state_id','county','county_id',queryStoreCountyID[0][0])
    queryStoreState=query.selectWhere('state_name','state','state_id',queryStoreStateID[0][0]) #name of the store's State    
    store_detail=[]
    store_detail.append(queryStoreCity[0][0])
    store_detail.append(queryStoreCounty[0][0])
    store_detail.append(queryStoreState[0][0])
    store_detail.append(queryStore[0][2])
    store_detail.append(queryStore[0][3])
    store_detail.append(queryStore[0][4])
    store_detail.append(queryStore[0][5])    
    return(store_detail)    



    





