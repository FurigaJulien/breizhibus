from BreizhibusBDD import BDD
import re
import tkinter.messagebox
from functools import partial
import tkinter as tk


class Application(tk.Tk):

    def __init__(self):
        
        tk.Tk.__init__(self)
        self.geometry("1024x720")
        self.create_widget()
        self.v=tk.IntVar()
        
        


    def create_widget(self):

        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)


        self.menu1 = tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="Fichier",menu=self.menu1)

        self.menu1.add_command(label="Ligne de bus",command=self.afficher_ligne)
        self.menu1.add_command(label="Bus",command=self.afficher_bus)

        

        

        """Titre"""
        self.champ_titre=tk.Label(self,text="Projet Breihzibus",padx="10",pady="10")
        self.champ_titre.config(font=("Courier", 44))
        self.champ_titre.pack(side="top")
        
        self.resultats=tk.Frame(self)
        self.resultats.pack()

        

# Gestionnaire de ligne

    def afficher_ligne(self):    
        
        for widget in self.resultats.winfo_children():
            widget.forget()

        self.lineFrame=tk.Frame(self.resultats,width=str(int(self.winfo_width())/2))

        self.resultatsFrame=tk.Frame(self.lineFrame)
        self.resultatsFrame.grid(row=1,column=0)
        self.lineFrame.pack()
        self.fenetreResultat=tk.Frame(self.resultatsFrame)
        self.fenetreResultat.pack()
        self.generateButtonStopFrame=tk.Frame(self.resultatsFrame)
        self.generateButtonStopFrame.pack()
        self.fenetreResultatStop=tk.Frame(self.resultatsFrame)
        self.fenetreResultatStop.pack()
        self.fenetreAjouterLigne=tk.Frame(self.resultatsFrame)

        self.button_show_lines()

     
# Gestionnaire de bus

    def afficher_bus(self):
        
        self.busList=BDD.getBus()
        for widget in self.resultats.winfo_children():
            widget.forget()
        self.gestionnaireBusFrame=tk.Frame(self.resultats)
        self.gestionnaireBusFrame.pack()

        self.tableFrame=tk.Frame(self.gestionnaireBusFrame)
        self.tableFrame.grid(row=0,column=0,padx="50")

        self.liste=["Numéro du bus","Immatriculation","Ligne affecté"]
        self.photo = tk.PhotoImage(file="C:/Users/julie/Desktop/Microsoft/Breizhibus/update.png")
        self.add = tk.PhotoImage(file="C:/Users/julie/Desktop/Microsoft/Breizhibus/add.png")
        self.delete = tk.PhotoImage(file="C:/Users/julie/Desktop/Microsoft/Breizhibus/del.png")
        

        for i in range(len(self.liste)):
            tk.Label(self.tableFrame,text=self.liste[i],padx="10",pady="10",borderwidth="1",relief="solid",width="12").grid(row=0,column=i)
        for i in range(len(self.busList)):
            tk.Label(self.tableFrame,text=self.busList[i].number,padx="10",pady="10",borderwidth="1",relief="solid",width="12").grid(row=i+1,column=0)
            tk.Label(self.tableFrame,text=self.busList[i].registration,padx="10",pady="10",borderwidth="1",relief="solid",width="12").grid(row=i+1,column=1)
            tk.Label(self.tableFrame,text=self.busList[i].line_name,padx="10",pady="10",borderwidth="1",relief="solid",width="12").grid(row=i+1,column=2)
            tk.Button(self.tableFrame, image=self.photo,command=partial(self.updateBus,self.busList[i])).grid(row=i+1,column=3)
            tk.Button(self.tableFrame, image=self.delete,command=partial(self.deleteBus,self.busList[i])).grid(row=i+1,column=4)
            
        tk.Button(self.tableFrame, image=self.add,command=self.afficher_bus).grid(row=len(self.busList)+2,column=2)
        

        self.addBusFrame=tk.Frame(self.gestionnaireBusFrame,width=str(int(self.winfo_width())/2),padx="50",height=(self.tableFrame.winfo_height()),borderwidth="1",relief="solid")
        self.addBusFrame.grid(row=0,column=1,sticky='n')


        self.titreVar=tk.StringVar(self)
        self.titreVar.set("Ajouter un bus :")
        self.titre=tk.Label(self.addBusFrame,textvariable=self.titreVar)
        self.titre.grid(row=0,column=1)
        #Numéro
        tk.Label(self.addBusFrame,text="Numéro :").grid(row=1,column=1)
        self.busNumberVar=tk.StringVar(self)
        self.busNumberVar.set(self.get_bus_number_option())
        
        self.busNumberInput=tk.Entry(self.addBusFrame,textvariable=self.busNumberVar,state="disabled")
        self.busNumberInput.grid(row=1,column=2,padx="15",pady="15")

        #Immatriculation
        tk.Label(self.addBusFrame,text="Immatriculation :").grid(row=2,column=1)

        self.busRegistrationVar=tk.StringVar(self)
        

        self.busRegistrationInput=tk.Entry(self.addBusFrame,textvariable=self.busRegistrationVar)
        self.busRegistrationInput.grid(row=2,column=2,padx="15",pady="15")

        #Nombre de place
        tk.Label(self.addBusFrame,text="Nombre de place :").grid(row=3,column=1)
        self.busNumberPlaceVar=tk.StringVar(self)
        self.busNumberPlaceVar.set("0")
        self.busNumberPlaceInput=tk.Entry(self.addBusFrame,textvariable=self.busNumberPlaceVar)
        self.busNumberPlaceInput.grid(row=3,column=2,padx="15",pady="15")

        #Ligne
        tk.Label(self.addBusFrame,text="Affecter a un ligne :").grid(row=4,column=1)
        self.busline=BDD.getLines()
        self.busLineOption=tk.StringVar(self)
        self.busLineOption.set(self.busline[0])
        self.busLineInput=tk.OptionMenu(self.addBusFrame,self.busLineOption,*self.busline)
    
        self.busLineInput.grid(row=4,column=2,padx="15",pady="15")

        self.addButton=tk.Button(self.addBusFrame,text="Ajouter un bus",command=self.createBus)
        self.addButton.grid(row=5,column=1,pady="15")
        
#Fonction pour les boutons 

    def show_lines(self,lines):

        for i in range(len(lines)):
            tk.Radiobutton(self.fenetreResultat,text=lines[i],padx="10", variable=self.v,value=lines[i].id).grid( row=0,column=i)
        tk.Button(self.generateButtonStopFrame, text="Afficher toute les arrets",command=self.button_show_stops).grid(row=0,column=0)
        
    def show_stop(self,stops,id_line):
        
        for i in range(len(stops)):
            tk.Label(self.fenetreResultatStop,text=stops[i],padx="10").grid( row=i+3,column=0)
        
        tk.Label(self.fenetreResultatStop,text="Liste des bus desservant cette ligne :",padx="10").grid( row=2,column=1)
        busInLine=[]
        busList=BDD.getBus()
        for i in range(len(busList)):
            if int(busList[i].line_id)==int(id_line):
                busInLine.append(busList[i])

        for i in range(len(busInLine)):
            tk.Label(self.fenetreResultatStop,text=busInLine[i].number,padx="10").grid( row=i+3,column=1)

    def button_show_lines(self):
        lines=BDD.getLines()
        self.show_lines(lines)

    def button_show_stops(self):
        for widget in self.fenetreResultatStop.winfo_children():
            widget.destroy()
        buslineStops,id=BDD.getStops(int(self.v.get()))
        self.show_stop(buslineStops,id)

    def get_bus_number_option(self):
        string=self.busList[-1].number
        if int(self.busList[-1].number[-2])<10:
            number=int(self.busList[-1].number[-1])+1
        else :
            number=int(self.busList[-1].number[-2])+1
        return string[0:3]+str(number)
    
    def checkValue(self):
        
        registrationCheck=re.compile("([A-Z]){2}([0-9]){3}([A-Z]){2}")
        print(re.fullmatch(registrationCheck,str(self.busRegistrationVar)))
        if re.fullmatch(registrationCheck,str(self.busRegistrationVar.get()))==None:
            msg="Veuillez saisir une immatriculation valide"
            tkinter.messagebox.showinfo( "Erreur", msg)
            return False
        if int(self.busNumberPlaceVar.get())<15:
            msg="Veuillez saisir un nombre de place supérieur a 15"
            tkinter.messagebox.showinfo( "Erreur", msg)
            return False
        if int(self.busNumberPlaceVar.get())>60:
            msg="Veuillez saisir un nombre de place inferieur a 60"
            tkinter.messagebox.showinfo( "Erreur", msg)
            return False
        return True

    def createBus(self):
        
        if self.checkValue()==True:
            number=str(self.busNumberVar.get())
            registration=str(self.busRegistrationVar.get())
            numberPlace=int(self.busNumberPlaceVar.get())
            name=self.busLineOption.get()
            BDD.createBus(name,number,registration,numberPlace)
            self.afficher_bus()

    def updateBusInBase(self,bus):
        number=str(self.busNumberVar.get())
        registration=str(self.busRegistrationVar.get())
        numberPlace=int(self.busNumberPlaceVar.get())
        idLigne=BDD.getIdLigne(self.busLineOption.get())
        if self.checkValue()==True:
            
            BDD.updateBusInBase(bus,number,registration,numberPlace,idLigne)
            self.afficher_bus()




    def updateBus(self,bus):
        self.titreVar.set("Modifier un bus :")
        self.busNumberVar.set(bus.number)
        self.busRegistrationVar.set(bus.registration)
        self.busNumberPlaceVar.set(bus.nb_place)
        for i in range(len(self.busline)):
            print(self.busline[i].id)
            print(bus.line_id)
            if int(self.busline[i].id)==int(bus.line_id):
                self.busLineOption.set(self.busline[i])
        
        self.addButton=tk.Button(self.addBusFrame,text="Modfier le bus",command=partial(self.updateBusInBase,bus))
        self.addButton.grid(row=5,column=1,pady="15")      

    def deleteBus(self,bus):
        BDD.deleteBus(bus)
        self.afficher_bus()