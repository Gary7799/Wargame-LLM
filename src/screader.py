import os

import sc2reader
from sc2reader.events import (
    UnitDoneEvent,
    UnitBornEvent,
    UnitDiedEvent,
    UnitInitEvent,
    UnitTypeChangeEvent,
    UpgradeCompleteEvent,
    TargetUnitCommandEvent,
    TrackerEvent,
    TargetPointCommandEvent,
    BasicCommandEvent,
    UpdateTargetUnitCommandEvent,
    UpdateTargetPointCommandEvent,
)

replay = sc2reader.load_replay(
    "../data/replay/1.SC2Replay",
    load_level=4,
)

print("Player 1 - " + replay.player[1].name)
print("Player 2 - " + replay.player[2].name)


def correctTime(e):
    arr = e._str_prefix()
    x = str(arr)
    a = x.split(".")
    a[1] = a[1][:2]
    time = (int(a[0]) * 60 * 16 + int(a[1]) * 16) / 22.4
    res = "{:02d}:{:02d}".format(int(time // 60), int(time % 60))
    return res


def get_event(replay):
    for event in replay.events:
        event_names = set([event.name for event in replay.events])
    events_of_type = {name: [] for name in event_names}
    for event in replay.events:
        events_of_type[event.name].append(event)
    return events_of_type


def output_event(e):
    if isinstance(e, TrackerEvent):
        return correctTime(e) + "\t" + str(e).replace(e._str_prefix(), "")
    else:
        return correctTime(e) + str(e).replace(e._str_prefix().split("\t")[0], "")


# events = get_event(replay)
# events_list = list(events.keys())
# print(events_list)
print(replay.winner.players)


# UnitDoneEvent
unit_done_events = [
    event for event in replay.events if isinstance(event, UnitDoneEvent)
]
for e in unit_done_events:
    print(output_event(e))

# UnitBornEvent
unit_born_events = [
    event for event in replay.events if isinstance(event, UnitBornEvent)
]
for e in unit_born_events:
    if e.unit_upkeeper is not None and e.second != 0:
        print(output_event(e))

# UnitDiedEvent
unit_died_events = [
    event for event in replay.events if isinstance(event, UnitDiedEvent)
]
for e in unit_died_events:
    if e.unit.owner is not None:
        print(output_event(e))

# UnitInitEvent
unit_init_events = [
    event for event in replay.events if isinstance(event, UnitInitEvent)
]
for e in unit_init_events:
    print(output_event(e))
#
# UnitTypeChangeEvent
unit_type_change_events = [
    event for event in replay.events if isinstance(event, UnitTypeChangeEvent)
]
for e in unit_type_change_events:
    print(output_event(e))

# UpgradeCompleteEvent
upgrade_complete_events = [
    event for event in replay.events if isinstance(event, UpgradeCompleteEvent)
]
for e in upgrade_complete_events:
    if e.second != 0:
        print(output_event(e))


###########################################################

# # TargetUnitCommandEvent
# target_unit_command_events = [
#     event for event in replay.events if isinstance(event, TargetUnitCommandEvent)
# ]
# for e in target_unit_command_events:
#     print(output_event(e))
#
# # TargetPointCommandEvent
# target_point_command_events = [
#     event for event in replay.events if isinstance(event, TargetPointCommandEvent)
# ]
# for e in target_point_command_events:
#     print(output_event(e))
#
#
# # BasicCommandEvent
# basic_command_events = [
#     event for event in replay.events if isinstance(event, BasicCommandEvent)
# ]
# for e in basic_command_events:
#     print(output_event(e))
#
#
# # UpdateTargetUnitCommandEvent
# update_target_unit_command_events = [
#     event for event in replay.events if isinstance(event, UpdateTargetUnitCommandEvent)
# ]
# for e in update_target_unit_command_events:
#     print(output_event(e))
#
# # UpdateTargetPointCommandEvent
# update_target_point_command_events = [
#     event for event in replay.events if isinstance(event, UpdateTargetPointCommandEvent)
# ]
# for e in update_target_point_command_events:
#     print(output_event(e))


# # SelectionEvent
# selection_events = events["SelectionEvent"]
# for e in selection_events:
#     print(e)

# # UnitPositionsEvent
# unit_position_events = events["UnitPositionsEvent"]
# for e in unit_position_events:
#     print(e.positions)

# # PlayerStatsEvent
# player_stats_events = events["PlayerStatsEvent"]
# for e in player_stats_events:
#     print(e.positions)

#
# with open("1.txt", "wt") as f:
#     for event_type in events_list:
#         event = events[event_type]
#         print(event_type, file=f)
#         for e in event:
#             # correctTime(e)
#             print(e, file=f)
