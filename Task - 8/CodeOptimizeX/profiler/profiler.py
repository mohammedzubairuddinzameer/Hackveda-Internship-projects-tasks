import cProfile
import pstats
import os
from datetime import datetime

ENABLE_PROFILING = os.getenv("ENABLE_PROFILING", "true").lower() == "true"
OUTPUT_DIR = "outputs/profiles"


def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def generate_filename(name="profile"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(OUTPUT_DIR, f"{name}_{timestamp}.prof")


def run_with_profiler(func, *args, sort_by="cumulative", lines=20, save=True, **kwargs):
    """
    Runs a function with cProfile and returns result + profile file path
    """

    ensure_output_dir()

    profiler = cProfile.Profile()

    print(f"[Profiler] Running function: {func.__name__}")

    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()

    stats = pstats.Stats(profiler).sort_stats(sort_by)

    print("\n[Profiler] Top Stats:")
    stats.print_stats(lines)

    file_path = None

    if save:
        file_path = generate_filename(func.__name__)
        profiler.dump_stats(file_path)
        print(f"\n[Profiler] Saved profile to: {file_path}")

    text_file = file_path.replace(".prof", ".txt")

    with open(text_file, "w") as f:
        stats.stream = f
        stats.print_stats(30)

    print(f"[Profiler] Text report saved to: {text_file}")
    return result, file_path


def profile_function(sort_by="cumulative", lines=20, save=True):
    @profile_function()
    def slow_function():
        total = 0
        for i in range(1_000_000):
            total += i
        return total


    if __name__ == "__main__":
        slow_function()

    def decorator(func):
        def wrapper(*args, **kwargs):
            return run_with_profiler(
                func,
                *args,
                sort_by=sort_by,
                lines=lines,
                save=save,
                **kwargs
            )
        return wrapper

    return decorator