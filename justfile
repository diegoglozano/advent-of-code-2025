# Advent of Code 2025

# Default recipe - show available commands
default:
    @just --list

# Run a day's solution with final data
run day:
    uv run src/day_{{day}}.py

# Run a day's solution with sample data (dev mode)
dev day:
    DEV=_sample uv run src/day_{{day}}.py

# Benchmark a day's solution
bench day:
    #!/usr/bin/env bash
    echo "Benchmarking day {{day}}..."
    echo ""
    echo "Running 10 iterations..."
    hyperfine --warmup 2 --runs 10 \
        --export-markdown "benchmark_day_{{day}}.md" \
        "uv run src/day_{{day}}.py" \
        || time uv run src/day_{{day}}.py

# Benchmark with sample data
bench-dev day:
    #!/usr/bin/env bash
    echo "Benchmarking day {{day}} (sample data)..."
    echo ""
    hyperfine --warmup 2 --runs 10 \
        --export-markdown "benchmark_day_{{day}}_sample.md" \
        "DEV=_sample uv run src/day_{{day}}.py" \
        || time DEV=_sample uv run src/day_{{day}}.py

# Run all available days
run-all:
    #!/usr/bin/env bash
    for file in src/day_*.py; do
        day=$(basename $file .py | sed 's/day_//')
        echo "═══════════════════════════════════════"
        echo "Running Day $day"
        echo "═══════════════════════════════════════"
        uv run $file
        echo ""
    done

# Compare performance between sample and final data
compare day:
    @echo "Sample data:"
    @just dev {{day}}
    @echo ""
    @echo "Final data:"
    @just run {{day}}
