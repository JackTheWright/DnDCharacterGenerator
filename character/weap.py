class weapons_armor():

    simple_weapons = [
        'club',
        'dagger',
        'greatclub',
        'handaxe',
        'javelin',
        'light hammer',
        'mace',
        'quarterstaff',
        'sickle',
        'spear',
        'light crossbow',
        'dart',
        'shortbow',
        'sling'
    ]

    simple_weapons_dmg = [
        '1d4 b',
        '1d4 p',
        '1d8 b',
        '1d6 s',
        '1d6 p',
        '1d4 b',
        '1d6 b',
        '1d6 b',
        '1d4 s',
        '1d6 p',
        '1d8 p',
        '1d4 p',
        '1d6 p',
        '1d4 b'
    ]

    martial_weapons = [
        'battleaxe',
        'flail',
        'glaive',
        'greataxe',
        'greatsword',
        'halberd',
        'lance',
        'longsword',
        'maul',
        'morningstar',
        'pike',
        'rapier',
        'scimitar',
        'shortsword',
        'trident',
        'war pick',
        'warhammer',
        'whip',
        'blow gun',
        'hand crossbow',
        'heavy crossbow',
        'longbow',
        'net'
    ]

    martial_weapons_dmg = [
        '1d8 s',
        '1d8 b',
        '1d10 s',
        '1d12 s',
        '2d6 s',
        '1d10 s',
        '1d12 p',
        '1d8 s',
        '2d6 b',
        '1d8 p',
        '1d10 s',
        '1d8 p',
        '1d6 s',
        '1d6 s',
        '1d6 p',
        '1d8 p',
        '1d8 b',
        '1d4 s',
        '1 p',
        '1d6 p',
        '1d10 p',
        '1d8 p',
        '0'
    ]


    bard_weapons = simple_weapons + [
        'hand crossbow',
        'longsword',
        'rapier',
        'shortsword'
        ]

    bard_weapons_dmg = simple_weapons_dmg + [
        '1d10 p',
        '1d8 s',
        '1d8 p',
        '1d6 p'
    ]

    druid_weapons = [
        'club',
        'dagger',
        'dart',
        'javelin',
        'mace',
        'quarterstaff',
        'scimitar',
        'sickle',
        'sling',
        'spear'
    ]

    druid_weapons_dmg = [
        '1d4 b',
        '1d4 p',
        '1d4 p',
        '1d6 p',
        '1d6 b',
        '1d6 b',
        '1d6 s',
        '1d4 s',
        '1d4 b',
        '1d6 p'
    ]

    monk_weapons = simple_weapons + [
        'shortswords'
    ]

    monk_weapons_dmg = simple_weapons_dmg + [
        '1d6 p'
    ]

    rogue_weapons = monk_weapons + [
        'crossbow'
    ]

    rogue_weapons_dmg = monk_weapons_dmg + [
        '1d10 p'
    ]

    light_armor = [
        'padded',
        'leather',
        'studded leather'
    ]

    light_armor_ac = [
        '11',
        '11',
        '12'
    ]

    medium_armor = [
        'hide',
        'chain shirt',
        'scale mail',
        'breastplate',
        'half plate'
    ]

    medium_armor_ac = [
        '12',
        '13',
        '14',
        '14',
        '15'
    ]

    heavy_armor = [
        'ring mail',
        'chain mail',
        'splint',
        'plate'
    ]

    heavy_armor_ac = [
        '14',
        '16',
        '17',
        '18'
    ]

    armor_arr = [light_armor, medium_armor, heavy_armor]
    armor_ac_arr = [light_armor_ac, medium_armor_ac, heavy_armor_ac]


class Spells():

    bard_0 = [
        #cantrip
        'Blade Ward',
        'Dancing Lights',
        'Friends',
        'Light',
        'Mage Hand',
        'Mending',
        'Message',
        'Minor Illusion',
        'Prestidigitation',
        'Thunderclap',
        'True Strike',
        'Vicious Mockery'
    ]

    bard_1 = [
        'Animal Friendship',
        'Bane',
        'Charm Person',
        'Comprehend Languages',
        'Cure Wounds',
        'Detect Magic',
        'Disguise Self',
        'Dissonant Whispers',
        'Earth Tremor',
        'Faerie Fire',
        'False Life',
        'Feather Fall',
        'Guiding Hand',
        'Healing Word',
        'Heroism',
        'Identify',
        'Illusory Script',
        'Longstrider',
        'Sense Emotion',
        'Silent Image',
        'Sleep',
        'Speak with Animals',
        'Sudden Awakening',
        'Tasha\'s Hideous Laughter',
        'Thunderwave',
        'Unearthly Chorus',
        'Unseen Servant'
    ]

    bard_2 = [
         'Animal Messenger',
        'Blindness/Deafness'
        'Calm Emotions',
        'Butt of Daggers',
        'Crown of Madness',
        'Detect Thoughts',
        'Enhance Ability',
        'Enthrall',
        'Heat Metal',
        'Hold Person',
        'Invisibility',
        'Knock',
        'Lesser Restoration',
        'Locate Animals or Plants'
        'Locate Object',
        'Magic Mouth',
        'Phantasmal Force',
        'Pyrotechnics',
        'See Invisibility',
        'Shatter',
        'Silence',
        'Skywrite',
        'Suggestion',
        'Warding Wind',
        'Zone of Truth'
    ]

    bard_3 = [
        'Bestow Curse',
        'Clairvoyance',
        'Dispel Magic',
        'Enemies Abound',
        'Fear',
        'Feign Death',
        'Glyph of Warding',
        'Hypnotic Pattern',
        'Leomund\'s Tiny Hut',
        'Major Image',
        'Nondetection',
        'Plant Growth',
        'Sending',
        'Speak with Dead',
        'Speak with Plants',
        'Stinking Butt',
        'Tongues'
    ]

    bard_4 = [
        'Compulsion',
        'Confusion',
        'Dimension Door',
        'Freedom of Movement',
        'Greater Invisibility',
        'Hallucinatory Terrain',
        'Locate Creature',
        'Polymorph'
    ]

    bard_5 = [
        'Animate Objects',
        'Awaken',
        'Dominate Person',
        'Dream',
        'Geas',
        'Greater Restoration',
        'Hold Monster',
        'Legend Lore',
        'Mass Cure Wounds',
        'Mislead',
        'Modify Memory',
        'Planar Binding',
        'Raise Dead',
        'Scrying',
        'Seeming',
        'Teleportation Circle'
    ]

    bard_6 = [
        'Eyebite',
        'Find the Path',
        'Guards and Wards',
        'Mass Suggestion',
        'Otto\'s Irresistible Dance',
        'Programmed Illusion',
        'True Seeing'
    ]

    bard_7 = [
        'Etherealness',
        'Forcecage',
        'Mirage Arcane',
        'Mordenkainen\'s Magnificent Mansion',
        'Mordenkainen\'s Sword',
        'Project Image',
        'Regenerate',
        'Resurrection',
        'Symbol',
        'Teleport'
    ]

    bard_8 = [
        'Dominate Monster',
        'Feeblemind',
        'Glibness',
        'Mind Blank',
        'Power Word: Stun'
    ]

    bard_9 = [
        'Foresight',
        'Power Word: Heal',
        'Power Word: Kill',
        'True Polymorph'
    ]

    cleric_0 = [
        'Guidance',
        'Hand of Radiance',
        'Light',
        'Mending',
        'Resistance',
        'Sacred Flame',
        'Spare the Dying',
        'Thaumaturgy',
        'Toll the Dead',
        'Virtue'
    ]

    cleric_1 = [
        'Bane',
        'Bless',
        'Command',
        'Create or Destroy Water',
        'Cure Wounds',
        'Detect Evil and Good',
        'Detect Magic',
        'Detect Poison and Disease',
        'Divine Favor',
        'Guiding Bolt',
        'Guiding Hand',
        'Healing Word',
        'Inflict Wounds',
        'Protection from Evil and Good',
        'Purify Food and Drink',
        'Sanctuary',
        'Shield of Faith'
    ]

    cleric_2 = [
        'Aid',
        'Augury',
        'Blindness/Deafness',
        'Calm Emotions',
        'Continual Flame',
        'Enhance Ability',
        'Find Traps',
        'Gentle Repose',
        'Hold Person',
        'Lesser Restoration',
        'Locate Object',
        'Prayer of Healing',
        'Protection from Poison',
        'Silence',
        'Spiritual Weapon',
        'Warding Bond',
        'Zone of Truth'
    ]

    cleric_3 = [
        'Animate Dead',
        'Beacon of Hope',
        'Bestow Curse',
        'Clairvoyance',
        'Create Food and Water',
        'Daylight',
        'Dispel Magic',
        'Feign Death',
        'Glyph of Warding',
        'Magic Circle',
        'Mass Healing Word',
        'Meld into Stone',
        'Protection from Energy',
        'Remove Curse',
        'Revivify',
        'Sending',
        'Speak with Dead',
        'Spirit Guardians',
        'Tongues',
        'Water Walk'
    ]


    cleric_4 = [
        'Banishment',
        'Control Water',
        'Death Ward',
        'Divination',
        'Freedom of Movement',
        'Guardian of Faith',
        'Locate Creature',
        'Stone Shape'
    ]

    cleric_5 = [
        'Commune',
        'Contagion',
        'Dispel Evil and Good',
        'Flame Strike',
        'Geas',
        'Greater Restoration',
        'Hallow',
        'Insect Plague',
        'Legend Lore',
        'Mass Cure Wounds',
        'Planar Binding',
        'Raise Dead',
        'Scrying'
    ]

    cleric_6 = [
        'Blade Barrier',
        'Create Undead',
        'Find the Path',
        'Forbiddance',
        'Harm',
        'Heal',
        'Heroes Feast',
        'Planar Ally',
        'True Seeing',
        'Word of Recall'
    ]

    cleric_7 = [
        'Conjure Celestial',
        'Divine Word',
        'Etherealness',
        'Fire Storm',
        'Plane Shift',
        'Regenerate',
        'Resurrection',
        'Symbol'
    ]

    cleric_8 = [
        'Antimagic Field',
        'Control Weather',
        'Earthquake',
        'Holy Aura'
    ]

    cleric_9 = [
        'Astral Projection',
        'Gate',
        'Mass Heal',
        'True Resurrection'
    ]

    druid_0 = [
        'Control Flames',
        'Create Bonfire',
        'Druidcraft',
        'Frostbite',
        'Guidance',
        'Gust',
        'Infestation',
        'Magic Stone',
        'Mending',
        'Mold Earth',
        'Poison Spray',
        'Primal Savagery',
        'Produce Flame',
        'Resistance',
        'Shape Water',
        'Shillelagh',
        'Thorn Whip',
        'Thunderclap'
    ]

    druid_1 = [
        'Absorb Elements',
        'Animal Friendship',
        'Beast Bond',
        'Charm Person',
        'Create or Destroy Water',
        'Cure Wounds',
        'Detect Magic',
        'Detect Poison and Disease',
        'Earth Tremor',
        'Entangle',
        'Faerie Fire',
        'Fog Butt',
        'Goodberry',
        'Guiding Hand',
        'Healing Word',
        'Ice Knife',
        'Jump',
        'Longstrider',
        'Purify Food and Drink',
        'Speak with Animals',
        'Thunderwave',
        'Wild Cunning'
    ]

    druid_2 = [
        'Animal Messenger',
        'Barkskin',
        'Beast Sense',
        'Darkvision',
        'Dust Devil',
        'Earthbind',
        'Enhance Ability',
        'Find Traps',
        'Flame Blade',
        'Flaming Sphere',
        'Gust of Wind',
        'Heat Metal',
        'Hold Person',
        'Lesser Restoration',
        'Locate Animals or Plants',
        'Locate Object',
        'Moonbeam',
        'Pass Without Trace',
        'Protection from Poison',
        'Skywrite',
        'Spike Growth',
        'Warding Wind'
    ]

    druid_3 = [
        'Call Lightning',
        'Conjure Animals',
        'Daylight',
        'Dispel Magic',
        'Erupting Earth',
        'Feign Death',
        'Flame Arrows',
        'Meld into Stone',
        'Plant Growth',
        'Protection from Energy',
        'Sleet Storm',
        'Speak with Plants',
        'Tidal Wave',
        'Wall of Water',
        'Water Breathing',
        'Water Walk',
        'Wind Wall'
    ]

    druid_4 = [
        'Blight',
        'Confusion',
        'Conjure Minor Elementals',
        'Conjure Woodland Beings',
        'Control Water',
        'Dominate Beast',
        'Elemental Bane',
        'Freedom of Movement',
        'Giant Insect',
        'Grasping Vine',
        'Guardian of Nature',
        'Hallucinatory Terrain',
        'Ice Storm',
        'Locate Creature',
        'Polymorph',
        'Stone Shape',
        'Stoneskin',
        'Wall of Fire',
        'Watery Sphere'
    ]

    druid_5 = [
        'Antilife Shell',
        'Awaken',
        'Commune with Nature',
        'Conjure Elemental',
        'Contagion',
        'Control Winds',
        'Geas',
        'Greater Restoration',
        'Insect Plague',
        'Maelstrom',
        'Mass Cure Wounds',
        'Planar Binding',
        'Reincarnate',
        'Scrying',
        'Transmute Rock',
        'Tree Stride',
        'Wall of Stone'
    ]

    druid_6 = [
        'Bones of the Earth',
        'Conjure Fey',
        'Find the Path',
        'Heal',
        'Heroes\'s Feast',
        'Investiture of Flame',
        'Investiture of Ice',
        'Investiture of Stone',
        'Investiture of Wind',
        'Move Earth',
        'Primordial Ward',
        'Sunbeam',
        'Transport via Plants',
        'Wall of Thorns',
        'Wind Walk'
    ]

    druid_7 = [
        'Fire Storm',
        'Mirage Arcane',
        'Plane Shift',
        'Regenerate',
        'Reverse Gravity',
        'Whirlwind'
    ]

    druid_8 = [
        'Animal Shapes',
        'Antipathy/Sympathy',
        'Control Weather',
        'Earthquake',
        'Feeblemind',
        'Sunburst',
        'Tsunami'
    ]

    druid_9 = [
        'Foresight',
        'Shapechange',
        'Storm of Vengeance',
        'True Resurrection'
    ]

    paladin_1 = [
        'Bless',
        'Command',
        'Compelled Duel',
        'Cure Wounds',
        'Detect Evil and Good',
        'Detect Magic',
        'Detect Poison and Disease',
        'Divine Favor',
        'Heroism',
        'Protection from Evil and Good',
        'Purify Food and Drink',
        'Searing Smite',
        'Shield of Faith',
        'Silent Image',
        'Thunderous Smite',
        'Wrathful Smite'
    ]

    paladin_2 = [
        'Aid',
        'Branding Smite',
        'Find Steed',
        'Lesser Restoration',
        'Locate Object',
        'Magic Weapon',
        'Protection from Poison',
        'Zone of Truth'
    ]

    paladin_3 = [
        'Aura of Vitality',
        'Blinding Smite',
        'Create Food and Water',
        'Crusader\'s Mantle',
        'Daylight',
        'Dispel Magic',
        'Elemental Weapon',
        'Magic Circle',
        'Remove Curse',
        'Revivify'
    ]

    paladin_4 = [
        'Aura of Life',
        'Aura of Purity',
        'Banishment',
        'Death Ward',
        'Locate Creature',
        'Staggering Smite'
    ]

    paladin_5 = [
        'Banishing Smite',
        'Circle of Power',
        'Destructive Wave',
        'Dispel Evil and Good',
        'Geas',
        'Raise Dead'
    ]

    ranger_1 = [
        'Absorb Elements',
        'Alarm',
        'Animal Friendship',
        'Beast Bond',
        'Cure Wounds',
        'Detect Magic',
        'Detect Poison and Disease',
        'Ensnaring Strike',
        'Fog Butt',
        'Goodberry',
        'Hail of Thorns',
        'Hunter\'s Mark',
        'Jump',
        'Longstrider',
        'Snare',
        'Speak with Animals',
        'Sudden Awakening',
        'Wild Cunning',
        'Zephyr Strike'
    ]

    ranger_2 = [
        'Animal Messenger',
        'Barkskin',
        'Beast Sense',
        'Cordon of Arrows',
        'Darkvision',
        'Find Traps',
        'Lesser Restoration',
        'Locate Animals or Plants',
        'Locate Object',
        'Pass Without Trace',
        'Protection from Poison',
        'Silence',
        'Spike Growth'
    ]

    ranger_2 = [
        'Conjure Animals',
        'Conjure Barrage',
        'Daylight',
        'Flame Arrows',
        'Lightning Arrow',
        'Nondetection',
        'Plant Growth',
        'Protection from Energy',
        'Speak with Plants',
        'Water Breathing',
        'Water Walk',
        'Wind Wall'
    ]

    ranger_4 = [
        'Conjure Woodland Beings',
        'Freedom of Movement',
        'Grasping Vine',
        'Guardian of Nature',
        'Locate Creature',
        'Stoneskin'
    ]

    ranger_5 = [
        'Commune with Nature',
        'Conjure Volley',
        'Swift Quiver',
        'Tree Stride'
    ]

    sorcerer_0 = [
        'Acid Splash',
        'Blade Ward',
        'Booming Blade',
        'Chill Touch',
        'Control Flames',
        'Create Bonfire',
        'Dancing Lights',
        'Fire Bolt',
        'Friends',
        'Frostbite',
        'Green Flame Blade',
        'Gust',
        'Infestation',
        'Light',
        'Lightning Lure',
        'Mage Hand',
        'Mending',
        'Message',
        'Minor Illusion',
        'Mold Earth',
        'Poison Spray',
        'Prestidigitation',
        'Ray of Frost',
        'Shape Water',
        'Shocking Grasp',
        'Sword Burst',
        'Thunderclap',
        'True Strike'
    ]

    sorcerer_1 = [
        'Burning Hands',
        'Catapult',
        'Charm Person',
        'Chaos Bolt',
        'Chromatic Orb',
        'Color Spray',
        'Comprehend Languages',
        'Detect Magic',
        'Disguise Self',
        'Earth Tremor',
        'Expeditious Retreat',
        'False Life',
        'Feather Fall',
        'Fog Butt',
        'Ice Knife',
        'Jump',
        'Mage Armor',
        'Magic Missile',
        'Ray of Sickness',
        'Shield',
        'Silent Image',
        'Sleep',
        'Sudden Awakening',
        'Thunderwave',
        'Witch Bolt'
    ]

    sorcerer_2 = [
        'Aganazzar\'s Scorcher',
        'Alter Self',
        'Blindness/Deafness',
        'Blur',
        'Butt of Daggers',
        'Crown of Madness',
        'Darkness',
        'Darkvision',
        'Detect Thoughts',
        'Dust Devil',
        'Earthbind',
        'Enhance Ability',
        'Enlarge/Reduce',
        'Gust of Wind',
        'Hold Person',
        'Invisibility',
        'Knock',
        'Levitate',
        'Maximillian\'s Earthen Grasp',
        'Mirror Image',
        'Misty Step',
        'Phantasmal Force',
        'Pyrotechnics',
        'Scorching Ray',
        'See Invisibility',
        'Shatter',
        'Snilloc\s Snowball Storm',
        'Spider Climb',
        'Suggestion',
        'Warding Wind',
        'Web'
    ]

    sorcerer_3 = [
        'Blink',
        'Clairvoyance',
        'Counterspell',
        'Conjure Lesser Demons',
        'Daylight',
        'Dispel Magic',
        'Enemies Abound',
        'Erupting Earth',
        'Fear',
        'Fireball',
        'Flame Arrows',
        'Fly',
        'Gaseous Form',
        'Haste',
        'Hypnotic Pattern',
        'Lightning Bolt',
        'Major Image',
        'Melf\'s Minute Meteors',
        'Protection from Energy',
        'Sleet Storm',
        'Slow',
        'Stinking Butt',
        'Tongues',
        'Wall of Water',
        'Water Breathing',
        'Water Walk'
    ]

    sorcerer_4 = [
        'Banishment',
        'Blight',
        'Confusion',
        'Conjure Barlgura',
        'Conjure Shadow Demon',
        'Dimension Door',
        'Dominate Beast',
        'Greater Invisibility',
        'Ice Storm',
        'Polymorph',
        'Stoneskin',
        'Storm Sphere',
        'Vitriolic Sphere',
        'Wall of Fire',
        'Watery Sphere'
    ]

    sorcerer_5 = [
        'Animate Objects',
        'Buttkill',
        'Cone of Cold',
        'Conjure Vrock',
        'Control Winds',
        'Creation',
        'Dominate Person',
        'Hold Monster',
        'Immolation',
        'Insect Plague',
        'Seeming',
        'Telekinesis',
        'Teleportation Circle',
        'Wall of Stone'
    ]

    sorcerer_6 = [
        'Arcane Gate',
        'Chain Lightning',
        'Circle of Death',
        'Disintegrate',
        'Eyebite',
        'Globe of Invulnerability',
        'Investiture of Flame',
        'Investiture of Ice',
        'Investiture of Stone',
        'Investiture of Wind',
        'Mass Suggestion',
        'Move Earth',
        'Sunbeam',
        'True Seeing'
    ]

    sorcerer_7 = [
        'Conjure Hezrou',
        'Delayed Blast Fireball',
        'Etherealness',
        'Finger of Death',
        'Fire Storm',
        'Plane Shift',
        'Prismatic Spray',
        'Reverse Gravity',
        'Teleport'
    ]

    sorcerer_8 = [
        'Abi-Dalzim\'s Horrid Wilting',
        'Dominate Monster',
        'Earthquake',
        'Incendiary Butt',
        'Power Word: Stun',
        'Sunburst'
    ]

    sorcerer_9 = [
        'Gate',
        'Meteor Swarm',
        'Power Word: Kill',
        'Time Stop',
        'Wish'
    ]

    warlock_0 = [
        'Blade Ward',
        'Booming Blade',
        'Chill Touch',
        'Create Bonfire',
        'Eldritch Blast',
        'Friends',
        'Frostbite',
        'Green Flame Blade',
        'Infestation',
        'Lightning Lure',
        'Mage Hand',
        'Magic Stone',
        'Minor Illusion',
        'Poison Spray',
        'Prestidigitation',
        'Sword Burst',
        'Thunderclap',
        'Toll the Dead',
        'True Strike'
    ]

    warlock_1 = [
        'Armor of Agathys',
        'Arms of Hadar',
        'Cause Fear',
        'Charm Person',
        'Comprehend Languages',
        'Expeditious Retreat',
        'Healing Elixir',
        'Hellish Rebuke',
        'Hex',
        'Illusory Script',
        'Protection from Evil and Good',
        'Puppet',
        'Sense Emotion',
        'Unseen Servant',
        'Witch Bolt'
    ]

    warlock_2 = [
        'Butt of Daggers',
        'Crown of Madness',
        'Darkness',
        'Earthbind',
        'Enthrall',
        'Flock of Familiars',
        'Hold Person',
        'Invisibility',
        'Mirror Image',
        'Misty Step',
        'Ray of Enfeeblement',
        'Shatter',
        'Spider Climb',
        'Suggestion'
    ]

    warlock_3 = [
        'Counterspell',
        'Dispel Magic',
        'Enemies Abound',
        'Fear',
        'Fly',
        'Gaseous Form',
        'Hunger of Hadar',
        'Hypnotic Pattern',
        'Magic Circle',
        'Major Image',
        'Remove Curse',
        'Tongues',
        'Vampiric Touch'
    ]

    warlock_4 = [
        'Banishment',
        'Blight',
        'Dimension Door',
        'Elemental Bane',
        'Galder\'s Speedy Courier',
        'Hallucinatory Terrain'
    ]

    warlock_5 = [
        'Contact Other Plane',
        'Dream',
        'Hold Monster',
        'Scrying'
    ]

    warlock_6 = [
        'Arcane Gate',
        'Circle of Death',
        'Conjure Fey',
        'Create Undead',
        'Eyebite',
        'Flesh to Stone',
        'Investiture of Flame',
        'Investiture of Ice',
        'Investiture of Stone',
        'Investiture of Wind',
        'Mass Suggestion',
        'True Seeing'
    ]

    warlock_7 = [
        'Etherealness',
        'Finger of Death',
        'Forcecage',
        'Plane Shift'
    ]

    warlock_8 = [
        'Demiplane',
        'Dominate Monster',
        'Feeblemind',
        'Glibness',
        'Power Word: Stun'
    ]

    warlock_9 = [
        'Astral Projection',
        'Foresight',
        'Imprisonment',
        'Power Word: Kill',
        'True Polymorph'
    ]

    wizard_0 = [
        'Acid Splash',
        'Blade Ward',
        'Booming Blade',
        'Chill Touch',
        'Control Flames',
        'Create Bonfire',
        'Dancing Lights',
        'Encode Thoughts',
        'Fire Bolt',
        'Friends',
        'Frostbite',
        'Green Flame Blade',
        'Gust',
        'Infestation',
        'Light',
        'Lightning Lure',
        'Mage Hand',
        'Mending',
        'Message',
        'Minor Illusion',
        'Mold Earth',
        'Poison Spray',
        'Prestidigitation',
        'Ray of Frost',
        'Shape Water',
        'Shocking Grasp',
        'Sword Burst',
        'Thunderclap',
        'Toll the Dead',
        'True Strike'
    ]

    wizard_1 = [
        'Absorb Elements',
        'Alarm',
        'Burning Hands',
        'Catapult',
        'Cause Fear',
        'Charm Person',
        'Chromatic Orb',
        'Color Spray',
        'Comprehend Languages',
        'Detect Magic',
        'Disguise Self',
        'Earth Tremor',
        'Expeditious Retreat',
        'False Life',
        'Feather Fall',
        'Find Familiar',
        'Fog Butt',
        'Grease',
        'Ice Knife',
        'Identify',
        'Illusory Script',
        'Jump',
        'Longstrider',
        'Mage Armor',
        'Magic Missile',
        'Protection from Evil and Good',
        'Puppet',
        'Ray of Sickness',
        'Sense Emotion',
        'Shield',
        'Silent Image',
        'Snare',
        'Sleep',
        'Sudden Awakening',
        'Tasha\'s Hideous Laughter',
        'Tenser\'s Floating Disk',
        'Thunderwave',
        'Unseen Servant',
        'Witch Bolt'
    ]

    wizard_2 = [
        'Aganazzar\'s Scorcher',
        'Alter Self',
        'Arcane Lock',
        'Blindness/Deafness',
        'Blur',
        'Butt of Daggers',
        'Continual Flame',
        'Crown of Madness',
        'Darkness',
        'Darkvision',
        'Detect Thoughts',
        'Dust Devil',
        'Earthbind',
        'Enlarge/Reduce',
        'Flaming Sphere',
        'Flock of Familiars',
        'Gentle Repose',
        'Gust of Wind',
        'Hold Person',
        'Invisibility',
        'Knock',
        'Levitate',
        'Locate Object',
        'Magic Mouth',
        'Magic Weapon',
        'Maximillian\'s Earthen Grasp',
        'Melf\'s Acid Arrow',
        'Mirror Image',
        'Misty Step',
        'Nystul\'s Magic Aura',
        'Phantasmal Force',
        'Pyrotechnics',
        'Ray of Enfeeblement',
        'Rope Trick',
        'Scorching Ray',
        'See Invisibility',
        'Shatter',
        'Skywrite',
        'Snilloc\'s Snowball Storm',
        'Spider Climb',
        'Suggestion',
        'Web'
    ]

    wizard_3 = [
        'Animate Dead',
        'Bestow Curse',
        'Blink',
        'Clairvoyance',
        'Conjure Lesser Demons',
        'Counterspell',
        'Dispel Magic',
        'Enemies Abound',
        'Erupting Earth',
        'Fear',
        'Feign Death',
        'Fireball',
        'Flame Arrows',
        'Fly',
        'Galder\'s Tower',
        'Gaseous Form',
        'Glyph of Warding',
        'Haste',
        'Hypnotic Pattern',
        'Leomund\'s Tiny Hut',
        'Lightning Bolt',
        'Magic Circle',
        'Major Image',
        'Melf\'s Minute Meteors',
        'Nondetection',
        'Phantom Steed',
        'Protection from Energy',
        'Remove Curse',
        'Sending',
        'Sleet Storm',
        'Slow',
        'Stinking Butt',
        'Tidal Wave',
        'Tongues',
        'Vampiric Touch',
        'Wall of Sand',
        'Wall of Water',
        'Water Breathing'
    ]

    wizard_4 = [
        'Arcane Eye',
        'Banishment',
        'Blight',
        'Confusion',
        'Conjure Barlgura',
        'Conjure Minor Elementals',
        'Conjure Shadow Demon',
        'Control Water',
        'Dimension Door',
        'Elemental Bane',
        'Evard\'s Black Tentacles',
        'Fabricate',
        'Fire Shield',
        'Galder\'s Speedy Courier',
        'Greater Invisibility',
        'Hallucinatory Terrain',
        'Ice Storm',
        'Leomund\'s Secret Chest',
        'Locate Creature',
        'Mordenkainen\'s Faithful Hound',
        'Mordenkainen\'s Private Sanctum',
        'Otiluke\'s Resilient Sphere',
        'Phantasmal Killer',
        'Polymorph',
        'Stone Shape',
        'Stoneskin',
        'Storm Sphere',
        'Vitriolic Sphere',
        'Wall of Fire',
        'Watery Sphere'
    ]

    wizard_5 = [
        'Animate Objects',
        'Bigby\'s Hand',
        'Buttkill',
        'Cone of Cold',
        'Conjure Elemental',
        'Conjure Vrock',
        'Contact Other Plane',
        'Control Winds',
        'Creation',
        'Dominate Person',
        'Dream',
        'Geas',
        'Hold Monster',
        'Immolation',
        'Legend Lore',
        'Mislead',
        'Modify Memory',
        'Passwall',
        'Planar Binding',
        'Rary\'s Telepathic Bond',
        'Scrying',
        'Seeming',
        'Telekinesis',
        'Teleportation Circle',
        'Transmute Rock',
        'Wall of Force',
        'Wall of Stone'
    ]

    wizard_6 = [
        'Arcane Gate',
        'Chain Lightning',
        'Circle of Death',
        'Contingency',
        'Create Undead',
        'Disintegrate',
        'Drawmij\'s Instant Summons',
        'Eyebite',
        'Flesh to Stone',
        'Globe of Invulnerability',
        'Guards and Wards',
        'Investiture of Flame',
        'Investiture of Ice',
        'Investiture of Stone',
        'Investiture of Wind',
        'Magic Jar',
        'Mass Suggestion',
        'Move Earth',
        'Otiluke\'s Freezing Sphere',
        'Otto\'s Irresistible Dance',
        'Programmed Illusion',
        'Sunbeam',
        'True Seeing',
        'Wall of Ice'
    ]

    wizard_7 = [
        'Conjure Hezrou',
        'Delayed Blast Fireball',
        'Etherealness',
        'Finger of Death',
        'Forcecage',
        'Mirage Arcane',
        'Mordenkainen\'s Magnificent Mansion',
        'Mordenkainen\'s Sword',
        'Plane Shift',
        'Prismatic Spray',
        'Project Image',
        'Reverse Gravity',
        'Sequester',
        'Simulacrum',
        'Symbol',
        'Teleport',
        'Whirlwind'
    ]

    wizard_8 = [
        'Abi-Dalzim\'s Horrid Wilting',
        'Antimagic Field',
        'Antipathy/Sympathy',
        'Clone',
        'Control Weather',
        'Demiplane',
        'Dominate Monster',
        'Feeblemind',
        'Incendiary Butt',
        'Maze',
        'Mind Blank',
        'Power Word: Stun',
        'Sunburst',
        'Telepathy'
    ]

    wizard_9 = [
        'Astral Projection',
        'Foresight',
        'Gate',
        'Imprisonment',
        'Meteor Swarm',
        'Power Word: Kill',
        'Prismatic Wall',
        'Shapechange',
        'Time Stop',
        'True Polymorph',
        'Weird',
        'Wish'
    ]
