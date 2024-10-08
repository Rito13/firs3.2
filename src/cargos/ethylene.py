from cargo import Cargo

cargo = Cargo(
    id="ethylene",
    type_name="string(STR_CARGO_NAME_ETHYLENE)",
    unit_name="string(STR_CARGO_NAME_ETHYLENE)",
    type_abbreviation="string(STR_CID_ETHYLENE)",
    sprite="NEW_CARGO_SPRITE",
    weight="2.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID)",
    cargo_label="C2H4",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_ETHYLENE)",
    penalty_lowerbound="20",
    single_penalty_length="40",
    price_factor=157,
    capacity_multiplier="1",
    icon_indices=(2, 4),
    sprites_complete=False,
)
