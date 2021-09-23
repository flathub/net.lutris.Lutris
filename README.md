# Lutris on Flatpak

[Lutris](https://lutris.net) is an Open Source gaming platform for Linux. It installs and launches games so you can start playing without the hassle of setting up your games. This repository allows installing Lutris through [Flatpak](https://flatpak.org).

___________________________________________

## Installation
1. Add Flathub Beta remote
   ```sh
   flatpak remote-add --user flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
   flatpak update --appstream
   ```
2. Install Lutris Beta
   ```sh
   flatpak install --user flathub-beta net.lutris.Lutris//beta
   ```
3. Install GNOME Compat and GL32 extensions
   ```sh
   flatpak install --user flathub org.gnome.Platform.Compat.i386 org.freedesktop.Platform.GL32.default org.freedesktop.Platform.GL.default
   ```
   Make sure that you install the same branches as the ones used by net.lutris.Lutris, usually the lastest ones.
   
   **DO NOT** confuse `org.gnome.Platform.Compat.i386` with `org.freedesktop.Platform.Compat.i386`.

## Running
Launch Lutris Beta from your desktop menu, or via command line:
```
flatpak run net.lutris.Lutris//beta
```
___________________________________________

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
   flatpak-builder --repo=lutris --force-clean --install-deps-from=flathub-beta  --user build-dir net.lutris.Lutris.yml
   ```
3. Add the local repo and install the flatpak
   ```sh
   flatpak remote-add --user lutris lutris --no-gpg-verify
   flatpak install --user lutris net.lutris.Lutris
   ```

### MangoHud

To enable MangoHud support simply install

```
flatpak install flathub org.freedesktop.Platform.VulkanLayer.MangoHud
```

### Clean up

```sh
flatpak uninstall --user net.lutris.Lutris
rm -rf ~/.var/app/net.lutris.Lutris .flatpak-builder
flatpak remote-delete lutris
```

___________________________________________

## Known issues

- [32-bit extensions aren't installed automatically](https://github.com/flathub/net.lutris.Lutris/issues/53) 
- [Destination Directory in ~/Games Cannot Be Found](https://github.com/flathub/net.lutris.Lutris/issues/89)

   Both of these issues are solved by installing the version of
   ```sh
   flatpak install --user flathub org.gnome.Platform.Compat.i386
   ```
   which corresponds to the GNOME runtime used by net.lutris.Lutris. If net.lutris.Lutris was installed without the `--user` flag, consider not using it for the extension.
- Lutris cannot detect my custom Games folder
   Related issue: [#79](https://github.com/flathub/net.lutris.Lutris/issues/79)

   Add the adequate filesystem override, and consider if the `--user` flag should be used
   ``` sh
   flatpak override --user --filesystem=/path/to/your/Folder net.lutris.Lutris
   ```
