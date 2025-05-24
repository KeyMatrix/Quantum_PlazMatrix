import sys

def main():
    if '--mode' in sys.argv:
        mode_index = sys.argv.index('--mode') + 1
        mode = sys.argv[mode_index] if mode_index < len(sys.argv) else 'default'
        source = sys.argv[-1]
        print(f"TreeOM CLI activated in '{mode}' mode with source: {source}")
        with open('logs/resonance.log', 'a') as log:
            log.write(f"Mode: {mode}, Source: {source}\n")
    else:
        print("No mode provided. Usage: python treeom_cli.py --mode sync GitHubEvents")

if __name__ == '__main__':
    main()