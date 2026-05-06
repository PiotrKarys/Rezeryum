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

# Rozwiązania Krytycznych Niespójności (K11 - K20)

---

### **K11: Mechanika Lochu (Tiery Bram vs Progi Mocy)**
**Diagnoza konfliktu:** Opis Bram wymusza stabilny „próg 4” jako standard rajdowy, podczas gdy `03_Progi_Mocy.md` prowadzi postęp inaczej i nie traktuje tego progu jako długiego etapu docelowego. Powstaje luka między progresją postaci a skalą instancji.
**Decyzja kanoniczna:** Utrzymujemy pięciostopniową skalę zagrożenia Bram, ale **Tier Bram nie jest tożsamy z progiem biologicznym postaci**. Tier opisuje środowisko i gęstość zagrożeń, a nie „wymagany numer progu” gracza.
**Konsekwencje:** Balans wraca do drużyn mieszanych (role wsparcia/awangardy), bez psucia ścieżek ewolucji ras. System Mocy pozostaje nadrzędny i nie wymusza sztucznego „progu parkingowego”.
**Plan wdrożenia:** `System_Mocy/08_Bramy.md` (sekcja tierów), `System_Mocy/03_Progi_Mocy_i_Przebudzenie.md` (doprecyzowanie relacji „próg vs środowisko”), wzmianki w `Frakcje_i_Zakony/06_Kartografowie_Otchlani.md`.

### **K12: Looting Pęknięć (regeneracja rdzeni bossów)**
**Diagnoza konfliktu:** Kartografowie opisują odrastanie rdzeni/serca, co niszczy sens harvestingu i ekonomii Kamieni Esencji.
**Decyzja kanoniczna:** Po śmierci bossa rdzeń **nie odrasta**; może wystąpić jedynie wtórna kondensacja szczątkowa strefy po długim czasie, bez przywrócenia tej samej istoty.
**Konsekwencje:** Utrzymana rzadkość łupu, sens zwiadu i ryzyka wypraw. Brak „farmy nieskończonej” z jednego ciała.
**Plan wdrożenia:** `Frakcje_i_Zakony/06_Kartografowie_Otchlani.md`, `System_Mocy/08_Bramy.md`, `System_Mocy/07_Iskrzyki_i_Kamienie_Esencji.md`.

### **K13: Ostrza Biedy a operacje w Riftach**
**Diagnoza konfliktu:** Frakcja uliczna została opisana jak podmiot swobodnie kontrolujący byty z Riftów, co przeczy skali zagrożeń Bram.
**Decyzja kanoniczna:** Ostrza Biedy **nie kontrolują** istot z Riftów; wykorzystują wyłącznie sabotaż szlaków, dezinformację i logistykę na obrzeżach.
**Konsekwencje:** Frakcja pozostaje groźna społecznie, ale nie narusza metafizyki Pęknięć ani hierarchii zagrożeń.
**Plan wdrożenia:** `Frakcje_i_Zakony/05_Ostrza_Biedy.md`, doprecyzowanie granic działań w `System_Mocy/08_Bramy.md`.

### **K14: Iskrzyk i „kieszeń przestrzenna”**
**Diagnoza konfliktu:** Jeden plik jednocześnie odbiera Iskrzykowi masę i daje mu zdolność noszenia przedmiotów.
**Decyzja kanoniczna:** Iskrzyk pozostaje bytem bezmasowym; „kieszeń” retconujemy na **technikę użytkownika** (mikrodepozyty, linki, zasobniki przy uprzęży), którą Iskrzyk tylko nawiguje.
**Konsekwencje:** Bez łamania udźwigu TTRPG i bez tworzenia „latającego muła”. Spójność ze słownikiem systemowym.
**Plan wdrożenia:** `System_Mocy/07_Iskrzyki_i_Kamienie_Esencji.md`, korekty ras korzystających z tej umiejętności.

### **K15: Latarnicy i zabezpieczanie nowych Pęknięć**
**Diagnoza konfliktu:** Latarnicy (formacja porządkowa) dostali kompetencje głębokich operacji ekspedycyjnych poza ich profilem.
**Decyzja kanoniczna:** Latarnicy zabezpieczają **strefę bastionową i perymetr**, a dalekie rozpoznanie/ekspedycje prowadzą wyspecjalizowane gildie i rajdy.
**Konsekwencje:** Czytelny podział ról frakcyjnych, brak teleportacji logistycznej służb miejskich.
**Plan wdrożenia:** `Frakcje_i_Zakony/01_Latarnicy.md`, odniesienia w `Geografia_i_Bastiony/Bastiony/*` i `System_Mocy/08_Bramy.md`.

### **K16: Kartografowie „wynajmują” Korzenników**
**Diagnoza konfliktu:** Korzennicy (siła najwyższego rzędu) zostali zdegradowani do roli egzekutorów sporów rynkowych.
**Decyzja kanoniczna:** Korzennicy są nieoperacyjni dla zleceń handlowych; Kartografowie używają własnych audytorów i arbitrażu gildyjnego.
**Konsekwencje:** Przywrócenie rangi Korzenników i wiarygodności drabiny zagrożeń.
**Plan wdrożenia:** `Frakcje_i_Zakony/06_Kartografowie_Otchlani.md`, `Frakcje_i_Zakony/04_Korzennicy.md`.

### **K17: Prawdziwe Imiona jako wymóg powszechnej ewolucji**
**Diagnoza konfliktu:** Szablony ras robią z Prawdziwego Imienia warunek standardowego rozwoju, choć to zjawisko skrajnie rzadkie.
**Decyzja kanoniczna:** Prawdziwe Imię jest **opcjonalnym, elitarnym katalizatorem**, nie wymogiem progów bazowych.
**Konsekwencje:** Zachowana rzadkość Imion i grywalność populacji nieelitarnych.
**Plan wdrożenia:** `Rasy/00_index.md`, `System_Mocy/04_Prawdziwe_Imiona.md`, `GLOSSARY_REZERYUM.md`.

### **K18: „Więź Pustki” Thrakkorów**
**Diagnoza konfliktu:** Cechę rasową oparto o mechanikę, której nie ma w aktualnym modelu więzi.
**Decyzja kanoniczna:** Minimalny retcon: „Więź Pustki” staje się **kulturową nazwą skrajnej Przysięgi (Vow)** z wysokim kosztem psychicznym, nie osobnym typem więzi.
**Konsekwencje:** Zachowany klimat Thrakkorów bez dodawania nowego silnika mechanicznego.
**Plan wdrożenia:** `Rasy/Thrakkor/02_Charakterystyka_i_Zdolnosci.md`, `System_Mocy/06_Wiezi_i_Symbiozy.md`, słownik.

### **K19: Reaktywacja starych terminów (Nurt/Eskalacja)**
**Diagnoza konfliktu:** Słownik i szablony odsyłają twórców do wycofanych pojęć, produkując błędy seryjnie.
**Decyzja kanoniczna:** Nurt/Eskalacja oznaczamy jako **archiwalne (deprecated)**; aktywny pozostaje model progów z bieżącego Systemu Mocy.
**Konsekwencje:** Ujednolicenie nomenklatury i koniec konfliktów redakcyjnych między nowymi plikami.
**Plan wdrożenia:** `GLOSSARY_REZERYUM.md`, `Rasy/00_index.md`, checklisty redakcyjne w indeksach działów.

### **K20: Milczący Imion i „wymazanie woli”**
**Diagnoza konfliktu:** Odbieranie Imienia opisano jak kasowanie osoby, co przeczy naturze Prawdziwego Imienia jako dodatku.
**Decyzja kanoniczna:** Sankcja Milczących to **złamanie rezonansu i degradacja statusu mocy**, nie ontologiczne wymazanie „ja”.
**Konsekwencje:** Wiarygodna inkwizycja bez łamania antropologii świata; nadal ciężka kara polityczno-magiczna.
**Plan wdrożenia:** `Frakcje_i_Zakony/02_Milczacy_Imion.md`, `System_Mocy/04_Prawdziwe_Imiona.md`.

# Rozwiązania Krytycznych Niespójności (K21 - K30)

---

### **K21: Orvhan i „unikalne Iskrzyki przenikające ściany”**
**Diagnoza konfliktu:** Opis rasowy czyni z cechy uniwersalnej (bezcielesność Iskrzyka) unikalność jednej rasy.
**Decyzja kanoniczna:** Każdy Iskrzyk przenika materię; unikalność Orvhan przenosimy na **precyzję mapowania i stabilność sygnału** w warunkach zakłóceń.
**Konsekwencje:** Spójność definicji Iskrzyka i zachowanie tożsamości Orvhan bez łamania systemu.
**Plan wdrożenia:** `Rasy/Orvhan/02_Charakterystyka_i_Zdolnosci.md`, `System_Mocy/07_Iskrzyki_i_Kamienie_Esencji.md`.

### **K22: Zarodki Cieni a zależność od Prawdziwego Imienia**
**Diagnoza konfliktu:** Warunek „mieszania z Prawdziwym Imieniem” czyni większość populacji odporną na Wydrążenie.
**Decyzja kanoniczna:** Wydrążenie wiąże się z **rezonansem Iskry i pęknięciem woli**, nie z posiadaniem Prawdziwego Imienia.
**Konsekwencje:** Zagrożenie Cieniem odzyskuje skalę społeczną; Imię pozostaje rzadkim wzmacniaczem, nie przepustką do infekcji.
**Plan wdrożenia:** `Zagrozenia/03_Zarodki_Cieni_i_Klatwy.md`, `System_Mocy/04_Prawdziwe_Imiona.md`, `World_Decisions.md`.

### **K23: Żniwiarze Cieni i „bezpieczna asymilacja skażenia”**
**Diagnoza konfliktu:** Frakcja opisana jakby neutralnie pochłaniała skażone Zerum bez ceny, co przeczy regule Hollowingu.
**Decyzja kanoniczna:** Żniwiarze stosują **kontrolowaną ekspozycję, rytuały filtracji i twarde limity**, a każdy kontakt niesie ryzyko degradacji.
**Konsekwencje:** Elitarność frakcji wynika z dyscypliny i kosztu, nie z immunitetu fabularnego.
**Plan wdrożenia:** `Frakcje_i_Zakony/03_Zniwiarze_Cieni.md`, `System_Mocy/01_Zerum_i_Splot.md`, `System_Mocy/06_Wiezi_i_Symbiozy.md`.

### **K24: Status populacyjny ras reliktowych**
**Diagnoza konfliktu:** Rozjazd między statusem „wymarłe” a aktywną obecnością społeczno-gospodarczą.
**Decyzja kanoniczna:** Minimalny retcon zgodny z Twoją uwagą: rasy reliktowe **istnieją jako rzadkie mniejszości** wewnątrz większych społeczeństw, bez własnych imperiów.
**Konsekwencje:** Zachowana grywalna obecność i egzotyka ras, bez niszczenia osi demograficznej świata.
**Plan wdrożenia:** `World_Decisions.md` (status ras), `Rasy/00_index.md`, odpowiednie sekcje w `Geografia_i_Bastiony/*`.

### **K25: Oś czasu historii vs bieżący stan świata**
**Diagnoza konfliktu:** Część opisów sugeruje jednoczesność wydarzeń, które w kanonie należą do różnych epok odbudowy po katastrofach.
**Decyzja kanoniczna:** Wprowadzamy **trójwarstwową chronologię**: Era Pęknięcia, Era Stabilizacji Bastionów, Era Obecna.
**Konsekwencje:** Czytelna przyczynowość dla polityki, migracji ras i zmian systemu mocy.
**Plan wdrożenia:** `Historia_Swiata/00_Index.md`, adnotacje epok w `World_Decisions.md` i indeksach działów.

### **K26: Geografia szlaków a dostęp do zasobów strategicznych**
**Diagnoza konfliktu:** Część tras handlowych opisana jest jak stale bezpieczna mimo zależności od stref wysokiego ryzyka.
**Decyzja kanoniczna:** Szlaki dzielimy na **stałe bastionowe** i **okna ekspedycyjne** (czasowe, konwojowane, o wysokiej stracie).
**Konsekwencje:** Wzrost wiarygodności ekonomii ryzyka i znaczenia eskort/frakcji ochronnych.
**Plan wdrożenia:** `Geografia_i_Bastiony/Bastiony/*/03_*.md`, `Frakcje_i_Zakony/07_Gildie_Handlowe.md`.

### **K27: Kompetencje frakcji porządkowych i militarnych**
**Diagnoza konfliktu:** Te same działania przypisane równolegle wielu frakcjom (nakładanie ról).
**Decyzja kanoniczna:** Ustanawiamy matrycę: **porządek wewnętrzny (Latarnicy), wywiad i mapowanie (Kartografowie), egzekutywa doktrynalna (Milczący), operacje anomalii (Żniwiarze)**.
**Konsekwencje:** Mniej kolizji fabularnych, łatwiejsze projektowanie konfliktów kampanijnych.
**Plan wdrożenia:** `Frakcje_i_Zakony/00_Index.md` + profile `01`, `02`, `03`, `06`.

### **K28: Słownik vs aktualna semantyka kanonu**
**Diagnoza konfliktu:** Definicje w słowniku są mieszanką wersji historycznych i bieżących, co produkuje sprzeczne interpretacje.
**Decyzja kanoniczna:** W słowniku każda definicja dostaje znacznik: **KANON AKTYWNY / ARCHIWUM / RETCON**.
**Konsekwencje:** Redakcja i twórcy mają jedno źródło prawdy bez przywracania martwych mechanik.
**Plan wdrożenia:** `GLOSSARY_REZERYUM.md`, linkowanie do sekcji źródłowych w `System_Mocy/*`.

### **K29: Skala zagrożeń lokalnych vs globalnych**
**Diagnoza konfliktu:** Niektóre opisy miejskie eskalują incydenty lokalne do poziomu quasi-apokalipsy, co rozmywa hierarchię zagrożeń.
**Decyzja kanoniczna:** Wprowadzamy cztery klasy: **Lokalne, Regionalne, Kontynentalne, Egzystencjalne**; tylko ostatnia dotyczy ryzyka upadku ładu świata.
**Konsekwencje:** Spójny ton dark fantasy bez ciągłego „końca świata”.
**Plan wdrożenia:** `World_Decisions.md`, `Zagrozenia/00_Index.md`, oznaczenia w plikach frakcyjnych.

### **K30: Rekrutacja zakonów a tożsamość rasowa**
**Diagnoza konfliktu:** Część tekstów traktuje zakony jak odrębne „rasy funkcjonalne”, co łamie zamknięty katalog ras.
**Decyzja kanoniczna:** Zakony to **instytucje ponadrasowe**; mogą mieć profile selekcji, ale nie zmieniają ontologii gatunku.
**Konsekwencje:** Utrzymany porządek biologii i czytelna różnica: rasa = pochodzenie, zakon = droga.
**Plan wdrożenia:** `Frakcje_i_Zakony/03_Zniwiarze_Cieni.md`, `Rasy/00_index.md`, `World_Decisions.md`.

# Rozwiązania Krytycznych Niespójności (K31 - K37)

---

### **K31: Strażnicy wysokiego rzędu ignorują realne zagrożenia polityczno-kultowe**
**Diagnoza konfliktu:** Opisy części frakcji sugerują selektywne „niedowidzenie” zagrożeń, mimo że te same byty mają mandat do ochrony ładu świata.
**Decyzja kanoniczna:** Wprowadzamy zasadę **progu interwencji**: byty najwyższego rzędu nie reagują na każdy konflikt polityczny, ale reagują, gdy zjawisko przekracza wskaźniki destabilizacji Splotu.
**Konsekwencje:** Brak sprzeczności między „rzadką obecnością” a faktyczną odpowiedzialnością strażników; polityka lokalna pozostaje domeną frakcji niższego rzędu.
**Plan wdrożenia:** `Frakcje_i_Zakony/04_Korzennicy.md`, `Frakcje_i_Zakony/02_Milczacy_Imion.md`, `World_Decisions.md`.

### **K32: Skala bierności vs skala inkwizycji**
**Diagnoza konfliktu:** Narracja miejscami jednocześnie przedstawia totalną inwigilację i pełną bezradność wobec jawnych centrów kultu.
**Decyzja kanoniczna:** Minimalny retcon: inkwizycja jest **silna operacyjnie, ale ograniczona politycznie i geograficznie**; jawne ośrodki funkcjonują przez układy władzy, nie przez „niewidzialność”.
**Konsekwencje:** Konflikt staje się wiarygodny (wojna wpływów, blokady jurysdykcyjne), bez obalania kompetencji Milczących.
**Plan wdrożenia:** `Frakcje_i_Zakony/02_Milczacy_Imion.md`, `Geografia_i_Bastiony/Bastiony/Mury_Koron/*`, `Frakcje_i_Zakony/08_Kulty_Pekniec.md`.

### **K33: Samowolny dual-classing Natur (Cień + Pryzmat)**
**Diagnoza konfliktu:** Niektóre opisy klas łamią regułę jednej Wrodzonej Natury i zakaz niektórych synergii.
**Decyzja kanoniczna:** Postać ma jedną Naturę bazową; „druga” manifestacja to **technika sprzętowa, taktyczna albo efekt zespołowy**, nie druga Natura użytkownika.
**Konsekwencje:** Utrzymanie matematyki balansu i czytelnych buildów TTRPG.
**Plan wdrożenia:** `System_Mocy/02_Natury_Zerum.md`, odpowiednie sekcje w `Geografia_i_Bastiony/*` (np. szkoły bojowe), `Rasy/00_index.md`.

### **K34: Rezonans zdegradowany względem Absolutu**
**Diagnoza konfliktu:** Fragmenty opisują Rezonans jako „podrzędny” wobec Absolutu, mimo że są to równorzędne ścieżki końcowe.
**Decyzja kanoniczna:** Rezonans i Absolut są **równoprawnymi szczytami**; różnią się profilem zastosowań, nie rangą ontologiczną.
**Konsekwencje:** Przywrócenie spójności drzewka progresji i ról końcowych postaci.
**Plan wdrożenia:** `System_Mocy/03_Progi_Mocy_i_Przebudzenie.md`, `System_Mocy/05_Glosy_Pierwszych.md`.

### **K35: Żniwiarze jako pacyfiści vs oskarżenia o masowe egzekucje cywilów**
**Diagnoza konfliktu:** Źródła dają sprzeczne obrazy tej samej frakcji: neutralni łowcy anomalii vs aktywna eksterminacja ludności.
**Decyzja kanoniczna:** Przyjmujemy mniej kolizyjny wariant: Żniwiarze **nie prowadzą czystek ludności**; wykonują punktowe eliminacje jednostek krytycznie skażonych, zwykle po ewakuacji strefy.
**Konsekwencje:** Zachowanie etosu zakonu i mrocznego tonu (trudne decyzje bez ludobójczego retconu).
**Plan wdrożenia:** `Frakcje_i_Zakony/03_Zniwiarze_Cieni.md`, `Frakcje_i_Zakony/08_Kulty_Pekniec.md`, `Zagrozenia/03_Zarodki_Cieni_i_Klatwy.md`.

### **K36: Tożsamość „Ostrzy Biedy” vs „Przysięgłych Więzi”**
**Diagnoza konfliktu:** Słownik i frakcje miejscami traktują nazwę po reworku i nazwę historyczną jak dwa odrębne byty.
**Decyzja kanoniczna:** „Przysięgli Więzi” to **nazwa archiwalna** tej samej formacji, obecnie funkcjonującej jako „Ostrza Biedy”.
**Konsekwencje:** Koniec sztucznego dublowania sił rebelianckich i klarowna genealogia frakcji.
**Plan wdrożenia:** `GLOSSARY_REZERYUM.md`, `Frakcje_i_Zakony/05_Ostrza_Biedy.md`, `Frakcje_i_Zakony/00_Index.md`.

### **K37: Legalizacja niekanonicznej Natury „Krew” przez plik o Głosach**
**Diagnoza konfliktu:** Dokument o Głosach sankcjonuje odrzuconą terminologię natur, podważając zamknięty układ ośmiu Natur.
**Decyzja kanoniczna:** „Krew” pozostaje **metaforą stylu użycia** (np. bio-kinetyka przez legalne Natury), nie osobną Naturą.
**Konsekwencje:** Zachowana spójność systemowa i możliwość utrzymania estetyki ras bez mnożenia bytów mechanicznych.
**Plan wdrożenia:** `System_Mocy/05_Glosy_Pierwszych.md`, `System_Mocy/02_Natury_Zerum.md`, `Rasy/Prosterzy/*`.

# Rozwiązania Krytycznych Niespójności (K38 - K42)

---

### **K38: Wymuszony „Zbrojmistrz” dla Progu 5**
**Diagnoza konfliktu:** Słownik narzuca obowiązkową profesję pośrednią dla awansu, której nie wspierają pliki systemowe.
**Decyzja kanoniczna:** „Wybitny Zbrojmistrz” to **opcjonalna ścieżka wsparcia rzemieślniczego**, nie warunek osiągnięcia Progu 5.
**Konsekwencje:** Zachowany indywidualny rozwój postaci i sens profesji craftingowych bez blokowania progresji.
**Plan wdrożenia:** `GLOSSARY_REZERYUM.md`, `System_Mocy/03_Progi_Mocy_i_Przebudzenie.md`, wzmianki w frakcjach rzemieślniczych.

### **K39: Degradacja Korzenników do roli „gończych”**
**Diagnoza konfliktu:** Pliki szkoleniowe używają Korzenników jak zwykłej służby dyscyplinarnej.
**Decyzja kanoniczna:** Korzennicy nie realizują spraw kadrowych; uczelnie i zakony korzystają z własnych struktur porządkowych.
**Konsekwencje:** Przywrócenie hierarchii kosmologicznej i wiarygodności skali interwencji.
**Plan wdrożenia:** `Frakcje_i_Zakony/09_Iglica_Nazwanych.md`, `Frakcje_i_Zakony/04_Korzennicy.md`.

### **K40: Zakon potraktowany jako odrębna rasa**
**Diagnoza konfliktu:** Żniwiarze Cieni bywają opisani jak „gatunek”, co łamie zamknięty katalog ras.
**Decyzja kanoniczna:** Żniwiarze to **zakon rekrutacyjny ponadrasowy**, bez statusu biologicznego.
**Konsekwencje:** Spójny podział: rasa = pochodzenie biologiczne, zakon = afiliacja i doktryna.
**Plan wdrożenia:** `Frakcje_i_Zakony/03_Zniwiarze_Cieni.md`, `Rasy/00_index.md`, `World_Decisions.md`.

### **K41: Totalna inwigilacja vs jawny kult w Murach Koron**
**Diagnoza konfliktu:** Jednoczesne twierdzenia o absolutnej kontroli Milczących i jawnej dominacji kultu tworzą sprzeczność wykonawczą.
**Decyzja kanoniczna:** Milczący mają skuteczność wysoką, lecz **nie absolutną**; Mury Koron funkcjonują jako strefa chronicznego sporu wpływów, infiltracji i rozejmów wymuszonych politycznie.
**Konsekwencje:** Konflikt staje się stabilny narracyjnie i nadaje sens długiej grze wywiadów.
**Plan wdrożenia:** `Frakcje_i_Zakony/02_Milczacy_Imion.md`, `Geografia_i_Bastiony/Bastiony/Mury_Koron/*`, `World_Decisions.md`.

### **K42: Legiony/Kulty i „natychmiastowy koniec świata”**
**Diagnoza konfliktu:** Opis zagrożenia podnosi lokalne działania kultów do niekanonicznej, pewnej apokalipsy globalnej.
**Decyzja kanoniczna:** Kulty i Legiony są **zagrożeniem wysokim, lecz nie automatycznie egzystencjalnym**; eskalacja globalna wymaga splotu wielu warunków i długiego procesu.
**Konsekwencje:** Utrzymanie tonu „świat pęknięty, ale trwały” zgodnie z osią `World_Decisions`.
**Plan wdrożenia:** `Zagrozenia/02_Legiony_Wydrazonych.md`, `Frakcje_i_Zakony/08_Kulty_Pekniec.md`, `World_Decisions.md`.
