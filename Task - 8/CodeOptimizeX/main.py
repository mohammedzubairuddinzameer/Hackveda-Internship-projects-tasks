from profiler.profiler import run_with_profiler
from code_optimizer import analyze_code, optimize_code

def workflow():
    data = ["for i in range(1000): pass"] * 100000
    
    print("[Workflow] Starting analysis...")
    a = analyze_code(data)

    print("[Workflow] Optimizing...")
    b = optimize_code(a)

    return b


if __name__ == "__main__":
    run_with_profiler(workflow)

    