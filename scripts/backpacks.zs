craftingTable.remove(<item:sophisticatedbackpacks:copper_backpack>);
craftingTable.remove(<item:sophisticatedbackpacks:iron_backpack>);
craftingTable.remove(<item:sophisticatedbackpacks:gold_backpack>);
craftingTable.remove(<item:sophisticatedbackpacks:diamond_backpack>);
craftingTable.remove(<item:sophisticatedbackpacks:netherite_backpack>);

craftingTable.addShaped("harder_copper_backpack", <item:sophisticatedbackpacks:copper_backpack>, [
    [<item:minecraft:copper_block>,<item:minecraft:copper_block>,<item:minecraft:copper_block>],
    [<item:minecraft:copper_block>,<item:sophisticatedbackpacks:backpack>,<item:minecraft:copper_block>],
    [<item:minecraft:copper_block>,<item:minecraft:copper_block>,<item:minecraft:copper_block>],
]);
craftingTable.addShaped("harder_iron_backpack", <item:sophisticatedbackpacks:iron_backpack>, [
    [<item:minecraft:iron_block>,<item:minecraft:iron_block>,<item:minecraft:iron_block>],
    [<item:minecraft:iron_block>,<item:sophisticatedbackpacks:copper_backpack>,<item:minecraft:iron_block>],
    [<item:minecraft:iron_block>,<item:minecraft:iron_block>,<item:minecraft:iron_block>],
]);
craftingTable.addShaped("harder_gold_backpack", <item:sophisticatedbackpacks:gold_backpack>, [
    [<item:minecraft:gold_block>,<item:minecraft:gold_block>,<item:minecraft:gold_block>],
    [<item:minecraft:gold_block>,<item:sophisticatedbackpacks:iron_backpack>,<item:minecraft:gold_block>],
    [<item:minecraft:gold_block>,<item:minecraft:gold_block>,<item:minecraft:gold_block>],
]);
craftingTable.addShaped("harder_diamond_backpack", <item:sophisticatedbackpacks:diamond_backpack>, [
    [<item:minecraft:diamond>,<item:minecraft:diamond_block>,<item:minecraft:diamond>],
    [<item:minecraft:diamond_block>,<item:sophisticatedbackpacks:gold_backpack>,<item:minecraft:diamond_block>],
    [<item:minecraft:diamond>,<item:minecraft:nether_star>,<item:minecraft:diamond>],
]);
craftingTable.addShaped("harder_netherite_backpack", <item:sophisticatedbackpacks:netherite_backpack>, [
    [<item:minecraft:netherite_ingot>,<item:minecraft:netherite_ingot>,<item:minecraft:netherite_ingot>],
    [<item:minecraft:netherite_ingot>,<item:sophisticatedbackpacks:diamond_backpack>,<item:minecraft:netherite_ingot>],
    [<item:minecraft:netherite_ingot>,<item:taxdl:dragon_scale> * 2,<item:minecraft:netherite_ingot>],
]);