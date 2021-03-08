from flask import Flask, jsonify

app = Flask(__name__)

def create_tree():
    tree = {
        "USA": ["CAN", "MEX"],
        "MEX": ["BLZ", "GTM"],
        "GTM": ["SLV", "HND"],
        "HND": ["NIC", None],
        "NIC": ["CRI", None],
        "CRI": ["PAN", None],
        "PAN": [None, None],
        "SLV": [None, None],
        "BLZ": [None, None],
        "CAN": [None, None]
    }

    return tree


def binarySearch(root, node):
    final_path = []
    current = node
    while current != "USA":
        for parent, child in root.items():
            if current in child:
                final_path.insert(0, current)
                current = parent
    final_path.insert(0, "USA")
    return final_path

@app.route('/<string:arg>')
def hello_world(arg: str):
    tree = create_tree()
    route = binarySearch(tree, arg.upper())
    return jsonify(
        destination=arg.upper(),
        list=route
    ), 200


if __name__ == '__main__':
    app.run()
