# reShop

**A Nintendo 3DS eShop remake for homebrew, built with libctru.**

[Discord](https://discord.gg/hqhRR2RCnd)

[![Discord](https://dcbadge.limes.pink/api/server/hqhRR2RCnd)](https://discord.gg/hqhRR2RCnd)
<img alt="gitleaks badge" src="https://img.shields.io/badge/protected%20by-gitleaks-blue">

> [!NOTE]
> reShop is back! This project was previously cancelled and is now being rebooted.
> Originally created by [Unitendo](https://github.com/Unitendo). Rebooted by LinkMakesMods.
> The codebase is under active development, so expect rough edges and breaking changes.

## What is reShop?

reShop is a community-driven storefront for 3DS homebrew that looks and feels like the original Nintendo eShop. Browse listings, read descriptions, view icons, and download and install apps straight to your console, all from a familiar interface.

## Features

- eShop-style interface with streamed background music
- App listings, descriptions, and icons fetched from a server
- Downloading with an animated progress display
- CIA installation from the SD card

## Roadmap

### Phase 1: Foundation (carried over from v1)
- [x] Licensing, base framework, and rendering
- [x] Streamed audio (custom implementation by @VirtuallyExisting)
- [x] HTTP downloading, based on devkitPro's example
- [x] Server-driven listings, descriptions, and icons
- [x] Download and CIA install flow, with animation
- [x] Complete eShop-style GUI
- [x] Closed and open betas

### Phase 2: Reboot
- [ ] Codebase cleanup and modernization
- [ ] [Reboot goals, e.g. stability, new backend, updated UI]
- [ ] Closed beta
- [ ] Open beta

### Phase 3: Community
- [ ] Realtime messaging under each listing (like Juxt communities)
- [ ] User rating system
- [ ] Friends list and in-app friending
- [ ] Suggested users based on similar games
- [ ] Fake currency and achievements: not required to get homebrew, but it unlocks leaderboard ranks and upgraded music options

### Phase 4: Expanded Library
- [ ] DS app downloads (not just DSiWare)
- [ ] Downloading from additional sources

## Building

### Requirements
- [devkitPro](https://devkitpro.org/wiki/Getting_Started) with devkitARM

### Install dependencies
```bash
sudo dkp-pacman -S 3ds-dev 3ds-opusfile 3ds-curl 3ds-mbedtls 3ds-zlib 3ds-bzip2 3ds-liblzma
```
Depending on your platform, you may not need `sudo` or the `dkp-` prefix.

### Compile
```bash
git clone https://github.com/Unitendo/reShop/
cd reShop
make
```

## Contributing

Contributions are welcome! Join the [Discord](https://discord.gg/hqhRR2RCnd) to chat, report bugs, or discuss ideas before opening a pull request.

## Credits

- **[Unitendo](https://github.com/Unitendo)**: original reShop project, including the base framework, rendering, downloading, installation, and eShop-style interface
- **LinkMakesMods**: reboot and all changes since
- **[@VirtuallyExisting](https://github.com/VirtuallyExisting)**: streamed audio implementation
- **[devkitPro](https://devkitpro.org/)** and the libctru team

## License

[Add license here]
