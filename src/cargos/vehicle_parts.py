from cargo import Cargo

cargo = Cargo(
    id="vehicle_parts",
    type_name="string(STR_CARGO_NAME_VEHICLE_PARTS)",
    unit_name="string(STR_CARGO_NAME_VEHICLE_PARTS)",
    type_abbreviation="string(STR_CID_VEHICLE_PARTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_FOOD_GRADE"],
    cargo_label="VPTS",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_VEHICLE_PARTS)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=151,
    capacity_multiplier="1",
    icon_indices=(14, 2),
    sprites_complete=True,
)
