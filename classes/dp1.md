# Sessió en línia del dia 23/11/2020: Programació Dinàmica

La programació dinàmica, inventada pel matemàtic Richard Bellman el 1953, és un mètode per a reduir el temps d'execució d'un algorisme mitjançant la utilització de **subproblemes superposats** i **subestructures òptimes**. El concepte de Subestructura òptima vol dir que es poden fer servir solucions òptimes de subproblemes per a trobar la solució òptima del problema en el seu conjunt. 


Podem dir que l'objectiu bàsic de la programació dinàmica consisteix en "descompondre" un problema d'optimització en ``k`` variables a una seria de problemes amb un menor número de variables i per tant més fàcils de resoldre. Què vol dir això: Si posem com a exemple el problema de la motxilla el que farem és reduir el problema inicial de ``n`` variables a ``n`` problemes amb 1 variable. En aquest sentit, podem dir que la programació dinàmica es basa en un mètode de descomposició.

A la pregunta: Es pot resoldre qualsevol problema mitjançant la programació dinàmica? La resposta és NO. Per poder resoldre un problema mitjançant programació dinàmica, aquest ha de complir una sèrie de condicions que anirem veient.

--- 
### Exemple: Successió de Fibonacci

Per exemple, trobar la solució de Fibonacci de 3 (``fib(3)``) suposa trobar la solució de ``fib(2)``i ``fib(1)``, és a dir, podem considerar que la solució òptima del problema  ``fib(3)`` és pot aconseguir trobant la solució als subproblemes ``fib(2)``i ``fib(1)``. Direm que un problema té subproblemes superposats quan fem servir un mateix subproblema per a resoldre diferents problemes majors. Per exemple, en la successió de Fibonacci de 5 (``fib(5)``), calcular la solució suposa calcular la ``fib(4)`` i ``fib(3)``. Una mala implementació per calcular ``fib(5)`` acabarà calculant ``fib(3)`` dos cops, i ``fib(2)`` dos o més cops. Això passa sempre que hi hagi subproblemes superposats: una mala implementació pot acabar desaprofitant temps recalculant les solucions òptimes a subproblemes que ja han estat resolts anteriorment.


---

En general, es poden resoldre problemes amb subestructures òptimes seguint aquests tres passos:

1. Dividir el problema en subproblemes més petits.
2. Resoldre aquests problemes de manera òptima fent servir aquest procés de tres passos recursivament.
3. Emprar aquestes solucions òptimes per a construir una solució òptima al problema original.

Els subproblemes es resolen al seu torn dividint-los en subproblemes més petits fins que s'assoleixi el cas base, on la solució al problema és trivial.


La programació dinàmica no hauria de ser un concepte nou per a vosaltres, de fet ja heu utilitzat aquest concepte a diversos problemes. Per trobar la solució de la successió de Fibonacci o bé per trobar el distancia d'edició d'una paraula P a una altra paraula Q (algoritmes de Levenshtein).


En resum, la programació dinàmica fa ús de:

1. Subproblemes superposats;
2. Subestructures òptimes;
3. Memorització.


**Divide & Conquer vs. Programació Dinàmica**
* Divide & Conquer: Dividir el problema amb subproblemes, solucionar el problema recursivament, i finalment combinar les seves solucions per tal de solucionar el problema original.
* Programació Dinàmica:
  * Aplicable quan els subproblemes no són independents, és a dir, quan els subproblemes comparteixen subproblemes.
  * Soluciona cada subproblema un únic cop i emmagatzema la solució dins una taula, evitant així tornar-ho a calcular si un altre cop es necessita resoldre el subproblema
  
### Successió de Fibonacci

Solució naive

```python
def fibonacci(n):
    if n<0:
        print("Incorrect input")
        return 0
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
print(fibonacci(5)) 

```


Solució amb programció dinàmica

```python
def fibonacci(n): 
    if n<0:
        print("Incorrect input")
        return 0
    # Taking 1st two fibonacci numbera as 0 and 1 
    f = [0, 1] 
     
    # compute Fibonacci from 2 to n 
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
     
print(fibonacci(5)) 
```

---

### Floyd Warshall
L'algoritme de Floyd Warshall és un algorisme per trobar els camins més curts en un graf ponderat amb pesos positius o negatius (però sense cicles negatius).

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/4NQ3HnhyNfQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

---

### Exercici 1: Problema canvi monedes

Problema: Donat un conjunt ``n`` tipus de monedes cada una d'elles amb un valor ``C_i`` (per exemple, 1€; 2€; 5€; 15€; 50€; 100€ ), i una quantitat Q, trobar el número mínim de monedes a utilitzar per obtenir la quantitat exacta.

#### Alguna proposta amb un algoritme greedy? 
* La solució és molt eficient, però és òptima?

Penseu ara amb una solució amb **Programació Dinàmica**. Per tal de resoldre el problema amb programació dinàmica hem de definir: 1) equació recurrent; 2) Casos base.

**Definició de l'equació recurrent:**

* ``Canvi(j,Q)``: Calcula el número mínim de monedes necessàries per a retornar una quantitat ``Q``, utilitzant els ``j`` primers tipus de monedes (és a dir, 1..j). Si j =3 i els nostres tipus de moneda son (1€; 2€; 5€; 15€; 50€; 100€) estem buscant una solució que únicament utilitza els 3 primers tipus, es a dir, (1€; 2€; 5€)

* La solució de ``Canvi(j,Q)`` pot utilizar ``k`` monedes de tipus ``j`` o pot no utilizar-ne cap.
  * Sinó utilitza cap moneda d'aquest tipus: ``Canvi(j,Q) = Canvi(i-1,Q)``
  * Si s'utilitza ``k`` monedes del tipus ``j``: ``Canvi(j,Q) = Canvi(j,Q-k*c_i) +  k``



* En qualsevol cas, el valor sempre serà el mínim:
  * ``Canvi(i,Q) = min_{k=0,1,..Q/C_i}{Canvi(i-1,Q-k*c_i) + k}``

**Casos base:**

* Si ``(j<1)`` o ``(Q<0)`` no hi ha cap solució al problema i ``Canvi(j,Q) = +inf``
* Per a qualsevol ``j>0``, ``Canvi(i,0) = 0``

**Definició de les taules utilitzades**

* Necessitem emmagetzemar els resultats de tots els subproblemes.
* El problema  resoldre és: ``Canvi(n,Q)``
  * Per tant necessitem una taula de ``n x Q`` d'enters, que anomenarem ``D``, on ``D[i,j]=Canvi(i,j)``
  
**Exemple:**
* Número de tipus de monedes ``n = 3``; Canvia retornar ``Q = 8``; valors de les monedes ``v = (1,4,6) `` 

|         | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---------|---|---|---|---|---|---|---|---|---|
| V_1 = 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| V_2 = 4 | 0 | 1 | 2 | 3 | 1 | 2 | 3 | 4 | 2 |
| V_3 = 6 | 0 | 1 | 2 | 3 | 1 | 2 | 1 | 2 | 2 |

Les columnes corresponen a la quantitat a retornar, i les files amb diferent tipus de monedes.


Per arribar a aquesta solució, hem de aplicar de dalt a baix i de esquerra a dreta, la funció de recurrencia:
* ``D[i,j] = min_{k=0,1,..Q/C_i}{D(i-1,Q-k*c_i) + k}``

**Implementeu el codi.**


--- 

### Problema de la motxilla 0/1

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/cJ21moQpofY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>



---
### Exercici 2: El viatge més barat pel riu
En un riu hi ha ``n`` embarcadors, en cadascun d’ells es pot llogar un bot per anar a un altre embarcador situat a una zona més baixa del riu. Suposem que no es pot remuntar el riu. Una taula de tarifes indica els costos de viatjar entre els diferents embarcadors. Se suposa que un viatge entre ``i`` i ``j`` pot sortir més barat fent diverses escales que no pas anar-hi directament.

El problema consisteix amb determinar el **cost mínim** per a anar d’un embarcador a un altre. Els costos vénen definits per la taula de tarifes, ``T``. Així, ``T [i, j]`` serà el cost d'anar de l'embarcador ``i`` a l'``j``. La matriu serà triangular superior d'ordre ``n``, on ``n`` és el nombre d’embarcadors.

La idea recursiva és que el cost es calcula de la següent manera: ``C (i, j) = T [i, k] + C (k, j)``

L'expressió recurrent per a la solució pot ser definida com: 

``C (i, j) = ``
* ``0`` si ``i = j``
* ``min(T[i,j] + C[k,j]),T[i,j])``  si  ``i<k<=j``


**Implementeu el codi.**

