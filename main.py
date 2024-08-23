class Race:
    def __init__(self, ability_score_increase, subrace, size, speed, racial_traits, languages):
       self.ability_score_increase = ability_score_increase
       self.subrace = subrace
       self.size = size
       self.speed = speed
       self.racial_traits = racial_traits
       self.languages = languages

    def __repr__(self):
        pass

class Pcclass:
    def __init__(self, armor_proficiency, weapons_proficiency, tools_proficiency, saving_throws_proficiency, skill_proficiency, pcclass_features, spellcaster_class):
        self.armor_proficiency = armor_proficiency
        self.weapons_proficiencyarmor_proficiency = weapons_proficiency
        self.tools_proficiencyarmor_proficiency = tools_proficiency
        self.saving_throws_proficiency = saving_throws_proficiency
        self.skills_proficiency = skill_proficiency
        self.pcclass_features = pcclass_features
        self.spellcaster_class = spellcaster_class

class Ability:
    def __init__(self, strenght, dexterity, consitution, intelligence, wisdom, charisma, skills):
        self.strenght = strenght
        self.dexterity = dexterity
        self.constitution = consitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.skills = skills
        
    def ability_score_modifier(self, score):
        return (score - 10) // 2

class Background: 
    def __init__(self, background_proficiencies, background_languages, background_features):
        self.background_proficiencies = background_proficiencies   
        self.backgound_languages = background_languages
        self.background_features = background_features

class Actions: 
    def __init__(self, attack, spells, inventory):
        self.attack = attack
        self.spells = spells
        self.inventory = inventory

class Character:
    def __init__(self, name, age, weight, height, defenses, conditions, personality_traits, ideals, bonds, flaws, gender, eyes, size, faith, hair, skin):
        pass
    
dnd_skills = {
    "Acrobatics": {
        "ability": "Dexterity",
        "proficient": False
    },
    "Animal Handling": {
        "ability": "Wisdom",
        "proficient": False
    },
    "Arcana": {
        "ability": "Intelligence",
        "proficient": False
    },
    "Athletics": {
        "ability": "Strength",
        "proficient": False
    },
    "Deception": {
        "ability": "Charisma",
        "proficient": False
    },
    "History": {
        "ability": "Intelligence",
        "proficient": False
    },
    "Insight": {
        "ability": "Wisdom",
        "proficient": False
    },
    "Intimidation": {
        "ability": "Charisma",
        "proficient": False
    },
    "Investigation": {
        "ability": "Intelligence",
        "proficient": False
    },
    "Medicine": {
        "ability": "Wisdom",
        "proficient": False
    },
    "Nature": {
        "ability": "Intelligence",
        "proficient": False
    },
    "Perception": {
        "ability": "Wisdom",
        "proficient": False
    },
    "Performance": {
        "ability": "Charisma",
        "proficient": False
    },
    "Persuasion": {
        "ability": "Charisma",
        "proficient": False
    },
    "Religion": {
        "ability": "Intelligence",
        "proficient": False
    },
    "Sleight of Hand": {
        "ability": "Dexterity",
        "proficient": False
    },
    "Stealth": {
        "ability": "Dexterity",
        "proficient": False
    },
    "Survival": {
        "ability": "Wisdom",
        "proficient": False
    }
}

