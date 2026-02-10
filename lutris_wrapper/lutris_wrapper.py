#!/usr/bin/env python3
import configparser
import sys
import os
import logging

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

COMPAT_EXT = "org.freedesktop.Platform.Compat.i386"
FLATPAK_INFO = "/.flatpak-info"
LUTRIS_PATH = "/app/bin/lutris"

# Map GNOME runtime versions to freedesktop SDK versions
GNOME_TO_FREEDESKTOP = {
    "49": "25.08",
    "48": "24.08",
    "47": "24.08",
    "46": "23.08",
}

# COMPAT_EXT = "org.gnome.Platform.FakeCompat.i386"  # testing
# FLATPAK_INFO = "flatpak-info"  # testing
# LUTRIS_PATH = "/usr/bin/pwd"  # testing


def build_window(window):
    window.props.title = "Flatpak Extension Missing"

    box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
    box.props.hexpand = True

    def on_clicked(_button):
        window.destroy()
        run_lutris()

    def on_copy_clicked(button):
        clipboard = button.get_display().get_clipboard()
        clipboard.set(get_command())

    button = Gtk.Button.new_with_label("Close")
    button.connect("clicked", on_clicked)

    copy_button = Gtk.Button.new_from_icon_name("edit-copy-symbolic")
    copy_button.connect("clicked", on_copy_clicked)

    label = Gtk.Label.new(
        "The GL compat extension is missing, wine apps won't work properly.\nPlease run:"
    )

    command = Gtk.Label.new("<tt>{}</tt>".format(get_command()))
    command.props.use_markup = True
    command.props.selectable = True
    command.add_css_class("view")

    hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
    hbox.append(command)
    hbox.append(copy_button)

    end_label = Gtk.Label.new("And then restart Lutris.")

    window.set_child(box)
    box.append(label)
    box.append(hbox)
    box.append(end_label)
    box.append(button)


def on_activate(app):
    window = Gtk.ApplicationWindow.new(app)
    build_window(window)
    window.present()


def get_command():
    flatpak_info = read_flatpak_info()
    _, _, _, gnome_version = flatpak_info["runtime"].split("/")
    # Map GNOME version to freedesktop SDK version
    fd_version = GNOME_TO_FREEDESKTOP.get(gnome_version, "25.08")
    command = "flatpak install --user flathub {}//{}".format(COMPAT_EXT, fd_version)
    return command


def read_flatpak_info():
    flatpak_info = configparser.ConfigParser()
    with open(FLATPAK_INFO, "r") as f:
        flatpak_info.read_file(f)

    return {
        "runtime": flatpak_info.get("Application", "runtime"),
        "app-extensions": dict(
            (
                s.split("=")
                for s in flatpak_info.get(
                    "Instance", "app-extensions", fallback=""
                ).split(";")
                if s
            )
        ),
        "runtime-extensions": dict(
            (
                s.split("=")
                for s in flatpak_info.get(
                    "Instance", "runtime-extensions", fallback=""
                ).split(";")
                if s
            )
        ),
    }


def run_lutris():
    argv = sys.argv[1:]
    os.execv(LUTRIS_PATH, [LUTRIS_PATH] + argv)


def main():
    info = read_flatpak_info()

    is_installed = COMPAT_EXT in info["app-extensions"]

    if is_installed:
        run_lutris()
    else:
        logging.warning(
            "Missing extension {}, see https://github.com/flathub/net.lutris.Lutris/issues/53".format(
                COMPAT_EXT
            )
        )
        app = Gtk.Application()
        app.connect("activate", on_activate)
        app.run()


if __name__ == "__main__":
    main()
