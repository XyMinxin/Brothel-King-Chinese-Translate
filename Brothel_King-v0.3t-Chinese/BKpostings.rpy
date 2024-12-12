#### BK QUESTS AND CLASSES ####
## Labels are used instead of Functions to make sure we are using global variables

label init_postings():
    python:
        # QUESTS #

        quest_templates = [
                        Quest("quest", name = _('Model needed'), main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = __("I'm an artist, an artist I tell thee! I need a muse. Clothing unnecessary."), sound = s_sigh),
                        Quest("quest", name = _('Private dance'), main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = __("Looking for a private, intimate dance...."), sound = s_sigh),
                        Quest("quest", name = _('Entertain my guests'), main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = __("My guests are arriving soon, and nothing is ready! This is a disaster! I need your help!"), sound = s_sigh),
                        Quest("quest", name = _('Escort needed'), main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = __("I have an important guild meeting, and I need to show them I'm not just anyone. Looking for an elite companion to impress those snobs."), sound = s_sigh),
                        Quest("quest", name = _('Make me feel young again'), main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'sex', description = __("It's been many a moon since lil' willy's gone to sleep. I need a girl to help me remember what it was like in the old days..."), sound = s_aaha),
                        Quest("quest", name = _('Setting a record'), main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'anal', description = __("I aim to break the record set by Long Dick Silver, and this will take long hours of practice... Help me get harder and stronger so that I can succeed!"), sound = s_aaha),
                        Quest("quest", name = _('Girlfriend needed'), main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'service', description = __("I feel lonely... Will you help me forget my troubles?"), sound = s_aaha),
                        Quest("quest", name = _('Hiring help'), main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = __("I need an extra maid to help out in the mansion. There is a very specific uniform..."), sound = s_aaha),
                        Quest("quest", name = _('Please teach my son'), main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'service', description = __("My son is already 21, and not yet married. He's a big oaf when it comes to women... Can you help him come out of his shell?"), sound = s_mmmh),
                        Quest("quest", name = _('Bored in Zan'), main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'sex', description = __("I'm stranded here, drinking ale all day at the local inn. I'm bored out of my mind. Please send me some 'entertainment'."), sound = s_mmmh),
                        Quest("quest", name = _('Back door man'), main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'anal', description = __("The men don't know, but the little girls understand..."), sound = s_mmmh),
                        Quest("quest", name = _('Night at the dungeon'), main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'fetish', description = __("Looking for partners to help us test our new contraption. C'mon! It will be fun!"), sound = s_mmmh),
                        Quest("quest", name = _('Private party'), main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'group', description = __("Hosting a large delegation at my house. We need girls to entertain our guests in every way possible..."), sound = s_aah),
                        Quest("quest", name = _('Ladies night'), main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'group', description = __("We are holding our traditional 'ladies night' at our local guild hall. Looking for a girl to play with a friend in front of the audience..."), sound = s_aah),
                        ]

        # CLASSES #

        class_templates = [
                            Quest("class", name = _('Modeling'), main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = __("Learn the secrets to looking fabulous and have perfect hair at all times! Who wants to look natural anyway?"), sound = s_sigh),
                            Quest("class", name = _('Dancing'), main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = __("Zomba! Bodyfighting! Aqua reggeaton!\nHurry before we make up even more silly names!"), sound = s_sigh),
                            Quest("class", name = _('Waitress'), main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = __("Learn the basics of working tables... You'll never spill a glass on a customer's crotch again, unless you want to!"), sound = s_sigh),
                            Quest("class", name = _('Geisha'), main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = __("Master all Zanic traditional arts, including the exact science of tea ceremony trigonometry. Don't look like an ass because your tea cup is off 5 degrees to the left!"), sound = s_sigh),
                            Quest("class", name = _('Massage'), main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = __("Spend a relaxing few days at the spa with us. It will be awesome! As for the teaching... Wait, what teaching?"), sound = s_aaha),
                            Quest("class", name = _('Swimming'), main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = __("The sun shining on exposed bodies... Water running along voluptuous curves... Tanning oil on glistening skin... And swimming, of course. Erm."), sound = s_aaha),
                            Quest("class", name = _('Singing'), main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = __("'Sing properly dammit, or I'll rip off your head and shove manure down your neck!'. How bad can a singing class be? Oh, you'll see..."), sound = s_aaha),
                            Quest("class", name = _('Maid'), main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = __("'If you want to clean up properly, you have to bend forward a lot more! More... More... Hmm, that's better.'"), sound = s_aaha),
                            Quest("class", name = _('XXX{#1}'), main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = __("Learn to pleasure a man... Or a woman, if you're so inclined. Why not learn both?{#1}"), sound = s_aah),
                            Quest("class", name = _('XXX'), main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = __("Learn to pleasure a man... Or a woman, if you're so inclined. Why not learn both?"), sound = s_aah),
                            Quest("class", name = _('Hardcore{#1}'), main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = __("We've got more tools than a hardware store, more beasts than the palace zoo... And by the time we're finished, they're all gonna fit inside of her!{#1}"), sound = s_scream),
                            Quest("class", name = _('Hardcore'), main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = __("We've got more tools than a hardware store, more beasts than the palace zoo... And by the time we're finished, they're all gonna fit inside of her!"), sound = s_scream),
                            ]

    return

#### END OF BK POSTINGS FILE ####
