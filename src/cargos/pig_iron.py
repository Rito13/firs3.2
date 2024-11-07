from cargo import Cargo

# pig iron, although the label implies it could be more generic iron
cargo = Cargo(
    id="pig_iron",
    type_name="string(STR_CARGO_NAME_PIG_IRON)",
    unit_name="string(STR_CARGO_NAME_PIG_IRON)",
    type_abbreviation="string(STR_CID_PIG_IRON)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="IRON",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PIG_IRON)",
    penalty_lowerbound="8",
    single_penalty_length="64",
    capacity_multiplier="1",
    price_factor=119,
    icon_indices=(4, 3),
    sprites_complete=True,
)
