n = int(input("Dati numarul de elemente din vector = "))
a=[]
print('Introduceti', n, 'elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    a=extend([x])
prit(a)
print('a)afişează pe ecran componentele tabloului la un interval de 5 poziţii=',*a[0:5])
print('b)afişează pe ecran numerele în ordinea inversă a introducerii în calculator=',*a[::-1])
b=sorted(a)
b.sort(reverse=True)
print(b)
print('c)sortează componentele tabloului în ordine descrescătoare',)
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print('d)afişează pe ecran doar componentele pare',*c)
print('afişează pe ecran media aritmetică a componentelor pare',sum(c)/len(c))
d=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        z=a[i]
        d.extend([z])
print('f) afişează pe ecran doar componentele impare',*d)
x,y=eval(input('Afisati valorile lui x si y='))
g=[]
for i in a:
    if(i>x) and (i%y!=0):
        g.extend([i])
print('g)	 afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură) este',*g)
x,y=eval(input('Dati alte valori lui x si y='))
h=[]
for i in a:
    if (i>x) and (i<y):
        h.extend([i])
print('h)	 afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură este',*h)
i=[]
for i in range(0,len(a)):
      if(i//10!=0) and (i//10<0):
            w=a.index(i)
            i.extend([w])
print('i)afişează pe ecran poziţiile (indicii) componentelor impare negative'*i)
print('j) afiseaza pe ecran pozitiile (indicii) componentelor ce contin doar doua cifre semnificative')
print('k) inlocuieste prima componenta a tabloului cu componenta de valoare minima din tabloul respectiv')
print('l)inlocuieste componenta de valoare minima din tabloul respectiv cu primacomponenta a acestuia')
print('m) creeaza un tablou nou, format doar din componentele pare ale tablouluiintrodus de la tastatura')
print('n) creeaza un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatura')
print('o) creeaza un tablou nou, format doar din acele componente ale tabloului introdus de la tastatura care au cel mult patru divizori')