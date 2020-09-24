class Subject():
    def __init__(self, name: str, display_text: str, topics: list = None):
        self.name = name
        self.display_text = display_text
        self.topics = topics


english_a_sl = Subject(
    "english_a_sl",
    "English A SL",
    [
        "Test1",
        "Test2",
        "Test3",
        "Test4",
        "Test5"
    ]
)

english_a_hl = Subject(
    "english_a_hl",
    "English A HL"
)

chinese_a_sl = Subject(
    "chinese_a_sl",
    "Chinese A SL"
)

chinese_a_hl = Subject(
    "chinese_a_hl",
    "Chinese A HL"
)

french_ab = Subject(
    "french_ab",
    "French ab initio"
)

german_ab = Subject(
    "german_ab",
    "German ab initio"
)

english_b_hl = Subject(
    "english_b_hl",
    "English B HL"
)

chinese_b_hl = Subject(
    "chinese_b_hl",
    "Chinese B HL"
)

history_sl = Subject(
    "history_sl",
    "History SL"
)

history_hl = Subject(
    "history_hl",
    "History HL"
)

business_sl = Subject(
    "business_sl",
    "Business SL"
)

business_hl = Subject(
    "business_hl",
    "Business HL"
)

economic_sl = Subject(
    "economic_sl",
    "Economic SL"
)

economic_hl = Subject(
    "economic_hl",
    "Economic HL"
)

psychology_sl = Subject(
    "psychology_sl",
    "Psychology SL"
)

physics_sl = Subject(
    "physics_sl",
    "Physics SL"
)

physics_hl = Subject(
    "physics_hl",
    "Physics HL"
)

chemistry_sl = Subject(
    "chemistry_sl",
    "Chemistry SL",
    [
      "CH1 - Stoichiometric Relationship",
      "CH2 - Atomic Structure",
      "CH3 - Periodicity",
      "CH4 - Chemical Bonding &Structure",
      "CH5 - Energetics/Thermochemistry",
      "CH6 - Chemical Kinetics",
      "CH7 - Equilibrium",
      "CH8 - Acids & Bases",
      "CH9 - Redox Processes",
      "CH10 - Organic Chemistry",
      "CH11 - Measurement & Data processing"
    ]
)

chemistry_hl = Subject(
    "chemistry_hl",
    "Chemistry HL",
    [
      "CH1 - Stoichiometric Relationship",
      "CH2 - Atomic Structure",
      "CH3 - Periodicity",
      "CH4 - Chemical Bonding &Structure",
      "CH5 - Energetics/Thermochemistry",
      "CH6 - Chemical Kinetics",
      "CH7 - Equilibrium",
      "CH8 - Acids & Bases",
      "CH9 - Redox Processes",
      "CH10 - Organic Chemistry",
      "CH11 - Measurement & Data processing",
      "CH12 - Atomic Structure",
      "CH12 - The Periodic Table",
      "CH13 - Chemical Bonding& Structure",
      "CH15 - Energetics/Thermochemistry",
      "CH16 - Chemical Kinetics",
      "CH17 - Equilibrium",
      "CH18 - Acids& Bases",
      "CH19 - Redox Processes",
      "CH20 - Organic Chemistry",
      "CH21 - Measurement & Analysis "
    ]
)

biology_sl = Subject(
    "biology_sl",
    "Biology SL",
    [
      "CH1 - Cell Biology",
      "CH2 - Molecular Biology",
      "CH3 - Genetic",
      "CH4 - Ecology",
      "CH5 - Evolution & Biodiversity",
      "CH6 - Human Physiology"
    ]
)

biology_hl = Subject(
    "biology_hl",
    "Biology HL",
    [
      "CH1 - Cell Biology",
      "CH2 - Molecular Biology",
      "CH3 - Genetic",
      "CH4 - Ecology",
      "CH5 - Evolution & Biodiversity",
      "CH6 - Human Physiology",
      "CH7 - Nucleic Acids",
      "CH8 - Metabolism, Cell & Respiration &Photosynthesis",
      "CH9 - Plant Biology",
      "CH10 - Genetics & Evolution",
      "CH11 - Animal Physiology"
      ]
)

sehs_sl = Subject(
    "sehs_sl",
    "SEHS SL"
)

sehs_hl = Subject(
    "sehs_hl",
    "SEHS HL"
)

math_sl = Subject(
    "math_sl",
    "Math SL"
)

math_hl = Subject(
    "math_hl",
    "Math HL"
)

visual_art_sl = Subject(
    "visual_art_sl",
    "Visual Art SL"
)

visual_art_hl = Subject(
    "visual_art_hl",
    "Visual Art HL"
)

music_sl = Subject(
    "music_sl",
    "Music SL"
)

music_hl = Subject(
    "music_hl",
    "Music HL"
)

ess_sl = Subject(
    "ess_sl",
    "ESS SL"
)
cs_sl = Subject(
    "cs_sl",
    "Computer Science SL"
)

cs_hl = Subject(
    "cs_hl",
    "Computer Science HL"
)

subject_dict = {
    "english_a_sl": english_a_sl,
    "english_a_hl": english_a_hl,
    "chinese_a_sl": chinese_a_sl,
    "chinese_a_hl": chinese_a_hl,
    "french_ab": french_ab,
    "german_ab": german_ab,
    "english_b_hl": english_b_hl,
    "chinese_b_hl": chinese_b_hl,
    "history_sl": history_sl,
    "history_hl": history_hl,
    "business_sl": business_sl,
    "business_hl": business_hl,
    "economic_sl": economic_sl,
    "economic_hl": economic_hl,
    "psychology_sl": psychology_sl,
    "physics_sl": physics_sl,
    "physics_hl": physics_hl,
    "chemistry_sl": chemistry_sl,
    "chemistry_hl": chemistry_hl,
    "biology_sl": biology_sl,
    "biology_hl": biology_hl,
    "sehs_sl": sehs_sl,
    "sehs_hl": sehs_hl,
    "math_sl": math_sl,
    "math_hl": math_hl,
    "visual_art_sl": visual_art_sl,
    "visual_art_hl": visual_art_hl,
    "music_sl": music_sl,
    "music_hl": music_hl,
    "ess_sl": ess_sl,
    "cs_sl": cs_sl,
    "cs_hl": cs_hl
}
