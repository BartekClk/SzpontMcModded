// Wyrównanie brakujących tagów sztabki z Create Big Cannons do standardu TFMG
<tag:items:forge:ingots>.add(<item:createbigcannons:steel_ingot>);
<tag:items:create:create_ingots>.add(<item:createbigcannons:steel_ingot>);
<tag:items:minecraft:beacon_payment_items>.add(<item:createbigcannons:steel_ingot>);

// Bezpośrednia wymiana 1:1 w ekwipunku (gdy maszyna wymaga konkretnego ID przedmiotu)
craftingTable.addShapeless("steel_cbc_to_tfmg", <item:tfmg:steel_ingot>, [<item:createbigcannons:steel_ingot>]);
craftingTable.addShapeless("steel_tfmg_to_cbc", <item:createbigcannons:steel_ingot>, [<item:tfmg:steel_ingot>]);