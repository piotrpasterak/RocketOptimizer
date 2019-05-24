# RocketOptimizer

##Problem
Problem, który jest poruszony w niniejszej pracy dotyczy rozważań nad konstrukcją pierwszego członu rakiety nośnej Saturn V. Rakieta ta jest jednym z największych i najpotężniejszych obiektów kosmicznych wyprodukowanych w dziejach ludzkości. W 1969 roku wyniosła na orbitę i pozwoliła misji Apollo wylądować na księżycu oraz powrócić z niego.
Mimo tak odpowiedzialnego zadania, cały obiekt jest połączeniem zarówno prostoty jak i bezpieczeństwa. Jest to wynikiem braków technologicznych tamtych czasów, presji czasu związanej z wyścigiem o podbój kosmosu oraz niezwykłej współpracy tysięcy naukowców i inżynierów. Postawienie na prostotę skutkuje tym, że opis fizyczny pracy pierwszego stopnia rakiety daje się wyrazić za pomocą kilku zmiennych i kilkunastu stałych. Jednak prawdziwym zadaniem jest określenie, jak ma wyglądać optymalna praca tego podzespołu.

##Wybrane Algorytmy optymalizacji
Wybrano dwa algorytmy optymalizacji nieliowej z ograniczeniami:
Metoda COBYLA która jest najbardziej preferowana ze wzgledu na mechanism przyblizania przez linearyzowanie.
Metodę trust-constr ktora wyznacza minimum bazujac na gradiencie.

Przyjęte ograniczenia wynikuja z wlasciwości fizycznych (średnica musi być dodatnia),
oraz z wlasciwosci funkcji celu (wartości rzeczywiste dla V)

##Rozwiazanie
przedstwawione w postaci x(R,r)

Dla metody COBYLA
fun: 27212.467859518427
x: array([ 2.5 , 11.25])

zaskakujaco COBYLA zwraca blad: 
'Did not converge to a solution satisfying the constraints"
Niemniej rozwiazanie jest w granicach i jest lepsze niz w przypadku trust-constr. 

Dla metody trust-constr
fun: 75329.42647468536
x: array([ 4.76232147, 10.12042058])

Uzyskane wyniki wskazuja ze algorytm COBYLA(Constrained Optimization BY Linear Approximation) jest lepsza metoda dla tego problemu.
Wynika to z charakteru funkcji celu która jest zbliżona do liniowej w znacznacej czesci wyznaczonej dzedziny.

Ostatecznie:
r = 2.5
R = 11.25
V = 27212.467859518427