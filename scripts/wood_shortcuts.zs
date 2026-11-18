import crafttweaker.api.tag.manager.ITagManager;
# Adding echo_logs from deepr_and_darker to tak logs
if(<tagmanager:items>.exists("deeperdarker:echo_logs")) {
    val logsTag = <tag:items:minecraft:logs>;
    val echoLogsTag = <tag:items:deeperdarker:echo_logs>;
    logsTag.add(echoLogsTag);
}

# 8 logs to 4 chests
craftingTable.addShaped("logs_to_chests", <item:minecraft:chest> * 4, [
    [<tag:items:minecraft:logs>, <tag:items:minecraft:logs>, <tag:items:minecraft:logs>],
    [<tag:items:minecraft:logs>, <item:minecraft:air>, <tag:items:minecraft:logs>],
    [<tag:items:minecraft:logs>, <tag:items:minecraft:logs>, <tag:items:minecraft:logs>]
]);

# 2 logs to 16 sticks
craftingTable.addShaped("logs_to_sticks", <item:minecraft:stick> * 16, [
    [<tag:items:minecraft:logs>],
    [<tag:items:minecraft:logs>]
]);