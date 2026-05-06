# Rozwiązania Krytycznych Niespójności (K1 - K10)

Poniższy dokument stanowi szczegółowe rozwinięcie i analizę decyzji projektowych dotyczących pierwszych dziesięciu punktów z pliku `krytyczne_niespojnosci.md`. Dokument ten jest krokiem pośrednim – służy do zatwierdzenia szczegółów wizji, zanim zmiany zostaną wprowadzone do odpowiednich plików (frakcji, geografii, ras i systemu mocy).

---

### **K1: Biologia Aurynn (Rasa vs System Mocy)**
**Decyzja Użytkownika:** System Mocy jest nadrzędny. Aurynn *nie dysponują* Głosami Pierwszych. Ich wyjątkowość opiera się na konieczności złączenia się z innym bytem w celu przeżycia. Złączenie nie jest negatywne, wymaga obopólnej zgody i zatrzymuje dla nich presję czasu/rozpadu. Nie mają żadnego dostępu do Głosów.
**Rozwinięcie i Analiza:**
- **Usunięcie Głosów:** Posiadanie darmowego dostępu do kosmicznej siły (Głosów Pierwszych) łamało balans gry i deprecjonowało unikalność Głosicieli. Całkowite wycięcie tej mechaniki z rasy Aurynn naprawia "cheatowanie" systemu.
- **Złączenie Symbiotyczne:** Zamiast agresywnego "pożerania" energii, Aurynn będą ewoluować wokół idei zrównoważonej i pożądanej symbiozy. Aurynn to rasa efemeryczna, która odczuwa postępujący "głód bytu" (lub upływ czasu), dopóki nie utworzy silnej Więzi z innym nosicielem Iskry. Zgoda obu stron tworzy niezwykle unikalny duet, w którym Aurynn zyskuje stabilność i zatrzymanie upływu czasu (biologiczna wieczność do momentu rozbicia więzi), a u partnera nie wywołuje to negatywnych skutków mechanicznych czy fabularnych (może oferować wsparcie pasywne w postaci lepszej percepcji czy harmonii Splotu).
- **Zasieg Edycji:** Należy całkowicie przepisać plik `Rasy/Aurynn/00_Overview.md` (oraz wszelkie pokrewne), usuwając wzmianki o Głosach oraz modyfikując mechanikę Złączenia.
--- wydaje sie mocno OP?


### **K2: Paradoks Roju u Velmari (Biologia vs System Mocy)**
**Decyzja Użytkownika:** System Mocy jest nadrzędny. Należy naprawić "Paradoks Roju".
**Rozwinięcie i Analiza:**
- **Problem Wydrążenia (Hollowing):** Dotychczas bycie częścią mentalnego ula (Roju Velmari) równało się w Systemie zerowaniu woli (Wydrążeniu) przez nadrzędny byt, co całkowicie kasowało grywalność jednostek i łowców Velmari.
- **Rozwiązanie:** Rój Velmari zostanie zredefiniowany. Nie jest to już "aktywna tyrania jednej woli", ale raczej biologiczne, pasywne dziedzictwo – rozproszona "Sieć Empatii" (lub Echa Kasty). Każdy Velmari ma swoje własne "ja" i wolną wolę, ale na poziomie podświadomym odczuwa nastroje i echa swoich pobratymców na niewielkie odległości. Zostaną oni odpięci od "Globalnego Splotu Ula", co przywróci im autonomię wymaganą do zostania Łowcami. "Wydrążenie" wciąż pozostaje mrocznym widmem magii, ale bycie Velmari samo z nim nie koreluje.
---super


### **K3: Wampiryzm Prosterzy na Pustkowiach**
**Decyzja Użytkownika:** Pozostawiono wolną rękę do dopracowania. 
**Rozwinięcie i Analiza:**
- **Problem:** Prosterzy, wchłaniając pasywnie Zerum z powietrza, byliby skazani na natychmiastową śmierć uduszeniową w Głębokiej Dziczy (gdzie darmowego Zerum według zapisków nie ma).
- **Rozwiązanie:** Usuniemy mechanikę "pasywnego wampiryzmu strefowego". Zamiast tego, wampiryzm dzikich form (lub mutacji) opiera się na bezpośrednim transferze z płynów, nosicieli lub materii biologicznej (fizyczne "wypijanie/absorbowanie" przetworzonego Zerum z krwiobiegu ofiar, bestii lub Kamieni Esencji). Ich mechanika biologiczna wymaga *zapasu* – Prosterzy działają jak "zbiorniki", ładując się w przyczółkach lub przed wyprawą i powoli zużywając zgromadzone zapasy. W Dziczy nie wysysają powietrza, tylko czerpią z rezerw we własnym ciele lub z bestii, na które polują.
---wydaje sie ok


### **K4: Zamknięcie Ekonomii (Krystaliczne Pola vs Pęknięcia)**
**Decyzja Użytkownika:** Działki i przedpola z pewnego rodzaju zasobami zostają w "Średniej Dziczy", a postacie mogą żyć poza Murem. Riffy/Bramy (prawdziwe generatory Kamieni Esencji) ukazywać się będą od Średniej Dziczy wzwyż (a nie w samym centrum osiedli ludzkich).
**Rozwinięcie i Analiza:**
- Ziemie przy Bastionach i przedpolach to obszary na wpół zbadane – można tam uprawiać standardowe rolne surowce i prowadzić ludzkie osadnictwo, lecz "Krystaliczne Pola pełne darmowego Zerum" będą traktowane wyłącznie jako skąpe złoża o niskiej wartości, przydatne do zasilania żarówki, ale rynkowo niemal bezwartościowe.
- Prawdziwe Kamienie Esencji (te trzymające gospodarki, za które Bastiony walczą) rodzą się *wyłącznie* we wnętrzach aktywnych Bram/Pęknięć, które otwierają się dopiero na skraju Średniej i Głębokiej Dziczy. Dzięki temu najemnicy (Gracze) zawsze będą mieli motywację do wymarszu z domów na niebezpieczne rubieże.
---wydaje sie ok


### **K5: Fałszywe Natury vs System Mocy**
**Decyzja Użytkownika:** System Mocy (Natury Zerum) jest bezwzględnie nadrzędny. Wszystkie pliki ras do poprawki.
**Rozwinięcie i Analiza:**
- Pozbywamy się z praw świata słów takich jak: "Runa", "Krew" czy "Biomasa" w ujęciu systemowym. Magia na całym świecie opiera się na 8 sztywnych Naturach (np. Rdza, Czas, Pryzmat). 
- Jeśli jakaś cywilizacja (np. Tharumi lub Prosterzy) używa magii przypominającej władanie Krwią, to fabularnie wynika to ze specyficznego kontrolowania ukierunkowanego np. Czasu czy Rozkładu (Rdzy) komórek, ale w twardej mechanice gry gracz *zawsze* deklaruje użycie jednej ze standardowych 8 Natur twardego kanonu. Dopilnuje to stabilności balansu i walk.
- Pliki opisowe poszczególnych ras zostaną wyczyszczone z łamania tych ograniczeń.
---zgadzam sie


### **K6: Zakon Korzenników vs Geografia Bastionów**
**Decyzja Użytkownika:** Pliki Frakcji (Korzennicy jako wyższy zakon anielsko-strażniczy) są nadrzędne. Ujęcie Geograficzne musi zostać zmienione.
**Rozwinięcie i Analiza:**
- W plikach Geografii musimy gruntownie usunąć wszelkie wzmianki o Korzennikach jako tanich "wyrzutkach/buntownikach" tłumionych na ulicach przez milicję.
- Korzennicy to absolutna Kosmiczna Potęga, zjawiająca się wyłącznie wtedy, gdy równowaga fizyczna planety i apogeum zmian tego wymaga. Zastąpimy w opisie geograficznym tych "ulicznych buntowników" np. uciskaną subkulturą cywilną lub odłamem kultystów (lub frakcją Ostrzy Biedy, o ile ma to logiczny sens).
---wydaje sie ok 

### **K7: Problem Wędrujących Miast i Stacjonarnych Bram**
**Decyzja Użytkownika:** Poruszające się miasta i przedpola muszą zostać na mapie w sposób dostosowany.
**Rozwinięcie i Analiza:**
- **Dostosowanie Logiki:** Skoro Bramy (źrodła zasobów dla cywilizacji) to obiekty absolutnie stacjonarne, "Wielkie Poruszające się Bastiony" (Nomadzi na Archaionach) nie mogą żyć *całkowicie* poza orbitą Pęknięć.
- **Rozwiązanie Mechaniczne:** Zostaną one zaprojektowane jako cykliczne "Platformy Zbieracze" bądź Lotniskowce. Metropolie na ogromnych bestiach / maszynach krążą wytyczonymi szlakami "Od Pęknięcia do Pęknięcia". Zatrzymują się na kilka dekad nad wielką, trwalszą lokacją rzuconą w świecie, eksplorują ją wysyłając łowców (kotwicząc system przesyłu), i kiedy pożywka drastycznie słabnie, miasto zrywa zakotwiczenie i rusza w wieloletni marsz ku następnemu sygnałowi.
---wydaje sie ok

### **K8: Szczepienie "Wymarłych" Ras Zylmari, Nythrai, Pyrrhani**
**Decyzja Użytkownika:** "Do dostosowania"
**Rozwinięcie i Analiza:**
- **Problem:** Floty rynkowe handlują z martwymi rasami (Pyrrhani), a Zylmari budują stacjonarne podwodne miasta, choć wedle `Master Indexu Ras` gatunki te stanowią wykoszoną plagę mutantów czy bytów bez formy na wymarciu.
- **Dostosowanie:** Te 3 gatunki otrzymają oficjalny status **Pół-Wymarłych (Reliktowych)**. Cywilizacyjne dominia zostały obrócone w pył, główna tkanka zmutowała i wymarła, ale nieliczne garstki biologicznych autochtonów zachowały poczytalność i formę w ekstremalnie odizolowanych rezerwatach (Poniżej oceanu, czy głęboko w izolowanych lejach). Spotkanie Zylmari w stolicy na rynku to ewenement, a ich giełdowe imperia z rąk historii przeszły na poziom hermetycznych "enklaw rzemieślniczych", z którymi handel polega niemal na mistyce i rzadkiej dyplomacji, nie na masówkach z tysiącem handlarzy obcej rasy.
---inaczej chce. wole zeby te gatunki istnialy w mniejszosci wewnatrz tych co pisalem w podstawie. maja byc rzadkie ale istniec byc podobne ale unikalne.

### **K9: Dodruk Pieniądza vs Ekonomia Złota/Kamieni**
**Decyzja Użytkownika:** Złoto pozostaje materiałem do codziennego użytku (fizycznie produkowanym), Kamienie Esencji jako wyższa i rzadsza waluta.
**Rozwinięcie i Analiza:**
- "Magiczny dodruk monet w skarbcach Gildii z oparów Splotu" zostanie całkowicie wycięty z plików Frakcji.
- Złoto odzyskuje status fizycznie wydobywanego i trudem bitego kruszcu. Służy do opłacania usług rzemieślników, czynszów, życia codziennego.
- Kamienie Esencji stają się surowcem strategicznym na poziomie wyższym. Używa się ich do ulepszeń ekwipunku, podtrzymania życia w Bastionach i potężnych transakcji handlowych z arystokracją lub mrocznym rynkiem gildyjnym. Zapobiega to magii dewaluacji pieniądza (inflacji czarów).

### **K10: Bunt Iskrzyków w rasach Vrakai i Ghorran**
**Decyzja Użytkownika:** System Mocy ma rację bytu chroniąc Iskrzyki jako obiektywy bez ciała. Vrakai/Ghorran muszą zostać zmienione.
**Rozwinięcie i Analiza:**
- **Problem:** Rasy przypisały sobie Iskrzyki jako "fizyczne noszące towary pszczoły" lub "ogromne, bojowe byty konne", co łamało nietykalną zmysłowo-lekką definicję Iskrzyka (radaru magii).
- **Usunięcie i Zamiennik:** Pliki frakcji/ras dostaną poprawki. Orwellowskie byty fizyczne, rasy zrzucają na karby np. naturalnej tresury zwierzyny łownej (Zwykłe bestie oswojone w dziczy) LUB (jeśli mowa o umiejętności Iskrzyka) Iskrzyk u tych ras ma po prostu doskonały zasięg pasywny i lepsze mapowanie terenu. Zero chwytania liny czy bycia żywym gończym tatusiem w walce. Iskrzyk to w całym uniwersum przezroczyste Echo Umysłu w przestrzeni, nic więcej.

---
### Podsumowanie i Prośba do Użytkownika:
Powyższe rozwiązania zostały przygotowane w oparciu o Twoje wytyczne (K1-K10). Zgadzają się z obranym kursem stabilizacji *Systemu Mocy* jako kanonicznego kręgosłupa i zachowują poetykę świata, jednocześnie spinając mechaniczną logikę (ekonomia, klasy postaci).

Daj mi znać w konwersacji powrotnej:
1. **Czy akceptujesz wszystkie powyższe wyklarowania na ich podstawie?** 
2. **Czy rzucać następne punkty partiami (jeśli uznasz format 10 punktów za czytelny, możesz dorzucić kolejne)?**
3. Czy zaktualizować od razu pliki główne dla tej dziesiątki?
