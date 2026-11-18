// // Ustaw dokładne ID szablonu i materiału z Tax's Dragon Legend (sprawdź przez /ct hand)
// var dragonTemplate = <item:taxdl:dragon_upgrade_smithing_template>;
// var dragonMaterial = <item:taxdl:dragon_ingot>;

// // 1. Usunięcie domyślnych receptur (z diamentowego ekwipunku) w Smithing Table
// smithing.remove(<item:taxdl:dragon_armor_helmet>);
// smithing.remove(<item:taxdl:dragon_armor_chestplate>);
// smithing.remove(<item:taxdl:dragon_armor_leggings>);
// smithing.remove(<item:taxdl:dragon_armor_boots>);
// smithing.remove(<item:taxdl:dragon_sword>);
// smithing.remove(<item:taxdl:dragon_pickaxe>);
// smithing.remove(<item:taxdl:dragon_axe>);
// smithing.remove(<item:taxdl:dragon_shovel>);
// smithing.remove(<item:taxdl:dragon_hoe>);

// // 2. Dodanie nowych receptur wymagających ekwipunku Netherite
// smithing.addTransformRecipe("dragon_helmet_netherite", <item:taxdl:dragon_armor_helmet>, dragonTemplate, <item:minecraft:netherite_helmet>, dragonMaterial);
// smithing.addTransformRecipe("dragon_chestplate_netherite", <item:taxdl:dragon_armor_chestplate>, dragonTemplate, <item:minecraft:netherite_chestplate>, dragonMaterial);
// smithing.addTransformRecipe("dragon_leggings_netherite", <item:taxdl:dragon_armor_leggings>, dragonTemplate, <item:minecraft:netherite_leggings>, dragonMaterial);
// smithing.addTransformRecipe("dragon_boots_netherite", <item:taxdl:dragon_armor_boots>, dragonTemplate, <item:minecraft:netherite_boots>, dragonMaterial);

// smithing.addTransformRecipe("dragon_sword_netherite", <item:taxdl:dragon_sword>, dragonTemplate, <item:minecraft:netherite_sword>, dragonMaterial);
// smithing.addTransformRecipe("dragon_pickaxe_netherite", <item:taxdl:dragon_pickaxe>, dragonTemplate, <item:minecraft:netherite_pickaxe>, dragonMaterial);
// smithing.addTransformRecipe("dragon_axe_netherite", <item:taxdl:dragon_axe>, dragonTemplate, <item:minecraft:netherite_axe>, dragonMaterial);
// smithing.addTransformRecipe("dragon_shovel_netherite", <item:taxdl:dragon_shovel>, dragonTemplate, <item:minecraft:netherite_shovel>, dragonMaterial);
// smithing.addTransformRecipe("dragon_hoe_netherite", <item:taxdl:dragon_hoe>, dragonTemplate, <item:minecraft:netherite_hoe>, dragonMaterial);