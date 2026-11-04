import os
import shutil

BASE_DIR = os.path.join("config", "ftbquests", "quests")
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

if os.path.exists(CHAPTERS_DIR):
    shutil.rmtree(CHAPTERS_DIR)
os.makedirs(CHAPTERS_DIR, exist_ok=True)

id_counter = 2000

def next_id():
    global id_counter
    id_counter += 1
    return f"{id_counter:016X}"

def make_quest(title, subtitle, desc, x, y, tasks, xp_reward=100, rewards=None, deps=None, shape="rsquare", size=1.0):
    """
    tasks: lista słowników, np.:
      [{"type": "checkmark", "title": "Rozumiem!"}]
      [{"type": "item", "item": "create:wrench", "count": 1}]
    rewards: lista krotek (item_id, count)
    """
    q_id = next_id()
    deps_str = ", ".join([f'"{d}"' for d in (deps or [])])
    desc_str = ",\n\t\t\t\t".join([f'"{line}"' for line in desc])

    # Budowanie zadań
    tasks_snbt = []
    for t in tasks:
        t_id = next_id()
        if t.get("type") == "checkmark":
            tasks_snbt.append(f"""				{{
					id: "{t_id}"
					title: "{t.get('title', 'Zrozumiałem!')}"
					type: "checkmark"
				}}""")
        else:
            cnt = t.get("count", 1)
            tasks_snbt.append(f"""				{{
					count: {cnt}L
					id: "{t_id}"
					item: "{t['item']}"
					type: "item"
				}}""")
    tasks_block = "\n".join(tasks_snbt)

    # Budowanie nagród
    rewards_snbt = []
    if xp_reward > 0:
        r_xp_id = next_id()
        rewards_snbt.append(f"""				{{
					id: "{r_xp_id}"
					type: "xp"
					xp: {xp_reward}
				}}""")
    for r_item, r_cnt in (rewards or []):
        r_id = next_id()
        rewards_snbt.append(f"""				{{
					count: {r_cnt}
					id: "{r_id}"
					item: "{r_item}"
					type: "item"
				}}""")
    rewards_block = "\n".join(rewards_snbt)

    snbt = f"""		{{
			dependencies: [{deps_str}]
			description: [
				{desc_str}
			]
			id: "{q_id}"
			rewards: [
{rewards_block}
			]
			shape: "{shape}"
			size: {size:.1f}d
			subtitle: "{subtitle}"
			tasks: [
{tasks_block}
			]
			title: "{title}"
			x: {x:.1f}d
			y: {y:.1f}d
		}}"""
    return q_id, snbt

def write_chapter(filename, title, icon, order_index, quests_snbt_list):
    c_id = next_id()
    quests_joined = "\n".join(quests_snbt_list)
    content = f"""{{
	default_hide_dependency_lines: false
	default_quest_shape: ""
	filename: "{filename}"
	group: ""
	icon: "{icon}"
	id: "{c_id}"
	order_index: {order_index}
	quest_links: [ ]
	quests: [
{quests_joined}
	]
	title: "{title}"
}}
"""
    with open(os.path.join(CHAPTERS_DIR, f"{filename}.snbt"), "w", encoding="utf-8") as f:
        f.write(content)

# ==============================================================================
# ROZDZIAŁ 0: PODRĘCZNIK INŻYNIERA (ZASADY, RPG, DZIAŁKI)
# ==============================================================================
ch0 = []
q_start, s = make_quest(
    "&6Witaj na serwerze!", "Przeczytaj zanim zaczniesz",
    [
        "&eTen przewodnik przeprowadzi Cię od pierwszego kilofa aż po rafinerie naftowe, sieć kolejową i ciężką artylerię.",
        "",
        "&c&lWAŻNE ZASADY MECHANIK:&r",
        "1. Zadania z ikoną &a[Ptaszka]&r to krótkie instrukcje. Kliknij na nie, aby odebrać darmowy EXP i odblokować dalszą gałąź.",
        "2. Zadania wieloblokowe wymagają od razu kompletu części, abyś nie został z połową niedziałającej maszyny."
    ],
    0, 0, [{"type": "checkmark", "title": "Zaczynamy!"}], 50, [("minecraft:bread", 16)], shape="pentagon", size=1.5
); ch0.append(s)

q_ponder, s = make_quest(
    "&bNajważniejszy klawisz: [W]", "System animacji Ponder",
    [
        "Mod &6Create&r nie ma skomplikowanych okienek GUI. Wszystko dzieje się fizycznie w świecie gry.",
        "",
        "&a&lJAK ZROZUMIEĆ DOWOLNĄ MASZYNĘ?&r",
        "Najedź kursorem na dowolny blok z Create w ekwipunku lub w wyszukiwarce &eJEI&r po prawej stronie i &6&lPRZYTRZYMAJ KLAWISZ [W]&r.",
        "",
        "Otworzy się interaktywna animacja 3D, którą możesz obracać i pauzować. Pokazuje ona dokładnie, z której strony podpiąć napęd!"
    ],
    -2, -2, [{"type": "checkmark", "title": "Wiem jak używać [W]"}], 100, deps=[q_start], shape="circle"
); ch0.append(s)

q_jl, s = make_quest(
    "&cCzemu nie mogę użyć kilofa?!", "Mod: Just Leveling [Klawisz K]",
    [
        "Na serwerze działa system rozwoju postaci &6Just Leveling&r.",
        "",
        "&e&lJAK TO DZIAŁA:&r",
        "1. Naciśnij klawisz &6[K]&r (lub sprawdź przypisanie w ustawieniach sterowania).",
        "2. Za zdobywane poziomy doświadczenia (XP) podnosisz swoje statystyki: &aMining&r, &aAttack&r, &aDefense&r, &aBuilding&r.",
        "3. Lepsze narzędzia (żelazne, diamentowe) oraz zbroje wymagają odpowiedniego poziomu danej cechy!",
        "",
        "&7Wskazówka: Wykonywanie tych zadań daje mnóstwo XP na start!"
    ],
    0, -2, [{"type": "checkmark", "title": "Otworzyłem menu [K]"}], 200, deps=[q_start], shape="circle"
); ch0.append(s)

q_chunks, s = make_quest(
    "&aOchrona Bazy i Chunkloading", "FTB Chunks & FTB Teams",
    [
        "Na serwerze są armaty i pociągi – zabezpiecz swój teren!",
        "",
        "&e&lINSTRUKCJA KROK PO KROKU:&r",
        "1. Otwórz ekwipunek &6[E]&r i kliknij ikonę &bTrzech Ludzików&r w lewym górnym rogu, aby stworzyć drużynę (&aFTB Teams&r) ze znajomymi.",
        "2. Kliknij ikonę &aMapy&r obok (lub naciśnij &6[M]&r i wybierz ikonę siatki chunków w lewym górnym rogu).",
        "3. &6Lewy Przycisk Myszy (LPM)&r zajmuje teren (chroni przed creeperami i graczami).",
        "4. &bShift + LPM&r włącza &lChunkloading&r – maszyny i pociągi na tym kwadracie będą pracować nawet, gdy wyjdziesz z bazy!"
    ],
    2, -2, [{"type": "checkmark", "title": "Zająłem swój teren"}], 100, deps=[q_start], shape="circle"
); ch0.append(s)

q_voice, s = make_quest(
    "&dCzat Głosowy i Radio", "Simple Voice Chat [Klawisz V]",
    [
        "Naciśnij klawisz &6[V]&r, aby otworzyć menu czatu głosowego.",
        "Możesz tam skonfigurować mikrofon, głośność poszczególnych graczy oraz tworzyć grupy radiowe dla konduktorów pociągów."
    ],
    2, 0, [{"type": "checkmark", "title": "Skonfigurowano mikrofon"}], 50, deps=[q_start], shape="circle"
); ch0.append(s)

q_bp, s = make_quest(
    "Plecak Inżyniera", "Slot Curios API",
    [
        "Stwórz swój pierwszy &6Traveler's Backpack&r.",
        "",
        "&a&lPRO-TIP:&r Nie musisz stawiać plecaka na ziemi ani blokować nim slotu na napierśnik!",
        "Kliknij okrągłą ikonkę w lewym górnym rogu swojej postaci w ekwipunku (&eCurios API&r) i włóż plecak w dedykowany slot &6Back&r. Otworzysz go skrótem &6[B]&r."
    ],
    0, 2, [{"type": "item", "item": "travelersbackpack:standard", "count": 1}], 150, [("minecraft:leather", 8)], deps=[q_start]
); ch0.append(s)

q_art, s = make_quest(
    "Poszukiwacz Reliktów", "Struktury i Artifacts",
    [
        "Świat generowany przez &6Tectonic&r kryje struktury z &6Create: Structures&r oraz podziemne obozowiska Mimików.",
        "Zdobyte tam przedmioty z moda &dArtifacts&r zakłada się w dodatkowe sloty biżuterii (Curios)."
    ],
    -2, 0, [{"type": "item", "item": "minecraft:compass", "count": 1}], 100, [("minecraft:golden_apple", 2)], deps=[q_start]
); ch0.append(s)

write_chapter("00_podrecznik", "0. Podręcznik i Zasady", "minecraft:writable_book", 0, ch0)

# ==============================================================================
# ROZDZIAŁ 1: LOGISTYKA I CENTRALNY MAGAZYN
# ==============================================================================
ch1 = []
q_drawers, s = make_quest(
    "Ściana Szuflad", "Storage Drawers",
    [
        "Zwykłe skrzynie szybko się zapchają. Szuflady przechowują dziesiątki stacków jednego przedmiotu.",
        "",
        "&e&lOBSŁUGA:&r",
        "• &aKliknięcie PPM:&r wkłada przedmiot (2x PPM wkłada wszystkie pasujące z ekwipunku!).",
        "• &aKliknięcie LPM:&r wyjmuje 1 sztukę (&6Shift + LPM&r wyjmuje cały stack)."
    ],
    0, 0, [{"type": "item", "item": "storagedrawers:oak_full_drawers_1", "count": 4}], 100, [("storagedrawers:oak_full_drawers_2", 8)]
); ch1.append(s)

q_compacting, s = make_quest(
    "&6Magiczna Szuflada Kompresująca", "Koniec z ręcznym robieniem bloków!",
    [
        "&bCompacting Drawers&r to jeden z najważniejszych bloków w grze.",
        "",
        "&e&lJAK TO DZIAŁA:&r",
        "Wrzuć do niej np. &6Sztabki Żelaza&r. Szuflada automatycznie i bez żadnego prądu udostępni Ci w trzech okienkach jednocześnie: &aBloki Żelaza&r, &aSztabki Żelaza&r oraz &aBryłki Żelaza (Nuggets)&r!",
        "Niezastąpione przy automatycznych pralniach żwiru z Create."
    ],
    0, -2, [{"type": "item", "item": "storagedrawers:compacting_drawers_3", "count": 2}], 200, [("storagedrawers:obsidian_storage_upgrade", 4)], deps=[q_drawers]
); ch1.append(s)

q_keys, s = make_quest(
    "Klucz i Ulepszenia Pojemności", "Blokowanie slotów",
    [
        "&6Drawer Key&r pozwala zablokować szufladę na konkretny przedmiot – nawet gdy wyjmiesz z niej ostatnią sztukę, automaty nie wrzucą tam śmieci.",
        "&6Void Upgrade&r niszczy nadmiar surowców po zapełnieniu szuflady (chroni fabryki przed zatkaniem i lagowaniem serwera!)."
    ],
    0, 2, [
        {"type": "item", "item": "storagedrawers:drawer_key", "count": 1},
        {"type": "item", "item": "storagedrawers:void_upgrade", "count": 2},
        {"type": "item", "item": "storagedrawers:iron_storage_upgrade", "count": 4}
    ], 150, [("storagedrawers:gold_storage_upgrade", 4)], deps=[q_drawers]
); ch1.append(s)

q_dctrl, s = make_quest(
    "Serce Szuflad: Kontroler", "Drawer Controller",
    [
        "Postaw &6Drawer Controller&r tak, aby stykał się ze ścianą Twoich szuflad.",
        "Wszystkie szuflady połączone ze sobą (do 12 bloków odległości) będą teraz widoczne przez ten jeden blok!"
    ],
    2, 0, [{"type": "item", "item": "storagedrawers:controller", "count": 1}], 200, [("storagedrawers:oak_trim", 16)], deps=[q_drawers]
); ch1.append(s)

q_toms_guide, s = make_quest(
    "&eJak działa Tom's Simple Storage?", "Przeczytaj przed budową terminala!",
    [
        "Wielu graczy myli dwa podstawowe bloki w tym modzie:",
        "",
        "1. &6Inventory Connector&r – stawia się go &aBEZPOŚREDNIO&r obok skrzynek lub obok &eDrawer Controllera&r. On skanuje przylegające magazyny.",
        "2. &6Crafting Terminal&r – to ekran z wyszukiwarką i stołem rzemieślniczym. Musisz postawić go bezpośrednio na &6Inventory Connectorze&r!",
        "",
        "&7Jeśli chcesz wyciągnąć ekran do innego pokoju, użyj Inventory Cable + Inventory Cable Connector."
    ],
    4, 0, [{"type": "checkmark", "title": "Rozumiem różnicę!"}], 50, deps=[q_dctrl], shape="circle"
); ch1.append(s)

q_toms_term, s = make_quest(
    "Centralny Terminal z Wyszukiwarką", "Zestaw startowy Tom's Storage",
    [
        "Zbierz komplet części, przyklej &6Inventory Connector&r do swojego &eDrawer Controllera&r, a na nim postaw &6Crafting Terminal&r.",
        "Od teraz masz jeden wspólny magazyn z wyszukiwarką w stylu AE2, połączony z JEI!"
    ],
    6, 0, [
        {"type": "item", "item": "toms_storage:ts.inventory_connector", "count": 1},
        {"type": "item", "item": "toms_storage:ts.crafting_terminal", "count": 1}
    ], 300, [("toms_storage:ts.inventory_cable", 16), ("toms_storage:ts.inventory_cable_connector", 2)], deps=[q_toms_guide]
); ch1.append(s)

q_toms_wifi, s = make_quest(
    "Kieszonkowe Wi-Fi do Magazynu", "Wireless Terminal",
    [
        "Zrób bezprzewodowy terminal i kliknij nim &6Shift + PPM&r na swój stacjonarny Crafting Terminal, aby je sparować.",
        "Możesz teraz zaglądać do swojego magazynu z dowolnego miejsca na terenie bazy!"
    ],
    8, 0, [{"type": "item", "item": "toms_storage:ts.wireless_terminal", "count": 1}], 350, [("minecraft:ender_pearl", 4)], deps=[q_toms_term]
); ch1.append(s)

write_chapter("01_logistyka", "1. Logistyka i Magazyn", "toms_storage:ts.crafting_terminal", 1, ch1)

# ==============================================================================
# ROZDZIAŁ 2: EPOKA ANDEZYTU (PODSTAWY CREATE)
# ==============================================================================
ch2 = []
q_alloy, s = make_quest(
    "Stop Andezytowy", "Fundament Inżynierii",
    [
        "Połącz zwykły Andezyt z bryłkami żelaza (Iron Nugget) lub cynku (Zinc Nugget).",
        "Zdobądź też drewno i kliknij odkorowany pień (Stripped Log) prawym przyciskiem myszy trzymając Andesite Alloy, aby stworzyć &6Andesite Casing&r!"
    ],
    0, 0, [
        {"type": "item", "item": "create:andesite_alloy", "count": 32},
        {"type": "item", "item": "create:andesite_casing", "count": 8}
    ], 150, [("create:andesite_alloy", 32)]
); ch2.append(s)

q_wrench_goggles, s = make_quest(
    "Klucz i Gogle Inżyniera", "Obowiązkowy ekwipunek",
    [
        "• &6Wrench (Klucz):&r Kliknij PPM, aby obrócić maszynę. Kliknij &aShift + PPM&r, aby natychmiast zebrać maszynę lub tory do ekwipunku bez niszczenia ich kilofem!",
        "• &6Goggles:&r Załóż je w slot Curios (Head). Pokazują dokładnie, ile jednostek mocy (&eSU - Stress Units&r) produkuje źródło i ile zjadają maszyny."
    ],
    0, -2, [
        {"type": "item", "item": "create:wrench", "count": 1},
        {"type": "item", "item": "create:goggles", "count": 1}
    ], 150, [("create:shaft", 32)], deps=[q_alloy]
); ch2.append(s)

q_gears_guide, s = make_quest(
    "&eJak zwiększyć prędkość (RPM)?", "Zasada kół zębatych (Przeczytaj!)",
    [
        "Koło wodne kręci się bardzo wolno (8 RPM). Jeśli podłączysz do niego prasę bezpośrednio, będzie pracować ślimaczym tempem!",
        "",
        "&a&lJAK PRZYSPIESZYĆ WAŁ DWUKROTNIE:&r",
        "1. Załóż na wał z koła wodnego &6Duże Koło Zębate (Large Cogwheel)&r.",
        "2. Po przekątnej obok niego postaw &6Małe Koło Zębate (Cogwheel)&r.",
        "3. Wał wychodzący z małego koła kręci się teraz &a2x szybciej&r! (Pamiętaj: wyższa prędkość = maszyny zużywają więcej SU)."
    ],
    2, -2, [{"type": "checkmark", "title": "Rozumiem przekładnie!"}], 100, deps=[q_alloy], shape="circle"
); ch2.append(s)

q_power, s = make_quest(
    "Pierwsza Elektrownia Kinetyczna", "Koła Wodne i Przekładnie",
    [
        "Zbuduj zestaw kół wodnych oraz kół zębatych.",
        "&7Wskazówka: Large Water Wheel daje aż 512 SU. Wystarczy wylać nad nim jedno wiadro wody!"
    ],
    2, 0, [
        {"type": "item", "item": "create:large_water_wheel", "count": 2},
        {"type": "item", "item": "create:cogwheel", "count": 8},
        {"type": "item", "item": "create:large_cogwheel", "count": 8},
        {"type": "item", "item": "create:gearbox", "count": 4}
    ], 200, [("create:shaft", 32)], deps=[q_alloy, q_gears_guide]
); ch2.append(s)

q_windmill, s = make_quest(
    "Potęga Wiatru", "Windmill Bearing",
    [
        "Wiatrak produkuje ogromne ilości SU niezależnie od wody.",
        "&e&lJAK ZBUDOWAĆ WIATRAK:&r",
        "1. Postaw &6Windmill Bearing&r.",
        "2. Przyklej do jego zielonej strony dowolny blok, a do niego przynajmniej &a8 bloków żagli (Windmill Sail)&r.",
        "3. Kliknij pustą ręką PPM na bok łożyska (Windmill Bearing), aby uruchomić strukturę! (Im więcej żagli aż do 128, tym więcej mocy)."
    ],
    2, 2, [
        {"type": "item", "item": "create:windmill_bearing", "count": 1},
        {"type": "item", "item": "create:white_sail", "count": 16}
    ], 250, [("create:white_sail", 16)], deps=[q_power]
); ch2.append(s)

q_press, s = make_quest(
    "Prasa Mechaniczna i Blachy", "Mechanical Press",
    [
        "Postaw &6Mechanical Press&r jedną kratkę nad &6Depotem&r (lub taśmociągiem).",
        "Rzuć na Depot sztabkę żelaza, miedzi lub złota, aby wykuć blachy (Sheets) niezbędne do dalszych maszyn."
    ],
    4, -2, [
        {"type": "item", "item": "create:mechanical_press", "count": 1},
        {"type": "item", "item": "create:depot", "count": 1},
        {"type": "item", "item": "create:iron_sheet", "count": 16}
    ], 200, [("minecraft:iron_ingot", 16)], deps=[q_power]
); ch2.append(s)

q_mixer, s = make_quest(
    "Mikser i Podwojenie Stopu", "Mechanical Mixer + Basin",
    [
        "&c&lUWAGA:&r &6Mechanical Mixer&r wymaga minimalnej prędkości &e30 RPM&r, aby w ogóle zadziałać! Użyj przekładni z kół zębatych (Duże -> Małe).",
        "Postaw go jedną kratkę nad &6Basinem&r (misą) i zasil od boku &aMałym Kołem Zębatym&r.Wrzucając do środka 1 Andezyt + 1 Bryłkę dostaniesz 2x więcej Andesite Alloy!"
    ],
    4, 0, [
        {"type": "item", "item": "create:mechanical_mixer", "count": 1},
        {"type": "item", "item": "create:basin", "count": 1}
    ], 200, [("minecraft:zinc_ingot", 16)], deps=[q_power, q_press]
); ch2.append(s)

q_belts, s = make_quest(
    "Taśmociągi, Lejki i Zsypy", "Logistyka Taśmowa",
    [
        "Przepal wodorosty (Kelp) w piecu na &6Dried Kelp&r, aby stworzyć pasy transmisyjne (&aMechanical Belt&r).",
        "• &6Andesite Funnel:&r wyciąga lub wkłada przedmioty ze skrzyni na taśmociąg.",
        "• &6Chute (Zsyp):&r zrzuca przedmioty pionowo w dół (albo w górę, jeśli pod spodem dmucha wentylator!)."
    ],
    4, 2, [
        {"type": "item", "item": "create:belt_connector", "count": 16},
        {"type": "item", "item": "create:andesite_funnel", "count": 8},
        {"type": "item", "item": "create:chute", "count": 8}
    ], 200, [("minecraft:dried_kelp_block", 16)], deps=[q_power]
); ch2.append(s)

q_fan_guide, s = make_quest(
    "&b4 Żywioły Dmuchawy", "Jak przetwarzać stacki za darmo!",
    [
        "&6Encased Fan&r to darmowy piec i płuczka, która przetwarza całe stacki naraz (na ziemi, na Depocie lub na taśmociągu):",
        "",
        "1. &9Dmuchawa -> Woda:&r Płukanie (&aBulk Washing&r). Zamienia Żwir (Gravel) w bryłki żelaza i krzemień, a Piasek w glinę!",
        "2. &6Dmuchawa -> Ognisko / Ogień:&r Wędzenie (&aBulk Smoking&r). Błyskawicznie piecze jedzenie i wodorosty.",
        "3. &cDmuchawa -> Lawa:&r Hutnictwo (&aBulk Blasting&r). Przepala rudy, bruk i kamień zupełnie &lBEZ WĘGLA&r!",
        "4. &bDmuchawa -> Ognisko Dusz (Soul Fire):&r Nawiedzanie (&aBulk Haunting&r). Zamienia zwykły piasek w Piasek Dusz (Soul Sand), a ten po wypłukaniu wodą daje &eKwarc i Złoto&r!"
    ],
    6, -1, [{"type": "checkmark", "title": "Zrozumiałem 4 tryby dmuchawy!"}], 150, deps=[q_press, q_mixer], shape="circle"
); ch2.append(s)

q_fans, s = make_quest(
    "Przemysłowa Pralnia i Huta", "Encased Fan w praktyce",
    [
        "Zbuduj zestaw 4 wentylatorów oraz młyn ręczny/mechaniczny (&6Millstone&r), który mieli bruk na żwir, a żwir na piasek.",
        "Połącz to z szufladami &eCompacting Drawers&r, aby zbudować pierwszą w pełni automatyczną fabrykę żelaza ze zwykłego bruku!"
    ],
    8, -1, [
        {"type": "item", "item": "create:encased_fan", "count": 4},
        {"type": "item", "item": "create:millstone", "count": 1}
    ], 300, [("minecraft:lava_bucket", 1), ("minecraft:soul_campfire", 2)], deps=[q_fan_guide]
); ch2.append(s)

q_contraptions, s = make_quest(
    "Ruchome Maszyny i Klejenie", "Wiertła, Piły, Kombajny i Super Glue",
    [
        "Maszyny takie jak &6Mechanical Drill&r, &6Mechanical Saw&r oraz &6Mechanical Harvester&r działają zarówno stacjonarnie, jak i na ruchomych konstrukcjach (np. na obracającym się &eMechanical Bearing&r lub wózku kopalnianym).",
        "",
        "&a&lJAK SKLEIĆ FARMY:&r",
        "Weź &6Super Glue&r w dłoń, kliknij PPM na pierwszy narożnik swojej ruchomej ramy i kliknij PPM na drugi narożnik, tworząc zielony zaznaczony obszar. Jeśli przykleisz do konstrukcji zwykłą &eSkrzynię&r lub &ebeczkę&r, wiertła i kombajny będą automatycznie odkładać plony do środka!"
    ],
    8, 1, [
        {"type": "item", "item": "create:mechanical_drill", "count": 3},
        {"type": "item", "item": "create:mechanical_saw", "count": 2},
        {"type": "item", "item": "create:mechanical_harvester", "count": 3},
        {"type": "item", "item": "create:super_glue", "count": 1},
        {"type": "item", "item": "create:portable_storage_interface", "count": 2}
    ], 350, [("create:linear_chassis", 16)], deps=[q_belts, q_mixer]
); ch2.append(s)

write_chapter("02_epoka_andezytu", "2. Epoka Andezytu", "create:wrench", 2, ch2)

# ==============================================================================
# ROZDZIAŁ 3: HYDRAULIKA, MIEDŹ I PRZEMYSŁ ZAKLINANIA
# ==============================================================================
ch3 = []
q_copper, s = make_quest(
    "Hydraulika Miedziana", "Rury, Pompy i Zbiorniki",
    [
        "Wykuj blachy miedziane, aby stworzyć rury (&6Fluid Pipe&r), pompy (&6Mechanical Pump&r) i zbiorniki (&6Fluid Tank&r).",
        "&7Wskazówka: Zbiorniki łączą się w wielkie silosy (do 3x3 w podstawie). Kliknij kluczem (Wrench) na rurę lub zbiornik, aby wstawić w nich okienko podglądu!"
    ],
    0, 0, [
        {"type": "item", "item": "create:fluid_pipe", "count": 16},
        {"type": "item", "item": "create:mechanical_pump", "count": 2},
        {"type": "item", "item": "create:fluid_tank", "count": 8}
    ], 200, [("create:fluid_pipe", 32)]
); ch3.append(s)

q_hose_pulley, s = make_quest(
    "&6Nieskończona Lawa z Netheru!", "Sekret Hose Pulley",
    [
        "&6Hose Pulley&r (Wąż z wyciągarką) opuszcza rurę ssącą w dół po podaniu napędu.",
        "",
        "&c&lUKRYTA MECHANIKA NIESKOŃCZONEGO ŹRÓDŁA:&r",
        "Jeśli opuścisz wąż na sam dół jeziora lawy w Netherze, które liczy &a&lco najmniej 10 000 bloków cieczy&r, mod Create uzna to jezioro za &6NIESKOŃCZONE&r!",
        "Pompa będzie pompować lawę bez wysuszania jeziora. Możesz nią zasilać kotły parowe w bazie na zawsze!"
    ],
    0, -2, [
        {"type": "item", "item": "create:hose_pulley", "count": 1},
        {"type": "item", "item": "create:item_drain", "count": 1},
        {"type": "item", "item": "create:spout", "count": 1}
    ], 300, [("minecraft:bucket", 4)], deps=[q_copper]
); ch3.append(s)

q_blaze, s = make_quest(
    "Wyprawa po Płomyki", "Blaze Burner",
    [
        "Weź pusty koszyk (&6Empty Blaze Burner&r) do Fortecy w Netherze i kliknij nim &aPPM na żywego Płomyka (Blaze)&r (albo na jego Spawner!).",
        "Postawiony pod Basinem i nakarmiony węglem (lub lawą przez słomkę z Crafts & Additions!) pozwala wytapiać Mosiądz."
    ],
    2, 0, [{"type": "item", "item": "create:blaze_burner", "count": 2}], 250, [("minecraft:coal_block", 8)], deps=[q_copper]
); ch3.append(s)

q_deployer, s = make_quest(
    "Mechaniczna Dłoń i Elektronika", "Rose Quartz & Deployer",
    [
        "1. Połącz Kwarc z 8x Redstone na &6Rose Quartz&r i przeszlifuj go papierem ściernym (&aSand Paper&r).",
        "2. Złóż &6Electron Tube&r oraz &6Deployer&r – maszynę, która symuluje klikanie ręką gracza lub uderzanie mieczem!"
    ],
    4, 0, [
        {"type": "item", "item": "create:polished_rose_quartz", "count": 8},
        {"type": "item", "item": "create:electron_tube", "count": 8},
        {"type": "item", "item": "create:deployer", "count": 2}
    ], 300, [("create:electron_tube", 8)], deps=[q_blaze]
); ch3.append(s)

q_ench_guide, s = make_quest(
    "&dJak kopiować Mending i robić Płynny EXP?", "Instrukcja: Enchantment Industry",
    [
        "Mod &6Create: Enchantment Industry&r całkowicie rewolucjonizuje zaklinanie:",
        "",
        "1. &aDisenchanter:&r Stań na nim osobiście (wypije z Ciebie EXP jako zieloną ciecz!) lub rzuć na niego niepotrzebne zaklęte przedmioty z mobów / rzuć Bryłki Doświadczenia (&eNugget of Experience&r). Wyciągnij płynny EXP rurą z boku.",
        "2. &bPrinter (Kopiarka Książek):&r Kliknij na niego od spodu dobrą zaklętą książką (np. Mending), doprowadź od góry rurą &aPłynny EXP&r i przepuszczaj pod nim na Depocie zwykłe czyste książki – skopiuje zaklęcie 1:1!",
        "3. &6Blaze Enchanter + Hyper-Enchanting:&r Nakarm go &eBlaze Cake&r (niebieski ogień!), a zaklnie przedmioty o &l+1 poziom wyżej niż limit Vanilli&r (np. Sharpness VI, Efficiency VI, Fortune IV)!"
    ],
    6, 0, [{"type": "checkmark", "title": "Zrozumiałem przemysł EXP!"}], 150, deps=[q_deployer], shape="circle"
); ch3.append(s)

q_ench_machines, s = make_quest(
    "Fabryka Zaklinania i Drukarnia", "Komplet maszyn EXP",
    [
        "Zbuduj pełny ciąg technologiczny do osuszania doświadczenia, drukowania ksiąg i automatycznego zaklinania z Płomykiem."
    ],
    8, 0, [
        {"type": "item", "item": "create_enchantment_industry:disenchanter", "count": 1},
        {"type": "item", "item": "create_enchantment_industry:printer", "count": 1},
        {"type": "item", "item": "create_enchantment_industry:enchanting_guide", "count": 1}
    ], 400, [("create:experience_nugget", 64), ("minecraft:book", 16)], deps=[q_ench_guide]
); ch3.append(s)

write_chapter("03_hydraulika_i_exp", "3. Hydraulika i Zaklinanie", "create_enchantment_industry:printer", 3, ch3)

# ==============================================================================
# ROZDZIAŁ 4: EPOKA MOSIĄDZU, PARA I KOLEJ TRANSKONTYNENTALNA
# ==============================================================================
ch4 = []
q_brass, s = make_quest(
    "Rewolucja Mosiądzu", "Stop Miedzi i Cynku",
    [
        "Postaw &6Blaze Burner&r pod &6Basinem&r z Mikserem, nakarm Płomyka paliwem i wrzuć do środka Sztabki Miedzi oraz Sztabki Cynku.",
        "Mosiądz odblokowuje inteligentne filtrowanie przedmiotów!"
    ],
    0, 0, [
        {"type": "item", "item": "create:brass_ingot", "count": 32},
        {"type": "item", "item": "create:brass_casing", "count": 8}
    ], 250, [("create:brass_ingot", 16)]
); ch4.append(s)

q_brass_logistics, s = make_quest(
    "Inteligentna Logistyka i Filtry", "Lejki, Tunele i Smart Chute",
    [
        "Maszyny mosiężne mają na ściance specjalną ramkę na filtr:",
        "• Przeciągnij na ramkę kółkiem myszy, aby wybrać dokładną ilość wypuszczanych sztuk (np. dokładnie po 64 na raz).",
        "• Włóż w ramkę przedmiot &6List Filter&r lub &6Attribute Filter&r, aby przepuszczać kilkanaście różnych przedmiotów jednym wyjściem!"
    ],
    0, -2, [
        {"type": "item", "item": "create:brass_funnel", "count": 8},
        {"type": "item", "item": "create:brass_tunnel", "count": 4},
        {"type": "item", "item": "create:smart_chute", "count": 4},
        {"type": "item", "item": "create:filter", "count": 4}
    ], 250, [("create:brass_sheet", 16)], deps=[q_brass]
); ch4.append(s)

q_crafters, s = make_quest(
    "Matryca 21x Mechanical Crafter", "Wielki Automat Rzemieślniczy",
    [
        "Zbuduj ścianę z 21 bloków &6Mechanical Crafter&r.",
        "",
        "&c&lBARDZO WAŻNE PRZY MONTAŻU:&r",
        "Na przodzie każdego Craftera jest mała &eżółta strzałka&r. Użyj klucza (&6Wrench&r), aby skierować strzałki tak, żeby wszystkie zbiegały się po kolei do &aJEDNEGO ostatniego bloku wyjściowego&r! Jeśli strzałki wskazują na siebie nawzajem, maszyna się zatnie."
    ],
    2, -2, [{"type": "item", "item": "create:mechanical_crafter", "count": 21}], 350, [("create:cogwheel", 16)], deps=[q_brass]
); ch4.append(s)

q_crushing, s = make_quest(
    "Koła Kruszące i Mechanizm Precyzyjny", "Crushing Wheels & Precision Mechanism",
    [
        "Wyprodukuj na matrycy Crafterów parę potężnych &6Crushing Wheels&r oraz stwórz linię montażową (Deployery) do &6Precision Mechanism&r.",
        "&7Pamiętaj: Dwa koła kruszące muszą obracać się DO ŚRODKA (przeciwnie do siebie), aby wciągać rudy!"
    ],
    4, -2, [
        {"type": "item", "item": "create:crushing_wheel", "count": 2},
        {"type": "item", "item": "create:precision_mechanism", "count": 8},
        {"type": "item", "item": "create:rotation_speed_controller", "count": 2}
    ], 400, [("minecraft:raw_iron", 64), ("create:raw_zinc", 64)], deps=[q_crafters]
); ch4.append(s)

q_steam_guide, s = make_quest(
    "&eJak działa Kocioł Parowy?", "Zasada 3 Zielonych Słupków",
    [
        "&6Steam Engine&r daje od 16 384 aż do 262 144 SU, ale kocioł wymaga równowagi 3 parametrów (widocznych w goglach po najechaniu na zbiornik):",
        "",
        "1. &bSize (Rozmiar):&r Postaw wieżę z &6Fluid Tank&r (min. 4 bloki zbiornika, np. podstawa 2x2 na 2 bloki w górę = 8 zbiorników).",
        "2. &cHeat (Ciepło):&r Postaw pod dnem zbiornika &6Blaze Burnery&r i nakarm je paliwem (bez ognia kocioł działa tylko w trybie pasywnym 2048 SU).",
        "3. &9Water (Woda):&r Pompuj do kotła wodę za pomocą &6Mechanical Pump&r z szybkością przynajmniej ~180 RPM! Jeśli słupek wody jest niższy niż słupek ciepła, silnik stanie!",
        "",
        "&aNa koniec przyklej Steam Engine na bok zbiornika i postaw na czubku jego ramienia pojedynczy Shaft (wał)!"
    ],
    2, 0, [{"type": "checkmark", "title": "Rozumiem 3 słupki kotła!"}], 150, deps=[q_brass], shape="circle"
); ch4.append(s)

q_steam_engine, s = make_quest(
    "Elektrownia Parowa", "Zestaw pod Kocioł",
    [
        "Zbierz komplet części na swój pierwszy pełnoprawny kocioł parowy z &6Steam Engine&r."
    ],
    4, 0, [
        {"type": "item", "item": "create:steam_engine", "count": 2},
        {"type": "item", "item": "create:fluid_tank", "count": 12},
        {"type": "item", "item": "create:blaze_burner", "count": 4},
        {"type": "item", "item": "create:mechanical_pump", "count": 2}
    ], 400, [("minecraft:lava_bucket", 4)], deps=[q_steam_guide]
); ch4.append(s)

q_train_guide, s = make_quest(
    "&bJak zbudować Pociąg Krok po Kroku?", "Przeczytaj uważnie! (Steam 'n' Rails)",
    [
        "Budowa pociągu ma ścisłą kolejność – pominięcie kroku uniemożliwi start:",
        "",
        "1. Połóż prosty odcinek torów (&6Train Track&r).",
        "2. Weź do ręki &6Train Station&r, kliknij &aLPM na tor&r (pojawi się strzałka kierunku jazdy), a potem postaw blok Stacji obok toru.",
        "3. Otwórz GUI Stacji i kliknij przycisk &b[Create New Train]&r – na torach pojawią się niebieskie podświetlone pola.",
        "4. Kliknij &6Train Casingiem&r (albo gotowym wózkiem Bogey ze Steam 'n' Rails) na niebieskie pole na torze – powstanie wózek z kołami!",
        "5. Zbuduj na wózku kabinę, postaw na niej &6Train Controls&r skierowane zgodnie ze strzałką na torze oraz fotel (&eSeat&r).",
        "6. &c&lNAJWAŻNIEJSZE:&r Sklej cały wagon (razem z wózkiem na torze!) za pomocą &aSuper Glue&r na zielono!",
        "7. Wróć do Stacji, wpisz nazwę pociągu i kliknij &a[Assemble Train]&r!"
    ],
    2, 2, [{"type": "checkmark", "title": "Wiem jak złożyć pociąg!"}], 200, deps=[q_brass], shape="circle"
); ch4.append(s)

q_train_parts, s = make_quest(
    "Zestaw Konstruktora Lokomotywy", "Stacja, Sterowanie i Tory",
    [
        "Wykraftuj na linii montażowej tory, stację kolejową, sterownice oraz gwizdek parowy. W nagrodę otrzymasz duży zapas torów i mostów!"
    ],
    4, 2, [
        {"type": "item", "item": "create:track", "count": 32},
        {"type": "item", "item": "create:track_station", "count": 2},
        {"type": "item", "item": "create: railway_casing", "count": 4} if False else {"type": "item", "item": "create:railway_casing", "count": 4},
        {"type": "item", "item": "create:controls", "count": 2},
        {"type": "item", "item": "create:steam_whistle", "count": 1}
    ], 450, [("create:track", 128), ("mcwbridges:iron_bridge_pier", 32)], deps=[q_train_guide]
); ch4.append(s)

q_train_signals, s = make_quest(
    "Automatyzacja Kolei i Rozkłady", "Semafory i Maszynista",
    [
        "Chcesz, aby pociąg sam woził rudy lub ropę z dalekich kopalń?",
        "• Posadź na fotelu przed sterownicą dowolnego moba (albo &6Blaze Burnera&r!).",
        "• Kliknij na niego wypełnionym rozkładem jazdy (&6Train Schedule&r).",
        "• Pociągi Create potrafią jeździć nawet przez &eniezaładowane chunki&r po całej mapie! Używaj &6Train Signal&r, aby dzielić tory na bloki i unikać zderzeń."
    ],
    6, 2, [
        {"type": "item", "item": "create:schedule", "count": 2},
        {"type": "item", "item": "create:track_signal", "count": 4},
        {"type": "item", "item": "create:portable_storage_interface", "count": 2}
    ], 400, [("create:track", 128)], deps=[q_train_parts]
); ch4.append(s)

write_chapter("04_mosiadz_i_kolej", "4. Mosiądz, Para i Kolej", "create:track_station", 4, ch4)

# ==============================================================================
# ROZDZIAŁ 5: PRZEMYSŁ NAFTOWY I ELEKTRYFIKACJA
# ==============================================================================
ch5 = []
q_oil_guide, s = make_quest(
    "&eJak znaleźć Ropę i postawić Kiwon?", "Instrukcja: Diesel Generators",
    [
        "Kiwon naftowy (&6Pumpjack&r) to konstrukcja wieloblokowa, która wymaga dokładnego ułożenia:",
        "",
        "1. &aSzukanie złoża:&r Chodź po świecie i klikaj PPM trzymając &6Oil Scanner&r. Szukaj chunka, w którym skaner pokaże złoże ropy!",
        "2. &bOdwiert:&r Na tym chunku wykop dziurę do samego &lBedrocka&r i poprowadź od samego dna pionowo w górę rury (&6Fluid Pipe&r). Na górze postaw &6Pumpjack Hole&r.",
        "3. &6Ramie Kiwona:&r Nad dziurą zbuduj słup i zamontuj poziomo belkę na &6Pumpjack Bearing&r (łożysku). Na końcu belki od strony dziury daj &6Pumpjack Head&r, a z tyłu daj &6Pumpjack Crank&r (korbę).",
        "4. &cSklejenie:&r Sklej samą górną ruchomą belkę (od łożyska przez głowicę do miejsca nad korbą) za pomocą &aSuper Glue&r, kliknij na łożysko pustą ręką i podłącz napęd do korby!"
    ],
    0, 0, [{"type": "checkmark", "title": "Zrozumiałem budowę Kiwona!"}], 150, shape="circle"
); ch5.append(s)

q_pumpjack_bom, s = make_quest(
    "Kompletny Zestaw Wiertniczy", "Wszystkie części Pumpjacka",
    [
        "Zbierz od razu wszystkie elementy wymagane do złożenia jednego działającego kiwona naftowego. Użyj podpowiedzi &6[W] Ponder&r na głowicy, aby zobaczyć układ 3D!"
    ],
    2, 0, [
        {"type": "item", "item": "createdieselgenerators:oil_scanner", "count": 1},
        {"type": "item", "item": "createdieselgenerators:pumpjack_head", "count": 1},
        {"type": "item", "item": "createdieselgenerators:pumpjack_crank", "count": 1},
        {"type": "item", "item": "createdieselgenerators:pumpjack_bearing", "count": 2},
        {"type": "item", "item": "createdieselgenerators:pumpjack_hole", "count": 1}
    ], 400, [("create:fluid_pipe", 64)], deps=[q_oil_guide]
); ch5.append(s)

q_distillation, s = make_quest(
    "Wieża Destylacyjna (Rafineria)", "Crude Oil -> Diesel & Benzyna",
    [
        "&e&lJAK ZBUDOWAĆ RAFINERIĘ:&r",
        "1. Postaw pionową wieżę ze zwykłych zbiorników &6Fluid Tank&r (np. wysokość 4 bloki).",
        "2. Pod jej dnem postaw &6Blaze Burner&r i rozpal ogień.",
        "3. Weź do ręki &6Distillation Controller&r i kliknij nim &aPPM na zbiornik&r – zwykły zbiornik zamieni się w kolumnę rektyfikacyjną z okienkami!",
        "4. Wpompuj na sam dół surową Ropę (&8Crude Oil&r) – na wyższych piętrach wieży oddzieli się &6Diesel&r oraz &eGasoline (Benzyna)&r!"
    ],
    4, 0, [
        {"type": "item", "item": "createdieselgenerators:distillation_controller", "count": 6},
        {"type": "item", "item": "create:fluid_tank", "count": 6}
    ], 400, [("create:fluid_tank", 8)], deps=[q_pumpjack_bom]
); ch5.append(s)

q_diesel_engines, s = make_quest(
    "Silniki Spalinowe i Modułowe", "Potężny moment obrotowy",
    [
        "Doprowadź rurą paliwo do &6Diesel Engine&r lub połącz w rząd kilka &6Modular Diesel Engine&r, aby uzyskać ogromną ilość SU na bardzo małej przestrzeni!"
    ],
    6, 0, [
        {"type": "item", "item": "createdieselgenerators:diesel_engine", "count": 1},
        {"type": "item", "item": "createdieselgenerators:modular_diesel_engine", "count": 2},
        {"type": "item", "item": "createdieselgenerators:engine_silencer", "count": 1}
    ], 450, [("createdieselgenerators:canister", 2)], deps=[q_distillation]
); ch5.append(s)

q_wires, s = make_quest(
    "Walcownia Drutu i Kabli", "Create Crafts & Additions",
    [
        "Przepuść blachy miedzi, żelaza i złota przez walcarkę (&6Rolling Mill&r), aby uzyskać druty, a następnie nawiń je na szpule (&6Spool&r)."
    ],
    0, 2, [
        {"type": "item", "item": "createaddition:rolling_mill", "count": 1},
        {"type": "item", "item": "createaddition:copper_spool", "count": 8},
        {"type": "item", "item": "createaddition:connector", "count": 8}
    ], 250, [("createaddition:copper_spool", 16)]
); ch5.append(s)

q_electricity, s = make_quest(
    "Prądnica i Silnik Elektryczny", "Konwersja SU <-> FE (Prąd)",
    [
        "Zamiast ciągnąć długie wały przez całą bazę:",
        "1. Podłącz &6Alternator&r do szybkiego źródła ruchu (np. silnika parowego lub spalinowego) – zamieni on SU na prąd elektryczny (FE).",
        "2. Postaw na maszynach złączki (&6Connector&r) i połącz je przewodem (&6Copper Spool&r).",
        "3. Na drugim końcu bazy postaw &6Electric Motor&r – zamieni on prąd z powrotem na ruch obrotowy o dowolnej prędkości (regulowanej na boku silnika)!"
    ],
    2, 2, [
        {"type": "item", "item": "createaddition:alternator", "count": 2},
        {"type": "item", "item": "createaddition:electric_motor", "count": 2}
    ], 400, [("createaddition:large_connector", 8)], deps=[q_wires]
); ch5.append(s)

q_accumulator, s = make_quest(
    "Bank Energii i Cewka Tesli", "Modular Accumulator & Tesla Coil",
    [
        "&6Modular Accumulator&r działa jak gigantyczna bateria wieloblokowa magazynująca miliony jednostek prądu FE.",
        "&6Tesla Coil&r postawiona nad Depotem pozwala ładować przedmioty prądem lub razić moby piorunami po podaniu sygnału Redstone!"
    ],
    4, 2, [
        {"type": "item", "item": "createaddition:modular_accumulator", "count": 4},
        {"type": "item", "item": "createaddition:tesla_coil", "count": 1}
    ], 450, [("createaddition:capacitor", 8)], deps=[q_electricity]
); ch5.append(s)

write_chapter("05_ropa_i_prad", "5. Ropa i Elektryfikacja", "createdieselgenerators:diesel_engine", 5, ch5)

# ==============================================================================
# ROZDZIAŁ 6: ZBROJENIA (BIG CANNONS) I WOLNY RYNEK
# ==============================================================================
ch6 = []
q_cbc_guide, s = make_quest(
    "&cJak odlać i wywiercić Lufę Armaty?", "Instrukcja: Create Big Cannons",
    [
        "W tym modzie nie wyklikasz dobrej armaty w zwykłym stole rzemieślniczym. Proces wygląda jak w prawdziwej hucie:",
        "",
        "1. &6Topienie metalu:&r Postaw &6Foundry Basin&r z pokrywką (&6Foundry Lid&r) na gorącym Blaze Burnerze, aby wytopić płynne żeliwo (Molten Cast Iron) lub brąz.",
        "2. &eOdlewanie (Casting):&r Postaw na ziemi drewniane ramki &6Casting Sand&r, wciśnij w nie formę rozmiaru lufy (np. &aMedium Cannon Mould&r) i wlej do środka płynny metal przez rurę ze Spoutem. Otrzymasz pełny, niewywiercony odlew (&7Unbored Cannon&r).",
        "3. &bWiercenie lufy (Boring):&r Postaw odlew na tokarce (obracającym się &6Mechanical Bearing&r) i wjedź w jego środek wiertarką lufową (&6Cannon Drill&r) zasilaną wodą przez pompę!",
        "4. &aMontaż:&r Złóż wywiercone segmenty lufy z zamkiem (&6Cannon Breech&r) na łożu (&6Cannon Mount&r) i sklej lufę (lub użyj Cannon Weldera)!"
    ],
    0, 0, [{"type": "checkmark", "title": "Zrozumiałem proces odlewniczy!"}], 200, shape="circle"
); ch6.append(s)

q_foundry, s = make_quest(
    "Odlewnia Artyleryjska", "Foundry Basin & Casting Sand",
    [
        "Zbuduj piec odlewniczy oraz piasek formierski do odlewania pierwszych segmentów dział."
    ],
    2, -1, [
        {"type": "item", "item": "createbigcannons:basin_foundry_lid", "count": 1},
        {"type": "item", "item": "createbigcannons:casting_sand", "count": 8},
        {"type": "item", "item": "createbigcannons:medium_cast_mould", "count": 1}
    ], 350, [("minecraft:iron_block", 8)], deps=[q_cbc_guide]
); ch6.append(s)

q_cannon_drill, s = make_quest(
    "Tokarka Lufowa i Łoże Działa", "Cannon Drill & Cannon Mount",
    [
        "Zbuduj wiertarkę lufową (&6Cannon Drill&r) do rozwiercania pełnych odlewów oraz obrotowe łoże armatnie (&6Cannon Mount&r)."
    ],
    4, -1, [
        {"type": "item", "item": "createbigcannons:cannon_drill", "count": 1},
        {"type": "item", "item": "createbigcannons:cannon_mount", "count": 1},
        {"type": "item", "item": "createbigcannons:yaw_controller", "count": 1}
    ], 450, [("createbigcannons:packed_gunpowder", 32)], deps=[q_foundry]
); ch6.append(s)

q_ammo, s = make_quest(
    "Amunicja i Ładunki Miotające", "Proch, Pociski i Zapalniki",
    [
        "Pamiętaj: Armata ładowana odtylcowo wymaga najpierw włożenia &6 Pocisku (Projectile/Shell)&r, a za nim odpowiedniej ilości &6Ładunków Prochowych (Powder Charge)&r!",
        "Zamknij zamek i podaj sygnał Redstone na &6Cannon Mount&r, aby oddać strzał!"
    ],
    6, -1, [
        {"type": "item", "item": "createbigcannons:powder_charge", "count": 8},
        {"type": "item", "item": "createbigcannons:solid_shot", "count": 8},
        {"type": "item", "item": "createbigcannons:impact_fuze", "count": 4}
    ], 500, [("minecraft:tnt", 16)], deps=[q_cannon_drill]
); ch6.append(s)

q_trading, s = make_quest(
    "Wolny Rynek Serwerowy", "Tom's Trading Network",
    [
        "Masz nadmiar stali, paliwa albo amunicji? Postaw &6Vending Machine&r na głównej stacji kolejowej i handluj automatycznie z innymi graczami na serwerze!"
    ],
    2, 1, [{"type": "item", "item": "toms_trading_network:vending_machine", "count": 1}], 400, [("minecraft:emerald_block", 4)]
); ch6.append(s)

write_chapter("06_zbrojenia_i_handel", "6. Artyleria i Ekonomia", "createbigcannons:cannon_mount", 6, ch6)

print("Wygenerowano pomyślnie rozszerzone drzewko 7 rozdziałów z poradnikami w config/ftbquests/quests/chapters/!")