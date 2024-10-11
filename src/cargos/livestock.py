from cargo import Cargo

cargo = Cargo(
    id="livestock",
    type_name="TTD_STR_CARGO_PLURAL_LIVESTOCK",
    unit_name="TTD_STR_CARGO_SINGULAR_LIVESTOCK",
    type_abbreviation="TTD_STR_ABBREV_LIVESTOCK",
    sprite="NEW_CARGO_SPRITE",
    weight="0.1875",  # average weight of a shetland pony apparently (and no we don't eat ponies, but eh)
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS"],
    cargo_label="LVST",
    units_of_cargo="TTD_STR_ITEMS",
    items_of_cargo="TTD_STR_QUANTITY_LIVESTOCK",
    penalty_lowerbound="0",
    single_penalty_length="15",
    price_factor=122,
    capacity_multiplier="1",
    icon_indices=(4, 0),
    sprites_complete=True,
)
