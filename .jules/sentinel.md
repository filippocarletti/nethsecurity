## 2026-05-21 - Secure Handling of Backups and Passphrases
**Vulnerability:** GPG passphrases in `ns.backup` were exposed to the process list via command-line arguments (`--passphrase`), and the backup passphrase file was created with default, potentially overly permissive, permissions.
**Learning:** Secrets passed as command-line arguments are globally visible to all local users via tools like `ps`. Relying on default file creation permissions can lead to sensitive data leakage if the system umask is not sufficiently restrictive.
**Prevention:** Always pass sensitive data to subprocesses via standard input (e.g., `gpg --passphrase-fd 0`). When creating files for secrets, use `os.open` with explicit restrictive permissions like `0o600` (read/write only for the owner).
