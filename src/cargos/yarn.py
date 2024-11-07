from cargo import Cargo

cargo = Cargo(
    id="yarn",
    type_name="string(STR_CARGO_NAME_YARN)",
    unit_name="string(STR_CARGO_NAME_YARN)",
    type_abbreviation="string(STR_CID_YARN)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.2",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="YARN",
    units_of_cargo="TTD_STR_ITEMS",
    items_of_cargo="string(STR_CARGO_UNIT_YARN)",
    penalty_lowerbound="8",
    single_penalty_length="90",
    price_factor=98,
    capacity_multiplier="1",
    icon_indices=(4, 1),
    sprites_complete=False,
)
