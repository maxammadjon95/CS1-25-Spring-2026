from collections import defaultdict

def read_log(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

def parse_lines(lines):
    for line in lines:
        try:
            timestamp, level, message = line.split(" | ")
            yield timestamp, level, message
        except ValueError:
            continue


def filter_levels(records):
    for timestamp, level, message in records:
        if level in ("ERROR", "WARNING"):
            yield timestamp, level, message


def extract_hour(records):
    for timestamp, level, message in records:
        hour = timestamp.split(" ")[1].split(":")[0]
        yield hour, level


def count_by_hour(records):
    result = defaultdict(lambda: {"ERROR": 0, "WARNING": 0})
    for hour, level in records:
        result[hour][level] += 1
    return result


def sort_result(result):
    return sorted(
        result.items(),
        key=lambda x: x[1]["ERROR"] + x[1]["WARNING"],
        reverse=True
    )


def analyze_log(filename):
    lines = read_log(filename)
    parsed = parse_lines(lines)
    filtered = filter_levels(parsed)
    hours = extract_hour(filtered)
    counts = count_by_hour(hours)
    return sort_result(counts)


if __name__ == "__main__":
    result = analyze_log("log2.txt")

    for hour, stats in result:
        print(hour, stats)