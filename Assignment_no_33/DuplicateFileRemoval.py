#!/usr/bin/env python3
"""
DuplicateFileRemoval.py

Duplicate File Removal Automation

Usage:
    python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>

Example:
    python DuplicateFileRemoval.py "E:/Data/Demo" 50 marvellousinfosystem@gmail.com

Email configuration is read from environment variables:
    SMTP_SERVER       default: smtp.gmail.com
    SMTP_PORT         default: 587
    SMTP_SENDER       sender email address
    SMTP_PASSWORD     SMTP/app password

For Gmail, use an App Password rather than your normal account password.
"""

import argparse
import hashlib
import logging
import os
import re
import smtplib
import sys
import time
from collections import defaultdict
from datetime import datetime
from email.message import EmailMessage


LOG_DIRECTORY = "Marvellous"
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_directory(path):
    """Validate that path is an absolute, existing, readable directory."""
    if not path:
        raise ValueError("Directory path must be provided.")

    if not os.path.isabs(path):
        raise ValueError("Directory path must be an absolute path.")

    if not os.path.exists(path):
        raise ValueError("Specified directory does not exist.")

    if not os.path.isdir(path):
        raise ValueError("Specified path is not a directory.")

    if not os.access(path, os.R_OK):
        raise PermissionError("Application does not have permission to read the directory.")


def validate_interval(value):
    """Validate a positive numeric interval in minutes."""
    try:
        interval = float(value)
    except (TypeError, ValueError):
        raise ValueError("Time interval must be a numeric value.")

    if interval <= 0:
        raise ValueError("Time interval must be greater than zero.")

    return interval


def validate_email(address):
    """Perform basic receiver email validation."""
    if not address:
        raise ValueError("Receiver email address must be provided.")

    if not EMAIL_PATTERN.match(address):
        raise ValueError("Invalid receiver email address.")

    return address


def create_log_file():
    """Create the Marvellous directory and a timestamp-based log file."""
    os.makedirs(LOG_DIRECTORY, exist_ok=True)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    filename = f"DuplicateRemovalLog_{timestamp}.log"
    path = os.path.join(LOG_DIRECTORY, filename)

    return path


def configure_logging(log_path):
    """Configure file-only logging as required by the assignment."""
    logger = logging.getLogger("DuplicateFileRemoval")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.FileHandler(log_path, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def calculate_checksum(file_path, algorithm="sha256"):
    """Calculate the checksum of a file."""
    hasher = hashlib.new(algorithm)

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(1024 * 1024)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()


def scan_files(directory, logger):
    """Recursively scan files and group files by checksum."""
    groups = defaultdict(list)
    total_files = 0
    errors = []

    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.abspath(os.path.join(root, filename))

            # Do not process the automation's own log directory if it is
            # located inside the scanned directory.
            if os.path.abspath(root).startswith(
                os.path.abspath(os.path.join(os.getcwd(), LOG_DIRECTORY))
            ):
                continue

            try:
                if not os.path.isfile(file_path):
                    continue

                if not os.access(file_path, os.R_OK):
                    raise PermissionError("File is not readable.")

                checksum = calculate_checksum(file_path)
                groups[checksum].append(file_path)
                total_files += 1

            except (OSError, PermissionError, ValueError) as error:
                errors.append(f"{file_path} -> {error}")
                logger.error("Unable to process file: %s | %s", file_path, error)

    return groups, total_files, errors


def remove_duplicates(groups, logger):
    """Keep the first file in every duplicate group and delete the rest."""
    duplicate_groups = 0
    duplicate_files_found = 0
    duplicate_files_deleted = 0
    deleted_files = []

    for checksum, paths in groups.items():
        if len(paths) <= 1:
            continue

        duplicate_groups += 1
        duplicate_files_found += len(paths) - 1

        # Keep the first discovered file as the original.
        original = paths[0]
        logger.info("Duplicate group checksum: %s", checksum)
        logger.info("Preserved original file: %s", original)

        for duplicate in paths[1:]:
            try:
                if not os.path.isfile(duplicate):
                    logger.error("Duplicate file no longer exists: %s", duplicate)
                    continue

                if not os.access(duplicate, os.R_OK | os.W_OK):
                    logger.error("Permission denied for deletion: %s", duplicate)
                    continue

                os.remove(duplicate)
                duplicate_files_deleted += 1
                deleted_files.append((duplicate, checksum))
                logger.info("Deleted duplicate file: %s", duplicate)

            except PermissionError as error:
                logger.error("Permission denied while deleting %s | %s", duplicate, error)
            except OSError as error:
                logger.error("Unable to delete %s | %s", duplicate, error)

    return (
        duplicate_groups,
        duplicate_files_found,
        duplicate_files_deleted,
        deleted_files,
    )


def build_email_body(start_time, completion_time, directory, total_files,
                     duplicate_found, duplicate_deleted):
    """Create the required email report body."""
    return f"""Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics:

Starting time of scanning: {start_time}
Completion time of scanning: {completion_time}
Directory scanned: {directory}
Total number of files scanned: {total_files}
Total number of duplicate files found: {duplicate_found}
Total number of duplicate files deleted: {duplicate_deleted}

Please find the detailed log file attached to this email.

Regards,
Marvellous Automation System
"""


def send_email(receiver, subject, body, attachment_path, logger):
    """Send the log file as an email attachment."""
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    sender = os.getenv("SMTP_SENDER")
    password = os.getenv("SMTP_PASSWORD")

    if not sender or not password:
        raise RuntimeError(
            "SMTP_SENDER and SMTP_PASSWORD environment variables are required "
            "to send email."
        )

    message = EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    with open(attachment_path, "rb") as file:
        data = file.read()

    message.add_attachment(
        data,
        maintype="application",
        subtype="octet-stream",
        filename=os.path.basename(attachment_path),
    )

    with smtplib.SMTP(smtp_server, smtp_port, timeout=30) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)

    logger.info("Email sent successfully to: %s", receiver)


def execute_operation(directory, receiver, logger):
    """Run one complete duplicate-file removal operation."""
    start_dt = datetime.now()
    start_time = start_dt.strftime("%d %B %Y, %I:%M:%S %p")

    logger.info("=" * 80)
    logger.info("Duplicate-file removal operation started.")
    logger.info("Directory scanned: %s", directory)
    logger.info("Starting time of scanning: %s", start_time)

    groups, total_files, errors = scan_files(directory, logger)

    (
        duplicate_groups,
        duplicate_found,
        duplicate_deleted,
        deleted_files,
    ) = remove_duplicates(groups, logger)

    completion_dt = datetime.now()
    completion_time = completion_dt.strftime("%d %B %Y, %I:%M:%S %p")

    logger.info("Total number of files scanned: %d", total_files)
    logger.info("Total duplicate groups found: %d", duplicate_groups)
    logger.info("Total duplicate files found: %d", duplicate_found)
    logger.info("Total duplicate files deleted: %d", duplicate_deleted)

    for path, checksum in deleted_files:
        logger.info("Deleted file: %s | Checksum: %s", path, checksum)

    if errors:
        logger.warning("Errors encountered during execution: %d", len(errors))
    else:
        logger.info("Errors encountered during execution: 0")

    logger.info("Completion time of scanning: %s", completion_time)

    body = build_email_body(
        start_time,
        completion_time,
        directory,
        total_files,
        duplicate_found,
        duplicate_deleted,
    )

    try:
        send_email(
            receiver,
            "Duplicate File Removal Operation Report",
            body,
            logger.handlers[0].baseFilename,
            logger,
        )
    except Exception as error:
        logger.error("Email delivery failed: %s", error)

    logger.info("Duplicate-file removal operation completed.")
    logger.info("=" * 80)

    return {
        "start_time": start_time,
        "completion_time": completion_time,
        "total_files": total_files,
        "duplicate_found": duplicate_found,
        "duplicate_deleted": duplicate_deleted,
    }


def create_parser():
    """Create the command-line parser with help and usage support."""
    parser = argparse.ArgumentParser(
        prog="DuplicateFileRemoval.py",
        description=(
            "Scan a directory recursively, identify duplicate files using "
            "SHA-256 checksums, delete duplicate copies, create a log file, "
            "and email the log file."
        ),
        usage=(
            "python DuplicateFileRemoval.py "
            "<AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>"
        ),
    )

    parser.add_argument("directory", help="Absolute directory path to scan.")
    parser.add_argument(
        "interval",
        type=float,
        help="Positive time interval in minutes between operations.",
    )
    parser.add_argument(
        "receiver_email",
        help="Email address that receives the operation report.",
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        directory = os.path.abspath(args.directory)
        validate_directory(directory)
        interval = validate_interval(args.interval)
        receiver = validate_email(args.receiver_email)

        log_path = create_log_file()
        logger = configure_logging(log_path)

        logger.info("Application started.")
        logger.info("Validated directory: %s", directory)
        logger.info("Validated interval: %.2f minute(s)", interval)
        logger.info("Validated receiver email: %s", receiver)
        logger.info("Log file: %s", log_path)

        while True:
            execute_operation(directory, receiver, logger)

            logger.info(
                "Next execution scheduled after %.2f minute(s).", interval
            )

            time.sleep(interval * 60)

    except KeyboardInterrupt:
        # No operational message is printed to console. If a logger exists,
        # it will already contain the execution history.
        sys.exit(0)

    except (ValueError, PermissionError, RuntimeError, OSError) as error:
        # Validation/startup errors are reported through a short stderr message.
        # Once logging starts, operational details are kept in the log file.
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
