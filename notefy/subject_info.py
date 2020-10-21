class Subject():
    def __init__(self, name: str, display_text: str, topics: list = None):
        self.name = name
        self.display_text = display_text
        self.topics = topics


english_a_sl = Subject(
    "english_a_sl",
    "English A SL",
    [
        "Paper 1",
        "IO"
    ]
)

english_a_hl = Subject(
    "english_a_hl",
    "English A HL",
    [
        "Paper 1",
        "IO"
    ]
)

chinese_a_sl = Subject(
    "chinese_a_sl",
    "Chinese A SL",
    [
        "Paper 1",
        "IO"
    ]
)

chinese_a_hl = Subject(
    "chinese_a_hl",
    "Chinese A HL",
    [
        "Paper 1",
        "IO"
    ]
)

french_ab = Subject(
    "french_ab",
    "French ab initio",
    [
        "Paper 2",
        "IO"
    ]
)

german_ab = Subject(
    "german_ab",
    "German ab initio",
    [
        "Paper 2",
        "IO"
    ]
)

english_b_hl = Subject(
    "english_b_hl",
    "English B HL",
    [
        "Paper 1",
        "Paper 2"
    ]
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
    "Business SL",
    [
        "CH1 - Business organization and environment",
        "CH2 - Human resource management",
        "CH3 - Finance and accounts",
        "CH4 - Marketing",
        "CH5 - Operations Management"
    ]
)

business_hl = Subject(
    "business_hl",
    "Business HL",
    [
        "CH1 - Business organization and environment",
        "CH2 - Human resource management",
        "CH3 - Finance and accounts",
        "CH4 - Marketing",
        "CH5 - Operations Management"
    ]
)

economic_sl = Subject(
    "economic_sl",
    "Economic SL",
    [
        "CH1 - Microeconomics",
        "CH2 - Macroeconomics",
        "CH3 - International Economics",
        "CH4 - Development Economics"
    ]
)

economic_hl = Subject(
    "economic_hl",
    "Economic HL",
    [
        "CH1 - Microeconomics",
        "CH2 - Macroeconomics",
        "CH3 - International Economics",
        "CH4 - Development Economics"
    ]
)

psychology_sl = Subject(
    "psychology_sl",
    "Psychology SL",
    [
        "CH1 - Biological approach to understanding behavior",
        "CH2 - Cognitive approach to understanding behavior",
        "CH3 - Sociocultural approach to understanding behavior"
    ]
)

physics_sl = Subject(
    "physics_sl",
    "Physics SL",
    [
        "CH1 - Measurements and Uncertainties",
        "CH2 - Mechanics",
        "CH3 - Thermal Physics",
        "CH4 - Waves",
        "CH5 - Electricity and Magnetism",
        "CH6 - Circular Motion and Gravitation",
        "CH7 - Atomic, Nuclear and Particle Physics",
        "CH8 - Energy Production",
    ]
)

physics_hl = Subject(
    "physics_hl",
    "Physics HL",
    [
        "CH1 - Measurements and Uncertainties",
        "CH2 - Mechanics",
        "CH3 - Thermal Physics",
        "CH4 - Waves",
        "CH5 - Electricity and Magnetism",
        "CH6 - Circular Motion and Gravitation",
        "CH7 - Atomic, Nuclear and Particle Physics",
        "CH8 - Energy Production",
        "CH9 - Wave Phenomena",
        "CH10 - Fields",
        "CH11 - Electromagnetic",
        "CH12 - Quantum and Nuclear Physics"

    ]
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
        "CH21 - Measurement & Analysis"
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
    "SEHS SL",
    [
        "CH1 - Anatomy",
        "CH2 - Exercise physiology",
        "CH3 - Energy systems",
        "CH4 - Movement analysis",
        "CH5 - Skill in sports",
        "CH6 - Measurement and evaluation of human performance"
    ]
)

sehs_hl = Subject(
    "sehs_hl",
    "SEHS HL",
    [
        "CH1 - Anatomy",
        "CH2 - Exercise physiology",
        "CH3 - Energy systems",
        "CH4 - Movement analysis",
        "CH5 - Skill in sports",
        "CH6 - Measurement and evaluation of human performance",
        "CH7 - Further anatomy",
        "CH8 - The endocrine system",
        "CH9 - Fatigue",
        "CH10 - Friction and drag",
        "CH11 - Skill acquisition and analysis",
        "CH12 - Genetics and athletic performance",
        "CH13 - Exercise and immunity "
    ]
)

math_sl = Subject(
    "math_sl",
    "Math SL",
    [
        "CH1 - Quadratics",
        "CH2 - Functions",
        "CH3 - Exponentials",
        "CH4 - Logarithms",
        "CH5 - Transforming Functions",
        "CH6 - Sequences and Series",
        "CH7 - The Binomial Expansion",
        "CH8 - The Unit Circle and Radian Measure",
        "CH9 - Non-Right angled triangle trigonometry",
        "CH10 - Trigonometric Functions",
        "CH11 - Trigonometric equations and identities",
        "CH12 - Vectors",
        "CH13 - Vector Applications",
        "CH14 - Introduction to Differential Calculus",
        "CH15 - Rules of Differentiation",
        "CH16 - Properties of Curves",
        "CH17 - Applications of Differential Calculus",
        "CH18 - Integration",
        "CH19 - Application of Integration",
        "CH20 - Descriptive Statistics",
        "CH21 - Linear Modelling",
        "CH22 - Probability",
        "CH23 - Discrete Random Variables",
        "CH24 - The Normal Distribution",
        "CH25 - Miscellaneous Questions"
    ]
)

math_hl = Subject(
    "math_hl",
    "Math HL",
    [
        "CH1 - Quadratics",
        "CH2 - Functions",
        "CH3 - Exponentials",
        "CH4 - Logarithms",
        "CH5 - Transforming Functions",
        "CH6 - Complex Numbers and Polynomials",
        "CH7 - Sequences and Series",
        "CH8 - Counting and the Binomial Expansion",
        "CH9 - Mathematical Induction",
        "CH10 - The Unit Circle and Radian Measure",
        "CH11 - Non-Right Angled Triangle Trigonometry",
        "CH12 - Trigonometric Functions",
        "CH13 - Trigonometric Equations and Identities",
        "CH14 - Vectors",
        "CH15 - Vector Applications",
        "CH16 - Complex Numbers",
        "CH17 - Introduction to Differential Calculus",
        "CH18 - Rules of Differentiation",
        "CH19 - Properties of Curves",
        "CH20 - Applications of Differential Calculus",
        "CH21 - Integration",
        "CH22 - Applications of Integration",
        "CH23 - Descriptive Statistics",
        "CH24 - Probability",
        "CH25 - Discrete Random Variables",
        "CH26 - Continuous Random Variables",
        "CH27 - Miscellaneous Questions"
    ]
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
    "ESS SL",
    [
        "CH1 - Systems and Models",
        "CH2 - The Ecosystem",
        "CH3 - Human Population, Carrying Capacity and Resource Use",
        "CH4 - Conservation and Biodiversity",
        "CH5 - Pollution Management",
        "CH6 - The issue of Global Warming",
        "CH7 - Environmental Value Systems"
    ]
)
cs_sl = Subject(
    "cs_sl",
    "Computer Science SL",
    [
        "CH1 - System fundamentals",
        "CH2 - Computer organization",
        "CH3 - Networks",
        "CH4 - Computational thinking, problem-solving and programming"
    ]
)

cs_hl = Subject(
    "cs_hl",
    "Computer Science HL",
    [
        "CH1 - System fundamentals",
        "CH2 - Computer organization",
        "CH3 - Networks",
        "CH4 - Computational thinking, problem-solving and programming",
        "CH5 - Abstract data structures",
        "CH6 - Resource management",
        "CH7 - Control"
    ]
)

geo_sl = Subject(
    "geo_sl",
    "Geography SL",
    [
        "CH1 - Changing population",
        "CH2 - Global climate-vulnerability and resilience",
        "CH3 - Global resource consumption and security"
    ]
)

geo_hl = Subject(
    "geo_hl",
    "Geography HL",
    [
        "CH1 - Changing population",
        "CH2 - Global climate-vulnerability and resilience",
        "CH3 - Global resource consumption and security",
        "CH4 - Power, places and networks",
        "CH5 - Human development and Diversity",
        "CH6 - Global risks and resilience"
    ]
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
    "cs_hl": cs_hl,
    "geo_sl": geo_sl,
    "geo_hl": geo_hl
}
