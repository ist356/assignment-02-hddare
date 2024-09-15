'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    sections = packaging_data.split(' / ')
    result_dict = {}
    
    for section in sections:
        parts = section.split(' in ')
        quantity_item = parts[0].split()
        quantity = int(quantity_item[0])
        item = ' '.join(quantity_item[1:])
        result_dict[item] = quantity
        container_parts = parts[1].split()
        container_quantity = int(container_parts[0])
        container_item = ' '.join(container_parts[1:])
        if container_quantity == 1:
            result_dict[container_item] = container_quantity
        else:
            plural_container_item = container_item + 's' if not container_item.endswith('s') else container_item
            result_dict[plural_container_item] = container_quantity
    keys = list(result_dict.keys())
    for key in keys:
        if key.endswith('s'):
            singular_key = key[:-1]
            if singular_key in result_dict:
                del result_dict[singular_key]
    result = [{key: value} for key, value in result_dict.items()]
    
    return result


def calc_total_units(package: list[dict]) -> int:
    total_items = 1
    for item_dict in package:
        for quantity in item_dict.values():
            total_items *= quantity
    
    return total_items


def get_unit(package: list[dict]) -> str:
    if not package:
        return None
    
    first_item = package[0]
    return list(first_item.keys())[0]

# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")