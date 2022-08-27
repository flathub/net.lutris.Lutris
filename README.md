# Lutris on Flatpak

[Lutris](https://lutris.net) is a video game preservation project.
It installs and launches games so you can start playing without the hassle of setting up your games.
This repository allows installing Lutris through [Flatpak](https://flatpak.org).

## Installation

   ```sh
   flatpak install flathub net.lutris.Lutris
   ```

## Running
Launch Lutris from your desktop menu, or via command line:
```
flatpak run net.lutris.Lutris
```

## Building

To compile Lutris as a Flatpak, you'll need both [Flatpak](https://flatpak.org/) and [Flatpak Builder](http://docs.flatpak.org/en/latest/flatpak-builder.html) installed. Once you manage that, do the following...

0. Clone this repository and `cd` into it
1. Add the git submodules
   ```sh
   git submodule init
   git submodule update
   ```
3. Add flathub-beta remote (same as in "Installation" section)
4. Compile the flatpak
   ```sh
   flatpak-builder --repo=lutris --force-clean --install-deps-from=flathub build-dir net.lutris.Lutris.yml
   ```
3. Add the local repo and install the flatpak
   ```sh
   flatpak remote-add lutris lutris --no-gpg-verify
   flatpak install lutris net.lutris.Lutris
   ```

### MangoHud

To enable MangoHud support install

```
flatpak install flathub org.freedesktop.Platform.VulkanLayer.MangoHud
```

## Known issues

- Lutris cannot detect my custom Games folder
   Related issue: [#79](https://github.com/flathub/net.lutris.Lutris/issues/79)

   Add the adequate filesystem override
   ``` sh
   flatpak override --filesystem=/path/to/your/Folder net.lutris.Lutris
   ```
