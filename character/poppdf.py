import os
import pdfrw
import random
import math

from . import race_names
from . import skills as s
from . import backgrounds
from . import weap


#CHARSHEET_PATH = 'static/charactersheet.pdf'
#CHARSHEET_OUTPUT_PATH = 'static/newcharactersheet.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def dictfiller(level):
    for key in data_dict.keys():
        data_dict[key] = ''

    races = ['dwarf', 'elf', 'halfling', 'human', 'dragonborn', 'gnome',\
        'halfelf', 'halforc', 'tiefling', 'goliath']
    classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk',\
            'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
    alignment = ['lawful', 'chaotic', 'good', 'good', 'good', 'good',\
            'chaotic', 'chaotic', 'chaotic', 'lawful']
    shield = 0
    percepflag = 0
    ability_score_improvements = 0
    allowed_spells = 0
    class_features = ''
    spell_slots = {'c': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
                    '7':0, '8':0, '9':0}

    STR = 0
    DEX = 0
    CON = 0
    INT = 0
    WIS = 0
    CHA = 0

    names = race_names.names()
    skills = s.skills()
    bg = backgrounds.backgrounds()
    weapons = weap.weapons_armor()

    skill = []
    # Background will be randomized

    # Playername is NPCGenerator
    data_dict['PlayerName'] = 'NPCGenerator'

    # race is randomized from races list
    race_ind = random.randint(0, len(races)-1)
    sex = random.randint(1,2)
    if sex is 1:
        sex_str = 'Male '
    else :
        sex_str = 'Female '
    race = races[race_ind]
    final_str = sex_str + race
    data_dict['Race '] = final_str

    # CharacterName will be randomized, based on race
    if sex is 1:
        if race_ind > 4 and race_ind != 8:
            data_dict['CharacterName'] = names.male_names[3][random.randint(0,39)]
        elif race_ind == 8:
            length = len(names.male_names[5])
            data_dict['CharacterName'] = names.male_names[5][random.randint(1, length-1)]
        else:
            length = len(names.male_names[race_ind])
            data_dict['CharacterName'] = names.male_names[race_ind][random.randint(0, length-1)]
    else:
        if race_ind > 4 and race_ind != 8:
            data_dict['CharacterName'] = names.female_names[3][random.randint(0,15)]
        elif race_ind == 8:
            length = len(names.female_names[5])
            data_dict['CharacterName'] = names.female_names[5][random.randint(1, length-1)]
        else:
            length = len(names.female_names[race_ind])
            data_dict['CharacterName'] = names.female_names[race_ind][random.randint(1, length-1)]

    # Alignment
    data_dict['Alignment'] = alignment[race_ind]

    # XP
    data_dict['XP'] = '0'

    # ProfBonus
    floor = (math.floor(level / 4))
    prof = 2 + floor
    data_dict['ProfBonus'] = str(prof)

    # Speed
    if race is 'dwarf' or race is 'halfling' or race is 'gnome':
        data_dict['Speed'] = '25'
    else:
        data_dict['Speed'] = '30'

    # Class
    class_ind = random.randint(0, len(classes)-1)
    charclass = classes[class_ind]
    data_dict['ClassLevel'] = charclass + ' ' + str(level)

    # Features and Traits
    if charclass is 'barbarian':
        STR, CON = 15, 14
        st1 = 'STR'
        st2 = 'CON'
        data_dict['HPMax'] = str(level * 12 + (2 * level))
        proficiencies = 'Armor: Light, Medium, Shields\nWeapons: Simple,\
        Martial'
        primal_path = 0
        primal_path_str = ''

        # leveling
        if level >= 1:
            class_features = 'Rage\nUnarmored Defence\n'

        if level >= 2:
            class_features += 'Reckless Attack\nDanger Sense\n'

        if level >= 3:
            primal_path = random.randint(0, 1)
            if primal_path == 0:
                primal_path_str = 'Path of the Wild Soul'
                class_features += 'Primal Path:\n -> ' + primal_path_str + '\nLingering Magic\nWild Surge\n'
            else:
                primal_path_str = 'Path of the Berserker'
                class_features = 'Primal Path:\n -> ' + primal_path_str + '\nFrenzy\n'

        if level >= 5:
            class_features += 'Extra Attack\nFast Movement\n'

        if level >= 6:
            if primal_path == 0:
                class_features += 'Magic Reserves\n'
            elif primal_path == 1:
                class_features += 'Mindless Rage\n'

        if level >= 7:
            class_features += 'Feral Instict\n'

        if level >= 9:
            class_features += 'Brutal Critical\n'

        if level >= 10:
            if primal_path == 0:
                class_features += 'Arcane Rebuke\n'
            elif primal_path == 1:
                class_features += 'Intimidating Presence\n'

        if level >= 11:
            class_features += 'Relentless Rage\n'

        if level >= 14:
            if primal_path == 0:
                class_features += 'Arcane Rebuke\n'
            elif primal_path == 1:
                class_features += 'Retaliation\n'

        if level >= 15:
            class_features += 'Persistant Rage\n'

        if level >= 18:
            class_features += 'Indomitable Might\n'

        if level >= 20:
            class_features += 'Primal Champion\n'




        # weapon selection
        wind = random.randint(0, len(weapons.martial_weapons)-1)
        weapon = weapons.martial_weapons[wind]
        dmg = weapons.martial_weapons_dmg[wind]

        #armor selection
        aind = random.randint(0, 1)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_c[acind]

        # shielf flag
        shield = random.randint(0,1)

        skill_rand_1 = random.randint(0, len(skills.barb_skills)-1)
        skill.append(skills.barb_skills[skill_rand_1])
        del skills.barb_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.barb_skills)-1)
        skill.append(skills.barb_skills[skill_rand_2])





    elif charclass is 'bard':
        DEX, CHA = 15, 14
        st1 = 'DEX'
        st2 = 'CHA'
        data_dict['HPMax'] = str(level * 8 + (2 * level))
        proficiencies = 'Armor: Light\n Weapons: Simple, Hand Crossbows, Longswords\nRapiers, Shortswords'
        bard_college = 0
        bard_college_str = ''

        #leveling
        if level >= 1:
            class_features = 'Spellcasting\nBardic Inspiration\n'
            # c = 2, 1 = 2
            spell_slots['c'] = 2
            spell_slots['1'] = 2
            allowed_spells = 4

        if level >= 2:
            # c = 2, 1 = 3
            class_features += 'Jack of All Trades\nSong of Rest\n'
            spell_slots['1'] = 3
            allowed_spells = 5

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            bard_college = random.randint(0, 1)
            if bard_college == 0:
                bard_college_str = 'College of Eloquence'
                class_features += 'Bard College:\n -> ' + bard_college_str + '\nUniversal Speech\nSoothing Words\n'
            else:
                bard_college_str = 'College of Lore'
                class_features += 'Bard College:\n -> ' + bard_college_str + '\nCutting Words\n'
            spell_slots['1'] += 1
            spell_slots['2'] = 2
            allowed_spells = 6

        if level >= 4:
            # c = 3, 1 = 4, 2 = 3
            spell_slots['c'] += 1
            spell_slots['2'] += 1
            allowed_spells = 7

        if level >= 5:
            # c = 3, 1 = 4, 2 = 3, 3 = 2
            allowed_spells = 8
            spell_slots['3'] = 2
            class_features += 'Bardic Inspiration\nFont of Inspiration\n'

        if level >= 6:
            # c = 3, 1 = 4, 2 = 3, 3 = 3
            spell_slots['3'] += 1
            allowed_spells = 9
            if bard_college == 0:
                class_features += 'Undeniable Logic\nCountercharm\n'
            elif bard_college == 1:
                class_features += 'Additional Magic Secrets\nCountercharm\n'

        if level >= 7:
            spell_slots['4'] += 1
            allowed_spells = 10

        if level >= 8:
            spell_slots['4'] += 1
            allowed_spells = 11

        if level >= 9:
            spell_slots['4'] += 1
            spell_slots['5'] = 1
            allowed_spells = 12
            class_features += 'Song of Rest\n'

        if level >= 10:
            spell_slots['c'] += 1
            spell_slots['5'] += 1
            allowed_spells = 14

        if level >= 11:
            spell_slots['6'] = 1
            allowed_spells = 15

        if level >= 12:
            do_nothing = 1

        if level >= 13:
            allowed_spells = 16
            spell_slots['7'] = 1

        if level >= 14:
            allowed_spells = 18
            if primal_path == 0:
                class_features += 'Infectious Inspiration\n'
            elif primal_path == 1:
                class_features += 'Peerless Skill\n'

        if level >= 15:
            allowed_spells = 19
            spell_slots['8'] = 1

        if level >= 16:
            allowed_spells = 19

        if level >= 17:
            allowed_spells = 20
            spell_slots['9'] = 1

        if level >= 18:
            allowed_spells = 22
            spell_slots['5'] += 1

        if level >= 19:
            spell_slots['6'] += 1

        if level >= 20:
            spell_slots['7'] += 1
            class_features += 'Superior Inspiration\n'

        #Weapon selection
        wind = random.randint(0, len(weapons.bard_weapons)-1)
        weapon = weapons.bard_weapons[wind]
        dmg = weapons.bard_weapons_dmg[wind]

        # Armor selection
        acind = random.randint(0, len(weapons.light_armor)-1)
        armor = weapons.light_armor[acind]
        armorclass = weapons.light_armor_ac[acind]


        skill_rand_1 = random.randint(0, len(skills.all_skills)-1)
        skill.append(skills.all_skills[skill_rand_1])
        del skills.all_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.all_skills)-1)
        skill.append(skills.all_skills[skill_rand_2])
        del skills.all_skills[skill_rand_2]
        skill_rand_3 = random.randint(0, len(skills.all_skills)-1)
        skill.append(skills.all_skills[skill_rand_3])

    elif charclass is 'cleric':
        WIS, CHA = 15, 14
        st1 = 'WIS'
        st2 = 'CHA'
        data_dict['HPMax'] = str(level * 8 + (2 * level))
        proficiencies = 'Armor: Light, Medium, Shields\n Weapons: Simple'

        # leveling
        if level >= 1:
            class_features = 'Spellcasting\nDivine Domain: Life\n'
            # c = 2, 1 = 2
            spell_slots['c'] = 2
            spell_slots['1'] = 2
            allowed_spells = 4

        if level >= 2:
            # c = 2, 1 = 3
            class_features += 'Channel Divinity\nDisciple of Life\n'
            spell_slots['1'] = 3
            allowed_spells = 5

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            spell_slots['1'] += 1
            spell_slots['2'] = 2
            allowed_spells = 6

        if level >= 4:
            # c = 3, 1 = 4, 2 = 3
            spell_slots['c'] += 1
            spell_slots['2'] += 1
            allowed_spells = 7

        if level >= 5:
            # c = 3, 1 = 4, 2 = 3, 3 = 2
            allowed_spells = 8
            spell_slots['3'] = 2
            class_features += 'Destroy Undead\n'

        if level >= 6:
            # c = 3, 1 = 4, 2 = 3, 3 = 3
            spell_slots['3'] += 1
            allowed_spells = 9
            class_features += 'Blessed Healer\n'

        if level >= 7:
            spell_slots['4'] += 1
            allowed_spells = 10

        if level >= 8:
            spell_slots['4'] += 1
            allowed_spells = 11
            class_features += 'Divine Strike\n'


        if level >= 9:
            spell_slots['4'] += 1
            spell_slots['5'] = 1
            allowed_spells = 12


        if level >= 10:
            spell_slots['c'] += 1
            spell_slots['5'] += 1
            allowed_spells = 14
            class_features += 'Divine Intervention\n'

        if level >= 11:
            spell_slots['6'] = 1
            allowed_spells = 15

        if level >= 12:
            do_nothing = 1

        if level >= 13:
            allowed_spells = 16
            spell_slots['7'] = 1

        if level >= 14:
            allowed_spells = 18

        if level >= 15:
            allowed_spells = 19
            spell_slots['8'] = 1

        if level >= 16:
            allowed_spells = 19

        if level >= 17:
            allowed_spells = 20
            spell_slots['9'] = 1
            class_features += 'Supreme Healing\n'

        if level >= 18:
            allowed_spells = 22
            spell_slots['5'] += 1

        if level >= 19:
            spell_slots['6'] += 1

        if level >= 20:
            spell_slots['7'] += 1
            class_features += 'Automatic Divine Intervention\n'

        # armor selection
        aind = random.randint(0, 1)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_c[acind]

        # weapon selection
        wind = random.randint(0, len(weapons.simple_weapons)-1)
        weapon = weapons.simple_weapons[wind]
        dmg = weapons.simple_weapons_dmg[wind]

        # shield flag
        shield = random.randint(0,1)


        skill_rand_1 = random.randint(0, len(skills.cleric_skills)-1)
        skill.append(skills.cleric_skills[skill_rand_1])
        del skills.cleric_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.cleric_skills)-1)
        skill.append(skills.cleric_skills[skill_rand_2])

    elif charclass is 'druid':
        INT, WIS = 15, 14
        st1 = 'INT'
        st2 = 'WIS'
        data_dict['HPMax'] = str(level * 8 + (2 * level))
        proficiencies = 'Armor: Light, Medium, Shields\n Weapons: Clubs, daggers, darts,\njavelins, maces, quarterstaffs,\nscimitars, sickles, slings, spears \nTools: Herbalism kit'
        druid_circle = 0
        druid_circle_str = ''


        # leveling
        if level >= 1:
            class_features = 'Spellcasting\nDruidic\n'
            # c = 2, 1 = 2
            spell_slots['c'] = 2
            spell_slots['1'] = 2
            allowed_spells = 4

        if level >= 2:
            # c = 2, 1 = 3
            druid_circle = random.randint(0, 3)
            if druid_circle == 0:
                druid_circle_str = 'Dreams'
                class_features += 'Wild Shape\nDruid Circle:\n -> ' + druid_circle_str + '\nBalm of the Summer Court\n'
                spell_slots['c'] += 1
            elif druid_circle == 1:
                druid_circle_str = 'Moon'
                class_features += 'Combat Wild Shape\nDruid Circle:\n -> ' + druid_circle_str + '\nCircle Forms\n'
            elif druid_circle == 2:
                druid_circle_str = 'Land'
                class_features += 'Wild Shape\nDruid Circle:\n -> ' + druid_circle_str + '\nNatural Recovery\n'
            elif druid_circle == 3:
                druid_circle_str = 'Spores'
                class_features += 'Wild Shape\nDruid Circle:\n -> ' + druid_circle_str + '\nHalo of Spores\nSymbiotic Entity\n'
            spell_slots['1'] = 3
            allowed_spells = 5

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            spell_slots['1'] += 1
            spell_slots['2'] = 2
            allowed_spells = 6

        if level >= 4:
            # c = 3, 1 = 4, 2 = 3
            spell_slots['c'] += 1
            spell_slots['2'] += 1
            allowed_spells = 7

        if level >= 5:
            # c = 3, 1 = 4, 2 = 3, 3 = 2
            allowed_spells = 8
            spell_slots['3'] = 2

        if level >= 6:
            # c = 3, 1 = 4, 2 = 3, 3 = 3
            spell_slots['3'] += 1
            allowed_spells = 9
            if druid_circle == 0:
                class_features += 'Hearth of Moonlight and Shadow\n'
            elif druid_circle == 1:
                class_features += 'Primal Strike\n'
            elif druid_circle == 2:
                class_features += 'Land\'s Stride\n'
            elif druid_circle == 3:
                class_features += 'Fungal Infestation\n'

        if level >= 7:
            spell_slots['4'] += 1
            allowed_spells = 10

        if level >= 8:
            spell_slots['4'] += 1
            allowed_spells = 11

        if level >= 9:
            spell_slots['4'] += 1
            spell_slots['5'] = 1
            allowed_spells = 12


        if level >= 10:
            spell_slots['c'] += 1
            spell_slots['5'] += 1
            allowed_spells = 14
            if druid_circle == 0:
                class_features += 'Hidden Paths\n'
            elif druid_circle == 1:
                class_features += 'Elemental Wild Shape\n'
            elif druid_circle == 2:
                class_features += 'Nature\'s Ward\n'
            elif druid_circle == 3:
                class_features += 'Spreading Spores\n'

        if level >= 11:
            spell_slots['6'] = 1
            allowed_spells = 15

        if level >= 12:
            do_nothing = 1

        if level >= 13:
            allowed_spells = 16
            spell_slots['7'] = 1

        if level >= 14:
            allowed_spells = 18
            if druid_circle == 0:
                class_features += 'Walker in Dreams\n'
            elif druid_circle == 1:
                class_features += 'Thousand Forms\n'
            elif druid_circle == 2:
                class_features += 'Nature\'s Sanctuary\n'
            elif druid_circle == 3:
                class_features += 'Fungal Body\n'

        if level >= 15:
            allowed_spells = 19
            spell_slots['8'] = 1

        if level >= 16:
            allowed_spells = 19

        if level >= 17:
            allowed_spells = 20
            spell_slots['9'] = 1

        if level >= 18:
            allowed_spells = 22
            spell_slots['5'] += 1
            class_features += 'Timeless Body\nBeast Spells\n'


        if level >= 19:
            spell_slots['6'] += 1

        if level >= 20:
            spell_slots['7'] += 1
            class_features += 'Arch Druid\n'


        # weapon selection
        wind = random.randint(0, len(weapons.druid_weapons)-1)
        weapon = weapons.druid_weapons[wind]
        dmg = weapons.druid_weapons_dmg[wind]

        # armor selection
        aind = random.randint(0, 1)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_c[acind]

        # shield flag
        shield = random.randint(0,1)

        skill_rand_1 = random.randint(0, len(skills.druid_skills)-1)
        skill.append(skills.druid_skills[skill_rand_1])
        del skills.druid_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.druid_skills)-1)
        skill.append(skills.druid_skills[skill_rand_2])

    elif charclass is 'fighter':
        STR, CON = 15, 14
        st1 = 'STR'
        st2 = 'CON'
        data_dict['HPMax'] = str(level * 10 + (2 * level))
        proficiencies = 'Armor: All, Shields\n Weapons: all'
        fighter_ma = 0
        fighter_ma_str = ''
        maneuver_str = ''
        fighting_styles = ['Archery', 'Defense', 'Dueling', 'Great Weapon Fighting', 'Protection', 'Two-Weapon Fighting']
        maneuvers = [
        'Commander\'s Strike',
        'Disarming Attack',
        'Distracting Strike',
        'Evasive Footwork',
        'Feinting Attack',
        'Goading Attack',
        'Lunging Attack',
        'Maneuvering Attack',
        'Menacing Attack',
        'Parry',
        'Precision Attack',
        'Pushing Attack',
        'Rally',
        'Riposte',
        'Sweeping Attack',
        'Trip Attack'
        ]


        #levelling
        if level >= 1:
            fighting_style = random.choice(fighting_styles)
            fighting_styles.remove(fighting_style)
            class_features = 'Fighting Style:\n -> ' + fighting_style + '\nSecond Wind\n'
            # c = 2, 1 = 2

        if level >= 2:
            # c = 2, 1 = 3
            fighter_ma = random.randint(0, 2)
            if fighter_ma == 0:
                fighter_ma_str = 'Champion'
                class_features += 'Action Surge\nMartial Archetype:\n -> ' + fighter_ma_str + '\n'
            elif fighter_ma == 1:
                fighter_ma_str = 'Battle Master'
                class_features = 'Action Surge\nMartial Archetype:\n -> ' + fighter_ma_str + '\n'
                m1 = random.choice(maneuvers)
                maneuvers.remove(m1)
                m2 = random.choice(maneuvers)
                maneuvers.remove(m2)
                m3 = random.choice(maneuvers)
                maneuvers.remove(m3)
                maneuver_str += m1 + '\n' + m2 + '\n' + m3 + '\n'
            elif fighter_ma == 2:
                fighter_ma_str = 'Eldritch Knight'
                class_features = 'Action Surge\nMartial Archetype:\n -> ' + fighter_ma_str + '\n'

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            if fighter == 0:
                class_features += 'Improved Critical\n'
            elif fighter_ma == 1:
                class_features += 'Combat Superiority\nStudent of War\n'
            elif fighter_ma == 2:
                class_features += 'Spellcasting\n'
                spell_slots['c'] = 2
                spell_slots['1'] = 2
                allowed_spells = 3

        if level >= 4:
            allowed_spells = 4

        if level >= 5:
            # c = 3, 1 = 4, 2 = 3, 3 = 2
            class_features += 'Extra Attack\n'

        if level >= 7:
            if fighter == 0:
                class_features += 'Remarkable Athlete\n'
            elif fighter_ma == 1:
                class_features += 'Know Your Enemy\n'
                m1 = random.choice(maneuvers)
                maneuvers.remove(m1)
                m2 = random.choice(maneuvers)
                maneuvers.remove(m2)
                m3 = random.choice(maneuvers)
                maneuvers.remove(m3)
                maneuver_str += m1 + '\n' + m2 + '\n' + m3 + '\n'
            elif fighter_ma == 2:
                class_features += 'War Magic\n'
                spell_slots['1'] = 4
                spell_slots['2'] = 2
                allowed_spells = 5

        if level >= 8:
            class_features += 'Indomitable\n'
            allowed_spells = 6


        if level >= 9:
            class_features += 'Indomitable\n'


        if level >= 10:
            if fighter == 0:
                fighting_style = random.choice(fighting_styles)
                class_features += 'Additional Fighting Style:\n -> ' + fighting_style + ' \n'
            elif fighter_ma == 1:
                class_features += 'Improved Combat Superiority\n'
            elif fighter_ma == 2:
                class_features += 'Eldritch Strike\n'
                allowed_spells = 7
                spell_slots['c'] = 3
                spell_slots['2'] = 3

        if level >= 11:
            spell_slots['6'] = 1
            allowed_spells = 8

        if level >= 12:
            do_nothing = 1

        if level >= 13:
            if fighter_ma == 2:
                allowed_spells = 9
                spell_slots['3'] = 2

        if level >= 14:
            allowed_spells = 10

        if level >= 15:
            if fighter == 0:
                class_features += 'Superior Critical\n'
            elif fighter_ma == 1:
                class_features += 'Relentless\n'
                m1 = random.choice(maneuvers)
                maneuvers.remove(m1)
                m2 = random.choice(maneuvers)
                maneuvers.remove(m2)
                m3 = random.choice(maneuvers)
                maneuvers.remove(m3)
                maneuver_str += m1 + '\n' + m2 + '\n' + m3 + '\n'
            elif fighter_ma == 2:
                class_features += 'Arcane Charge\n'

        if level >= 16:
            allowed_spells = 11
            spell_slots['3'] = 3

        if level >= 18:
            if fighter == 0:
                class_features += 'Survivor\n'
            elif fighter_ma == 2:
                class_features += 'Improved War Magic\n'


        if level >= 19:
            spell_slots['4'] = 1
            allowed_spells = 12

        if level >= 20:
            allowed_spells = 13

        if fighter_ma == 1:
            class_features += maneuver_str
        # weapon selection
        wind = random.randint(0, len(weapons.martial_weapons)-1)
        weapon = weapons.martial_weapons[wind]
        dmg = weapons.martial_weapons_dmg[wind]

        #armor selection
        aind = random.randint(0, 2)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_c[acind]

        # shielf flag
        shield = random.randint(0,1)

        skill_rand_1 = random.randint(0, len(skills.fighter_skills)-1)
        skill.append(skills.fighter_skills[skill_rand_1])
        del skills.fighter_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.fighter_skills)-1)
        skill.append(skills.fighter_skills[skill_rand_2])

    elif charclass is 'monk':
        STR, DEX = 15, 14
        st1 = 'STR'
        st2 = 'DEX'
        data_dict['HPMax'] = str(level * 8 + (2 * level))
        proficiencies = 'Weapons: simple, shortswords\nTools: Artisans tool, One Instrument\n'
        disciplines_3 = [
        'Fangs of the Fire Snake',
        'Fist of Four Thunders',
        'Fist of Unbroken Air',
        'Rush of the Gale Spirits',
        'Shape the Flowing River',
        'Sweeping Cinder Strike',
        'Water Whip'
        ]
        disciplines_6 = [
        'Clench of the North Wind',
        'Gong of the Summit'
        ]
        disciplines_11 = [
        'Flames of the Pheonix',
        'Mist Stance',
        'Ride the Wind'
        ]
        disciplines_17 = [
        'Breath of Winter',
        'Eternal Mountain Defense',
        'River of Hungry Flame',
        'Wave of Rolling Earth'
        ]
        mon_trad = 0
        mon_trad_str = ''
        ki_total = 0

        #levelling
        if level >= 1:
            class_features = 'Unarmored Defense\nMartial Arts\n'

        if level >= 2:
            class_features += 'Unarmored Movement\n'
            ki_total = IDKLOL

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            mon_trad = random.randint(0, 5)
            if mon_trad == 0:
                mon_trad_str = 'Drunken Master'
                class_features += 'Monastic Tradition:\n -> ' + mon_trad_str + '\nDrunken Technique\nDeflect Missiles\n'
                #proficiency in performance
            elif mon_trad == 1:
                mon_trad_str = 'Four Elements'
                class_features += 'Monastic Tradition:\n -> ' + mon_trad_str + '\nElemental Attunement\n' + random.choice(disciplines_3) + '\nDeflect Missiles\n'
            elif mon_trad == 2:
                mon_trad_str = 'Kensei'
                class_features += 'Monastic Tradition:\n -> ' + mon_trad_str + '\nPath of the Kensei\nDeflect Missiles\n'
            elif mon_trad == 3:
                mon_trad_str = 'Long Death'
                class_features += 'Monastic Tradition:\n -> ' + mon_trad_str + '\nTouch of Death\nDeflect Missiles\n'
            elif mon_trad == 4:
                mon_trad_str = 'Open Hand'
                class_features += 'Monastic Tradition:\n -> ' + mon_trad_str + '\nOpen Hand Technique\nDeflect Missiles\n'
            elif mon_trad == 5:
                mon_trad_str = 'Shadow'
                class_features += 'Monastic Tradition:\n -> ' + mon_trad_str + '\nShadow Arts\nDeflect Missiles\n'


        if level >= 4:
            # c = 3, 1 = 4, 2 = 3
            class_features += 'Slow Fall\n'

        if level >= 5:
            class_features = 'Extra Attack\nStunning Strike\n'

        if level >= 6:
            if mon_trad == 0:
                class_features += 'Ki-Empowered Strikes\nTipsy Sway\n'
            elif mon_trad == 1:
                class_features += 'Ki-Empowered Strikes\n' + random.choice(disciplines_6) + '\n'
            elif mon_trad == 2:
                class_features += 'Ki-Empowered Strikes\nOne With the Blade\n'
            elif mon_trad == 3:
                class_features += 'Ki-Empowered Strikes\nHour of Reaping\n'
            elif mon_trad == 4:
                class_features += 'Ki-Empowered Strikes\nWholeness of Body\n'
            elif mon_trad == 5:
                class_features += 'Ki-Empowered Strikes\nShadow Step\n'

        if level >= 7:
            class_features += 'Evasion\nStillness of Mind\n'

        if level >= 8:
            spell_slots['4'] += 1
            allowed_spells = 11

        if level >= 10:
            spell_slots['c'] += 1
            spell_slots['5'] += 1
            allowed_spells = 14
            class_features += 'Purity of Body\n'

        if level >= 11:
            if mon_trad == 0:
                class_features += 'Drunkard\'s Luck\n'
            elif mon_trad == 1:
                class_features += random.choice(disciplines_11) + '\n'
            elif mon_trad == 2:
                class_features += 'Sharpen the Blade\n'
            elif mon_trad == 3:
                class_features += 'Mastery of Death\n'
            elif mon_trad == 4:
                class_features += 'Tranquility\n'
            elif mon_trad == 5:
                class_features += 'Cloak of Shadows\n'

        if level >= 12:
            do_nothing = 1

        if level >= 13:
            class_features += 'Tongue of the Sun and Moon\n'

        if level >= 14:
            class_features += 'Diamond Soul\n'

        if level >= 15:
            class_features += 'Timeless Body\n'

        if level >= 16:
            do_nothing = 1

        if level >= 17:
            if mon_trad == 0:
                class_features += 'Intoxicated Frenzy\n'
            elif mon_trad == 1:
                class_features += random.choice(disciplines_17) + '\n'
            elif mon_trad == 2:
                class_features += 'Unerring Accuracy\n'
            elif mon_trad == 3:
                class_features += 'Touch of the Long Death\n'
            elif mon_trad == 4:
                class_features += 'Quivering Palm\n'
            elif mon_trad == 5:
                class_features += 'Opportunist\n'

        if level >= 18:
            class_features += 'Empty Body\n'

        if level >= 19:
            do_nothing = 1

        if level >= 20:
            class_features += 'Perfect Self\n'

        # weapon selection
        wind = random.randint(0, len(weapons.monk_weapons)-1)
        weapon = weapons.monk_weapons[wind]
        dmg = weapons.monk_weapons_dmg[wind]

        armor = 'cloth'
        armorclass = '12'

        skill_rand_1 = random.randint(0, len(skills.monk_skills)-1)
        skill.append(skills.monk_skills[skill_rand_1])
        del skills.monk_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.monk_skills)-1)
        skill.append(skills.monk_skills[skill_rand_2])

    elif charclass is 'paladin':
        WIS, CHA = 15, 14
        st1 = 'WIS'
        st2 = 'CHA'
        data_dict['HPMax'] = str(level * 10 + (2 * level))
        proficiencies = 'Armor: all\n Weapons: simple, martial'
        fighting_styles = ['Defense', 'Dueling', 'Great Weapon Fighting', 'Protection']
        sacred_oath = 0
        sacred_oath_str = ''


        #levelling
        if level >= 1:
            class_features = 'Divine Sense\nLay on Hands\n'

        if level >= 2:
            fighting_style = random.choice(fighting_styles)
            fighting_styles.remove(fighting_style)
            class_features += 'Fighting Style: ' + fighting_style + 'Spellcasting\nDivine Smite\n'
            spell_slots['1'] = 2

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            spell_slots['1'] = 3
            sacred_oath = random.randint(0, 5)
            if sacred_oath == 0:
                sacred_oath_str = 'Ancients'
                class_features += 'Sacred Oath:\n -> ' + sacred_oath_str + '\n' + random.choice(['Nature\'s Wrath', 'Turn the Faithless']) + '\nDivine Health\n'
            elif sacred_oath == 1:
                sacred_oath_str = 'Conquest'
                class_features += 'Sacred Oath:\n -> ' + sacred_oath_str + '\n' + random.choice(['Conquering Presence', 'Guided Strike']) + '\nDivine Health\n'
            elif sacred_oath == 2:
                sacred_oath_str = 'Crown'
                class_features += 'Sacred Oath:\n -> ' + sacred_oath_str + '\n' + random.choice(['Champion Challenge', 'Turn the Tide']) + '\nDivine Health\n'
            elif sacred_oath == 3:
                sacred_oath_str = 'Devotion'
                class_features += 'Sacred Oath:\n -> ' + sacred_oath_str + '\n' + random.choice(['Sacred Weapon', 'Turn the Unholy']) + '\nDivine Health\n'
            elif sacred_oath == 4:
                sacred_oath_str = 'Vengeance'
                class_features += 'Sacred Oath:\n -> ' + sacred_oath_str + '\n' + random.choice(['Abjure Enemy', 'Vow of Enmity']) + '\nDivine Health\n'
            elif sacred_oath == 5:
                sacred_oath_str = 'Oathbreaker'
                class_features += 'Sacred Oath:\n -> ' + sacred_oath_str + '\n' + random.choice(['Control Undead', 'Dreadful Aspect']) + '\nDivine Health\n'


        if level >= 4:
            do_nothing = 1

        if level >= 5:
            class_features += 'Extra Attack\n'
            spell_slots['1'] = 4
            spell_slots['2'] = 2


        if level >= 6:
            class_features += 'Aura of Protection\n'

        if level >= 7:
            spell_slots['2'] = 3
            if sacred_oath == 0:
                class_features += 'Aura of Warding\n'
            elif sacred_oath == 1:
                class_features += 'Aura of Conquest\n'
            elif sacred_oath == 2:
                class_features += 'Divine Allegiance\n'
            elif sacred_oath == 3:
                class_features += 'Aura of Devotion\n'
            elif sacred_oath == 4:
                class_features += 'Relentless Avenger\n'
            elif sacred_oath == 5:
                class_features += 'Aura of Hate\n'

        if level >= 8:
            do_nothing = 1

        if level >= 9:
            spell_slots['3'] = 2

        if level >= 10:
            class_features += 'Aura of Courage\n'

        if level >= 11:
            spell_slots['3'] = 3


        if level >= 12:
            do_nothing = 1

        if level >= 13:
            spell_slots['4'] = 1

        if level >= 14:
            class_features += 'Cleansing Touch\n'

        if level >= 15:
            spell_slots['4'] = 2
            if sacred_oath == 0:
                class_features += 'Undying Sentinel\n'
            elif sacred_oath == 1:
                class_features += 'Scornful Rebuke\n'
            elif sacred_oath == 2:
                class_features += 'Unyielding Saint\n'
            elif sacred_oath == 3:
                class_features += 'Purity of Spirit\n'
            elif sacred_oath == 4:
                class_features += 'Soul of Vengeance\n'
            elif sacred_oath == 5:
                class_features += 'Supernatural Resistance\n'

        if level >= 16:
            do_nothing = 1

        if level >= 17:
            spell_slots['4'] = 3
            spell_slots['5'] = 1


        if level >= 18:
            class_features += 'Empty Body\n'

        if level >= 19:
            spell_slots['5'] = 2

        if level >= 20:
            if sacred_oath == 0:
                class_features += 'Elder Champion\n'
            elif sacred_oath == 1:
                class_features += 'Invincible Conqueror\n'
            elif sacred_oath == 2:
                class_features += 'Exalted Champion\n'
            elif sacred_oath == 3:
                class_features += 'Holy Nimbus\n'
            elif sacred_oath == 4:
                class_features += 'Avenging Angel\n'
            elif sacred_oath == 5:
                class_features += 'Dread Lord\n'

        # weapon selection
        wind = random.randint(0, len(weapons.martial_weapons)-1)
        weapon = weapons.martial_weapons[wind]
        dmg = weapons.martial_weapons_dmg[wind]

        #armor selection
        aind = random.randint(0, 2)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_c[acind]

        # shielf flag
        shield = random.randint(0,1)

        skill_rand_1 = random.randint(0, len(skills.paladin_skills)-1)
        skill.append(skills.paladin_skills[skill_rand_1])
        del skills.paladin_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.paladin_skills)-1)
        skill.append(skills.paladin_skills[skill_rand_2])

    elif charclass is 'ranger':
        STR, DEX = 15, 14
        st1 = 'STR'
        st2 = 'DEX'
        data_dict['HPMax'] = str(level * 10 + (2 * level))
        proficiencies = 'Armor: Light, Medium, Shields\nWeapons: simple, martial'
        fighting_styles = ['Defense', 'Dueling', 'Two-Weapon Fighting', 'Archery']
        ranger_at = 0
        ranger_at_str = ''

        #levelling
        if level >= 1:
            class_features = 'Favored Enemy\nNatural Explorer\n'

        if level >= 2:
            fighting_style = random.choice(fighting_styles)
            fighting_styles.remove(fighting_style)
            class_features += 'Fighting Style: ' + fighting_style + 'Spellcasting\n'
            spell_slots['1'] = 2

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            spell_slots['1'] = 3
            ranger_at = random.randint(0, 1)
            if ranger_at == 0:
                ranger_at_str = 'Hunter'
                class_features += 'Primeval Awareness\nRanger Conclave:\n -> ' + ranger_at_str + '\nRanger\'s Companion\n'
                #proficiency in performance
            elif ranger_at == 1:
                ranger_at_str = 'Beast Master'
                class_features += 'Primeval Awareness\nRanger Conclave:\n -> ' + ranger_at_str + '\n' + random.choice(['Colossus Slayer', 'Giant Killer', 'Horde Breaker']) + '\n'

        if level >= 4:
            do_nothing = 1

        if level >= 5:
            class_features += 'Extra Attack\n'
            spell_slots['1'] = 4
            spell_slots['2'] = 2


        if level >= 6:
            class_features += 'Aura of Protection\n'

        if level >= 7:
            spell_slots['2'] = 3
            if ranger_at == 0:
                class_features += random.choice(['Escape the Horde', 'Multiattack Defense', 'Steel Will']) + '\n'
            elif ranger_at == 1:
                class_features += 'Exceptional Training\n'


        if level >= 8:
            class_features += 'Land\'s Stride\n'

        if level >= 9:

            spell_slots['3'] = 2

        if level >= 10:
            class_features += 'Hide in Plain Sight\n'

        if level >= 11:
            spell_slots['3'] = 3
            if ranger_at == 0:
                class_features += 'Multiattack\n'
            elif ranger_at == 1:
                class_features += 'Bestial Fury\n'


        if level >= 12:
            do_nothing = 1

        if level >= 13:
            spell_slots['4'] = 1

        if level >= 14:
            class_features += 'Vanish\n'

        if level >= 15:
            spell_slots['4'] = 2
            if ranger_at == 0:
                class_features += random.choice(['Evasion', 'Stand Against the Tide', 'Uncanny Dodge']) + '\n'
            elif ranger_at == 1:
                class_features += 'Share Spells\n'

        if level >= 16:
            do_nothing = 1

        if level >= 17:
            spell_slots['4'] = 3
            spell_slots['5'] = 1


        if level >= 18:
            class_features += 'Feral Senses\n'

        if level >= 19:
            spell_slots['5'] = 2

        if level >= 20:
            class_features += 'Foe Slayer'

        # armor selection
        aind = random.randint(0, 1)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_c[acind]

        # weapon selection
        wind = random.randint(0, len(weapons.martial_weapons)-1)
        weapon = weapons.martial_weapons[wind]
        dmg = weapons.martial_weapons_dmg[wind]

        # shield flag
        shield = random.randint(0,1)

        skill_rand_1 = random.randint(0, len(skills.ranger_skills)-1)
        skill.append(skills.ranger_skills[skill_rand_1])
        del skills.ranger_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.ranger_skills)-1)
        skill.append(skills.ranger_skills[skill_rand_2])

    elif charclass is 'rogue':
        DEX, INT = 15, 14
        st1 = 'DEX'
        st2 = 'INT'
        data_dict['HPMax'] = str(level * 8 + (2 * level))
        proficiencies = 'Armor: Light\nWeapons: simple, shortswords, crossbows\n Tools: Thieves tool'
        rogue_at = 0
        rogue_at_str = ''

        #levelling
        if level >= 1:
            class_features = 'Expertise\nSneak Attack\nThieves\' Cant\n'

        if level >= 2:
            class_features += 'Cunning Action\n'

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            allowed_spells = 3
            spell_slots['1'] = 2
            rogue_at = random.randint(0, 2)
            if rogue_at == 0:
                rogue_at_str = 'Thief'
                class_features += 'Roguish Archetype:\n -> ' + rogue_at_str + '\nFast Hands\nSecond-Story Work\n'
            elif rogue_at == 1:
                rogue_at_str = 'Assassin'
                class_features += 'Roguish Archetype:\n -> ' + rogue_at_str + '\n'
                #proficiencies with disguise and poisoners kit
            elif rogue_at == 2:
                rogue_at_str = 'Arcane Trickster'
                class_features += 'Roguish Archetype:\n -> ' + rogue_at_str + '\nSpellcasting\nMage Hand Legerdemain\n'

        if level >= 4:
            allowed_spells = 4
            spell_slots['1'] = 3

        if level >= 5:
            class_features += 'Uncanny Dodge\n'


        if level >= 6:
            class_features += 'Aura of Protection\n'

        if level >= 7:
            allowed_spells = 5
            spell_slots['2'] = 3
            spell_slots['1'] = 4
            class_features += 'Evasion\n'

        if level >= 8:
            allowed_spells = 6
            class_features += 'Land\'s Stride'

        if level >= 9:

            if rogue_at == 0:
                class_features += 'Supreme Sneak\n'
            elif rogue_at == 1:
                class_features += 'Infiltration Expertise\n'
                #proficiencies with disguise and poisoners kit
            elif rogue_at == 2:
                class_features += 'Magical Ambush\n'

        if level >= 10:
            allowed_spells = 7
            spell_slots['2'] = 3
            class_features += 'Hide in Plain Sight\n'

        if level >= 11:
            allowed_spells = 8
            spell_slots['3'] = 3
            class_features += 'Reliable Talent\n'

        if level >= 13:
            allowed_spells = 9
            spell_slots['3'] = 2
            if rogue_at == 0:
                class_features += 'Use Magic Device\n'
            elif rogue_at == 1:
                class_features += 'Impostor\n'
                #proficiencies with disguise and poisoners kit
            elif rogue_at == 2:
                class_features += 'Versatile Trickster\n'

        if level >= 14:
            allowed_spells = 10
            class_features += 'Blindsense\n'

        if level >= 15:
            class_features += 'Slippery Mind\n'

        if level >= 16:
            allowed_spells = 11
            spell_slots['3'] = 3

        if level >= 17:
            if rogue_at == 0:
                class_features += 'Thief\'s Reflexes\n'
            elif rogue_at == 1:
                class_features += 'Death Strike\n'
            elif rogue_at == 2:
                class_features += 'Spell Thief\n'


        if level >= 18:
            class_features += 'Elusive\n'

        if level >= 19:
            allowed_spells = 12
            spell_slots['4'] = 1

        if level >= 20:
            allowed_spells = 13
            class_features += 'Stroke of Luck\n'

        #Weapon selection
        wind = random.randint(0, len(weapons.rogue_weapons)-1)
        weapon = weapons.rogue_weapons[wind]
        dmg = weapons.rogue_weapons_dmg[wind]

        # Armor selection
        acind = random.randint(0, len(weapons.light_armor)-1)
        armor = weapons.light_armor[acind]
        armorclass = weapons.light_armor_ac[acind]

        skill_rand_1 = random.randint(0, len(skills.rogue_skills)-1)
        skill.append(skills.rogue_skills[skill_rand_1])
        del skills.rogue_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.rogue_skills)-1)
        skill.append(skills.rogue_skills[skill_rand_2])
        del skills.rogue_skills[skill_rand_2]
        skill_rand_3 = random.randint(0, len(skills.rogue_skills)-1)
        skill.append(skills.rogue_skills[skill_rand_3])
        del skills.rogue_skills[skill_rand_3]
        skill_rand_4 = random.randint(0, len(skills.rogue_skills)-1)
        skill.append(skills.rogue_skills[skill_rand_4])

    elif charclass is 'sorcerer':
        CON, CHA = 15, 14
        st1 = 'CON'
        st2 = 'CHA'
        data_dict['HPMax'] = str(level * 6 + (2 * level))
        proficiencies = 'Armor: Light\nWeapons: Very Simple'
        sorc_orig = 0
        sorc_orig_str = ''
        meta_magics = ''
        metamagic_mods = [
        'Careful Spell',
        'Distant Spell',
        'Empowered Spell',
        'Extended Spell',
        'Heightened Spell',
        'Quickened Spell',
        'Subtle Spell',
        'Twinned Spell'
        ]

        #levelling
        if level >= 1:
            # c = 2, 1 = 2
            spell_slots['c'] = 4
            spell_slots['1'] = 2
            allowed_spells = 2
            sorc_orig = random.randint(0, 2)
            if sorc_orig == 0:
                sorc_orig_str = 'Draconic Bloodline'
                #get some dragon bonuses
                class_features += 'Sorcerous Origins:\n -> ' + sorc_orig_str + '\nDraconic Resilience\n'
            elif sorc_orig == 1:
                sorc_orig_str = 'Wild Magic'
                class_features += 'Sorcerous Origins:\n -> ' + sorc_orig_str + '\nWild Magic Surge\nTides of Chaos\n'
            elif sorc_orig == 2:
                sorc_orig_str = 'Shadow'
                class_features += 'Sorcerous Origins:\n -> ' + sorc_orig_str + '\nEyes of the Dark\nStrength of the Grave\n'

        if level >= 2:
            # c = 2, 1 = 3
            class_features += 'Font of Magic\nSorcery Points\nFlexible Casting\n'
            spell_slots['1'] = 3
            allowed_spells = 3

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            m1 = random.choice(metamagic_mods)
            metamagic_mods.remove(m1)
            m2 = random.choice(metamagic_mods)
            metamagic_mods.remove(m2)
            meta_magics += 'Metamagic: \n ' + m1 + '\n ' + m2 + '\n '
            spell_slots['1'] += 1
            spell_slots['2'] = 2
            allowed_spells = 4

        if level >= 4:
            # c = 3, 1 = 4, 2 = 3
            spell_slots['c'] += 1
            spell_slots['2'] += 1
            allowed_spells = 5

        if level >= 5:
            # c = 3, 1 = 4, 2 = 3, 3 = 2
            allowed_spells = 6
            spell_slots['3'] = 2

        if level >= 6:
            # c = 3, 1 = 4, 2 = 3, 3 = 3
            spell_slots['3'] += 1
            allowed_spells = 7
            if sorc_orig == 0:
                class_features += 'Elemental Affinity\n'
            elif sorc_orig == 1:
                class_features += 'Bend Luck\n'
            elif sorc_orig == 2:
                class_features += 'Hound of Ill Omen\n'

        if level >= 7:
            spell_slots['4'] += 1
            allowed_spells = 8

        if level >= 8:
            spell_slots['4'] += 1
            allowed_spells = 9

        if level >= 9:
            spell_slots['4'] += 1
            spell_slots['5'] = 1
            allowed_spells = 10


        if level >= 10:
            spell_slots['c'] += 1
            spell_slots['5'] += 1
            allowed_spells = 11


        if level >= 11:
            spell_slots['6'] = 1
            allowed_spells = 12

        if level >= 13:
            allowed_spells = 13
            spell_slots['7'] = 1

        if level >= 14:
            if sorc_orig == 0:
                class_features += 'Dragon Wings\n'
            elif sorc_orig == 1:
                class_features += 'Controlled Chaos\n'
            elif sorc_orig == 2:
                class_features += 'Shadow Walk\n'

        if level >= 15:
            allowed_spells = 14
            spell_slots['8'] = 1

        if level >= 17:
            allowed_spells = 15
            spell_slots['9'] = 1

        if level >= 18:
            spell_slots['5'] += 1
            if sorc_orig == 0:
                class_features += 'Draconic Presence\n'
            elif sorc_orig == 1:
                class_features += 'Spell Bombardment\n'
            elif sorc_orig == 2:
                class_features += 'Umbral Form\n'

        if level >= 19:
            spell_slots['6'] += 1

        if level >= 20:
            spell_slots['7'] += 1
            class_features += 'Sorcerous Restoration\n'

        #Weapon selection
        wind = random.randint(0, len(weapons.simple_weapons)-1)
        weapon = weapons.simple_weapons[wind]
        dmg = weapons.simple_weapons_dmg[wind]

        # Armor selection
        acind = random.randint(0, len(weapons.light_armor)-1)
        armor = weapons.light_armor[acind]
        armorclass = weapons.light_armor_ac[acind]

        skill_rand_1 = random.randint(0, len(skills.sorcerer_skills)-1)
        skill.append(skills.sorcerer_skills[skill_rand_1])
        del skills.sorcerer_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.sorcerer_skills)-1)
        skill.append(skills.sorcerer_skills[skill_rand_2])

    elif charclass is 'warlock':
        WIS, CHA = 15, 14
        st1 = 'WIS'
        st2 = 'CHA'
        data_dict['HPMax'] = str(level * 8 + (2 * level))
        proficiencies = 'Armor: Light\nWeapons: Simple'
        patron = 0
        patron_str = ''

        #levelling
        if level >= 1:
            # c = 2, 1 = 2
            patron = random.randint(0, 3)
            if patron == 0:
                patron_str = 'Archfey'
                #get some dragon bonuses
                class_features += 'Patron:\n -> ' + patron_str + '\nFey Presence\n'
            elif patron == 1:
                patron_str = 'Celestial'
                #bonus cantrips
                class_features += 'Patron:\n -> ' + patron_str + '\nHealing Light\n'
            elif patron == 2:
                patron_str = 'Fiend'
                class_features += 'Patron:\n -> ' + patron_str + '\nDark One\'s Blessing\n'
            elif patron == 3:
                patron_str = 'Great Old One'
                class_features += 'Patron:\n -> ' + patron_str + '\nAwakened Mind\n'


        if level >= 2:
            # c = 2, 1 = 3
            class_features += 'Eldritch Evocation\n'
            spell_slots['1'] = 3
            allowed_spells = 3

        if level >= 3:
            #c = 2, 1 = 4, 2 = 2
            pact_boon = ['Pact of the Blade', 'Pact of the Chain', 'Pact of the Tome']
            m1 = random.choice(pact_boon)
            metamagic_mods.remove(m1)
            m2 = random.choice(pact_boon)
            metamagic_mods.remove(m2)
            meta_magics += 'Pact Boon: \n ' + m1 + '\n ' + m2 + '\n '
            spell_slots['1'] += 1
            spell_slots['2'] = 2
            allowed_spells = 4

        if level >= 4:
            # c = 3, 1 = 4, 2 = 3
            spell_slots['c'] += 1
            spell_slots['2'] += 1
            allowed_spells = 5

        if level >= 5:
            # c = 3, 1 = 4, 2 = 3, 3 = 2
            allowed_spells = 6
            spell_slots['3'] = 2

        if level >= 6:
            # c = 3, 1 = 4, 2 = 3, 3 = 3
            spell_slots['3'] += 1
            allowed_spells = 7
            if patron == 0:
                class_features += 'Misty Escape\n'
            elif patron == 1:
                class_features += 'Radiant Soul\n'
            elif patron == 2:
                class_features += 'Dark One\'s Own Luck\n'
            elif patron == 3:
                class_features += 'Entropic Ward\n'

        if level >= 7:
            spell_slots['4'] += 1
            allowed_spells = 8

        if level >= 8:
            spell_slots['4'] += 1
            allowed_spells = 9

        if level >= 9:
            spell_slots['4'] += 1
            spell_slots['5'] = 1
            allowed_spells = 10


        if level >= 10:
            spell_slots['c'] += 1
            spell_slots['5'] += 1
            allowed_spells = 11
            if patron == 0:
                class_features += 'Beguiling Defenses\n'
            elif patron == 1:
                class_features += 'Celestial Resistance\n'
            elif patron == 2:
                class_features += 'Fiendish Resilience\n'
            elif patron == 3:
                class_features += 'Thought Shield\n'


        if level >= 11:
            class_features += 'Mystic Arcanum\n'
            spell_slots['6'] = 1
            allowed_spells = 12

        if level >= 13:
            allowed_spells = 13
            spell_slots['7'] = 1

        if level >= 14:
            if patron == 0:
                class_features += 'Dark Delirium\n'
            elif patron == 1:
                class_features += 'Searing Vengeance\n'
            elif patron == 2:
                class_features += 'Hurl Through Hell\n'
            elif patron == 3:
                class_features += 'Create Thrall\n'


        if level >= 15:
            allowed_spells = 14
            spell_slots['8'] = 1

        if level >= 16:
            do_nothing = 19

        if level >= 17:
            allowed_spells = 15
            spell_slots['9'] = 1

        if level >= 18:
            spell_slots['5'] += 1

        if level >= 19:
            spell_slots['6'] += 1

        if level >= 20:
            spell_slots['7'] += 1
            class_features += 'Eldritch Master\n'

        #Weapon selection
        wind = random.randint(0, len(weapons.simple_weapons)-1)
        weapon = weapons.simple_weapons[wind]
        dmg = weapons.simple_weapons_dmg[wind]

        # Armor selection
        acind = random.randint(0, len(weapons.light_armor)-1)
        armor = weapons.light_armor[acind]
        armorclass = weapons.light_armor_ac[acind]

        skill_rand_1 = random.randint(0, len(skills.warlock_skills)-1)
        skill.append(skills.warlock_skills[skill_rand_1])
        del skills.warlock_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.warlock_skills)-1)
        skill.append(skills.warlock_skills[skill_rand_2])

    elif charclass is 'wizard':
        INT, WIS = 15, 14
        st1 = 'INT'
        st2 = 'WIS'
        data_dict['HPMax'] = str(level * 6 + (2 * level))
        proficiencies = 'Armor: Light\nWeapons: Very Simple'
        tradition = 0
        tradition_str = ''

        #levelling
        if level >= 1:
            # c = 2, 1 = 2
            spell_slots['c'] = 4
            spell_slots['1'] = 2
            allowed_spells = 2
            class_features = 'Spellcasting\nSpellbook\n'

        if level >= 2:
            # c = 2, 1 = 3
            spell_slots['1'] = 3
            allowed_spells = 3
            tradition = random.randint(0, 12)

            if tradition == 1 and race is not 'elf':
                tradition = 2

            if tradition == 0:
                tradition_str = 'Abjuration'
                #get some dragon bonuses
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nAbjuration Savant\nArcane Ward\n'
            elif tradition == 1:
                tradition_str = 'Bladesinger'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nTraining in War and Song\nBladesong\n'
            elif tradition == 2:
                tradition_str = 'Conjuration'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nConjuration Savant\nMinor Conjuration\n'
            elif tradition == 3:
                tradition_str = 'Divination'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nDivination Savant\nPortent\n'
            elif tradition == 4:
                tradition_str = 'Enchantment'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nEnchantment Savant\nHypnotic Gaze\n'
            elif tradition == 5:
                tradition_str = 'Evocation'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nEvocation Savant\nSculpt Spells\n'
            elif tradition == 6:
                tradition_str = 'Illusion'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nIllusion Savant\nImproved Minor Illusion\n'
            elif tradition == 7:
                tradition_str = 'Invention'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nTools of the Inventor\nArcanomechanical Armor\nReckless Casting\n'
            elif tradition == 8:
                tradition_str = 'Lore Mastery'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nSpell Secrets\nAltering Spells\n'
            elif tradition == 9:
                tradition_str = 'Necromancy'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nNecromancy Savant\nGrim Harvest\n'
            elif tradition == 10:
                tradition_str = 'Theurgy'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nDivine Inspiration\nArcane Initiate\nChannel Arcana\nDivine Arcana\n'
            elif tradition == 11:
                tradition_str = 'Transmutation'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nTransmutation Savant\nMinor Alchemy\n'
            elif tradition == 12:
                tradition_str = 'War Magic'
                class_features += 'Arcane Tradition:\n -> ' + tradition_str + '\nArcane Deflection\nTactical Wit\n'

        if level >= 3:
            spell_slots['1'] += 1
            spell_slots['2'] = 2
            allowed_spells = 4

        if level >= 4:
            spell_slots['c'] += 1
            spell_slots['2'] += 1
            allowed_spells = 5

        if level >= 5:
            allowed_spells = 6
            spell_slots['3'] = 2

        if level >= 6:
            spell_slots['3'] += 1
            allowed_spells = 7
            if tradition == 0:
                class_features += 'Projected Ward\n'
            elif tradition == 1:
                class_features += 'Extra Attack\n'
            elif tradition == 2:
                class_features += 'Benign Transportation\n'
            elif tradition == 3:
                class_features += 'Expert Divination\n'
            elif tradition == 4:
                class_features += 'Instinctive Charm\n'
            elif tradition == 5:
                class_features += 'Potent Cantrips\n'
            elif tradition == 6:
                class_features += 'Malleable Illusions\n'
            elif tradition == 7:
                class_features += 'Alchemical Casting\n'
            elif tradition == 8:
                class_features += 'Alchemical Casting\n'
            elif tradition == 9:
                class_features += 'Undead Thralls\n'
            elif tradition == 10:
                class_features += 'Arcane Acolyte\n'
            elif tradition == 11:
                class_features += 'Transmuter\'s Stone\n'
            elif tradition == 12:
                class_features += 'Power Surge\n'


        if level >= 7:
            spell_slots['4'] += 1
            allowed_spells = 8

        if level >= 8:
            spell_slots['4'] += 1
            allowed_spells = 9

        if level >= 9:
            spell_slots['4'] += 1
            spell_slots['5'] = 1
            allowed_spells = 10


        if level >= 10:
            spell_slots['c'] += 1
            spell_slots['5'] += 1
            allowed_spells = 11
            if tradition == 0:
                class_features += 'Improved Abjuration\n'
            elif tradition == 1:
                class_features += 'Song of Defense\n'
            elif tradition == 2:
                class_features += 'Focused Transportation\n'
            elif tradition == 3:
                class_features += 'The Third Eye\n'
            elif tradition == 4:
                class_features += 'Split Enchantment\n'
            elif tradition == 5:
                class_features += 'Empowered Evocation\n'
            elif tradition == 6:
                class_features += 'Illusory Self\n'
            elif tradition == 7:
                class_features += 'Prodigious Inspiration\n'
            elif tradition == 8:
                class_features += 'Prodigious Memory\n'
            elif tradition == 9:
                class_features += 'Inured to Undeath\n'
            elif tradition == 10:
                class_features += 'Arcane Priest\n'
            elif tradition == 11:
                class_features += 'Shapechanger\n'
            elif tradition == 12:
                class_features += 'Durable Magic\n'


        if level >= 11:
            spell_slots['6'] = 1
            allowed_spells = 12

        if level >= 13:
            allowed_spells = 13
            spell_slots['7'] = 1

        if level >= 14:
            if tradition == 0:
                class_features += 'Spell Resistance\n'
            elif tradition == 1:
                class_features += 'Song of Victory\n'
            elif tradition == 2:
                class_features += 'Durable Summons\n'
            elif tradition == 3:
                class_features += 'Greater Portent\n'
            elif tradition == 4:
                class_features += 'Alter Memories\n'
            elif tradition == 5:
                class_features += 'Overchannel\n'
            elif tradition == 6:
                class_features += 'Illusory Reality\n'
            elif tradition == 7:
                class_features += 'Controlled Chaos\n'
            elif tradition == 8:
                class_features += 'Master of Magic\n'
            elif tradition == 9:
                class_features += 'Command Undead\n'
            elif tradition == 10:
                class_features += 'Arcane High Priest\n'
            elif tradition == 11:
                class_features += 'Master Transmuter\n'
            elif tradition == 12:
                class_features += 'Deflecting Shroud\n'


        if level >= 15:
            allowed_spells = 14
            spell_slots['8'] = 1

        if level >= 17:
            allowed_spells = 15
            spell_slots['9'] = 1

        if level >= 18:
            spell_slots['5'] += 1
            class_features += 'Spell Mastery\n'

        if level >= 19:
            spell_slots['6'] += 1

        if level >= 20:
            spell_slots['7'] += 1
            class_features += 'Signature Spells\n'

        #Weapon selection
        wind = random.randint(0, len(weapons.simple_weapons)-1)
        weapon = weapons.simple_weapons[wind]
        dmg = weapons.simple_weapons_dmg[wind]

        # Armor selection
        acind = random.randint(0, len(weapons.light_armor)-1)
        armor = weapons.light_armor[acind]
        armorclass = weapons.light_armor_ac[acind]

        skill_rand_1 = random.randint(0, len(skills.wizard_skills)-1)
        skill.append(skills.wizard_skills[skill_rand_1])
        del skills.wizard_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, len(skills.wizard_skills)-1)
        skill.append(skills.wizard_skills[skill_rand_2])

    print('\n', charclass, race, '\n')
    print('\n', skill, '\n')
    print('\n', st1, st2, '\n')


    STR, DEX, CON, INT, WIS, CHA, features_traits = \
    skills.skill_setter(STR, DEX, CON, INT, WIS, CHA, race, charclass, class_features, level)

    if st1 is 'STR' or st2 is 'STR':
        data_dict['ST Strength'] = str(prof + int(skills.mod_get(STR)))
    if st1 is 'DEX' or st2 is 'DEX':
        data_dict['ST Dexterity'] = str(prof + int(skills.mod_get(DEX)))
    if st1 is 'CON' or st2 is 'CON':
        data_dict['ST Constitution'] = str(prof + int(skills.mod_get(CON)))
    if st1 is 'INT' or st2 is 'INT':
        data_dict['ST Intelligence'] = str(prof + int(skills.mod_get(INT)))
    if st1 is 'WIS' or st2 is 'WIS':
        data_dict['ST Wisdom'] = str(prof + int(skills.mod_get(WIS)))
    if st1 is 'CHA' or st2 is 'CHA':
        data_dict['ST Charisma'] = str(prof + int(skills.mod_get(CHA)))

    data_dict['STR'] = str(STR)
    data_dict['STRmod'] = skills.mod_get(STR)
    data_dict['DEX'] = str(DEX)
    data_dict['DEXmod '] = skills.mod_get(DEX)
    data_dict['CON'] = str(CON)
    data_dict['CONmod'] = skills.mod_get(CON)
    data_dict['INT'] = str(INT)
    data_dict['INTmod'] = skills.mod_get(INT)
    data_dict['WIS'] = str(WIS)
    data_dict['WISmod'] = skills.mod_get(WIS)
    data_dict['CHA'] = str(CHA)
    data_dict['CHamod'] = skills.mod_get(CHA)

    data_dict['AC'] = str(int(armorclass) + int(skills.mod_get(DEX)) + (2 * shield))
    data_dict['Equipment'] = armor
    data_dict['Wpn Name'] = weapon
    data_dict['AttacksSpellcasting'] = weapon
    data_dict['Wpn1 Damage'] = dmg
    data_dict['Wpn1 AtkBonus'] = '+' + str(prof + int(skills.mod_get(STR)))

    data_dict['Features and Traits'] = features_traits
    data_dict['ProficienciesLang'] = proficiencies

    data_dict['SP'] = str(4 * random.randint(0, level))
    data_dict['GP'] = str(3 * random.randint(0, level))
    data_dict['CP'] = str(5 * random.randint(0, level))
    data_dict['EP'] = str(2 * random.randint(0, level))
    data_dict['PP'] = str(1 * random.randint(0, level))

    for ability in skill:
        if ability in skills.Strength_skills:
            data_dict[ability] = str(prof + int(skills.mod_get(STR)))
        elif ability in skills.Dexterity_skills:
            data_dict[ability] = str(prof + int(skills.mod_get(DEX)))
        elif ability in skills.Intelligence_skills:
            data_dict[ability] = str(prof + int(skills.mod_get(INT)))
        elif ability in skills.Wisdom_skills:
            data_dict[ability] = str(prof + int(skills.mod_get(WIS)))
        elif ability in skills.Charisma_skills:
            data_dict[ability] = str(prof + int(skills.mod_get(CHA)))
        if ability is 'Perception':
            data_dict['Passive'] = str(prof + int(skills.mod_get(WIS)))
            percepflag = 1

    if percepflag is 0:
        data_dict['Passive'] = skills.mod_get(WIS)

    bglen = len(bg.backs)
    randombgind = random.randint(0, bglen-1)
    background = bg.backs[randombgind]
    backgrounders = list(background)
    if '_' in backgrounders:
        ind = backgrounders.index('_')
        backgrounders[ind] = ' '
    data_dict['Background'] = ''.join(backgrounders)
    ind = bg.backs.index(background)

    data_dict['PersonalityTraits '] = bg.backs_arrs[ind][random.randint(0, 5)]
    data_dict['Ideals'] = bg.backs_arrs[ind][random.randint(6, 11)]
    data_dict['Bonds'] = bg.backs_arrs[ind][random.randint(12, 17)]
    data_dict['Flaws'] = bg.backs_arrs[ind][random.randint(18, 23)]


    return

def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict, level):
    dictfiller(level)
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    print(os.path.abspath(output_pdf_path))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

data_dict = {
   'ClassLevel': '',
   'Background': '',
   'PlayerName': '',
   'CharacterName': '',
   'Race ': '',
   'Alignment': '',
   'XP': '',
   'Inspiration': '',
   'STR': '',
   'ProfBonus': '',
   'AC': '',
   'Initiative': '',
   'Speed': '',
   'PersonalityTraits': '',
   'STRmod': '',
   'ST Strength': '',
   'DEX': '',
   'Ideals': '',
   'DEXmod ': '',
   'Bonds': '',
   'CON': '',
   'HDTotal': '',
   'Check Box 12': '',
   'Check Box 13': '',
   'Check Box 14': '',
   'CONmod': '',
   'Check Box 15': '',
   'Check Box 16': '',
   'Check Box 17': '',
   'HD': '',
   'Flaws': '',
   'INT': '',
   'ST Dexterity': '',
   'ST Constitution': '',
   'ST Intelligence': '',
   'ST Wisdom': '',
   'ST Charisma': '',
   'Acrobatics': '',
   'Animal': '',
   'Athletics': '',
   'Deception ': '',
   'History ': '',
   'Wpn Name': '',
   'Wpn1 AtkBonus': '',
   'Wpn1 Damage': '',
   'Insight': '',
   'Intimidation': '',
   'Wpn Name 2': '',
   'Wpn2 AtkBonus': '',
   'Wpn Name 3': '',
   'Wpn3 AtkBonus': '',
   'Check Box 11': '',
   'Check Box 18': '',
   'Check Box 19': '',
   'Check Box 20': '',
   'Check Box 21': '',
   'Check Box 22': '',
   'INTmod': '',
   'Wpn2 Damage': '',
   'Investigation ': '',
   'WIS': '',
   'Arcana': '',
   'Perception ': '',
   'WISmod': '',
   'CHA': '',
   'Nature': '',
   'Performance': '',
   'Medicine': '',
   'Religion': '',
   'Stealth ': '',
   'Check Box 23': '',
   'Check Box 24': '',
   'Check Box 25': '', #Perception single item
   'Check Box 26': '',
   'Check Box 27': '',
   'Check Box 28': '',
   'Check Box 29': '',
   'Check Box 30': '',
   'Check Box 31': '',
   'Check Box 32': '',
   'Check Box 33': '',
   'Check Box 34': '',
   'Check Box 35': '',
   'Check Box 36': '',
   'Check Box 37': '',
   'Check Box 38': '',
   'Check Box 39': '',
   'Check Box 40': '',
   'Persuasion': '',
   'HPMax': '',
   'HPCurrent': '',
   'HPTemp': '',
   'Wpn3 Damage': '',
   'SleightofHand': '',
   'CHamod': '',
   'Survival': '',
   'AttacksSpellcasting': '',
   'Passive': '',
   'CP': '',
   'ProficienciesLang': '',
   'SP': '',
   'EP': '',
   'GP': '',
   'PP': '',
   'Equipment': '',
   'Features and Traits': '',
}

if __name__ == '__main__':
    write_fillable_pdf(CHARSHEET_PATH, CHARSHEET_OUTPUT_PATH, data_dict, level)
