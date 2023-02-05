from math import *
def fichier(pos):
    try:
        f=open(pos+'.txt','r')
    except: raise Exception("Ce fichier n'existe pas")
    op=f.readlines()
    f.close()
    for i in op:
        for j in i.replace('sin','').replace('cos','').replace('tan','').replace('log','').replace('e',''):
            if j not in ['(',')','*','**','+','-','/','.',"\n",' ','%']:
                try:
                    float(j)
                except: raise Exception("l'oppération {} est mal écrite".format(i))
    try:
        eq=list(map(lambda x:eval(x.strip()),op))
    except: raise Exception("Il y a une oppération mal écrite:")
    k=open('Resultat.txt','w')
    for i in range(len(op)):
        k.write(op[i].replace('\n','').strip()+'='+str(eq[i]))
        k.write('\n')
    k.close()
    print('Terminé avec succés')
    input('Appiez sur Entrée pour fermer...')
    quit()
def interface():
    import tkinter
    import tkinter.ttk
    g=tkinter.Tk()
    g.title('Ghassene Calculatrice')
    g.geometry('500x120')
    la=tkinter.Label(g,text="Donner l'emplacement de fichier qui contient\nles opération mathématique:")
    la.place(relx=0.0,rely=0.0)
    bu=tkinter.ttk.Button(g,text='  Calcul  ')
    en=tkinter.Entry(g,width=70)
    la.pack()
    en.pack()
    bu.pack()
    def couplage():
        return fichier(en.get())
    ph1=tkinter.PhotoImage(file='arrow-left.png')
    bu.config(image=ph1,compound=tkinter.LEFT,command=couplage)
    def fermer(g):
        g.destroy()
    buC=tkinter.ttk.Button(g,text='Fermer',command=lambda :fermer(g))
    buC.pack()
    ph2=tkinter.PhotoImage(file='close_hover.png')
    buC.config(image=ph2,compound=tkinter.LEFT)
    #butri=tkinter.ttk.button(g,text='Trier')
    #def RTri():
    g.mainloop()
def tri(t,n):
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if t[j]<t[mini]:
                mini=j
        t[mini],t[i]=t[i],t[mini]
    return t
  


if '__main__'==__name__:
    interface()