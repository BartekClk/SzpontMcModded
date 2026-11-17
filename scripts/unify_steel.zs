import crafttweaker.api.recipe.replacement.Replacer;

// Wyrównanie tagów sztabki z Create Big Cannons do standardu TFMG
<tag:items:forge:ingots>.add(<item:createbigcannons:steel_ingot>);
<tag:items:create:create_ingots>.add(<item:createbigcannons:steel_ingot>);
<tag:items:minecraft:beacon_payment_items>.add(<item:createbigcannons:steel_ingot>);

// Zamiana sztywnych odwołań w recepturach crafting table na wspólny tag
Replacer.forTypes(craftingTable)
    .replacing(<item:createbigcannons:steel_ingot>, <tag:items:forge:ingots/steel>)
    .replacing(<item:tfmg:steel_ingot>, <tag:items:forge:ingots/steel>)
    .execute();