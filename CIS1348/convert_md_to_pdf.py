#!/usr/bin/env python3
"""
Convert all markdown files to PDF using pandoc.
Walks through all subdirectories and converts each .md file to .pdf
"""

import os
import subprocess
from pathlib import Path


def convert_md_to_pdf(base_dir):
    """
    Walk through all subdirectories and convert .md files to .pdf using pandoc.

    Args:
        base_dir: The base directory to start searching from
    """
    base_path = Path(base_dir)

    # Counter for tracking
    converted = 0
    failed = 0

    # Walk through all subdirectories
    for md_file in base_path.rglob("*.md"):
        # Generate output PDF path (same name, different extension)
        pdf_file = md_file.with_suffix(".pdf")

        try:
            print(f"Converting: {md_file.relative_to(base_path)} -> {pdf_file.name}")

            # Run pandoc command with xelatex for better Unicode support
            result = subprocess.run(
                ["pandoc", str(md_file), "-o", str(pdf_file),
                 "--pdf-engine=xelatex"],
                capture_output=True,
                text=True,
                check=True
            )

            converted += 1

        except subprocess.CalledProcessError as e:
            print(f"  ERROR: Failed to convert {md_file.name}")
            print(f"  {e.stderr}")
            failed += 1

        except FileNotFoundError:
            print("ERROR: pandoc is not installed or not in PATH")
            print("Install pandoc: sudo apt install pandoc (or your package manager)")
            return

    # Summary
    print(f"\n{'='*50}")
    print(f"Conversion complete!")
    print(f"Successfully converted: {converted} files")
    if failed > 0:
        print(f"Failed: {failed} files")
    print(f"{'='*50}")


if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = Path(__file__).parent

    print(f"Searching for markdown files in: {script_dir}")
    print(f"{'='*50}\n")

    convert_md_to_pdf(script_dir)
