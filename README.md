<p align="center">
  <img src="assets/banner.svg" alt="reShop: a Nintendo 3DS homebrew eShop remake" width="100%">
</p>

<p align="center">
  <a href="https://discord.gg/hqhRR2RCnd"><img alt="Discord" src="https://dcbadge.limes.pink/api/server/hqhRR2RCnd"></a>
  <img alt="gitleaks badge" src="https://img.shields.io/badge/protected%20by-gitleaks-blue">
  <img alt="License: PolyForm Noncommercial" src="https://img.shields.io/badge/license-PolyForm%20Noncommercial-orange">
</p>

> [!NOTE]
> reShop is back! This project was previously cancelled and is now being rebooted with permission from Unitendo, the original owner.
> The codebase is under active development, so expect rough edges and breaking changes.

## What is reShop?

reShop is a storefront for 3DS homebrew that looks and feels like the original Nintendo eShop. Browse listings, read descriptions, view icons, and download and install apps straight to your console, all from a familiar interface.

## Features

- eShop-style interface with streamed background music
- App listings, descriptions, and icons fetched from a server
- Downloading with an animated progress display
- CIA installation from the SD card

## Roadmap

### Phase 1: Foundation (from the original reShop)
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
git clone https://github.com/LinkMakesMods/reShop/
cd reShop
make
```

## Contributing

Contributions are welcome! Join the [Discord](https://discord.gg/hqhRR2RCnd) to chat, report bugs, or discuss ideas before opening a pull request. By contributing, you agree that your changes are released under the same license as the project.

## Credits

![reShop credits](assets/permission.png)

- **[Unitendo](https://github.com/Unitendo)**: original reShop project, including the base framework, rendering, downloading, installation, and eShop-style interface
- **LinkMakesMods**: reboot and all changes since
- **[@VirtuallyExisting](https://github.com/VirtuallyExisting)**: streamed audio implementation
- **[devkitPro](https://devkitpro.org/)** and the libctru team

## License

reShop is licensed under the [PolyForm Noncommercial License 1.0.0](License.md). You're free to use, modify, and share it for personal and other noncommercial purposes. Commercial use is not permitted.

Portions of this project are based on the original reShop by Unitendo.

## Disclaimer

reShop is a fan-made homebrew project. It is not affiliated with, endorsed by, or sponsored by Nintendo. Nintendo, Nintendo 3DS, and Nintendo eShop are trademarks of Nintendo.
