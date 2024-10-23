from cargo import Cargo

# generic common grey metal: steel, aluminium etc
cargo = Cargo(
    id="metal",
    type_name="string(STR_CARGO_NAME_METAL)",
    unit_name="string(STR_CARGO_NAME_METAL)",
    type_abbreviation="string(STR_CID_METAL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_FOOD_GRADE"],
    cargo_label="METL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_METAL)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=135,
    icon_indices=(1, 4),
    sprites_complete=False,
)
