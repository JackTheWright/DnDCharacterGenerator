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
