from cargo import Cargo

cargo = Cargo(
    id="textiles",
    type_name="string(STR_CARGO_NAME_TEXTILES)",
    unit_name="string(STR_CARGO_NAME_TEXTILES)",
    type_abbreviation="string(STR_CID_TEXTILES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_FOOD_GRADE"],
    cargo_label="TEXT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_TEXTILES)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=151,
    capacity_multiplier="1",
    icon_indices=(14, 2),
    sprites_complete=False,
)
