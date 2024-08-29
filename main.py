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
    def __init__(self, name, age, weight, height, defenses, conditions, personality_traits, ideals, bonds, flaws, gender, eyes, size, faith, hair, skin, proficient, level):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.defenses = defenses
        self.conditions = conditions
        self.personality_traits = personality_traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.gender = gender
        self.eyes = eyes
        self.size = size
        self.faith = faith
        self.hair = hair
        self.skin = skin
        self.proficient = proficient
        self.level = level

def update_proficiency(dnd_skills, skill_name, proficient):
    if skill_name in dnd_skills:
        dnd_skills[skill_name]["proficient"] = proficient
    else:
        print(f"Skill '{skill_name}' does not exist.")   

         
dnd_skills = {
    "Acrobatics": {
        "ability": "Dexterity",
        "proficient": False,
        "double_proficiency": False
    },
    "Animal Handling": {
        "ability": "Wisdom",
        "proficient": False,
        "double_proficiency": False
    },
    "Arcana": {
        "ability": "Intelligence",
        "proficient": False,
        "double_proficiency": False
    },
    "Athletics": {
        "ability": "Strength",
        "proficient": False,
        "double_proficiency": False
    },
    "Deception": {
        "ability": "Charisma",
        "proficient": False,
        "double_proficiency": False
    },
    "History": {
        "ability": "Intelligence",
        "proficient": False,
        "double_proficiency": False
    },
    "Insight": {
        "ability": "Wisdom",
        "proficient": False,
        "double_proficiency": False
    },
    "Intimidation": {
        "ability": "Charisma",
        "proficient": False,
        "double_proficiency": False
    },
    "Investigation": {
        "ability": "Intelligence",
        "proficient": False,
        "double_proficiency": False
    },
    "Medicine": {
        "ability": "Wisdom",
        "proficient": False,
        "double_proficiency": False
    },
    "Nature": {
        "ability": "Intelligence",
        "proficient": False,
        "double_proficiency": False
    },
    "Perception": {
        "ability": "Wisdom",
        "proficient": False,
        "double_proficiency": False
    },
    "Performance": {
        "ability": "Charisma",
        "proficient": False,
        "double_proficiency": False
    },
    "Persuasion": {
        "ability": "Charisma",
        "proficient": False,
        "double_proficiency": False
    },
    "Religion": {
        "ability": "Intelligence",
        "proficient": False,
        "double_proficiency": False
    },
    "Sleight of Hand": {
        "ability": "Dexterity",
        "proficient": False,
        "double_proficiency": False
    },
    "Stealth": {
        "ability": "Dexterity",
        "proficient": False,
        "double_proficiency": False
    },
    "Survival": {
        "ability": "Wisdom",
        "proficient": False,
        "double_proficiency": False
    }
}

level = 1


#Human 
human_size = "medium"

#Standard Human
standard_human = "Standard"
standard_human_ability = Ability(1,1,1,1,1,1)
standard_human_lenguage = "common"
standard_human_speed = 30

#Variant Human
variant_human_ability = Ability(input())
variant_human_proficient_skill = input({"Name": "skill"})

#Dwarf
dwarf_size = "medium"
dwarf_speed = 25
#Dwarven features 
dwarven_resilence = "You have advantage on saving throws against poison, and you have resistance against poison damage."
dwarven_resistance = {"poison": True}

dwarven_combat_training = "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."
dwarven_combat_training_proficiencies = {"battleaxe": True, "handaxe": True, "light hammer": True, "warhammer": True}

stonecunning = "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."

dwarf_features =(dwarven_resilence, dwarven_combat_training, stonecunning)

dwarf_tool_proficiency = input("Select one tool proficiency: smith's tools, brewer supplies or mason tools")

#Hill Dward
hill_dwarf = "Hill Dwarf"
hill_dwarf_ability = Ability(0,0,2,0,1,0, 0)
dwarven_toughness = {"Dwarven Toughness": "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."}
hill_dwarf_features = dwarven_toughness
dwarven_toughness_hp = 1 + (level - 1)

#Mountain Dwarf
mountain_dwarf = "Mountain Dwarf"
mountain_dwarf_ability = Ability(2,0,2,0,0,0, 0)
dwarven_armor_training = {"Dwarven Armor Training": "You have proficiency with light and medium armor"}
mountain_dward_features = dwarven_armor_training
mountain_dwarf_proficiency = {"Light armor": True, "Medium armor": True}

#Elf 
elf_size = "Medium"
elf_speed = 30
elf_languages = ("Common", "Elven")
darkvision = {"Darkvision": "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."}
fey_ancestry = {"Fey Ancestry": "You have advantage on saving throws against being charmed, and magic can't put you to sleep."}
trance = {"Trance": "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is trance. While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep."}
keen_senses = {"Keen Senses": "You have proficiency in the Perception skill."}
elf_skill_proficiencies = {"Perception":{"proficient": True}}
elf_features = {darkvision, fey_ancestry, trance, keen_senses}

#Dark Elf
dark_elf_abilities_increase = Ability(0, 2, 0, 0, 0, 1)
superior_darkvision = {"Superior Dark Vision": "Your darkvision has a range of 120 feet, instead of 60."}
sunlight_sensitivity = {"Sunlight Sensitivity": "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight."}
drow_magic = {"Drow Magic": "You know the Dancing Lights cantrip. When you reach 3rd level, you can cast the Faerie Fire spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the Darkness spell once and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."}
drow_weapon_training = {"Drow weapon Training": "You have proficiency with rapiers, shortswords, and hand crossbows."}
dark_elf_features = {superior_darkvision, sunlight_sensitivity, drow_magic, drow_weapon_training}
dark_elf_proficiencies = {"Rapiers" : True, "Shortsword": True, "Hand Crossbow": True}

#High Elf 
high_elf_abilities_increase = Ability(0, 2, 0, 1, 0, 0)
high_elf_cantrip = {"Cantrip": "You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it."}
extra_language = {"Extra Language": "You can read, speak, and write one additional language of your choice."}
extra_language_choice = input("Enter a valid language:")

#Wood Elf
wood_elf_abilities_increase = Ability(0, 2, 0, 0, 1, 0)
wood_elf_speed = elf_speed + 5
mask_of_the_wild = {"Mask of the Wild": "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."}

#Wood and High Elf
elf_weapon_training = {"Elf Weapon Training": "You have proficiency with the longsword, shortsword, shortbow, and longbow."}
elf_weapon_proficiencies = {"Longsword": True, "Shortsword": True, "Shortbow": True, "Longbow": True}

#Dragonborn

dragonborn_abilities_increase = Ability(2, 0, 0, 0, 0, 1)
dragonborn_size = "Medium"
dragonborn_speed = 30
dragonborn_color = {
    "Black":
        {"Damage type": "Acid",
         "Breath weapon": "5 by 30 ft. line (DEX save)"
        },
    "Blue":
        {"Damage type": "Lightning",
         "Breath weapon": "5 by 30 ft. line (DEX save)"
        },
    "Brass":
        {
        "Damage type": "Fire",
        "Breath weapon": "5 by 30 ft. line (DEX save)"
        },
    "Bronze":
        {
         "Damage type": "Lightning",
         "Breath weapon": "5 by 30 ft. line (DEX save)" 
        },
    "Copper":
        {
         "Damage type": "Acid",
         "Breath weapon": "5 by 30 ft. line (DEX save)" 
        },
    "Gold":
        {
         "Damage type": "Fire",
         "Breath weapon": "15 ft. cone (DEX save)" 
        },
    "Green":
        {
         "Damage type": "Poison",
         "Breath weapon": "15 ft. cone (CON save)" 
        },
    "Red":
        {
         "Damage type": "Fire",
         "Breath weapon": "15 ft. cone (DEX save)" 
        },
    "Silver":
        {
         "Damage type": "Cold",
         "Breath weapon": "15 ft. cone (CON save)" 
        },
    "White":
        {
         "Damage type": "Cold",
         "Breath weapon": "15 ft. cone (CON save)" 
        }          
    } 

dragonborn_color_selection = dragonborn_color[input("Select yout dragonborn color")]
breath_weapon = {"Breath Weapon": "You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest."}
damage_resistance = dragonborn_color[input("Select yout dragonborn color")]["Damage type"]
dragonborn_languages = ("Common", "Draconic")

#Gnome
gnome_size = "Small"
gnome_speed = 25
gnome_cunning = {"Gonme Cunning": "You have advantage on all Intelligence, Wisdom, and Charisma saves against magic."}
gnome_lenguages = ("Common", "Gnomish")
gnome_features = darkvision + gnome_cunning

#Forest Gnome
forest_gnome_ability_score_increase = Ability(0,1, 0, 2, 0, 0)
natural_illusionnist = {"Natural Illusionist": "You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it."}
speak_with_small_beast = {"Speak with Small Beast": "Through sound and gestures, you may communicate simple ideas with Small or smaller beasts."}

#Rock Gnome
rock_gnome_ability_score_increase = Ability(0, 0, 1, 2, 0, 0)
artificer_lore = {"Artificer's Lore": "Whenever you make an Intelligence (History) check related to magical, alchemical, or technological items, you can add twice your proficiency bonus instead of any other proficiency bonus that may apply."}
tinker = {"Tinker": "You have proficiency with artisan tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options:"}
tinker_options = {
    "Clockwork Toy": "This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.",
    "Fire Starter": "The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.",
    "Music Box": "When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed."
}