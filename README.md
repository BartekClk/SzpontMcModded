# ⚙️ SZPONT MC: Modded [1.20.1 Forge]

> Zorientowana na inżynierię, przemysł ciężki, logistykę kolejową i wojnę artyleryjską paczka modów dla serwera **SZPONT MC**.

![Minecraft Version](https://img.shields.io/badge/Minecraft-1.20.1-brightgreen?style=flat-square)
![Modloader](https://img.shields.io/badge/Modloader-Forge%2047.3.0-orange?style=flat-square)
![Managed with](https://img.shields.io/badge/Managed%20with-Packwiz-blue?style=flat-square)
![Voice Chat](https://img.shields.io/badge/Voice%20Chat-Proximity%20UDP-blueviolet?style=flat-square)

---

<!-- MODS_START -->
<!-- MODS_END -->

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