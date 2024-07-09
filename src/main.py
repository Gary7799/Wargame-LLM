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


directory_path = " \\TVZ - Reaper Expand"
for root, dirs, files in os.walk(directory_path):
    for file in files:
        # 检查文件扩展名是否为.sc
        if file.endswith('.SC2Replay'):
            # 获取文件的完整路径
            full_path = os.path.join(root, file)
            dir_name, file_name = os.path.split(full_path)
            new_file_name = os.path.splitext(file_name)[0] + '.txt'
            # 构造新的文件路径
            new_full_path = os.path.join(dir_name, new_file_name)

            # 对文件进行操作
            replay = sc2reader.load_replay(
                full_path,
                load_level=4,
            )
            with open(new_full_path, 'w') as f:
                unit_done_events = [
                    event for event in replay.events if isinstance(event, UnitDoneEvent)
                ]
                for e in unit_done_events:
                    print(output_event(e), file=f)

                unit_born_events = [
                    event for event in replay.events if isinstance(event, UnitBornEvent)
                ]
                for e in unit_born_events:
                    if e.unit_upkeeper is not None and e.second != 0:
                        print(output_event(e), file=f)

                unit_died_events = [
                    event for event in replay.events if isinstance(event, UnitDiedEvent)
                ]
                for e in unit_died_events:
                    if e.unit.owner is not None:
                        print(output_event(e), file=f)

                unit_init_events = [
                    event for event in replay.events if isinstance(event, UnitInitEvent)
                ]
                for e in unit_init_events:
                    print(output_event(e), file=f)

                unit_type_change_events = [
                    event for event in replay.events if isinstance(event, UnitTypeChangeEvent)
                ]
                for e in unit_type_change_events:
                    print(output_event(e), file=f)

                upgrade_complete_events = [
                    event for event in replay.events if isinstance(event, UpgradeCompleteEvent)
                ]
                for e in upgrade_complete_events:
                    if e.second != 0:
                        print(output_event(e), file=f)

                winner = str(replay.winner.players) + " is the winner."
                print(winner, file=f)
