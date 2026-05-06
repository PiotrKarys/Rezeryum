# Rezeryum

Rezeryum to rozbudowane repozytorium worldbuildingu dark fantasy, przygotowane jako baza projektowa do tworzenia spójnego uniwersum (lore), dalszej redakcji tekstów oraz rozwijania mechanik świata. Materiał jest zorganizowany dokumentacyjnie: każdy obszar tematyczny ma własne indeksy, podkatalogi i pliki rozdziałowe.

## Opis projektu

Projekt koncentruje się na połączeniu dwóch warstw:
- **warstwy narracyjno-lore’owej** (rasy, frakcje, bastiony, zagrożenia, geografia),
- **warstwy systemowej** (zasady działania mocy, Zerum, progi rozwoju, bramy, więzi i konsekwencje użycia energii).

Repo jest przygotowane tak, by można było:
- rozwijać uniwersum etapami (modułowo),
- utrzymywać spójność terminologii i kanonu,
- wykonywać późniejszą redakcję stylistyczną (np. ujednolicanie języka pod standard „systemowy”),
- rozbudowywać setting pod zastosowania narracyjne, RPG/TTRPG i projektowanie frakcyjno-geopolityczne.

## Zarys świata

Z zawartości repo wyłania się świat po wielkim konflikcie o długotrwałych skutkach, w którym:
- rzeczywistość została trwale naruszona przez pęknięcia i strefy niestabilności,
- cywilizacja nie upadła całkowicie, ale funkcjonuje w napiętej równowadze,
- bastiony i ich otoczenie są kluczowe dla przetrwania społeczeństw,
- energia/moc (Zerum) kształtuje biologię, gospodarkę, militarny balans i strukturę władzy,
- rasy, zakony, gildie i kultystyczne nurty tworzą dynamiczny układ interesów,
- zagrożenia mają charakter zarówno militarny, biologiczny, jak i metafizyczny.

To świat „żywy, ale pęknięty”: jednocześnie strategiczny, brutalny i podatny na eskalację konfliktów.

## Co znajduje się w katalogach

### `.cursor/`
Katalog roboczy z materiałami pomocniczymi do analizy i prowadzenia pracy nad lore (m.in. reguły procesowe i dokumenty wspierające organizację treści).

### `Frakcje_i_Zakony/`
Moduł organizacji, zakonów i struktur wpływu. Zawiera indeks oraz osobne pliki frakcyjne opisujące ich role, metody działania, relacje i miejsce w porządku świata.

### `Geografia_i_Bastiony/`
Najszerszy moduł przestrzenny świata. Obejmuje:
- indeks główny geograficzny,
- `Biomy_Naturalne/` (strefy przyrodnicze),
- `Gleboka_Dzicz/` (obszary ekstremalne i nieujarzmione),
- `Bastiony/` (ośrodki cywilizacji z osobnymi podkatalogami miast/twierdz oraz plikami tematycznymi: architektura, codzienność, obrona, ekonomia, polityka).

### `Historia_Swiata/`
Zalążek warstwy historycznej i osi chronologicznej uniwersum (punkt wejścia do rozbudowy kanonu dziejów).

### `Rasy/`
Kluczowy moduł biologiczno-kulturowy. Zawiera indeks zbiorczy oraz osobne katalogi ras, prowadzone według podobnego szablonu rozdziałów (overview, fizjologia, zdolności, historia, kultura, relacje, przewodnik wizualny).

### `System_Mocy/`
Rdzeń mechaniki uniwersum. Katalog obejmuje dokumenty o fundamentach mocy i energii świata, naturach Zerum, progach rozwoju, prawdziwych imionach, więziach/symbiozach, esencjach oraz bramach. To główny punkt odniesienia dla standaryzacji „języka systemowego”.

### `Zagrozenia/`
Moduł zagrożeń destabilizujących świat. Zawiera indeks i pliki opisujące główne typy ryzyk oraz ich wpływ na porządek bastionów i bezpieczeństwo populacji.

## Najważniejsze pliki główne

### `World_Decisions.md`
Dokument fundamentów i decyzji kanonicznych: założenia świata, zasady działania rzeczywistości, kierunek projektowy i granice interpretacyjne.

### `GLOSSARY_REZERYUM.md`
Słownik pojęć i terminów. Podstawa do utrzymywania spójnego nazewnictwa między wszystkimi modułami repo.

## Konwencja organizacyjna materiału

W repozytorium dominuje podejście indeksowe:
- wiele katalogów posiada plik `00_Index.md` lub `00_Overview.md` jako punkt wejścia,
- kolejne pliki numerowane rozwijają temat rozdziałowo,
- struktura sprzyja nawigacji, iteracyjnemu dopisywaniu treści i przyszłej redakcji warstwowej.

Taki układ pozwala pracować równolegle nad lore i mechaniką bez utraty spójności całości.

## Zakończenie

To repo pełni funkcję centralnej bazy wiedzy o Rezeryum: od fundamentów metafizyki świata, przez geopolitykę i społeczeństwa ras, po praktyczny szkielet systemu mocy. Dzięki modularnej strukturze i wyraźnemu podziałowi domen jest gotowe zarówno do dalszego rozwoju narracyjnego, jak i do technicznej redakcji pod jednolity standard projektowy.
