timing = """
intro 2:30
me 1:20
plugins-trust] 2:00
cost-stack] 3:30
llm implementation-small) 2:00
small things 7:00
"""


def calculate():
    total_seconds = 0
    for line in timing.strip().splitlines():
        parts = line.strip().split()
        if not parts:
            continue
        time_str = parts[-1]
        mins, secs = time_str.split(":")
        total_seconds += int(mins) * 60 + int(secs)

    minutes = total_seconds // 60
    seconds = total_seconds % 60
    print(f"Total: {minutes}:{seconds:02d}")


if __name__ == "__main__":
    calculate()
