# Performance Testing with JMeter

Apache JMeter covers load, stress, and endurance testing. Atlas functional tests (pytest) stay separate; JMeter plans live under `performance/jmeter/`.

## Setup

- Install Java 17+ and [Apache JMeter 5.6+](https://jmeter.apache.org/download_jmeter.cgi)
- Build plans in the GUI, but **run them in non-GUI mode**.

## Suggested layout

```
performance/jmeter/
  plans/posts-load.jmx
  data/users.csv
  results/            # git-ignored
```

## Plan structure

- **User Defined Variables:** `host`, `threads`, `rampup`, `duration` via `${__P(name,default)}`
- **Thread Group:** users, ramp-up, duration
- **HTTP Request Defaults** + **HTTP Header Manager**
- **CSV Data Set Config** for parameterised data
- **Assertions:** response code and duration (e.g. p95 thresholds)
- **Listeners:** only in GUI debugging; none for real runs

## Running

```bash
jmeter -n -t performance/jmeter/plans/posts-load.jmx \
  -Jhost=jsonplaceholder.typicode.com -Jthreads=20 -Jrampup=30 -Jduration=300 \
  -l performance/jmeter/results/run.jtl \
  -e -o performance/jmeter/results/report
```

`-n` non-GUI, `-l` raw results, `-e -o` HTML dashboard.

## Guidelines

- Only load-test systems you own or are authorised to test; Atlas' public demo endpoints must not be load-tested.
- Run against a production-like, isolated environment.
- Define SLOs first (e.g. p95 < 500 ms, error rate < 1%) and fail the build when exceeded.
- Warm up, then measure; keep the load generator unsaturated.
- Run in CI nightly or on demand, not on every PR; archive the `.jtl` and HTML report as artifacts.
