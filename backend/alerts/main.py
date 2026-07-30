from backend.alerts.diff import diff_tariffs

def run_alerts(previous, current):
    changes = diff_tariffs(previous, current)
    return changes

if __name__ == "__main__":
    print("alerts worker")
