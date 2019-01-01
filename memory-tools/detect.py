import linecache
import tracemalloc


def display_top(snapshot, group_by='lineno', limit=10):
    snapshot = snapshot.filter_trace((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>")
    ))

    top_stats = snapshot.statistics(group_by)
    print("Top %s line" % limit)
    for idx, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s %.1f KiB" % (idx, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print("      %s" % line)

        other = top_stats[limit:]
        if other:
            size = sum(stat.size for stat in other)
            print("%s ohter: %.1f KiB" % (len(other), size / 1024))
        total = sum(stat.size for stat in top_stats)
        print("Total allocated size: %.1f KiB" % (total / 1024))
