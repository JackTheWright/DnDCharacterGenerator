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


def dictfiller():
    races = ['dwarf', 'elf', 'halfling', 'human', 'dragonborn', 'gnome',\
        'halfelf', 'halforc', 'tiefling', 'goliath']
    classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk',\
            'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
    alignment = ['lawful', 'chaotic', 'good', 'good', 'good', 'good',\
            'chaotic', 'chaotic', 'chaotic', 'lawful']
    level = 3
    shield = 0
    percepflag = 0

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
        armorclass = armor_ac_arr[acind]

        # shielf flag
        shield = random.randint(0,1)

        skill_rand_1 = random.randint(0, 5)
        skill.append(skills.barb_skills[skill_rand_1])
        del skills.barb_skills[skill_rand_1]
        skill_rand_2 = random.randint(0, 4)
        skill.append(skills.barb_skills[skill_rand_2])

    elif charclass is 'bard':
        DEX, CHA = 15, 14
        st1 = 'DEX'
        st2 = 'CHA'
        data_dict['HPMax'] = str(level * 8 + (2 * level))
        proficiencies = 'Armor: Light\n Weapons: Simple, Hand Crossbows, Longswords\nRapiers, Shortswords'

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

        # armor selection
        aind = random.randint(0, 1)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_ac_arr[acind]

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

        # weapon selectio
        wind = random.randint(0, len(weapons.druid_weapons)-1)
        weapon = weapons.druid_weapons[wind]
        dmg = weapons.druid_weapons_dmg[wind]

        # armor selection
        aind = random.randint(0, 1)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_ac_arr[acind]

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
        armorclass = armor_ac_arr[acind]

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
        armorclass = armor_ac_arr[acind]

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

        # armor selection
        aind = random.randint(0, 1)
        armor_t = weapons.armor_arr[aind]
        armor_c = weapons.armor_ac_arr[aind]
        acind = random.randint(0, len(armor_t)-1)
        armor = armor_t[acind]
        armorclass = armor_ac_arr[acind]

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

    STR, DEX, CON, INT, WIS, CHA, features_traits = \
    skills.skill_setter(STR, DEX, CON, INT, WIS, CHA, race, charclass)

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
    data_dict['Wpn1 Damage'] = dmg
    data_dict['Wpn1 AtkBonus'] = str(prof + int(skill.mod_get(STR)))

    data_dict['Features and Traits'] = features_traits
    data_dict['ProficienciesLang'] = proficiencies

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

def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    dictfiller()
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
   'Deception': '',
   'History': '',
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
   'Investigation': '',
   'WIS': '',
   'Arcana': '',
   'Perception': '',
   'WISmod': '',
   'CHA': '',
   'Nature': '',
   'Performance': '',
   'Medicine': '',
   'Religion': '',
   'Stealth': '',
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
    write_fillable_pdf(CHARSHEET_PATH, CHARSHEET_OUTPUT_PATH, data_dict)
