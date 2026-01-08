import os
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "docs/problem-brief.md",
    "docs/ethical-impact-assessment.md",
    "docs/system-card.md",
    "docs/user-experience-notes.md",
    "src/demo.py",
    "examples/case_normal.json",
    "examples/case_edge.json",
    "examples/case_failure.json"
]

REQUIRED_DIRS = [
    "docs",
    "src",
    "tests",
    "examples",
    "assets"
]

def check_structure():
    root = Path.cwd()
    missing_files = []
    missing_dirs = []

    print("Checking project structure...")
    
    for d in REQUIRED_DIRS:
        if not (root / d).is_dir():
            missing_dirs.append(d)
            
    for f in REQUIRED_FILES:
        if not (root / f).exists():
            missing_files.append(f)

    if missing_dirs:
        print(f"❌ Missing directories: {', '.join(missing_dirs)}")
    else:
        print("✅ All required directories present.")

    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
    else:
        print("✅ All required files present.")

    return len(missing_files) == 0 and len(missing_dirs) == 0

def main():
    if not check_structure():
        print("\n⚠️  Project structure deemed incomplete.")
        sys.exit(1)
    
    print("\n🎉 Project structure validation passed!")
    # Future: Add checks for content (e.g. headers in markdown files)

if __name__ == "__main__":
    main()
