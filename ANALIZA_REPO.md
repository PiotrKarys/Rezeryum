# Analiza struktury repozytorium Rezeryum

## Cel pliku
Szybka mapa repozytorium do orientacji: co gdzie leży i jak moduły łączą się logicznie.

## Rdzeń dokumentacji
- `README.md` — opis projektu, zakres i główne moduły.
- `World_Decisions.md` — decyzje kanoniczne i kierunek świata.
- `GLOSSARY_REZERYUM.md` — słownik terminów.
- `rozwiazania.md` i `krytyczne_niespojnosci.md` — robocze materiały spójnościowe/redakcyjne.

## Główne moduły treści
- `System_Mocy/` — mechanika świata (Zerum, progi, więzi, bramy, esencje).
- `Rasy/` — opisy ras według powtarzalnego schematu rozdziałów.
- `Geografia_i_Bastiony/` — biomy, Dzicz, bastiony (z podmodułami miast).
- `Frakcje_i_Zakony/` — struktury wpływu i organizacje.
- `Zagrozenia/` — ryzyka i byty destabilizujące.
- `Historia_Swiata/` — zalążek osi historycznej.

## Wzorzec organizacyjny
- Dominują pliki startowe `00_Index.md` / `00_Overview.md`.
- Kolejne rozdziały mają numerację (`01_`, `02_`, ...), co ułatwia iteracyjne rozbudowywanie.
- Najbardziej rozbudowane gałęzie to `Rasy/` oraz `Geografia_i_Bastiony/`.

## Szybka nawigacja
1. Zacznij od `README.md`.
2. Następnie przeczytaj `World_Decisions.md` i `GLOSSARY_REZERYUM.md`.
3. Dla reguł świata: `System_Mocy/00_Index.md`.
4. Dla sceny polityczno-społecznej: `Rasy/00_index.md` + `Frakcje_i_Zakony/00_Index.md`.
5. Dla mapy świata: `Geografia_i_Bastiony/00_Index.md`.

## Stan
Repozytorium jest dokumentacyjne (markdown-first), gotowe do dalszego worldbuildingu i redakcji kanonu.
