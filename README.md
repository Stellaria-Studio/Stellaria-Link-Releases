# Stellaria Link releases

Official **binary-only** distribution for Stellaria Link by Stellaria Studio.
Application and PassSDK source remain private. Required open-source notices,
licenses and protocol foundation source are included inside the application.

## Install on macOS

Download the DMG for your architecture from the [versioned releases](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases).
Open it, drag **Stellaria Link** to **Applications**, and open the app.
Import an airport HTTPS subscription, review compatibility and choose a node.

These are beta builds with a local ad hoc signature; Apple Developer ID signing
and notarization are not provided. If macOS blocks first launch, inspect the
source of the download and use **System Settings → Privacy & Security → Open Anyway**.
Do not disable macOS security globally.

The bundled Core works in application-proxy mode without changing system network
settings. System proxy and whole-device VPN are explicit connection modes; native
VPN requires a separate administrator-approved network helper. Do not run two
whole-device VPNs together. Preserve a working VPN until you explicitly switch.

## Updates

In **Settings → Connection → Software and Core updates**, choose **Check for updates**.
Automatic checks run on launch if due and at most daily; they only offer updates.
Choose **Later**, **Core only**, or **Update application**. Application updates
require Link to be disconnected and its host restoration confirmed. Core-only
updates preserve the active connection and take effect at the next explicit
connection. The previous app/core remains available for rollback.

The fixed `beta` release carries the signed platform manifest. Versioned releases
carry the matching DMG, app ZIP and independently signed Core package. No GitHub
login or access token is needed. The embedded Ed25519 key verifies manifest,
platform, version, hash and archive size before installation. The public key is
in [public-key.txt](public-key.txt); publishing a new key here does not change an
installed app's trust. Tampered, stale, unsafe-archive and downgrade updates are
refused. Offline failures preserve the current application and connection.

Version **0.10.1** displays **0J01b**: major, alphabetic minor (A=1, J=10),
two build digits, and `b` for beta. Only macOS Apple Silicon is packaged in this
round; other platforms and architectures are not implied.

## Account and qualification

The sidebar account entry opens the separate official Stellaria Pass system web
authentication window. Tokens use the SDK's macOS Keychain host; Link never asks
for the account password. Supporter status comes from the account service.

This beta is not a claim of universal traffic invisibility, comprehensive Mihomo
superiority, seven-day stability, battery efficiency or whole-device qualification.
Controlled application-proxy tests and protocol-specific defenses have limited
scope. Real node capability, identity requirements and host-restoration safety
still apply. Keep diagnostic exports private: they may describe local settings.
