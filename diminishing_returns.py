import random
from collections import defaultdict
from rich.console import Console
from rich.table import Table

console = Console()

chance_of_success = [
    0.5, 0.55, 0.55*1.1
]

task_count = 10
runs = 1

console.print(f"\n[bold]Number of tasks: {task_count}, averaged over {runs} runs[/bold]\n")
for chance in chance_of_success:
    avg_lengths = defaultdict(float)

    for _ in range(runs):
        success = int(chance * task_count)
        tasks = ['1'] * success + ['0'] * (task_count - success)
        random.shuffle(tasks)
        tasks = ''.join(tasks)

        chains = tasks.split('0')
        chains = [c for c in chains if len(c) > 0]

        lengths = {}
        for c in chains:
            lengths[len(c)] = lengths.get(len(c), 0) + 1

        for length, count in lengths.items():
            avg_lengths[length] += count

    for length in avg_lengths:
        avg_lengths[length] /= runs

    console.print(f"[bold cyan]Chance of success: {int(chance * 100)}%[/bold cyan]")

    table = Table(show_header=True, header_style="bold magenta", padding=(0, 1))
    table.add_column("Chain Length", justify="center")
    table.add_column("Avg Count", justify="center")
    table.add_column("Visual", justify="left")
    for length, count in sorted(avg_lengths.items()):
        if round(count) < 1:
            continue
        table.add_row(
            str(length),
            f"{count:.1f}",
            "●" * int(round(count)),
        )
    console.print(table)

    total_chains = sum(avg_lengths.values())
    weighted_sum = sum(length * count for length, count in avg_lengths.items())
    avg_chain = weighted_sum / total_chains if total_chains else 0
    console.print(f"  Average chain length: [bold green]{avg_chain:.2f}[/bold green]")
    console.print()
