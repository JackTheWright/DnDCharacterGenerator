# File for skills, each class has their own
import random

class skills:

    all_skills = [
    'Athletics',
    'Acrobatics',
    'SleightofHand',
    'Stealth',
    'Arcana',
    'History',
    'Investigation',
    'Nature',
    'Religion',
    'AnimalHandling',
    'Insight',
    'Medicine',
    'Perception',
    'Survival',
    'Deception',
    'Intimidation',
    'Performance',
    'Persuasion'
    ]

    Strength_skills = [
    'Athletics'
    ]

    Dexterity_skills = [
    'Acrobatics',
    'Sleight of Hand',
    'Stealth'
    ]

    Intelligence_skills = [
    'Arcana'
    'History',
    'Investigation',
    'Nature',
    'Religion'
    ]

    Wisdom_skills = [
    'Animal Handling',
    'Insight',
    'Medicine',
    'Perception',
    'Survival'
    ]

    Charisma_skills = [
    'Deception',
    'Intimidation',
    'Performance',
    'Persuasion'
    ]

    barb_skills = [
    'AnimalHandling',
    'Athletics',
    'Intimidation',
    'Nature',
    'Perception',
    'Survival'
    ]

    cleric_skills = [
    'History',
    'Insight',
    'Medicine',
    'Persuasion',
    'Religion'
    ]

    druid_skills = [
    'Arcana',
    'AnimalHandling',
    'Insight',
    'Medicine',
    'Nature',
    'Perception',
    'Religion',
    'Survival'
    ]

    fighter_skills = [
    'Acrobatics',
    'Animal Handling',
    'Athletics',
    'History',
    'Insight',
    'Intimidation',
    'Perception',
    'Survival'
    ]

    monk_skills = [
    'Acrobatics',
    'Athletics',
    'History',
    'Insight',
    'Religion',
    'Stealth'
    ]

    paladin_skills = [
    'Athletics',
    'Insight',
    'Intimidation',
    'Medicine',
    'Persuasion',
    'Religion'
    ]

    ranger_skills = [
    'AnimalHandling',
    'Athletics',
    'Insight',
    'Investigation',
    'Nature',
    'Perception',
    'Stealth',
    'Survival'
    ]

    rogue_skills = [
    'Acrobatics',
    'Athletics',
    'Deception',
    'Insight',
    'Intimidation',
    'Investigation',
    'Perception',
    'Performance',
    'Persuasion',
    'SleightofHand',
    'Stealth'
    ]

    sorcerer_skills = [
    'Arcana',
    'Deception',
    'Insight',
    'Intimidation',
    'Persuasion',
    'Religion'
    ]

    warlock_skills = [
    'Arcana',
    'Deception',
    'History',
    'Intimidation',
    'Investigation',
    'Nature',
    'Religion'
    ]

    wizard_skills = [
    'Arcana',
    'History',
    'Insight',
    'Investigation',
    'Medicine',
    'Religion'
    ]

    def skill_setter(self, STR, DEX, CON, INT, WIS, CHA, race, charclass):
        skill_points = [13, 12, 10, 8]
        tools = ['smiths tools', 'brewer supplies', 'masons tools']
        languages = ['Dwarven', 'Elvish', 'Fae', 'Draconic', 'Halfling',
        'Gnomish', 'Orc', 'Infernal', 'Giant']
        color = [ 'Black', 'Copper', 'Bronze', 'Blue', 'Brass', 'Gold', 'Red',\
         'Green', 'Silver', 'White' ]
        count = 0
        random.shuffle(tools)
        random.shuffle(skill_points)
        random.shuffle(languages)
        random.shuffle(color)

        if STR == 0:
            STR = skill_points[count]
            count += 1
        if DEX == 0:
            DEX = skill_points[count]
            count += 1
        if CON == 0:
            CON = skill_points[count]
            count += 1
        if INT == 0:
            INT = skill_points[count]
            count += 1
        if WIS == 0:
            WIS = skill_points[count]
            count += 1
        if CHA == 0:
            CHA = skill_points[count]
            count += 1

        if race is 'dwarf':
            CON += 2
            features_traits = 'Darkvision\nDwarven Resilience\nDwarven Combat Training\nStonecunning\n' + tools[0] + '\nLanguages: Common, Dwarven'
        elif race is 'elf':
            DEX += 2
            features_traits = 'Darkvision\nKeen Senses\nFey Ancestry\nTrance\nLanguages: Common, Elvish'
        elif race is 'halfling':
            DEX += 2
            features_traits = 'Lucky\nBrave\nHalfling Nimbleness\nLanguages:Common, Halfling'
        elif race is 'human':
            STR += 1
            DEX += 1
            CON += 1
            INT += 1
            WIS += 1
            CHA += 1
            features_traits = 'Languages: Common, ' + languages[0]
        elif race is 'dragonborn':
            STR += 2
            CHA += 1
            features_traits = 'Draconic Ancestry\nBreath Weapon\nDamage Resistance\nLanguages: Common, Draconic\nColor: ' + color[0]
        elif race is 'gnome':
            INT += 2
            features_traits = 'Darkvision\nGnome Cunning\nLanguages: Common, Gnomish'
        elif race is 'halfelf':
            CHA += 2
            features_traits = 'Darkvision\nFey Ancestry\nSkill Versatility\nLanguages: Common, Elvish'
        elif race is 'halforc':
            STR += 2
            CON += 1
            features_traits = 'Darkvision\nMenacing\nRelentless Endurance\nSavage Attacks\nLanguages: Common, Orc'
        elif race is 'tiefling':
            CHA += 2
            INT += 1
            features_traits = 'Darkvision\nHellish Resistance\nInfernal Legacy\nLanguages: Common, Infernal'
        elif race is 'goliath':
            STR += 2
            CON += 1
            features_traits = 'Natural Athlete\nStone\'s Endurance\nPowerful Build\nMountain Born\nLanguages: Common, Giant'

        return STR, DEX, CON, INT, WIS, CHA, features_traits


    def mod_get(self, skill):
        if skill == 1:
            mod = '-5'
        elif skill == 2 or skill == 3:
            mod = '-4'
        elif skill == 4 or skill == 5:
            mod = '-3'
        elif skill == 6 or skill == 7:
            mod = '-2'
        elif skill == 8 or skill == 9:
            mod = '-1'
        elif skill == 10 or skill == 11:
            mod = '0'
        elif skill == 12 or skill == 13:
            mod = '+1'
        elif skill == 14 or skill == 15:
            mod = '+2'
        elif skill == 16 or skill == 17:
            mod = '+3'
        elif skill == 18 or skill == 19:
            mod = '+4'
        elif skill == 20 or skill == 21:
            mod = '+5'
        elif skill == 22 or skill == 23:
            mod = '+6'
        elif skill == 24 or skill == 25:
            mod = '+7'
        elif skill == 26 or skill == 27:
            mod = '+8'
        elif skill == 28 or skill == 29:
            mod = '+9'
        elif skill == 30:
            mod = '+10'
        return mod
