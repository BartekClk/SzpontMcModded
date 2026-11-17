// Dopisanie brakujących pni z Deeper and Darker oraz wszystkich okorowanych logów do głównego tagu
<tag:items:minecraft:logs>.add(<tag:items:deeperdarker:echo_logs>);
<tag:items:minecraft:logs>.add(<tag:items:forge:stripped_logs>);
<tag:items:minecraft:logs>.add(<tag:items:create:modded_stripped_logs>);

// 2 dowolne logi pionowo -> 16 patyków (działa też w siatce 2x2 w ekwipunku)
craftingTable.addShaped("logs_to_sticks", <item:minecraft:stick> * 16, [
    [<tag:items:minecraft:logs>],
    [<tag:items:minecraft:logs>]
]);

// 8 dowolnych logów dookoła -> 4 skrzynki
craftingTable.addShaped("logs_to_chests", <item:minecraft:chest> * 4, [
    [<tag:items:minecraft:logs>, <tag:items:minecraft:logs>, <tag:items:minecraft:logs>],
    [<tag:items:minecraft:logs>, <item:minecraft:air>, <tag:items:minecraft:logs>],
    [<tag:items:minecraft:logs>, <tag:items:minecraft:logs>, <tag:items:minecraft:logs>]
]);