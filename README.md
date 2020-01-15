# Lutris on Flatpak

[Lutris](https://lutris.net) is an Open Source gaming platform for Linux. It installs and launches games so you can start playing without the hassle of setting up your games. This repository allows installing Lutris through [Flatpak](https://flatpak.org).

___________________________________________

## Installation
1. Add Flathub Beta remote
   ```
   flatpak remote-add --user flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
   flatpak update --appstream
   ```
2. Install Lutris Beta
   ```
   flatpak install --user flathub-beta net.lutris.Lutris//beta
   ```

## Running
Launch Lutris Beta from your desktop menu, or via command line:
```
flatpak run net.lutris.Lutris//beta
```
___________________________________________

## Building

To compile Lutris as a Flatpak, you'll need both [Flatpak](https://flatpak.org/) and [Flatpak Builder](http://docs.flatpak.org/en/latest/flatpak-builder.html) installed. Once you manage that, do the following...

0. Clone this repository and `cd` into it
1. Add flathub-beta remote (same as in "Installation" section)
2. Compile the flatpak
   ```
   flatpak-builder --repo=lutris --force-clean --install-deps-from=flathub-beta  --user build-dir net.lutris.Lutris.yml
   ```
3. Add the local repo and install the flatpak
   ```
   flatpak remote-add --user lutris lutris --no-gpg-verify
   flatpak install --user lutris net.lutris.Lutris
   ```

### Clean up

```
flatpak uninstall --user net.lutris.Lutris
rm -rf ~/.var/app/net.lutris.Lutris .flatpak-builder
flatpak remote-delete lutris
```
