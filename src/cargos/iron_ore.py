from cargo import Cargo

cargo = Cargo(
    id="iron_ore",
    type_name="TTD_STR_CARGO_PLURAL_IRON_ORE",
    unit_name="TTD_STR_CARGO_SINGULAR_IRON_ORE",
    type_abbreviation="TTD_STR_ABBREV_IRON_ORE",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_BULK"],
    cargo_label="IORE",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_IRON_ORE",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=90,
    capacity_multiplier="1",
    icon_indices=(9, 0),
    sprites_complete=True,
)
