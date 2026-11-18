<recipetype:create:crushing>.addJsonRecipe("sandstone_to_four_sand", {
    "ingredients": [
        {
            "item": "minecraft:sandstone"
        }
    ],
    "processingTime": 150,
    "results": [
        {
            "count": 4,
            "item": "minecraft:sand"
        }
    ]
});
<recipetype:create:crushing>.addJsonRecipe("red_sandstone_to_four_sand", {
    "ingredients": [
        {
            "item": "minecraft:red_sandstone"
        }
    ],
    "processingTime": 150,
    "results": [
        {
            "count": 4,
            "item": "minecraft:red_sand"
        }
    ]
});

craftingTable.remove(<item:tfmg:brass_pipe>);
craftingTable.addShaped("brass_pipe", <item:tfmg:brass_pipe>*4, [
    [<item:create:brass_sheet>,<item:create:brass_ingot>,<item:create:brass_sheet>]
]);