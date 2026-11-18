var dragonTemplate = <item:taxdl:dragon_upgrade_1_smithing_table>;
var dragonMaterial = <item:taxdl:dragon_scale>;

smithing.remove(<item:taxdl:dragon_skin_armor_helmet>);
smithing.remove(<item:taxdl:dragon_skin_armor_chestplate>);
smithing.remove(<item:taxdl:dragon_skin_armor_leggings>);
smithing.remove(<item:taxdl:dragon_skin_armor_boots>);
smithing.remove(<item:taxdl:dragon_skin_axe>);
smithing.remove(<item:taxdl:dragon_skin_pickaxe>);
smithing.remove(<item:taxdl:dragon_skin_sword>);

smithing.addTransformRecipe("dragon_skin_armor_helmet", <item:taxdl:dragon_skin_armor_helmet>, dragonTemplate, <item:minecraft:netherite_helmet>, dragonMaterial);
smithing.addTransformRecipe("dragon_skin_armor_chestplate", <item:taxdl:dragon_skin_armor_chestplate>, dragonTemplate, <item:minecraft:netherite_chestplate>, dragonMaterial);
smithing.addTransformRecipe("dragon_skin_armor_leggings", <item:taxdl:dragon_skin_armor_leggings>, dragonTemplate, <item:minecraft:netherite_leggings>, dragonMaterial);
smithing.addTransformRecipe("dragon_skin_armor_boots", <item:taxdl:dragon_skin_armor_boots>, dragonTemplate, <item:minecraft:netherite_boots>, dragonMaterial);
smithing.addTransformRecipe("dragon_skin_armor_axe", <item:taxdl:dragon_skin_axe>, dragonTemplate, <item:minecraft:netherite_axe>, dragonMaterial);
smithing.addTransformRecipe("dragon_skin_armor_pickaxe", <item:taxdl:dragon_skin_pickaxe>, dragonTemplate, <item:minecraft:netherite_pickaxe>, dragonMaterial);
smithing.addTransformRecipe("dragon_skin_armor_sword", <item:taxdl:dragon_skin_sword>, dragonTemplate, <item:minecraft:netherite_sword>, dragonMaterial);