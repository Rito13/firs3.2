from economy import Economy
economy = Economy(id = "LESSER_POLAND",
	numeric_id = 1,
	# as of May 2015 the following cargos must have fixed positions if used by an economy:
	# passengers: 0, mail: 2, goods 5, food 11
	# keep the rest of the cargos alphabetised
	# bump the min. compatible version if this list changes
	cargos = [
		'passengers',
		'alcohol',
		'mail',
		'bauxite',
		'building_materials',
		'goods',
		'canola',
		'chemicals',
		'clay',
		'coal',
		'engineering_supplies',
		'food',
		'farm_supplies',
		'fish',
		'fruits',
		'grain',
		'iron_ore',
		'livestock',
		'timber',
		'packaging',
		'metal',
		'milk',
		'oil',
		'petrol',
		'plant_fibres',
		'recyclables',
		'salt',
		'sand',
		'scrap_metal',
		'stone',
		'sugar_beet',
		'sulphur',
		'logs',
		'wool',
		'zinc',
		'soda_ash',
	],
	cargoflow_graph_tuning={
        # also any industries with !!!!??????? will be automatically added to wormhole_industries
        "wormhole_industries": [
        ],
        "cargos_with_individual_produce_nodes": [
        ],
        "cargos_with_individual_accept_nodes": [
        ],
        "group_edges_subgraphs": [
        ],
        "ranking_subgraphs": [
        	("sink", ["port"]),
        ],
        "clusters": [
            {
                "nodes": ["iron_ore", "coal", "scrap_metal"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["sand", "grain"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["dredging_site", "clay_pit", "quarry","coal_mine", "oil", "salt"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["junk_yard", "iron_ore_mine","forest"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["brick_works", "cement_plant", "lime_kiln"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["blast_furnace", "iron_works", "aluminium_plant", "bauxite"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["dairy", "fishing_harbour", "sugar_refinery", "stockyard","goods","building_materials","alcohol"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["dairy_farm", "fishing_grounds", "fruit_plantation"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["metal_workshop", "furniture_factory", "packaging"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["textile_mill", "plastics_plant"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["sawmill", "paper_mill"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["sheep_farm", "mixed_farm"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["ammonia_plant", "smithy_forge", "machine_shop"],
                "rank": "same",
                "color": "white",
            },
            {
            	"nodes": ["chemicals", "petrol", "logs", "power_plant", "flour_mill", "food"],
                "rank": "same",
                "color": "white",
            },
        ],
    },
)

# some deliberate overlapping of biomes for mixing at boundaries
# in order to remove this change some industries
economy.add_biome(
    "more_west",
    min_x_percent=0,
    max_x_percent=100,
    min_y_percent=0,
    max_y_percent=60,
)
economy.add_biome(
    "less_west",
    min_x_percent=0,
    max_x_percent=100,
    min_y_percent=40,
    max_y_percent=100,
)
