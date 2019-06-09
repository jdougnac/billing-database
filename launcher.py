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
    queryInvoiceDate=query.selectWhere('invoice_date','invoice','invoice_id',invoiceNumber)
    queryInvoice=query.selectWhere('*','purchase_detail','invoice_id',invoiceNumber)
    detail=''    
    invoiceDate=queryInvoiceDate[0][0]
    invoiceDate = datetime.datetime.strptime(str(invoiceDate), '%Y-%m-%d')
    invoiceDate=invoiceDate.strftime('%b %d,%Y')
    
    total=0
    detail+='Invoice Number: '+str(invoiceNumber)+'\n'
    detail+='Date: '+str(invoiceDate)+'\n'
    #this loop fetches and prints the detail of each product: ID number, price, and amount purchased
    for x in queryInvoice:
        queryProduct=query.selectWhere('*','product','product_id',int(x[1]))
        detail+="Code: "+str(x[1])+". Product: "+ str(queryProduct[0][1])+". Price: "+str(x[2])+". Amount: "+str(x[3])+". Subtotal: "+str(x[2]*x[3])+"\n"
        total+=x[2]*x[3]    
    detail+="Total: "+str(total)+"\n"
    #this looks for the customer's details in order to add them to the invoice
    queryCustomer=query.selectWhere('customer_id','invoice','invoice_id',invoiceNumber  )  
    queryCustomerDetails = query.selectWhere('*','customer','customer_id',queryCustomer[0][0])
    queryCity = query.selectWhere('city_name','city','city_id',queryCustomerDetails[0][1])
    detail+="Client: "+str(queryCustomerDetails[0][6])+" "+str(queryCustomerDetails[0][7])+" ID: "+str(queryCustomerDetails[0][0])+" Address: "+str(queryCustomerDetails[0][8])+" "+str(queryCustomerDetails[0][9])+str(queryCustomerDetails[0][10])+","+queryCity[0][0]+"\n"
    return(detail)



def detail_product(productNumber):
    #this query fetches the information available on any given product
    queryProduct=query.selectWhere('*','product','product_id',productNumber)    
    product_detail="ID: "+str(queryProduct[0][0])+" Product: "+queryProduct[0][1]+" Available Stock: "+str(queryProduct[0][2])+" Current Price: "+str(queryProduct[0][3])
    return(product_detail)


def detail_customer(customerNumber):
    #this query fetches the information available on any given customer
    queryCustomer= query.selectWhere('*','customer','customer_id',customerNumber)
    queryCity = query.selectWhere('*','city','city_id',queryCustomer[0][1])
    queryCounty = query.selectWhere('*','county','county_id',queryCity[0][1])
    queryState = query.selectWhere('*','state','state_id',queryCounty[0][1])
    customer_detail=" System ID: "+str(queryCustomer[0][0])+" Name: "+queryCustomer[0][6]+" "+str(queryCustomer[0][7])+" Age: "+str(queryCustomer[0][4])+" ID No "+str(queryCustomer[0][5])+" Phone Number: "+ str(queryCustomer[0][11])+"\n"+"Address: "+str(queryCustomer[0][8])+" "+str(queryCustomer[0][9])+", "+str(queryCity[0][2])+", "+str(queryCounty[0][2])+", "+str(queryState[0][1])
    return(customer_detail)

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


    




