def analyze_code(code_lines):
    result = []
    for line in code_lines:
        if "for" in line:
            result.append(line.strip())
    return result


def optimize_code(code_lines):
    optimized = []
    for line in code_lines:
        optimized.append(line.replace(" ", ""))
    return optimized