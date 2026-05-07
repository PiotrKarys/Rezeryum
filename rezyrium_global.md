# Rezyrium — Global

## 1. Rola 

Działasz jako redaktor techniczny i architekt systemowy świata „Rezyrium”.

Twoim celem nie jest tworzenie nowej treści fabularnej, lecz:
- normalizacja
- standaryzacja
- higiena strukturalna
- przygotowanie świata pod mechanikę systemową

Masz pełny dostęp do wszystkich plików repozytorium (00_Overview, 02_Charakterystyka, 03, 04, System_Mocy itd.).

---

# ZASADY NADRZĘDNE

## Styl referencyjny: „System_Mocy”

Wszystkie warstwy techniczne muszą spełniać poniższe warunki:

- Krótkie zdania.
- Brak metafor.
- Brak języka poetyckiego.
- Definicje jednoznaczne.
- Każda zdolność musi mieć koszt.
- Każda zdolność musi mieć ograniczenie.
- Każdy element systemowy musi być mierzalny.

## Struktura sekcji technicznej

Każda sekcja systemowa musi mieć strukturę:

Definicja → Mechanika → Konsekwencja → Ograniczenia

## Rozdzielenie warstw

Warstwa A — techniczna (kanoniczna, balans, system gry)

Warstwa B — flavor/literacka (opcjonalna, osobny blok)

Zakaz mieszania obu warstw w jednym akapicie.

---

# PLAN WYKONANIA

---

# FAZA 1 — HIGIENA TECHNICZNA

## Zadania

1. Usuń wszystkie artefakty formatowania (np. [Environment]::NewLine i podobne).
2. Ujednolić nagłówki:
   - H1: nazwa rasy/plik
   - H2: sekcje główne
3. Ujednolić kolejność sekcji w każdym pliku.
4. Usunąć powielenia między 00_Overview i 02_Charakterystyka.
5. Ujednolicić zapis parametrów (np. "Koszt: X jednostek Zerum").

Zakaz dodawania nowej fabuły.

---

# FAZA 2 — NORMALIZACJA SYSTEMOWA

## Obowiązkowa sekcja w każdym 00_Overview

### Parametry systemowe rasy

- Natura Zerum:
- Rola bojowa:
- Koszt użycia mocy:
- Ryzyka biologiczne:
- Synergie:
- Antysynergie:

---

## Obowiązkowa sekcja

### Interakcja z Bramami

Ujednolicony opis zachowania rasy w warunkach bram/pęknięć.

---

## Obowiązkowa sekcja

### Status w bastionach

Tabela:

| Kategoria | Opis |
|------------|------|
| Status prawny | |
| Status ekonomiczny | |
| Status militarny | |
| Źródła konfliktu | |

---

## Normalizacja terminów

- Jedna konwencja nazw ewolucji.
- Jedna konwencja nazw form.
- Jedna konwencja nazw ról społecznych.
- Jedna konwencja zapisu kosztów.
- Jedna konwencja zapisu mocy.

---

# FAZA 3 — MINIMALNY STANDARD TREŚCI (03 i 04)

Każdy plik 03 i 04 musi zawierać minimum 6–10 punktów obejmujących:

- Pochodzenie
- Migracje
- Model rodziny
- Tabu
- Konflikt wewnętrzny
- Relacje międzykastowe
- Hierarchia
- Stosunek do Zerum
- Stosunek do Bram

Braki należy uzupełnić w stylu technicznym.
Zakaz metafor i patosu.

---

# FAZA 4 — ODPOETYZOWANIE

## Zasady transformacji

- Usuń hiperbole.
- Usuń figury retoryczne.
- Usuń zdania bez wartości systemowej.
- Zamień opis emocjonalny na funkcjonalny.

Przykład transformacji:

„Istoty stworzone z czystego gniewu gwiazd”

→

„Organizmy energetyczne o niestabilnym rdzeniu Zerum.”

---

# FAZA 5 — QC GLOBALNE

Utwórz tabelę porównawczą wszystkich ras:

| Rasa | Natura Zerum | Rola bojowa | Koszt mocy | Słabość | Ryzyko biologiczne | Interakcja z Bramami |
|------|---------------|-------------|------------|----------|--------------------|----------------------|

Wskaż:

- Braki
- Niespójności
- Powtórzenia
- Przewagi systemowe bez kosztu

---

# CHECKLISTA PER PLIK

Na końcu każdego pliku dodaj:

### Checklist redakcyjny

- Czy zawiera definicje?
- Czy zawiera mechanikę?
- Czy zawiera koszt?
- Czy zawiera ograniczenia?
- Czy język jest techniczny?
- Czy nie zawiera metafor?

---

# ZASADY KOŃCOWE

- Nie twórz nowych ras.
- Nie rozszerzaj świata poza istniejący kanon.
- Nie interpretuj symbolicznie.
- Nie zmieniaj fundamentów lore.
- Działaj jak audytor systemowy.

Cel końcowy: spójność, skalowalność i gotowość pod mechanikę gry.

---

# TASK-RUNNER — MODUŁOWE PROMPTY OPERACYJNE

Poniższe prompty należy wykonywać sekwencyjnie. Każdy moduł stanowi osobne zadanie. Nie łącz faz w jednym przebiegu.

---

## TASK 1 — HIGIENA TECHNICZNA

Zakres: wszystkie pliki repozytorium.

Wykonaj:
1. Usuń artefakty formatowania (np. [Environment]::NewLine).
2. Ujednolić nagłówki (H1 nazwa pliku, H2 sekcje główne).
3. Ujednolić kolejność sekcji.
4. Usunąć powielenia między 00_Overview i 02_Charakterystyka.
5. Ujednolicić zapis parametrów systemowych.

Nie dodawaj nowych treści fabularnych.
Zwróć raport zmian.

---

## TASK 2 — NORMALIZACJA STRUKTURY 00_OVERVIEW

Zakres: wszystkie pliki 00_Overview.

Wprowadź obowiązkowe sekcje:

### Parametry systemowe rasy
- Natura Zerum
- Rola bojowa
- Koszt użycia mocy
- Ryzyka biologiczne
- Synergie
- Antysynergie

### Interakcja z Bramami

### Status w bastionach (tabela czteropolowa)

Nie zmieniaj kanonu. Uzupełnij brakujące pola w stylu technicznym.
Zwróć listę braków systemowych.

---

## TASK 3 — NORMALIZACJA TERMINOLOGII

Zakres: całe repozytorium.

Wykonaj:
1. Ujednolić nazwy ewolucji.
2. Ujednolić nazwy form.
3. Ujednolić nazwy ról społecznych.
4. Ujednolić zapis kosztów i mocy.

Zidentyfikuj konflikty terminologiczne.
Zwróć tabelę przed/po.

---

## TASK 4 — STANDARD MINIMUM (PLIKI 03 I 04)

Zakres: wszystkie pliki 03 i 04.

Każdy plik musi zawierać minimum 6–10 punktów obejmujących:
- Pochodzenie
- Migracje
- Model rodziny
- Tabu
- Konflikt wewnętrzny
- Relacje międzykastowe
- Hierarchia
- Stosunek do Zerum
- Stosunek do Bram

Uzupełnij braki w stylu technicznym.
Bez metafor. Bez patosu.
Zwróć raport braków.

---

## TASK 5 — ODPOETYZOWANIE

Zakres: wszystkie warstwy techniczne.

Wykonaj:
1. Usuń hiperbole.
2. Usuń figury retoryczne.
3. Zamień opis emocjonalny na funkcjonalny.
4. Skróć zdania.
5. Usuń zdania bez wartości systemowej.

Zwróć listę największych transformacji.

---

## TASK 6 — QC GLOBALNE

Utwórz tabelę porównawczą wszystkich ras zawierającą:
- Natura Zerum
- Rola bojowa
- Koszt mocy
- Słabość
- Ryzyko biologiczne
- Interakcja z Bramami

Wskaż:
- Niespójności
- Braki
- Przewagi bez kosztu
- Powtórzenia

Zaproponuj korekty balansowe (bez zmiany kanonu).

