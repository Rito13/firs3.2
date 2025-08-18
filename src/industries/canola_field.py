from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
	id='canola_field',
	prod_cargo_types_with_multipliers=[('CAOA',20)],
	prob_in_game='4',
	prob_random='11',
	map_colour='55',
	location_checks=dict(cluster=[72, 4]),
	prospect_chance='0.75',
	name='string(STR_IND_CANOLA_FIELD)',
	nearby_station_name='string(STR_STATION_CANOLA_FIELD)',
	fund_cost_multiplier='45',
	sprites_complete=False,
	primary_production_random_factor_set="medium_range",
	colour_scheme_name="scheme_1_elton", # It is an random choice, needs testing
)

industry.enable_in_economy(
    "LESSER_POLAND",
)

industry.add_tile(id='canola_field_tile_1',
                  location_checks=TileLocationChecks(disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='empty'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 52, -31, -21)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 52, -31, -21)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 52, -31, -21)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 52, -31, -21)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 52, -31, -21)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 52, -31, -21)],
)

industry.add_spritelayout(
    id='canola_field_spritelayout_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='canola_field_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='canola_field_spritelayout_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='canola_field_spritelayout_4',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='canola_field_spritelayout_5',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='canola_field_spritelayout_6',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    terrain_aware_ground=True
)

industry.add_industry_layout(
    id='canola_field_industry_layout_1',
    layout=[(0, 0, 'canola_field_tile_1', 'canola_field_spritelayout_6'),
	    (0, 1, 'canola_field_tile_1', 'canola_field_spritelayout_6'),
	    (0, 2, 'canola_field_tile_1', 'canola_field_spritelayout_6'),
            (1, 0, 'canola_field_tile_1', 'canola_field_spritelayout_3'),
	    (1, 1, 'canola_field_tile_1', 'canola_field_spritelayout_4'),
            (1, 2, 'canola_field_tile_1', 'canola_field_spritelayout_5'),
            (2, 0, 'canola_field_tile_1', 'canola_field_spritelayout_6'),
            (2, 1, 'canola_field_tile_1', 'canola_field_spritelayout_6'),
	    (2, 2, 'canola_field_tile_1', 'canola_field_spritelayout_6'),
            (3, 0, 'canola_field_tile_1', 'canola_field_spritelayout_3'),
	    (3, 1, 'canola_field_tile_1', 'canola_field_spritelayout_4'),
	    (3, 2, 'canola_field_tile_1', 'canola_field_spritelayout_5'),
	    (4, 1, 'canola_field_tile_1', 'canola_field_spritelayout_2'),
	    ]
)
