from tkinter import *
from tkinter import ttk
from tkinter import Tk, Checkbutton, DISABLED
import reports
import query

class MyApp(Tk):
 
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        self.frames = {}
        #here area the different tabs
        for F in (Start, Invoice, Customer, Product, CreateInvoice):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky = NSEW)
        self.show_frame(Start)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def get_page(self, classname):
        '''Returns an instance of a page given its class name as a string'''
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None

class Start(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Start').grid()

        invoiceButton = ttk.Button(self, text='Invoice',
                                  command=lambda: controller.show_frame(Invoice))
        customerButton = ttk.Button(self, text='Customer',
                                  command=lambda: controller.show_frame(Customer))
        productButton = ttk.Button(self, text='Product',
                                  command=lambda: controller.show_frame(Product))
        createInvoiceButton = ttk.Button(self, text='Create Invoice',
                                  command=lambda: controller.show_frame(CreateInvoice))        
        #change button command
        reportButton = ttk.Button(self, text='Product',
                                  command=lambda: controller.show_frame(Product))            
        invoiceButton.grid()
        customerButton.grid()
        productButton.grid()
        createInvoiceButton.grid()


class Invoice(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Invoice').grid()
        self.invoiceID=Label(self, text ="ID:")
        self.invoiceIDTXT=Entry(self)
        #change button command
        searchInvoiceButton = ttk.Button(self, text='Search',  
                                  command=lambda: loadInvoice(int(self.invoiceIDTXT.get())))
        self.invoiceDate=Label(self, text ="Date:")
        self.invoiceDateTXT=Entry(self)
        self.invoiceStore=Label(self, text ="Store:")
        self.invoiceStoreTXT=Entry(self)
        self.invoiceCustomer=Label(self, text ="Customer:")
        self.invoiceCustomerID=Label(self, text ="ID:")
        self.invoiceCustomerIDTXT=Entry(self)        
        self.invoiceCustomerFirstName=Label(self, text ="First Name:")
        self.invoiceCustomerFirstNameTXT=Entry(self)
        self.invoiceCustomerLastName=Label(self, text ="Last Name:")
        self.invoiceCustomerLastNameTXT=Entry(self)
        self.invoiceCustomerAddress=Label(self, text ="Address:")
        self.invoiceCustomerAddressStreet=Label(self, text ="Street:")
        self.invoiceCustomerAdressStreetTXT=Entry(self)        
        self.invoiceCustomerAddressNumber=Label(self, text ="Number:")
        self.invoiceCustomerAddressNumberTXT=Entry(self)
        self.invoiceCustomerAdressExtra=Label(self, text ="Extra:")
        self.invoiceCustomerAdressExtraTXT=Entry(self)
        self.invoiceCustomerAdressCity=Label(self, text ="City:")
        self.invoiceCustomerAdressCityTXT=Entry(self)        
        self.productLabel=Label(self, text ="Products:")
        #create the query and, for each product, create a loop. Also, create
        #a loop on the grid section in order to put the products in the right
        #order.
        startButton = ttk.Button(self, text='Start',
                             command=lambda: controller.show_frame(Start))
        customerButton = ttk.Button(self, text='Customer',
                                  command=lambda: controller.show_frame(Customer))       

        self.invoiceID.grid(row=1,column=0)
        self.invoiceIDTXT.grid(row=1,column=1)
        searchInvoiceButton.grid(row=1, column=2)                                  
        self.invoiceDate.grid(row=2,column=2)
        self.invoiceDateTXT.grid(row=2,column=3)
        self.invoiceStore.grid(row=3,column=0)
        self.invoiceStoreTXT.grid(row=3,column=1)
        self.invoiceCustomer.grid(row=4, column=0)
        self.invoiceCustomerID.grid(row=5, column=0)
        self.invoiceCustomerIDTXT.grid(row=6, column=0) 
        self.invoiceCustomerFirstName.grid(row=5, column=1)
        self.invoiceCustomerFirstNameTXT.grid(row=6, column=1)
        self.invoiceCustomerLastName.grid(row=5, column=2)
        self.invoiceCustomerLastNameTXT.grid(row=6, column=2)
        self.invoiceCustomerAddress.grid(row=7, column=0)
        self.invoiceCustomerAddressStreet.grid(row=8, column=0)
        self.invoiceCustomerAdressStreetTXT.grid(row=9, column=0)
        self.invoiceCustomerAddressNumber.grid(row=8, column=1)
        self.invoiceCustomerAddressNumberTXT.grid(row=9, column=1)
        self.invoiceCustomerAdressExtra.grid(row=8, column=2)
        self.invoiceCustomerAdressExtraTXT.grid(row=9, column=2)
        self.invoiceCustomerAdressCity.grid(row=8, column=3)
        self.invoiceCustomerAdressCityTXT.grid(row=9, column=3)
        self.productLabel.grid(row=10, column=0)

        startButton.grid(row=0, column=4)
        customerButton.grid(row=1, column=4)
        
        def loadInvoice(invoiceID):
            get_invoice=self.controller.get_page('Invoice')
            tempInvoice=reports.detail_invoice(invoiceID)[1]
            get_invoice.invoiceDateTXT.delete(0,END)
            get_invoice.invoiceDateTXT.insert(0,tempInvoice[2])
            get_invoice.invoiceStoreTXT.delete(0,END)
            get_invoice.invoiceStoreTXT.insert(0,tempInvoice[0][0]+', '+tempInvoice[0][1])
            for item in tempInvoice:
                print('zz',item)
            get_invoice.invoiceCustomerIDTXT.delete(0,END)
            get_invoice.invoiceCustomerIDTXT.insert(0,tempInvoice[4][0][0])            
            get_invoice.invoiceCustomerFirstNameTXT.delete(0,END)
            get_invoice.invoiceCustomerFirstNameTXT.insert(0,tempInvoice[4][0][6])                                        
            get_invoice.invoiceCustomerLastNameTXT.delete(0,END)
            get_invoice.invoiceCustomerLastNameTXT.insert(0,tempInvoice[4][0][7])                                         
            get_invoice.invoiceCustomerAdressStreetTXT.delete(0,END)
            get_invoice.invoiceCustomerAdressStreetTXT.insert(0,tempInvoice[4][0][8])                                              
            get_invoice.invoiceCustomerAddressNumberTXT.delete(0,END)
            get_invoice.invoiceCustomerAddressNumberTXT.insert(0,tempInvoice[4][0][9])                                              
            get_invoice.invoiceCustomerAdressExtraTXT.delete(0,END)
            get_invoice.invoiceCustomerAdressExtraTXT.insert(0,tempInvoice[4][0][10])                                            
            get_invoice.invoiceCustomerAdressCityTXT.delete(0,END)
            get_invoice.invoiceCustomerAdressCityTXT.insert(0,tempInvoice[5][0][2])
            total=0
            productRow=11
            #this loop deletes all existing products, in order
            #for the window to properly show the corresponding products
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) >= productRow:
                    label.grid_forget()
            for product in tempInvoice[3]:
                self.invoiceProductID=Label(self, text ="ID:")                
                self.invoiceProductIDTXT=Entry(self)
                self.invoiceProductName=Label(self, text ="Name:")
                self.invoiceProductNameTXT=Entry(self)
                self.invoiceProductPrice=Label(self, text ="Price:")
                self.invoiceProductPriceTXT=Entry(self)
                self.invoiceProductAmount=Label(self, text = "Amount:")
                self.invoiceProductAmountTXT=Entry(self)                
                self.invoiceProductSubtotal=Label(self, text = "Subtotal:")
                self.invoiceProductSubtotalTXT=Entry(self)
                

                self.invoiceProductID.grid(row=productRow,column=0)                
                self.invoiceProductName.grid(row=productRow,column=1)                
                self.invoiceProductPrice.grid(row=productRow,column=2)                
                self.invoiceProductAmount.grid(row=productRow,column=3)                           
                self.invoiceProductSubtotal.grid(row=productRow,column=4)
                productRow+=1
                self.invoiceProductIDTXT.grid(row=productRow,column=0)
                self.invoiceProductNameTXT.grid(row=productRow,column=1)
                self.invoiceProductPriceTXT.grid(row=productRow,column=2)
                self.invoiceProductAmountTXT.grid(row=productRow,column=3)   
                self.invoiceProductSubtotalTXT.grid(row=productRow,column=4)
                productRow+=1
                            
                self.invoiceProductIDTXT.insert(0,product[0])
                self.invoiceProductNameTXT.insert(0,product[1])
                self.invoiceProductPriceTXT.insert(0,product[2])
                self.invoiceProductAmountTXT.insert(0,product[3])
                self.invoiceProductSubtotalTXT.insert(0,product[4])              
               
            self.invoiceTotal=Label(self, text ="Total:") 
            self.invoiceTotalTXT=Entry(self)
            self.invoiceTotal.grid(row=productRow,column=4)
            productRow+=1
            self.invoiceTotalTXT.grid(row=productRow,column=4)
            productRow+=1
            self.invoiceTotalTXT.insert(0,tempInvoice[8])
         





class Customer(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Customer').grid()
        self.invoiceCustomerID=Label(self, text ="ID:")
        self.invoiceCustomerIDTXT=Entry(self)
        #change button command
        searchCustomerButton = ttk.Button(self, text='Search',  
                                  command=lambda: loadCustomer(int(self.invoiceCustomerIDTXT.get())))       
        self.invoiceCustomerFirstName=Label(self, text ="First Name:")
        self.invoiceCustomerFirstNameTXT=Entry(self)
        self.invoiceCustomerLastName=Label(self, text ="Last Name:")
        self.invoiceCustomerLastNameTXT=Entry(self)
        self.invoiceCustomerStateID=Label(self, text ="State ID:")
        self.invoiceCustomerStateIDTXT=Entry(self)

        self.invoiceCustomerAge=Label(self, text ="Age:")
        self.invoiceCustomerAgeTXT=Entry(self)
        self.invoiceCustomerGender=Label(self, text ="Gender:")
        self.invoiceCustomerGenderTXT=Entry(self)        
        self.invoiceCustomerType=Label(self, text ="Customer Type:")
        self.invoiceCustomerTypeTXT=Entry(self)
        self.invoiceCustomerTelephone=Label(self, text ="Phone Number:")
        self.invoiceCustomerTelephoneTXT=Entry(self)        
        
        self.invoiceCustomerAddress=Label(self, text ="Address:")
        self.invoiceCustomerAddressStreet=Label(self, text ="Street:")
        self.invoiceCustomerAdressStreetTXT=Entry(self)        
        self.invoiceCustomerAddressNumber=Label(self, text ="Number:")
        self.invoiceCustomerAddressNumberTXT=Entry(self)
        self.invoiceCustomerAdressExtra=Label(self, text ="Extra:")
        self.invoiceCustomerAdressExtraTXT=Entry(self)
        self.invoiceCustomerAdressCity=Label(self, text ="City:")
        self.invoiceCustomerAdressCityTXT=Entry(self)
        self.invoiceCustomerAdressCounty=Label(self, text ="County:")
        self.invoiceCustomerAdressCountyTXT=Entry(self)
        self.invoiceCustomerAdressState=Label(self, text ="State:")
        self.invoiceCustomerAdressStateTXT=Entry(self)          
        

        startButton = ttk.Button(self, text='Start',
                                  command=lambda: controller.show_frame(Start))
        invoiceButton = ttk.Button(self, text='Invoice',
                                  command=lambda: controller.show_frame(Invoice))
        productButton = ttk.Button(self, text='Product',
                                  command=lambda: controller.show_frame(Product)) 
        
        self.invoiceCustomerID.grid(row=1, column=0)
        self.invoiceCustomerIDTXT.grid(row=1, column=1)
        searchCustomerButton.grid(row=1, column=2)
        self.invoiceCustomerFirstName.grid(row=3, column=0)
        self.invoiceCustomerFirstNameTXT.grid(row=4, column=0)
        self.invoiceCustomerLastName.grid(row=3, column=1)
        self.invoiceCustomerLastNameTXT.grid(row=4, column=1)
        self.invoiceCustomerStateID.grid(row=3, column=2)
        self.invoiceCustomerStateIDTXT.grid(row=4, column=2)

        self.invoiceCustomerAge.grid(row=5, column=0)
        self.invoiceCustomerAgeTXT.grid(row=6, column=0)
        self.invoiceCustomerGender.grid(row=5, column=1)
        self.invoiceCustomerGenderTXT.grid(row=6, column=1)        
        self.invoiceCustomerType.grid(row=5, column=2)
        self.invoiceCustomerTypeTXT.grid(row=6, column=2)
        self.invoiceCustomerTelephone.grid(row=5, column=3)
        self.invoiceCustomerTelephoneTXT.grid(row=6, column=3)        

        
        self.invoiceCustomerAddress.grid(row=7, column=0)
        self.invoiceCustomerAddressStreet.grid(row=8, column=0)
        self.invoiceCustomerAdressStreetTXT.grid(row=9, column=0)
        self.invoiceCustomerAddressNumber.grid(row=8, column=1)
        self.invoiceCustomerAddressNumberTXT.grid(row=9, column=1)
        self.invoiceCustomerAdressExtra.grid(row=8, column=2)
        self.invoiceCustomerAdressExtraTXT.grid(row=9, column=2)
        self.invoiceCustomerAdressCity.grid(row=10, column=0)
        self.invoiceCustomerAdressCityTXT.grid(row=11, column=0)        
        self.invoiceCustomerAdressCounty.grid(row=10, column=1)
        self.invoiceCustomerAdressCountyTXT.grid(row=11, column=1) 
        self.invoiceCustomerAdressState.grid(row=10, column=2)
        self.invoiceCustomerAdressStateTXT.grid(row=11, column=2)
        


        invoiceButton.grid()
        startButton.grid()
        productButton.grid()

        def loadCustomer(customerID):
            get_customer=self.controller.get_page('Customer')
            tempCustomer=reports.detail_customer(customerID)[1]
            print(tempCustomer)
            get_customer.invoiceCustomerFirstNameTXT.delete(0,END)
            get_customer.invoiceCustomerFirstNameTXT.insert(0,tempCustomer[1])
            get_customer.invoiceCustomerLastNameTXT.delete(0,END)
            get_customer.invoiceCustomerLastNameTXT.insert(0,tempCustomer[2])
            get_customer.invoiceCustomerStateIDTXT.delete(0,END)
            get_customer.invoiceCustomerStateIDTXT.insert(0,tempCustomer[3])
            get_customer.invoiceCustomerAgeTXT.delete(0,END)
            get_customer.invoiceCustomerAgeTXT.insert(0,tempCustomer[4])
            get_customer.invoiceCustomerGenderTXT.delete(0,END)
            get_customer.invoiceCustomerGenderTXT.insert(0,tempCustomer[5])
            get_customer.invoiceCustomerTypeTXT.delete(0,END)
            get_customer.invoiceCustomerTypeTXT.insert(0,tempCustomer[6])
            get_customer.invoiceCustomerTelephoneTXT.delete(0,END)
            get_customer.invoiceCustomerTelephoneTXT.insert(0,tempCustomer[7])
            get_customer.invoiceCustomerAdressStreetTXT.delete(0,END)
            get_customer.invoiceCustomerAdressStreetTXT.insert(0,tempCustomer[8])
            get_customer.invoiceCustomerAddressNumberTXT.delete(0,END)
            get_customer.invoiceCustomerAddressNumberTXT.insert(0,tempCustomer[9])
            get_customer.invoiceCustomerAdressExtraTXT.delete(0,END)
            get_customer.invoiceCustomerAdressExtraTXT.insert(0,tempCustomer[10])
            get_customer.invoiceCustomerAdressCityTXT.delete(0,END)
            get_customer.invoiceCustomerAdressCityTXT.insert(0,tempCustomer[11])
            get_customer.invoiceCustomerAdressCountyTXT.delete(0,END)
            get_customer.invoiceCustomerAdressCountyTXT.insert(0,tempCustomer[12])
            get_customer.invoiceCustomerAdressStateTXT.delete(0,END)
            get_customer.invoiceCustomerAdressStateTXT.insert(0,tempCustomer[13])
            

                


class Product(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Product').grid()
        self.productID=Label(self, text ="ID:")      
        self.productIDTXT=Entry(self)
        #change button command
        searchProductButton = ttk.Button(self, text='Search',  
                                  command=lambda: loadProduct(int(self.productIDTXT.get())))

        self.productName=Label(self, text ="Product:")
        self.productNameTXT=Entry(self)
        self.productPrice=Label(self, text ="Price:")
        self.productPriceTXT=Entry(self)         
        self.productStock=Label(self, text ="Available Stock:")
        self.productStockTXT=Entry(self)        
       
        startButton = ttk.Button(self, text='Start',
                             command=lambda: controller.show_frame(Start))
        customerButton = ttk.Button(self, text='Customer',
                                  command=lambda: controller.show_frame(Customer))       

        self.productID.grid(row=1, column=0)           
        self.productIDTXT.grid(row=1, column=1)
        searchProductButton.grid(row=1, column=2) 
        self.productName.grid(row=2, column=0)
        self.productNameTXT.grid(row=3, column=0)
        self.productPrice.grid(row=2, column=1)
        self.productPriceTXT.grid(row=3, column=1)        
        self.productStock.grid(row=2, column=2)
        self.productStockTXT.grid(row=3, column=2)

        
        startButton.grid()                
        customerButton.grid()
        def loadProduct(productID):
            get_product=self.controller.get_page('Product')
            tempProduct=reports.detail_product(productID)[1]
            print(tempProduct)
            get_product.productNameTXT.delete(0,END)
            get_product.productNameTXT.insert(0,tempProduct[0])
            get_product.productPriceTXT.delete(0,END)
            get_product.productPriceTXT.insert(0,tempProduct[1])
            get_product.productStockTXT.delete(0,END)
            get_product.productStockTXT.insert(0,tempProduct[2])   


class CreateInvoice(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        


        self.invoiceDateDay = StringVar()        
        self.createInvoiceDay=Label(self, text ="Day:")
        self.createInvoiceDayDrop= OptionMenu(self,self.invoiceDateDay,'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
        self.invoiceDateMonth = StringVar()
        self.createInvoiceMonth=Label(self, text ="Month:")
        self.createInvoiceMonthDrop= OptionMenu(self,self.invoiceDateMonth,'01','02','03','04','05','06','07','08','09','10','11','12')
        self.invoiceDateYear = StringVar()
        self.createInvoiceYear=Label(self, text ="Year:")
        self.createInvoiceYearDrop= OptionMenu(self,self.invoiceDateYear,'2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040','2041','2042','2043','2044','2045','2046','2047','2048','2049','2050')                                                                    
        self.createInvoiceDayTXT=Entry(self)
        self.createInvoiceMonthTXT=Entry(self)
        self.createInvoiceYearTXT=Entry(self)
        #change command
        addDateButton = ttk.Button(self, text='Add Date', command=lambda: loadDate(self.invoiceDateDay.get(), self.invoiceDateMonth.get(),self.invoiceDateYear.get()))

                                   

        self.createInvoiceStoreID=Label(self, text ="Store ID:")
        self.createInvoiceStoreIDTXT=Entry(self)
        self.createInvoiceStoreStreet=Label(self, text ="Street:")
        self.createInvoiceStoreStreetTXT=Entry(self)
        self.createInvoiceStoreNumber=Label(self, text ="Number:")
        self.createInvoiceStoreNumberTXT=Entry(self)
        self.createInvoiceStoreDetail=Label(self, text ="Detail:")
        self.createInvoiceStoreDetailTXT=Entry(self)

        self.createInvoiceProduct=Label(self, text ="Product:")        
        self.createInvoiceProductID=Label(self, text ="ID:")
        self.createInvoiceProductIDTXT=Entry(self)
        self.createInvoiceProductAmount=Label(self, text ="Amount:")
        self.createInvoiceProductAmountTXT=Entry(self)
        addProductButton = ttk.Button(self, text='Add Product',
                             command=lambda: loadProduct(int(self.createInvoiceProductIDTXT.get()),int(self.createInvoiceProductAmountTXT.get())))

        self.createInvoiceProduct1ID=Label(self, text ="ID:")
        self.createInvoiceProduct1IDTXT=Entry(self)
        self.createInvoiceProduct1Name=Label(self, text ="Product:")
        self.createInvoiceProduct1NameTXT=Entry(self)
        self.createInvoiceProduct1Amount=Label(self, text ="Amount:")
        self.createInvoiceProduct1AmountTXT=Entry(self)
        self.createInvoiceProduct1Price=Label(self, text ="Price:")
        self.createInvoiceProduct1PriceTXT=Entry(self)
        self.createInvoiceProduct1Subtotal=Label(self, text ="Subtotal:")
        self.createInvoiceProduct1SubtotalTXT=Entry(self)
        removeProduct1Button = ttk.Button(self, text='Remove',
                                  command=lambda: removeProduct(1))            

        self.createInvoiceProduct2ID=Label(self, text ="ID:")
        self.createInvoiceProduct2IDTXT=Entry(self)
        self.createInvoiceProduct2Name=Label(self, text ="Product:")
        self.createInvoiceProduct2NameTXT=Entry(self)
        self.createInvoiceProduct2Amount=Label(self, text ="Amount:")
        self.createInvoiceProduct2AmountTXT=Entry(self)
        self.createInvoiceProduct2Price=Label(self, text ="Price:")
        self.createInvoiceProduct2PriceTXT=Entry(self)
        self.createInvoiceProduct2Subtotal=Label(self, text ="Subtotal:")
        self.createInvoiceProduct2SubtotalTXT=Entry(self)
        removeProduct2Button = ttk.Button(self, text='Remove',
                                  command=lambda: removeProduct(2))                                          

        self.createInvoiceProduct3ID=Label(self, text ="ID:")
        self.createInvoiceProduct3IDTXT=Entry(self)
        self.createInvoiceProduct3Name=Label(self, text ="Product:")
        self.createInvoiceProduct3NameTXT=Entry(self)
        self.createInvoiceProduct3Amount=Label(self, text ="Amount:")
        self.createInvoiceProduct3AmountTXT=Entry(self)
        self.createInvoiceProduct3Price=Label(self, text ="Price:")
        self.createInvoiceProduct3PriceTXT=Entry(self)
        self.createInvoiceProduct3Subtotal=Label(self, text ="Subtotal:")
        self.createInvoiceProduct3SubtotalTXT=Entry(self)
        removeProduct3Button = ttk.Button(self, text='Remove',
                                  command=lambda: removeProduct(3))                                          
        
        
        self.createInvoiceProduct4ID=Label(self, text ="ID:")
        self.createInvoiceProduct4IDTXT=Entry(self)
        self.createInvoiceProduct4Name=Label(self, text ="Product:")
        self.createInvoiceProduct4NameTXT=Entry(self)
        self.createInvoiceProduct4Amount=Label(self, text ="Amount:")
        self.createInvoiceProduct4AmountTXT=Entry(self)
        self.createInvoiceProduct4Price=Label(self, text ="Price:")
        self.createInvoiceProduct4PriceTXT=Entry(self)
        self.createInvoiceProduct4Subtotal=Label(self, text ="Subtotal:")
        self.createInvoiceProduct4SubtotalTXT=Entry(self)
        removeProduct4Button = ttk.Button(self, text='Remove',
                                  command=lambda: removeProduct(4))                                          

        self.createInvoiceProduct5ID=Label(self, text ="ID:")
        self.createInvoiceProduct5IDTXT=Entry(self)
        self.createInvoiceProduct5Name=Label(self, text ="Product:")
        self.createInvoiceProduct5NameTXT=Entry(self)
        self.createInvoiceProduct5Amount=Label(self, text ="Amount:")
        self.createInvoiceProduct5AmountTXT=Entry(self)
        self.createInvoiceProduct5Price=Label(self, text ="Price:")
        self.createInvoiceProduct5PriceTXT=Entry(self)
        self.createInvoiceProduct5Subtotal=Label(self, text ="Subtotal:")
        self.createInvoiceProduct5SubtotalTXT=Entry(self)
        removeProduct5Button = ttk.Button(self, text='Remove',
                                  command=lambda: removeProduct(5))                                          

        self.createInvoiceProduct6ID=Label(self, text ="ID:")
        self.createInvoiceProduct6IDTXT=Entry(self)
        self.createInvoiceProduct6Name=Label(self, text ="Product:")
        self.createInvoiceProduct6NameTXT=Entry(self)
        self.createInvoiceProduct6Amount=Label(self, text ="Amount:")
        self.createInvoiceProduct6AmountTXT=Entry(self)
        self.createInvoiceProduct6Price=Label(self, text ="Price:")
        self.createInvoiceProduct6PriceTXT=Entry(self)
        self.createInvoiceProduct6Subtotal=Label(self, text ="Subtotal:")
        self.createInvoiceProduct6SubtotalTXT=Entry(self)
        removeProduct6Button = ttk.Button(self, text='Remove',
                                  command=lambda: removeProduct(6))                                          

        self.createInvoiceProduct7ID=Label(self, text ="ID:")
        self.createInvoiceProduct7IDTXT=Entry(self)
        self.createInvoiceProduct7Name=Label(self, text ="Product:")
        self.createInvoiceProduct7NameTXT=Entry(self)
        self.createInvoiceProduct7Amount=Label(self, text ="Amount:")
        self.createInvoiceProduct7AmountTXT=Entry(self)
        self.createInvoiceProduct7Price=Label(self, text ="Price:")
        self.createInvoiceProduct7PriceTXT=Entry(self)
        self.createInvoiceProduct7Subtotal=Label(self, text ="Subtotal:")
        self.createInvoiceProduct7SubtotalTXT=Entry(self)
        removeProduct7Button = ttk.Button(self, text='Remove',
                                  command=lambda: removeProduct(7))                                          

        self.createInvoiceProduct8ID=Label(self, text ="ID:")
        self.createInvoiceProduct8IDTXT=Entry(self)
        self.createInvoiceProduct8Name=Label(self, text ="Product:")
        self.createInvoiceProduct8NameTXT=Entry(self)
        self.createInvoiceProduct8Amount=Label(self, text ="Amount:")
        self.createInvoiceProduct8AmountTXT=Entry(self)
        self.createInvoiceProduct8Price=Label(self, text ="Price:")
        self.createInvoiceProduct8PriceTXT=Entry(self)
        self.createInvoiceProduct8Subtotal=Label(self, text ="Subtotal:")
        self.createInvoiceProduct8SubtotalTXT=Entry(self)
        removeProduct8Button = ttk.Button(self, text='Remove',
                                  command=lambda: removeProduct(8))

        self.createInvoiceProductTotal=Label(self, text ="Total:")
        self.createInvoiceProductTotalTXT=Entry(self)        

        self.createInvoiceStoreCity=Label(self, text ="Store City:")
        self.createInvoiceStoreCityTXT=Entry(self)
        self.createInvoiceStoreCounty=Label(self, text ="Store County:")
        self.createInvoiceStoreCountyTXT=Entry(self)
        self.createInvoiceStoreState=Label(self, text ="Store State:")
        self.createInvoiceStoreStateTXT=Entry(self)
        self.createInvoiceStorePhone=Label(self, text ="Store Phone:")
        self.createInvoiceStorePhoneTXT=Entry(self)            
        
        addStoreButton = ttk.Button(self, text='Add Store',
                             command=lambda: loadStore(int(self.createInvoiceStoreIDTXT.get())))


        
        self.createInvoiceCustomer=Label(self, text ="Customer:")
        self.createInvoiceCustomerID=Label(self, text ="Customer ID:")
        self.createInvoiceCustomerIDTXT=Entry(self)
        #change command
        addCustomerButton = ttk.Button(self, text='Add Customer',
                             command=lambda: loadCustomer(int(self.createInvoiceCustomerIDTXT.get())))


        
        self.createInvoiceCustomerFirstName=Label(self, text ="First Name:")
        self.createInvoiceCustomerFirstNameTXT=Entry(self)
        self.createInvoiceCustomerLastName=Label(self, text ="Last Name:")
        self.createInvoiceCustomerLastNameTXT=Entry(self)
        self.createInvoiceCustomerAge=Label(self, text ="Age:")
        self.createInvoiceCustomerAgeTXT=Entry(self)
        self.createInvoiceCustomerTelephone=Label(self, text ="Phone Number:")
        self.createInvoiceCustomerTelephoneTXT=Entry(self)        

        self.createInvoiceCustomerGender=Label(self, text ="Gender:")
        self.createInvoiceCustomerGenderTXT=Entry(self)
        self.createInvoiceCustomerStateID=Label(self, text ="State ID:")
        self.createInvoiceCustomerStateIDTXT=Entry(self)
        self.createInvoiceCustomerType=Label(self, text ="Customer Type:")
        self.createInvoiceCustomerTypeTXT=Entry(self)         
        
        self.createInvoiceCustomerAddress=Label(self, text ="Address:")
        self.createInvoiceCustomerAddressStreet=Label(self, text ="Street:")
        self.createInvoiceCustomerAdressStreetTXT=Entry(self)        
        self.createInvoiceCustomerAddressNumber=Label(self, text ="Number:")
        self.createInvoiceCustomerAddressNumberTXT=Entry(self)
        self.createInvoiceCustomerAdressExtra=Label(self, text ="Extra:")
        self.createInvoiceCustomerAdressExtraTXT=Entry(self)
        self.createInvoiceCustomerAdressCity=Label(self, text ="City:")
        self.createInvoiceCustomerAdressCityTXT=Entry(self)
        self.createInvoiceCustomerAdressCounty=Label(self, text ="County:")
        self.createInvoiceCustomerAdressCountyTXT=Entry(self)
        self.createInvoiceCustomerAdressState=Label(self, text ="State:")
        self.createInvoiceCustomerAdressStateTXT=Entry(self)
        createInvoiceButton=ttk.Button(self, text='Create Invoice',
                             command=lambda: createNewInvoice())   

        #create the query and, for each product, create a loop. Also, create
        #a loop on the grid section in order to put the products in the right
        #order.
        startButton = ttk.Button(self, text='Start',
                             command=lambda: controller.show_frame(Start))
        customerButton = ttk.Button(self, text='Customer',
                                  command=lambda: controller.show_frame(Customer))       


        self.createInvoiceDay.grid(row=0,column=0)
        self.createInvoiceDayDrop.grid(row=1,column=0)
        self.createInvoiceMonth.grid(row=0,column=1)
        self.createInvoiceMonthDrop.grid(row=1,column=1)
        self.createInvoiceYear.grid(row=0,column=2)
        self.createInvoiceYearDrop.grid(row=1,column=2)

        self.createInvoiceDayTXT.grid(row=2,column=0)
        self.createInvoiceMonthTXT.grid(row=2,column=1)
        self.createInvoiceYearTXT.grid(row=2,column=2)
        addDateButton.grid(row=1,column=3)

        
        self.createInvoiceStoreID.grid(row=3,column=0)
        self.createInvoiceStoreIDTXT.grid(row=3,column=1)
        addStoreButton.grid(row=3, column=2)

        self.createInvoiceProduct.grid(row=0,column=4)  
        self.createInvoiceProductID.grid(row=1,column=4)
        self.createInvoiceProductIDTXT.grid(row=2,column=4)
        self.createInvoiceProductAmount.grid(row=1,column=5)
        self.createInvoiceProductAmountTXT.grid(row=2,column=5)
        addProductButton.grid(row=2,column=6)

        self.createInvoiceProduct1ID.grid(row=3, column=4)
        self.createInvoiceProduct1IDTXT.grid(row=4, column=4)
        self.createInvoiceProduct1Name.grid(row=3, column=5)
        self.createInvoiceProduct1NameTXT.grid(row=4, column=5)
        self.createInvoiceProduct1Amount.grid(row=3, column=6)
        self.createInvoiceProduct1AmountTXT.grid(row=4, column=6)
        self.createInvoiceProduct1Price.grid(row=3, column=7)
        self.createInvoiceProduct1PriceTXT.grid(row=4, column=7)
        self.createInvoiceProduct1Subtotal.grid(row=3, column=8)
        self.createInvoiceProduct1SubtotalTXT.grid(row=4, column=8)
        removeProduct1Button.grid(row=4,column=9)

        self.createInvoiceProduct2ID.grid(row=5, column=4)
        self.createInvoiceProduct2IDTXT.grid(row=6, column=4)
        self.createInvoiceProduct2Name.grid(row=5, column=5)
        self.createInvoiceProduct2NameTXT.grid(row=6, column=5)
        self.createInvoiceProduct2Amount.grid(row=5, column=6)
        self.createInvoiceProduct2AmountTXT.grid(row=6, column=6)
        self.createInvoiceProduct2Price.grid(row=5, column=7)
        self.createInvoiceProduct2PriceTXT.grid(row=6, column=7)
        self.createInvoiceProduct2Subtotal.grid(row=5, column=8)
        self.createInvoiceProduct2SubtotalTXT.grid(row=6, column=8)
        removeProduct2Button.grid(row=6,column=9)

        self.createInvoiceProduct3ID.grid(row=7, column=4)
        self.createInvoiceProduct3IDTXT.grid(row=8, column=4)
        self.createInvoiceProduct3Name.grid(row=7, column=5)
        self.createInvoiceProduct3NameTXT.grid(row=8, column=5)
        self.createInvoiceProduct3Amount.grid(row=7, column=6)
        self.createInvoiceProduct3AmountTXT.grid(row=8, column=6)
        self.createInvoiceProduct3Price.grid(row=7, column=7)
        self.createInvoiceProduct3PriceTXT.grid(row=8, column=7)
        self.createInvoiceProduct3Subtotal.grid(row=7, column=8)
        self.createInvoiceProduct3SubtotalTXT.grid(row=8, column=8)
        removeProduct3Button.grid(row=8,column=9)

        self.createInvoiceProduct4ID.grid(row=9, column=4)
        self.createInvoiceProduct4IDTXT.grid(row=10, column=4)
        self.createInvoiceProduct4Name.grid(row=9, column=5)
        self.createInvoiceProduct4NameTXT.grid(row=10, column=5)
        self.createInvoiceProduct4Amount.grid(row=9, column=6)
        self.createInvoiceProduct4AmountTXT.grid(row=10, column=6)
        self.createInvoiceProduct4Price.grid(row=9, column=7)
        self.createInvoiceProduct4PriceTXT.grid(row=10, column=7)
        self.createInvoiceProduct4Subtotal.grid(row=9, column=8)
        self.createInvoiceProduct4SubtotalTXT.grid(row=10, column=8)
        removeProduct4Button.grid(row=10,column=9)

        self.createInvoiceProduct5ID.grid(row=11, column=4)
        self.createInvoiceProduct5IDTXT.grid(row=12, column=4)
        self.createInvoiceProduct5Name.grid(row=11, column=5)
        self.createInvoiceProduct5NameTXT.grid(row=12, column=5)
        self.createInvoiceProduct5Amount.grid(row=11, column=6)
        self.createInvoiceProduct5AmountTXT.grid(row=12, column=6)
        self.createInvoiceProduct5Price.grid(row=11, column=7)
        self.createInvoiceProduct5PriceTXT.grid(row=12, column=7)
        self.createInvoiceProduct5Subtotal.grid(row=11, column=8)
        self.createInvoiceProduct5SubtotalTXT.grid(row=12, column=8)
        removeProduct5Button.grid(row=12,column=9)

        self.createInvoiceProduct6ID.grid(row=13, column=4)
        self.createInvoiceProduct6IDTXT.grid(row=14, column=4)
        self.createInvoiceProduct6Name.grid(row=13, column=5)
        self.createInvoiceProduct6NameTXT.grid(row=14, column=5)
        self.createInvoiceProduct6Amount.grid(row=13, column=6)
        self.createInvoiceProduct6AmountTXT.grid(row=14, column=6)
        self.createInvoiceProduct6Price.grid(row=13, column=7)
        self.createInvoiceProduct6PriceTXT.grid(row=14, column=7)
        self.createInvoiceProduct6Subtotal.grid(row=13, column=8)
        self.createInvoiceProduct6SubtotalTXT.grid(row=14, column=8)
        removeProduct6Button.grid(row=14,column=9)

        self.createInvoiceProduct7ID.grid(row=15, column=4)
        self.createInvoiceProduct7IDTXT.grid(row=16, column=4)
        self.createInvoiceProduct7Name.grid(row=15, column=5)
        self.createInvoiceProduct7NameTXT.grid(row=16, column=5)
        self.createInvoiceProduct7Amount.grid(row=15, column=6)
        self.createInvoiceProduct7AmountTXT.grid(row=16, column=6)
        self.createInvoiceProduct7Price.grid(row=15, column=7)
        self.createInvoiceProduct7PriceTXT.grid(row=16, column=7)
        self.createInvoiceProduct7Subtotal.grid(row=15, column=8)
        self.createInvoiceProduct7SubtotalTXT.grid(row=16, column=8)
        removeProduct7Button.grid(row=16,column=9)	
	
        self.createInvoiceProduct8ID.grid(row=17, column=4)
        self.createInvoiceProduct8IDTXT.grid(row=18, column=4)
        self.createInvoiceProduct8Name.grid(row=17, column=5)
        self.createInvoiceProduct8NameTXT.grid(row=18, column=5)
        self.createInvoiceProduct8Amount.grid(row=17, column=6)
        self.createInvoiceProduct8AmountTXT.grid(row=18, column=6)
        self.createInvoiceProduct8Price.grid(row=17, column=7)
        self.createInvoiceProduct8PriceTXT.grid(row=18, column=7)
        self.createInvoiceProduct8Subtotal.grid(row=17, column=8)
        self.createInvoiceProduct8SubtotalTXT.grid(row=18, column=8)
        removeProduct8Button.grid(row=18,column=9)

        self.createInvoiceProductTotal.grid(row=19, column=8)
        self.createInvoiceProductTotalTXT.grid(row=20,column=8)        

	

        self.createInvoiceStoreStreet.grid(row=4, column=0)
        self.createInvoiceStoreStreetTXT.grid(row=5, column=0)
        self.createInvoiceStoreNumber.grid(row=4, column=1)
        self.createInvoiceStoreNumberTXT.grid(row=5, column=1)
        self.createInvoiceStoreDetail.grid(row=4, column=2)
        self.createInvoiceStoreDetailTXT.grid(row=5, column=2)
        
        
        self.createInvoiceStoreCity.grid(row=6,column=0)
        self.createInvoiceStoreCityTXT.grid(row=7,column=0)
        self.createInvoiceStoreCounty.grid(row=6,column=1)
        self.createInvoiceStoreCountyTXT.grid(row=7,column=1)
        self.createInvoiceStoreState.grid(row=6,column=2)
        self.createInvoiceStoreStateTXT.grid(row=7,column=2)
        self.createInvoiceStorePhone.grid(row=6,column=3)
        self.createInvoiceStorePhoneTXT.grid(row=7,column=3)
        

        self.createInvoiceCustomer.grid(row=8, column=0)
        self.createInvoiceCustomerID.grid(row=9, column=0)
        self.createInvoiceCustomerIDTXT.grid(row=9, column=1)
        addCustomerButton.grid(row=9, column=2)
        self.createInvoiceCustomerFirstName.grid(row=10, column=0)
        self.createInvoiceCustomerFirstNameTXT.grid(row=11, column=0)
        self.createInvoiceCustomerLastName.grid(row=10, column=1)
        self.createInvoiceCustomerLastNameTXT.grid(row=11, column=1)
        self.createInvoiceCustomerAge.grid(row=10, column=2)
        self.createInvoiceCustomerAgeTXT.grid(row=11, column=2)
        self.createInvoiceCustomerTelephone.grid(row=10, column=3)
        self.createInvoiceCustomerTelephoneTXT.grid(row=11, column=3)
        self.createInvoiceCustomerGender.grid(row=12, column=0)
        self.createInvoiceCustomerGenderTXT.grid(row=13, column=0)
        self.createInvoiceCustomerStateID.grid(row=12, column=1)
        self.createInvoiceCustomerStateIDTXT.grid(row=13, column=1)
        self.createInvoiceCustomerType.grid(row=12, column=2)
        self.createInvoiceCustomerTypeTXT.grid(row=13, column=2)
        self.createInvoiceCustomerAddress.grid(row=14, column=0)        
        self.createInvoiceCustomerAddressStreet.grid(row=15, column=0)
        self.createInvoiceCustomerAdressStreetTXT.grid(row=16, column=0)
        self.createInvoiceCustomerAddressNumber.grid(row=15, column=1)
        self.createInvoiceCustomerAddressNumberTXT.grid(row=16, column=1)
        self.createInvoiceCustomerAdressExtra.grid(row=15, column=2)
        self.createInvoiceCustomerAdressExtraTXT.grid(row=16, column=2)
        self.createInvoiceCustomerAdressCity.grid(row=17, column=0)
        self.createInvoiceCustomerAdressCityTXT.grid(row=18, column=0)
        self.createInvoiceCustomerAdressCounty.grid(row=17, column=1)
        self.createInvoiceCustomerAdressCountyTXT.grid(row=18, column=1)
        self.createInvoiceCustomerAdressState.grid(row=17, column=2)
        self.createInvoiceCustomerAdressStateTXT.grid(row=18, column=2)
        createInvoiceButton.grid(row=18, column=3)
        self.total=0
        
        startButton.grid()                
        customerButton.grid()

        def loadDate(day, month, year):
            get_createInvoice=self.controller.get_page('CreateInvoice')
            get_createInvoice.createInvoiceDayTXT.delete(0,END)
            get_createInvoice.createInvoiceDayTXT.insert(0, day)
            get_createInvoice.createInvoiceMonthTXT.delete(0,END)
            get_createInvoice.createInvoiceMonthTXT.insert(0, month)
            get_createInvoice.createInvoiceYearTXT.delete(0,END)
            get_createInvoice.createInvoiceYearTXT.insert(0, year)

        def loadStore(storeID):
            get_createInvoice=self.controller.get_page('CreateInvoice')
            
            tempStore=reports.detail_store(storeID)            
            get_createInvoice.createInvoiceStoreCityTXT.delete(0,END)
            get_createInvoice.createInvoiceStoreCityTXT.insert(0,tempStore[0])
            get_createInvoice.createInvoiceStoreCountyTXT.delete(0,END)
            get_createInvoice.createInvoiceStoreCountyTXT.insert(0,tempStore[1])
            get_createInvoice.createInvoiceStoreStateTXT.delete(0,END)
            get_createInvoice.createInvoiceStoreStateTXT.insert(0,tempStore[2])
            get_createInvoice.createInvoiceStorePhoneTXT.delete(0,END)
            get_createInvoice.createInvoiceStorePhoneTXT.insert(0,tempStore[6])
            

            get_createInvoice.createInvoiceStoreStreetTXT.delete(0,END)
            get_createInvoice.createInvoiceStoreStreetTXT.insert(0,tempStore[3])            
            get_createInvoice.createInvoiceStoreNumberTXT.delete(0,END)
            get_createInvoice.createInvoiceStoreNumberTXT.insert(0,tempStore[4])
            get_createInvoice.createInvoiceStoreDetailTXT.delete(0,END)
            get_createInvoice.createInvoiceStoreDetailTXT.insert(0,tempStore[5])

        def loadCustomer(customerID):
            get_createInvoice=self.controller.get_page('CreateInvoice')
            tempCustomer=reports.detail_customer(customerID)[1]            
            get_createInvoice.createInvoiceCustomerFirstNameTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerFirstNameTXT.insert(0,tempCustomer[1])
            get_createInvoice.createInvoiceCustomerLastNameTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerLastNameTXT.insert(0,tempCustomer[2])
            get_createInvoice.createInvoiceCustomerStateIDTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerStateIDTXT.insert(0,tempCustomer[3])
            get_createInvoice.createInvoiceCustomerAgeTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerAgeTXT.insert(0,tempCustomer[4])
            get_createInvoice.createInvoiceCustomerGenderTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerGenderTXT.insert(0,tempCustomer[5])
            get_createInvoice.createInvoiceCustomerTypeTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerTypeTXT.insert(0,tempCustomer[6])
            get_createInvoice.createInvoiceCustomerTelephoneTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerTelephoneTXT.insert(0,tempCustomer[7])
            get_createInvoice.createInvoiceCustomerAdressStreetTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerAdressStreetTXT.insert(0,tempCustomer[8])
            get_createInvoice.createInvoiceCustomerAddressNumberTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerAddressNumberTXT.insert(0,tempCustomer[9])
            get_createInvoice.createInvoiceCustomerAdressExtraTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerAdressExtraTXT.insert(0,tempCustomer[10])
            get_createInvoice.createInvoiceCustomerAdressCityTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerAdressCityTXT.insert(0,tempCustomer[11])
            get_createInvoice.createInvoiceCustomerAdressCountyTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerAdressCountyTXT.insert(0,tempCustomer[12])
            get_createInvoice.createInvoiceCustomerAdressStateTXT.delete(0,END)
            get_createInvoice.createInvoiceCustomerAdressStateTXT.insert(0,tempCustomer[13])
        def loadProduct(productID,productAmount):
            get_createInvoice=self.controller.get_page('CreateInvoice')
            
            productList1=[self.createInvoiceProduct1IDTXT.get(),self.createInvoiceProduct1IDTXT,self.createInvoiceProduct1NameTXT,self.createInvoiceProduct1AmountTXT, self.createInvoiceProduct1PriceTXT, self.createInvoiceProduct1SubtotalTXT]
            productList2=[self.createInvoiceProduct2IDTXT.get(),self.createInvoiceProduct2IDTXT,self.createInvoiceProduct2NameTXT,self.createInvoiceProduct2AmountTXT, self.createInvoiceProduct2PriceTXT, self.createInvoiceProduct2SubtotalTXT]
            productList3=[self.createInvoiceProduct3IDTXT.get(),self.createInvoiceProduct3IDTXT,self.createInvoiceProduct3NameTXT,self.createInvoiceProduct3AmountTXT, self.createInvoiceProduct3PriceTXT, self.createInvoiceProduct3SubtotalTXT]
            productList4=[self.createInvoiceProduct4IDTXT.get(),self.createInvoiceProduct4IDTXT,self.createInvoiceProduct4NameTXT,self.createInvoiceProduct4AmountTXT, self.createInvoiceProduct4PriceTXT, self.createInvoiceProduct4SubtotalTXT]
            productList5=[self.createInvoiceProduct5IDTXT.get(),self.createInvoiceProduct5IDTXT,self.createInvoiceProduct5NameTXT,self.createInvoiceProduct5AmountTXT, self.createInvoiceProduct5PriceTXT, self.createInvoiceProduct5SubtotalTXT]
            productList6=[self.createInvoiceProduct6IDTXT.get(),self.createInvoiceProduct6IDTXT,self.createInvoiceProduct6NameTXT,self.createInvoiceProduct6AmountTXT, self.createInvoiceProduct6PriceTXT, self.createInvoiceProduct6SubtotalTXT]
            productList7=[self.createInvoiceProduct7IDTXT.get(),self.createInvoiceProduct7IDTXT,self.createInvoiceProduct7NameTXT,self.createInvoiceProduct7AmountTXT, self.createInvoiceProduct7PriceTXT, self.createInvoiceProduct7SubtotalTXT]
            productList8=[self.createInvoiceProduct8IDTXT.get(),self.createInvoiceProduct8IDTXT,self.createInvoiceProduct8NameTXT,self.createInvoiceProduct8AmountTXT, self.createInvoiceProduct8PriceTXT, self.createInvoiceProduct8SubtotalTXT]
            productListFinal=[productList1,productList2,productList3,productList4,productList5,productList6,productList7,productList8]
            isProductRepeated=0            
            for item in productListFinal:
                if item[0] == str(productID):                    
                    isProductRepeated=1
            if int(productAmount)-int(productAmount)==0  and isProductRepeated==0:
                
                for item in productListFinal:                    
                    if item[0] =='':
                        tempProduct=reports.detail_product(productID)[1]                        
                        item[1].delete(0,END)
                        item[1].insert(0,productID)
                        item[2].delete(0,END)
                        item[2].insert(0,tempProduct[0])
                        item[3].delete(0,END)
                        item[3].insert(0,productAmount)
                        item[4].delete(0,END)
                        item[4].insert(0,tempProduct[1])
                        item[5].delete(0,END)
                        item[5].insert(0,str(int(productAmount)*int(tempProduct[1])))
                        self.total+=int(productAmount)*int(tempProduct[1])
                        self.createInvoiceProductTotalTXT.delete(0,END)
                        self.createInvoiceProductTotalTXT.insert(0,self.total)
                        
                        break
        def removeProduct(place):
            productRemoveList1=[self.createInvoiceProduct1IDTXT,self.createInvoiceProduct1NameTXT,self.createInvoiceProduct1AmountTXT, self.createInvoiceProduct1PriceTXT, self.createInvoiceProduct1SubtotalTXT]
            productRemoveList2=[self.createInvoiceProduct2IDTXT,self.createInvoiceProduct2NameTXT,self.createInvoiceProduct2AmountTXT, self.createInvoiceProduct2PriceTXT, self.createInvoiceProduct2SubtotalTXT]
            productRemoveList3=[self.createInvoiceProduct3IDTXT,self.createInvoiceProduct3NameTXT,self.createInvoiceProduct3AmountTXT, self.createInvoiceProduct3PriceTXT, self.createInvoiceProduct3SubtotalTXT]
            productRemoveList4=[self.createInvoiceProduct4IDTXT,self.createInvoiceProduct4NameTXT,self.createInvoiceProduct4AmountTXT, self.createInvoiceProduct4PriceTXT, self.createInvoiceProduct4SubtotalTXT]
            productRemoveList5=[self.createInvoiceProduct5IDTXT,self.createInvoiceProduct5NameTXT,self.createInvoiceProduct5AmountTXT, self.createInvoiceProduct5PriceTXT, self.createInvoiceProduct5SubtotalTXT]
            productRemoveList6=[self.createInvoiceProduct6IDTXT,self.createInvoiceProduct6NameTXT,self.createInvoiceProduct6AmountTXT, self.createInvoiceProduct6PriceTXT, self.createInvoiceProduct6SubtotalTXT]
            productRemoveList7=[self.createInvoiceProduct7IDTXT,self.createInvoiceProduct7NameTXT,self.createInvoiceProduct7AmountTXT, self.createInvoiceProduct7PriceTXT, self.createInvoiceProduct7SubtotalTXT]
            productRemoveList8=[self.createInvoiceProduct8IDTXT,self.createInvoiceProduct8NameTXT,self.createInvoiceProduct8AmountTXT, self.createInvoiceProduct8PriceTXT, self.createInvoiceProduct8SubtotalTXT]
            productRemoveListFinal=[productRemoveList1,productRemoveList2,productRemoveList3,productRemoveList4,productRemoveList5,productRemoveList6,productRemoveList7,productRemoveList8]            
            productRemoveSubtotal=productRemoveListFinal[place-1]
            self.total-=int(productRemoveSubtotal[4].get())
            self.createInvoiceProductTotalTXT.delete(0,END)
            self.createInvoiceProductTotalTXT.insert(0,self.total)            
            for item in productRemoveListFinal[place-1]:                        
                item.delete(0,END)

        def createNewInvoice():
            createInvoiceStoreID=self.createInvoiceStoreIDTXT.get()
            createInvoiceCustomerID=self.createInvoiceCustomerIDTXT.get()
            createInvoiceDate="'"+self.createInvoiceYearTXT.get()+"-"+self.createInvoiceMonthTXT.get()+"-"+self.createInvoiceDayTXT.get()+"'"
            createInvoiceList1=[self.createInvoiceProduct1IDTXT.get(),self.createInvoiceProduct1AmountTXT.get()]
            createInvoiceList2=[self.createInvoiceProduct2IDTXT.get(),self.createInvoiceProduct2AmountTXT.get()]
            createInvoiceList3=[self.createInvoiceProduct3IDTXT.get(),self.createInvoiceProduct3AmountTXT.get()]
            createInvoiceList4=[self.createInvoiceProduct4IDTXT.get(),self.createInvoiceProduct4AmountTXT.get()]
            createInvoiceList5=[self.createInvoiceProduct5IDTXT.get(),self.createInvoiceProduct5AmountTXT.get()]
            createInvoiceList6=[self.createInvoiceProduct6IDTXT.get(),self.createInvoiceProduct6AmountTXT.get()]
            createInvoiceList7=[self.createInvoiceProduct7IDTXT.get(),self.createInvoiceProduct7AmountTXT.get()]
            createInvoiceList8=[self.createInvoiceProduct8IDTXT.get(),self.createInvoiceProduct8AmountTXT.get()]
            createInvoiceListFinal=[createInvoiceList1,createInvoiceList2,createInvoiceList3,createInvoiceList4,createInvoiceList5,createInvoiceList6,createInvoiceList7,createInvoiceList8]  
            createInvoiceProductListInfo=[]            
            for item in createInvoiceListFinal:
                print('zz',item)
                if item[0]!='' and int(item[0])>0 and int(item[1])>0:
                    tempProductList=[int(item[0]),int(item[1])]
                    createInvoiceProductListInfo.append(tempProductList)
            query.createInvoice(createInvoiceStoreID, createInvoiceCustomerID, createInvoiceDate, createInvoiceProductListInfo)
                

            
            
app = MyApp()
app.title('Multi-Page Test App')
app.mainloop()

