# TODO: Translation updated at 2022-03-01 21:22

# game/BKscreens.rpy:8190
translate chinese packstates_menu_da3bbd8f:

    # "Oftentimes, a Girlpack creator may wish to change some of the picture names to better fit Brothel King's tagging system. The packstate feature helps updating girlpacks without having to download hundreds of pictures all over again."
    "通常，Girlpack的创作者可能希望更改一些图片名称，以更好地适应Brothel King的标签系统。packstate功能有助于更新girlpack，而无需重新下载数百张图片。"

# game/BKscreens.rpy:8191
translate chinese packstates_menu_83fb1d69:

    # "" "{b}Packstates{/b} contain all the necessary information to keep the tags of a Girlpack up to date. These files need to be put into the {color=[c_magenta]}/game/[packdir]{/color} directory and named exactly like the girlpack they are for."
    "" "{b}Packstates{/b}包含所有必要的信息，以使Girlpack的标签保持最新。这些文件需要放在{color=[c_magenta]}/game/[packdir]{/color}目录中，并与它们的girlpack名称完全相同。"

# game/BKscreens.rpy:8192
translate chinese packstates_menu_35c34b3e:

    # "" "During the renaming process, a {b}log file{/b} is created in the BrothelKing main directory\n({color=[c_magenta]}packstate_log.txt{/color}), showing in detail everything that was changed."
    "" "在重命名的过程中， {b}日志文件{/b}会被生成在游戏的根目录下\n({color=[c_magenta]}packstate_log.txt{/color})并显示所有被改变的任何细节。"

# game/BKscreens.rpy:8193
translate chinese packstates_menu_88f8438c:

    # "" "You can also do a {b}simulation{/b}. This creates the same log file, but without actually renaming any files. This lets you check which changes would be made, without any risk."
    "" "你也可以进行一个{b}模拟{/b}。这将创建相同的日志文件，但不实际重命名任何文件。这使您可以检查将进行哪些更改，而不会有任何风险。"

# game/BKscreens.rpy:8194
translate chinese packstates_menu_9b65325a:

    # "" "No files are actually deleted. Instead, unwanted files are tagged as {b}_TRASH{/b}. These files will not get used by BrothelKing, so you can safely just leave them there, or delete them for real. You may notice the duplicate tag on some _TRASH files - these are duplicates of existing images."
    "" "没有文件会真的被删除。相反，不需要的文件被标记为{b}_TRASH{/b}。这些文件不会被Brotherking使用，所以您可以安全地将它们留在那里，或者删除它们。您可能会注意到一些重复标签在_TRASH文件上，这些是已存在图片的复制品。"

# game/BKscreens.rpy:8195
translate chinese packstates_menu_f158589e:

    # "" "If you have added your own images, they will get tagged as {b}_UNRECOGNIZED{/b} by default. They will still get used by BrothelKing."
    "" "如果你也添加了一些自己的图片，他们会被默认标记为{b}_UNRECOGNIZED{/b}。他们也依然会被用在BrothelKing中。"

# game/BKscreens.rpy:8196
translate chinese packstates_menu_4afe306a:

    # "Please note that {b}duplicates{/b} only get detected for recognized images. You can change this behavior in the {b}packstates menu{/b} (Ignore will not even rename them, Hide will prevent them from showing in the game)."
    "请注意，只有识别的图片才会检测到{b}复制品{/b}。您可以在{b}packstates menu{/b}中更改此行为（“忽略”甚至不会重命名它们，“隐藏”将阻止它们在游戏中显示）。"

# game/BKscreens.rpy:8197
translate chinese packstates_menu_53287101:

    # "" "That's all! Why not try a {b}simulation{/b} and see if the {color=[c_magenta]}/packstate_log.txt{/color} shows any useful changes?"
    "" "这就是所有内容了。为什么不试一次{b}模拟{/b}，并观察是否{color=[c_magenta]}/packstate_log.txt{/color}会显示一些有用的改变呢？"

translate chinese strings:

    # game/BKscreens.rpy:4566
    old "Ok"
    new "Ok"

    # game/BKscreens.rpy:7528
    old "Content settings"
    new "内容设置"

    # game/BKscreens.rpy:7569
    old "Picture settings"
    new "图片设置"

    # game/BKscreens.rpy:7613
    old "UI settings"
    new "UI设置"

    # game/BKscreens.rpy:7673
    old "Misc"
    new "杂项"

    # game/BKscreens.rpy:7803
    old "Girl pack mix"
    new "人物包组合"

    # game/BKscreens.rpy:7803
    old "Update packstates"
    new "更新包状态"

    # game/BKscreens.rpy:7806
    old "Would you like to see girl ratings (this may take some time if you have many girl packs)?"
    new "你喜欢看女孩评分吗(如果你有很多人物包，这可能需要一些时间)？"

    # game/BKscreens.rpy:8186
    old "Welcome to the packstate feature (courtesy of {color=[c_magenta]}{b}Chris12{/b}{/color})"
    new "欢迎使用包装状态特性(该功能由{color=[c_magenta]}{b}Chris12{/b}{/color}提供)"

    # game/BKscreens.rpy:8186
    old "Introduction to Packstates"
    new "包状态简介"

    # game/BKscreens.rpy:8186
    old "Unrecognized Images: [preferences.packstate_unrecognized]"
    new "未识别的图片:[preferences.packstate_unrecognized]"

    # game/BKscreens.rpy:8186
    old "Simulation"
    new "模拟"

    # game/BKscreens.rpy:8186
    old "Apply packstate"
    new "应用包状态"

    # game/BKscreens.rpy:8201
    old "Hide: Rename and don't show unrecognized images.\nRename: Rename unrecognized images, but show them.\nIgnore: Don't rename unrecognized images. Will also show them.\n Removes any _UNRECOGNIZED tags again.\n(Renaming means adding _UNRECOGNIZED as tag to the filename)"
    new "隐藏:重命名，不显示无法识别的图像。\n 重命名:重命名无法识别的图像，但显示它们。\n 忽略:不要重命名无法识别的图像。也会展示给他们看。\n 再次删除任何未识别的标记。\n (重命名意味着在文件名中添加_UNRECOGNIZED as标签)"

    # game/BKscreens.rpy:8201
    old "Hide"
    new "隐藏"

    # game/BKscreens.rpy:8201
    old "Rename"
    new "重命名"

    # game/BKscreens.rpy:8201
    old "Ignore"
    new "忽略"

    # game/BKscreens.rpy:8201
    old "Back (don't change setting)"
    new "返回(不改变设置)"

    # game/BKscreens.rpy:8221
    old "It is recommended that you backup your girls folder and run a simulation beforehand. There is no Undo operation!{fast}{nw}"
    new "建议你先备份您的人物文件夹并试运行模拟。无法撤销操作！{fast}{nw}"
