from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Sistema di gestione di un ristorante")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TEMPO--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFORMAZIONI------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Sistema di gestione di un ristorante",bg="darkblue",fg="white",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="black",anchor=W)
lblinfo.grid(row=1,column=0)

#---------------Calcalatrice------------------
text_Input=StringVar()
operatore =""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operatore
    operatore=operatore + str(numbers)
    text_Input.set(operatore)

def clrdisplay():
    global operatore
    operatore=""
    text_Input.set("")

def eqals():
    global operatore
    sumup=str(eval(operatore))

    text_Input.set(sumup)
    operatore = ""

def Ref():
    numeroordine=float(spaghettialloscoglio.get())
    spaghetti =float(spaghettialloscoglio.get())
    scaloppine = float(scaloppineallimone.get())
    insalata = float(insalataestate.get())
    patatine = float(patatinefritte.get())
    Penne = float(Pennegamberiesalmone.get())
    Bevande = float(mountaindew.get())

    spaghettiprezzo =spaghetti*50
    scaloppineprezzo =scaloppine*60
    insalataprezzo =insalata*250
    patatineprezzo =patatine*50
    Penneprezzo =Penne*75
    Bevandeprezzo =Bevande*45

    costocena = "P",str('%.2f'% (spaghettiprezzo +scaloppineprezzo + insalataprezzo +patatineprezzo + Penneprezzo + Bevandeprezzo))
    Tasse_da_pagare=((spaghettiprezzo +  scaloppineprezzo + insalataprezzo + patatineprezzo +  Penneprezzo + Bevandeprezzo)*0.33)
    Totalecosto=(spaghettiprezzo +  scaloppineprezzo + insalataprezzo + patatineprezzo  + Penneprezzo + Bevandeprezzo)
    Ser_Costo=((spaghettiprezzo +  scaloppineprezzo + insalataprezzo + patatineprezzo + Penneprezzo + Bevandeprezzo)/99)
    Servizio="P",str('%.2f'% Ser_Costo)
    Totale_prezzo="P",str( Tasse_da_pagare + Totalecosto + Ser_Costo)
    Tassepagatte="P",str('%.2f'% Tasse_da_pagare)

    Servizio_Costo.set(Servizio)
    costo.set(costocena)
    Tasse.set(Tassepagatte)
    SubTotale.set(costocena)
    Totale.set(Totale_prezzo)


def qexit():
    root.destroy()

def reset():
    ordine.set("")
    spaghettialloscoglio.set("")
    scaloppineallimone.set("")
    insalataestate.set("")
    patatinefritte.set("")
    SubTotale.set("")
    Totale.set("")
    Servizio_Costo.set("")
    mountaindew.set("")
    Tasse.set("")
    costo.set("")
    Pennegamberiesalmone.set("")


btn7=Button(f2,padx=16,pady=16,bd=4, fg="red",font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="+",bg="black", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="-",bg="black", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="*",bg="black", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="c",bg="black", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="red", font=('ariel', 20 ,'bold'),text="=",bg="black",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="/",bg="black", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)

#---------------------------------------------------------------------------------------
ado = StringVar()
spaghettialloscoglio = StringVar()
scaloppineallimone = StringVar()
insalataestate = StringVar()
patatinefritte = StringVar()
SubTotale = StringVar()
Totale = StringVar()
Servizio_Costo = StringVar()
mountaindew = StringVar()
Tasse = StringVar()
costo = StringVar()
ordine= StringVar()
Pennegamberiesalmone = StringVar()


lblordine = Label(f1, font=( 'aria' ,16, 'bold' ),text="Numero ordine",fg="red",bd=10,anchor='w')
lblordine.grid(row=0,column=0)
txtordine = Entry(f1, font=('ariel' ,16,'bold'), textvariable=ado, bd=6, insertwidth=4, bg="white", justify='right')
txtordine.grid(row=0,column=1)

lblspaghettialloscoglio = Label(f1, font=('aria' , 16, 'bold'), text="spaghetti_allo_scoglio", fg="green", bd=10, anchor='w')
lblspaghettialloscoglio.grid(row=1, column=0)
txtspaghettialloscoglio = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=spaghettialloscoglio, bd=6, insertwidth=4, bg="white", justify='right')
txtspaghettialloscoglio.grid(row=1, column=1)

lblscaloppineallimone = Label(f1, font=('aria' , 16, 'bold'), text="scaloppine_al_limone", fg="green", bd=10, anchor='w')
lblscaloppineallimone.grid(row=2, column=0)
txtscaloppineallimone = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=scaloppineallimone, bd=6, insertwidth=4, bg="white", justify='right')
txtscaloppineallimone.grid(row=2, column=1)


lblinsalataestate = Label(f1, font=('aria' , 16, 'bold'), text="insalata_estate", fg="green", bd=10, anchor='w')
lblinsalataestate.grid(row=3, column=0)
txtinsalataestate = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=insalataestate, bd=6, insertwidth=4, bg="white", justify='right')
txtinsalataestate.grid(row=3, column=1)

lblpatatinefritte = Label(f1, font=('aria' , 16, 'bold'), text="patatine_fritte", fg="green", bd=10, anchor='w')
lblpatatinefritte.grid(row=4, column=0)
txtpatatinefritte = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=patatinefritte, bd=6, insertwidth=4, bg="white", justify='right')
txtpatatinefritte.grid(row=4, column=1)

lblPennegamberiesalmone = Label(f1, font=('aria' , 16, 'bold'), text="Penne_gamberi_e_salmone", fg="green", bd=10, anchor='w')
lblPennegamberiesalmone.grid(row=5, column=0)
txtPennegamberiesalmone = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Pennegamberiesalmone, bd=6, insertwidth=4, bg="white", justify='right')
txtPennegamberiesalmone.grid(row=5, column=1)

#--------------------------------------------------------------------------------------
lblmountaindew = Label(f1, font=('aria' , 16, 'bold'), text="Bevande", fg="green", bd=10, anchor='w')
lblmountaindew.grid(row=0, column=2)
txtmountaindew = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=mountaindew, bd=6, insertwidth=4, bg="white", justify='right')
txtmountaindew.grid(row=0, column=3)

lblcosto = Label(f1, font=( 'aria' ,16, 'bold' ),text="costo",fg="red",bd=10,anchor='w')
lblcosto.grid(row=1,column=2)
txtcosto = Entry(f1,font=('ariel' ,16,'bold'), textvariable=costo ,bd=6,insertwidth=4,bg="white" ,justify='right')
txtcosto.grid(row=1,column=3)

lblServizio_Costo = Label(f1, font=( 'aria' ,16, 'bold' ),text="Costo del servizio",fg="red",bd=10,anchor='w')
lblServizio_Costo.grid(row=2,column=2)
txtServizio_Costo = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Servizio_Costo , bd=6,insertwidth=4,bg="white" ,justify='right')
txtServizio_Costo.grid(row=2,column=3)

lblTasse = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tasse",fg="red",bd=10,anchor='w')
lblTasse.grid(row=3,column=2)
txtTasse = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tasse , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTasse.grid(row=3,column=3)

lblSubTotale = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotale",fg="red",bd=10,anchor='w')
lblSubTotale.grid(row=4,column=2)
txtSubTotale = Entry(f1,font=('ariel' ,16,'bold'), textvariable=SubTotale , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubTotale.grid(row=4,column=3)

lblTotale = Label(f1, font=( 'aria' ,16, 'bold' ),text="Totale",fg="red",bd=10,anchor='w')
lblTotale.grid(row=5,column=2)
txtTotale = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Totale , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTotale.grid(row=5,column=3)

#-----------------------------------------pulsanti------------------------------------------
lblTotale = Label(f1,text="---------------------",fg="white")
lblTotale.grid(row=6,columnspan=3)

btnTotale=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="Totale", bg="blue",command=Ref)
btnTotale.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="green",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Lista dei prezi")
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Prodoti", bg="darkblue", fg="white", bd=5)
    lblrestaurant.grid(row=0, column=0)
    lblrestaurant = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=2)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Prezzo",bg="darkblue", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="spaghetti_allo_scoglio", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="scaloppine_al_limone", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="60", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="insalata_estate", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="250", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="patatine_fritte", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Penne_gamberi_e_salmone", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="75", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Bevande", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="Prezzo", bg="green",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()

