Blueprint Studio Terminal - SSH Setup Guide
==========================================

This directory stores SSH configuration and keys for secure remote access.

PASSWORDLESS SSH ACCESS:
1. Generate a key pair (if you don't have one):
   ssh-keygen -t ed25519 -C "homeassistant@blueprintstudio"

2. Copy your public key to the remote server:
   ssh-copy-id user@remote-server

3. Your private key will be automatically used from this directory

SSH KEY FILES:
- id_rsa / id_rsa.pub (RSA keys - older, still supported)
- id_ed25519 / id_ed25519.pub (Ed25519 keys - recommended, more secure)
- id_ecdsa / id_ecdsa.pub (ECDSA keys)
- config (SSH client configuration)
- known_hosts (Fingerprints of servers you've connected to)

SECURITY NOTES:
- Never share your private keys (files without .pub extension)
- Private keys should have 600 permissions (read/write for owner only)
- Public keys (.pub files) can be safely shared
- Host key verification protects against man-in-the-middle attacks

TROUBLESHOOTING:
- If connection is slow, check ServerAliveInterval in config
- If key is rejected, ensure proper permissions: chmod 600 ~/.ssh/id_*
- For debugging, use: ssh -v user@host (verbose mode)
