// Remove the default sandpaper polishing recipe for polished rose quartz
<recipetype:create:sandpaper_polishing>.remove(<item:create:polished_rose_quartz>);

// Add a custom sandpaper polishing recipe yielding 4 polished rose quartz
<recipetype:create:sandpaper_polishing>.addJsonRecipe("polished_rose_quartz_x4", {
    "type": "create:sandpaper_polishing",
    "ingredients": [
        {
            "item": "create:rose_quartz"
        }
    ],
    "results": [
        {
            "item": "create:polished_rose_quartz",
            "count": 4
        }
    ]
});