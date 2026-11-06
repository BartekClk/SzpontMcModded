# ⚙️ SZPONT MC: Modded [1.20.1 Forge]

> Zorientowana na inżynierię, przemysł ciężki, logistykę kolejową i wojnę artyleryjską paczka modów dla serwera **SZPONT MC**.

![Minecraft Version](https://img.shields.io/badge/Minecraft-1.20.1-brightgreen?style=flat-square)
![Modloader](https://img.shields.io/badge/Modloader-Forge%2047.3.0-orange?style=flat-square)
![Managed with](https://img.shields.io/badge/Managed%20with-Packwiz-blue?style=flat-square)
![Voice Chat](https://img.shields.io/badge/Voice%20Chat-Proximity%20UDP-blueviolet?style=flat-square)

---

## 🛠️ Filary Rozgrywki

* 🚂 **Kolej Transkontynentalna i Ruchoma Mechanika:** Rozbudowana sieć połączeń kolejowych (*Create: Steam 'n' Rails*), automatyczne składy transportowe, semafory, fabryki andezytu oraz mechaniczne żurawie i wiertnice.
* 🛢️ **Przemysł Naftowy i Energetyka:** Wydobycie ropy naftowej kiwonami (*Pumpjack*), rektyfikacja frakcyjna na olej napędowy i benzynę (*Diesel Generators*) oraz generowanie prądu FE (*Create Crafts & Additions*).
* 💥 **Ciężka Artyleria i Wojna Oblężnicza:** Odlewanie żeliwnych luf w formach piaskowych, obróbka skrawaniem na tokarkach i budowa dział dalekosiężnych (*Create Big Cannons*).
* 📦 **Zintegrowany Magazyn:** Automatyczna segregacja w kompresujących szufladach (*Storage Drawers*) spięta z centralnym terminalem bezprzewodowym (*Tom's Simple Storage*).
* 📜 **Rozwój Postaci i Misje:** Dedykowana kampania technologiczna prowadząca przez ukryte mechaniki (*FTB Quests*) połączona z atrybutami RPG (*Just Leveling*).
* 🌍 **Organiczny Świat i Realistyczna Akustyka:** Monumentalne łańcuchy górskie (*Tectonic*), przestrzenna fizyka dźwięku i pogłos w halach (*Sound Physics Remastered*) oraz płynne animacje mobów (*Fresh Animations*).

---

## ⌨️ Niezbędnik Klawiszologii

| Skrót | Mod / Funkcja | Do czego służy? |
|---|---|---|
| **`[W]`** *(Przytrzymaj)* | **Create Ponder** | Otwiera animowany podgląd 3D maszyny z instrukcją podłączenia napędu. |
| **`[K]`** | **Just Leveling** | Drzewko atrybutów postaci (Mining, Strength, Building itp.). |
| **`[V]`** | **Simple Voice Chat** | Ustawienia mikrofonu, głośności graczy i kanałów radiowych. |
| **`[M]`** | **FTB Chunks** | Mapa świata, claimowanie działki (LPM) i chunkloading maszyn (Shift+LPM). |
| **`[B]`** | **Traveler's Backpack** | Otwieranie założonego w slot Curios plecaka bez zdejmowania go na ziemię. |

---

## 💻 Wymagania Sprzętowe

* **Pamięć RAM:** Przypisz od **4 GB do 6 GB RAM** w ustawieniach launchera (nie zaleca się przydzielania więcej niż 8 GB, aby uniknąć mikroprzycięć Garbage Collectora).
* **Środowisko:** Java 17 (x64).
* **Silnik graficzny:** W paczkę wbudowany jest *Embeddium* – **nie instaluj OptiFine**, gdyż wywoła on błąd kompatybilności z modelami *Create*.

---

## 🔧 Zarządzanie Paczką (Dla Deweloperów)

Paczka korzysta z metadanych **Packwiz**. Modyfikacje `.jar` nie są śledzone bezpośrednio w repozytorium.

```bash
# Aktualizacja indeksu po edycji plików
packwiz refresh

# Eksport gotowej paczki dla graczy
packwiz mr export

# Dodanie nowego modu
packwiz mr add <slug>