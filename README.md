# Lutris on Flatpak

[Lutris](https://lutris.net) is an Open Source gaming platform for Linux. It installs and launches games so you can start playing without the hassle of setting up your games. This repository allows installing Lutris through [Flatpak](https://flatpak.org).

___________________________________________

## How install Lutris Beta
1. Install Flathub Beta
   1. Open the application called 'Terminal'
   2. In this application run the command:
```
flatpak remote-add flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo && flatpak update --appstream
```
2. Install Lutris Beta
   1. Open the application called 'Terminal'
   2. In this application run the command:
```
flatpak install --user flathub-beta net.lutris.Lutris//Beta
```

## How run Lutris Beta
   1. Open the application called 'Terminal'
   2. In this application run the command:
```
flatpak run net.lutris.Lutris//Beta
```
___________________________________________

## Build

To compile Lutris as a Flatpak, you'll need both [Flatpak](https://flatpak.org/) and [Flatpak Builder](http://docs.flatpak.org/en/latest/flatpak-builder.html) installed. Once you manage that, do the following...

0. Clone this repository...
  ```
  git clone --recursive https://github.com/flathub/net.lutris.Lutris.git
  cd net.lutris.Lutris
  ```

1. Add the platform dependencies...
  ```
  flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
  flatpak install --user flathub org.freedesktop//18.08
  flatpak install --user flathub org.freedesktop.Platform//18.08
  ```

2. Compile and install the Flatpak...
  ```
  flatpak-builder --user --repo=lutris --force-clean build-dir net.lutris.Lutris.yml
  flatpak remote-add --user lutris lutris --no-gpg-verify
  flatpak install --user lutris net.lutris.Lutris
  ```

3. Run it...
  ```
  flatpak run net.lutris.Lutris
  ```

## Clean up

```
flatpak uninstall --user net.lutris.Lutris
rm -rf ~/.var/app/net.lutris.Lutris .flatpak-builder
flatpak remote-delete lutris
```
