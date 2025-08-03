def analyze_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    errors = [line for line in logs if "ERROR" in line]
    print(f"Found {len(errors)} error(s) in the log file.")
    for err in errors:
        print(err.strip())

if __name__ == "__main__":
    analyze_log("sample_log.txt")