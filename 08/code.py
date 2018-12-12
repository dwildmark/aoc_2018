
def parse_input_to_list():
    with open("input.txt", "r") as file:
        strn = file.read()
        input_list = [int(i) for i in strn.split(" ")]
        return input_list


def process_node(node_desc_list):
    num_children = node_desc_list.pop(0)
    num_metadata = node_desc_list.pop(0)

    node = {
        "children": [],
        "metadata": []
    }
    for child in range(num_children):
        node["children"].append(process_node(node_desc_list))

    for data in range(num_metadata):
        node["metadata"].append(node_desc_list.pop(0))

    return node

def get_metadata_sum(node):
    sum = 0
    for child in node["children"]:
        sum += get_metadata_sum(child)

    for metadata in node["metadata"]:
        sum += metadata

    return sum

def part_one():
    node_descriptors = parse_input_to_list()
    tree = process_node(node_descriptors)

    print get_metadata_sum(tree)



part_one()
