# PBF File Scraper

This project is a Python script to download large numbers of PBF (Protocolbuffer Binary Format) files from a remote tile server. It systematically downloads files for all combinations of two 5-digit numbers, saving them locally and logging any errors.

## Features

- Downloads PBF files from a specified URL pattern
- Saves files in a local directory (`pbf_files/`)
- Skips files that already exist
- Logs failed downloads and errors to `error_log.txt`
- Progress bar for download status

## Requirements

- Python 3.7+
- `requests`
- `tqdm`

Install dependencies with:

```bash
pip install requests tqdm
```

## Usage

1. Clone or download this repository.
2. Run the script:
   ```bash
   python main.py
   ```
3. Downloaded files will be saved in the `pbf_files/` directory.
4. Errors and failed downloads are logged in `error_log.txt`.

## Customization

- You can adjust the download range by changing the `process_combinations(START, END)` call in `main.py`.
- The number of parallel threads can be set with the `NUM_THREADS` variable (currently not used for true parallelism, but can be extended).

## Notes

- The script is designed to be memory-efficient and robust against network errors.
- Some files may not exist on the server; these are logged as failures.

## License

This project is provided for educational and research purposes only.
