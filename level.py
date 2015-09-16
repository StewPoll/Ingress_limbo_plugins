"""!level <number>: Returns the requirements to reach the given level.
Gives the AP and Badge requirements for the level the user requests.
Usage:
    !level <number>
Result:
    Requirements for level <number>:
    AP Requirements: <value>
    Badge Requirements
"""

import re

levels = {
    1: {"ap": 0},
    2: {"ap": 2500},
    3: {"ap": 20000},
    4: {"ap": 70000},
    5: {"ap": 150000},
    6: {"ap": 300000},
    7: {"ap": 600000},
    8: {"ap": 1200000},
    9: {
        "ap": 2400000,
        "badges": {
            "silver": 4,
            "gold": 1
        }
    },
    10: {
        "ap": 4000000,
        "badges": {
            "silver": 5,
            "gold": 2
        }
    },
    11: {
        "ap": 6000000,
        "badges": {
            "silver": 6,
            "gold": 4
        }
    },
    12: {
        "ap": 8400000,
        "badges": {
            "silver": 7,
            "gold": 6
        }
    },
    13: {
        "ap": 12000000,
        "badges": {
            "gold": 7,
            "platinum": 1
        }
    },
    14: {
        "ap": 17000000,
        "badges": {
            "platinum": 2
        }
    },
    15: {
        "ap": 24000000,
        "badges": {
            "platinum": 3
        }
    },
    16: {
        "ap": 40000000,
        "badges": {
            "platinum": 4,
            "black": 2
        }
    }
}

def get_text(level):
    global levels
    ap_text = "AP Required: {}".format(levels[level]["ap"])
    try:
        badge_text = "Badges Required: "
        for badge in levels[level]['badges']:
            badge_text += "{} x :badge_{}:, ".format(levels[level]['badges'][badge], badge)
        badge_text = badge_text[:-2]
    except KeyError:
        badge_text = "No Badges required for level {}".format(level)
    return "Requirements for level {}:\n{}\n{}".format(level, ap_text, badge_text)


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!level (.*)", str(text))
    if match:
        try:
            level = int(match[0])
            if level > 16 or level < 1:
                return "Please enter a valid level. (1 <-> 16)"
            else:
                return get_text(level)
        except ValueError:
            return "Please enter a valid number for the level"
    else:
        return
