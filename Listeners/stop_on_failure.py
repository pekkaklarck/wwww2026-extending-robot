def end_keyword(data, result):
    if result.status == "FAIL":
        input(f"\nExecution failed: {result.message}\nPress enter to continue.")
