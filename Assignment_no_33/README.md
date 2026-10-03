# Duplicate File Removal Automation

## Project Title
Duplicate File Removal Automation Using Python

## Project Description
This automation script recursively scans a specified directory, identifies duplicate files using SHA-256 checksums, preserves one original copy, deletes the remaining duplicate copies, creates a timestamp-based log file inside the `Marvellous` directory, and sends the log file to a specified email address.

## Features
- Recursive directory scanning
- SHA-256 checksum-based duplicate detection
- Automatic duplicate-file deletion
- Timestamp-based log generation
- Periodic execution
- Email notification with log attachment
- Command-line arguments
- `--help` and usage information
- Directory, interval, email, and file validation
- Exception handling
- Modular functions
- Operational messages written to the log instead of normal console output

## Requirements
- Python 3.9 or newer
- Standard Python libraries only
- Internet connection for email delivery
- SMTP credentials for the sender account

## Installation
No third-party package is required.

## Email Configuration

Set these environment variables before running:

### Windows CMD
```cmd
set SMTP_SENDER=your_email@gmail.com
set SMTP_PASSWORD=your_gmail_app_password
```

Optional:
```cmd
set SMTP_SERVER=smtp.gmail.com
set SMTP_PORT=587
```

For Gmail, use a Google App Password. Do not put your real password directly in the Python source code.

## Execution Command

```cmd
python DuplicateFileRemoval.py "E:\Data\Demo" 50 marvellousinfosystem@gmail.com
```

Arguments:

1. `AbsoluteDirectoryPath` - absolute path of the directory to scan
2. `TimeIntervalInMinutes` - positive numeric interval
3. `ReceiverEmailAddress` - email recipient

## Help

```cmd
python DuplicateFileRemoval.py --help
```

## Usage

```cmd
python DuplicateFileRemoval.py --usage
```

`argparse` normally accepts `--help`; the program's help output also documents the required command format.

## Log Structure

A directory named `Marvellous` is created in the current working directory.

Example:

```text
Marvellous/
└── DuplicateRemovalLog_03_10_2026_23_55_00.log
```

The log records:
- Starting time
- Completion time
- Directory scanned
- Total files scanned
- Duplicate groups
- Duplicate files found
- Duplicate files deleted
- Complete paths of deleted files
- SHA-256 checksum values
- Errors
- Email delivery status

## Important Safety Note
Deleting duplicate files is destructive. Test the script on a sample directory first and keep backups of important data.

The first file in each checksum group is preserved and the remaining files are deleted.

## Project Structure

```text
Python_Assignment_33/
├── DuplicateFileRemoval.py
├── README.md
└── requirements.txt
```

## Expected Workflow

```text
Command-line arguments
        ↓
Input validation
        ↓
Create Marvellous directory/log
        ↓
Recursively scan files
        ↓
Calculate SHA-256 checksums
        ↓
Group duplicate files
        ↓
Preserve first file
        ↓
Delete remaining duplicates
        ↓
Record statistics and deleted paths
        ↓
Attach log to email
        ↓
Send report
        ↓
Wait for specified interval
        ↓
Repeat
```
