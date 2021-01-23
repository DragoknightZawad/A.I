import math
root = {"status": "min",
        "value": "",
        "childs": [
                {
                "status": "max",
                "value": "",
                "childs": [
                    {"value": 5, "childs": []},
                    {"value": 3, "childs": []},
                    {"value": 9, "childs": []}
                    ]
                },
                {
                "status": "max",
                "value": "",
                "childs": [
                     {"value": 2, "childs": []},
                     {"value": 8, "childs": []},               
                    ]
                }
            ]
        }
def Max_Value(state):
    if len(state["childs"]) == 0:
        return state["value"]
    v = -(math.inf)
    for c in state["childs"]:
        v = max(v, Min_Value(c))
    state["value"] = v
    return v
    
def Min_Value(state):
    if len(state["childs"]) == 0:
        return state["value"] 
    v = (math.inf)
    
    for c in state["childs"]:
        v = min(v, Max_Value(c))
    state["value"] = v
    return v
if root["status"] == "min":
    Min_Value(root)
print(root["value"])
