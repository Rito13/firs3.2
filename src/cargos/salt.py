from cargo import Cargo

cargo = Cargo(
    id="salt",
    type_name="string(STR_CARGO_NAME_SALT)",
    unit_name="string(STR_CARGO_NAME_SALT)",
    type_abbreviation="string(STR_CID_SALT)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_BULK"],
    cargo_label="SALT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SALT)",
    penalty_lowerbound="36",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=94,
    icon_indices=(3, 4),
    sprites_complete=True,
)
