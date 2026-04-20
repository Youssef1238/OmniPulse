import json

def Compare(target,id)->bool:
    with open('state.json','r') as f:
        data = json.load(f)
    for state in data["states"]:
        if state["target"] == target and state["last_seen"] != id:
            state["last_seen"] = id
            with open('state.json','w') as f:
                json.dump(data,f)
            return True
    return False
    




