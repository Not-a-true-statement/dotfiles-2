from libqtile import widget
from libqtile.lazy import lazy

font_family = "Caskaydia Cove Nerd Font"
colors = {
    "black": ["#111111", "#111111"],
    "dark": ["#2A2A2A", "#2A2A2A"],
    "red": ["#A54C3F", "#A54C3F"],
    "gray": ["#444444", "#444444"],
    "white": ["#FFFFFF", "#FFFFFF"],
    "green": ["#98C379", "#98C379"],
    "yellow": ["#E5C07B", "#E5C07B"],
    "magenta": ["#C678DD", "#C678DD"],
    "cyan": ["#56B6C2", "#56B6C2"],
    "gray2": ["555555", "555555"],
}


def default_conf(fontsize=12, fg=colors["white"], bg=colors["black"]):
    return {
        "font": font_family,
        "fontsize": fontsize,
        "foreground": fg,
        "background": bg,
    }


def default_icon(fontsize=14, icon="", fg=colors["red"], pad=10):
    return {
        "font": font_family,
        "fontsize": fontsize,
        "text": icon,
        "foreground": fg,
        "padding": pad,
        "center_aligned": True,
    }


def separator(pad=15):
    return widget.Sep(
        **default_conf(),
        padding=pad,
        linewidth=0,
    )


widget_list = [
    widget.TextBox(
        mouse_callbacks={'Button1': lazy.shutdown()},
        **default_icon(fontsize=15, icon="   ", fg=colors["white"]),
        background=colors["red"],
    ),
    separator(),
    widget.GroupBox(
        **default_conf(bg=colors["dark"]),
        spacing=0,
        padding=10,
        borderwidth=3,
        highlight_method="block",
        this_current_screen_border=colors["red"],
        this_screen_border=colors["gray"],
        other_current_screen_border = colors["red"],
        highlight_color=colors["black"],
        inactive=colors["gray2"],
        active=colors["white"],
        roundeinactivd=False,
        center_aligned=True,
        disable_drag=True,
        rainbow=False,
        margin_x=-2,
    ),
    separator(),
    widget.TextBox(
        **default_icon(icon="裡", fg=colors["white"]),
        background=colors["red"],
    ),
    widget.WindowName(
        **default_conf(bg=colors["dark"]),
        padding=10,
        fmt="{}",
        max_chars=15,
    ),
    widget.Spacer(),
    widget.TextBox(
        **default_icon(icon=" ", fg=colors["white"]),
        background=colors["red"],
    ),
    widget.CheckUpdates(
        **default_conf(bg=colors["dark"]),
        padding=10,
        distro="Arch_checkupdates",
        display_format="{updates}",
        no_update_string="0",
        colour_have_updates=colors["white"],
        colour_no_updates=colors["white"],
        update_interval=120,
    ),
    separator(),
    widget.TextBox(
        **default_icon(icon=" ", fg=colors["white"]),
        background=colors["red"],
    ),
    widget.Mpris2(
        **default_conf(bg=colors["dark"]),
        padding=10,
        paused_text="\uf001 (\uead1) {track} \uf001",
        playing_text="\uf001 (\ueb2c) {track} \uf001",
        max_chars=20,
        stopped_text="",
    ),
    separator(),
    widget.TextBox(
        **default_icon(icon="", fg=colors["white"]),
        background=colors["red"],
    ),
    widget.CryptoTicker(
        **default_conf(bg=colors["dark"]),
        format='{crypto}: ${amount:,.2f}',
        padding=10,
    ),
    separator(),
    # FOR WIRELESS CONNECTION.
    # widget.TextBox(
    #     **default_icon(icon=" ", fg=colors["white"]),
    #     background=colors["red"],
    # ),
    # separator(),
    # widget.Net(
    #     **default_conf(bg=colors["dark"]),
    #     interface="wlan0",
    #     prefix="k",
    # ),
    widget.TextBox(
        **default_icon(icon=" ", fg=colors["white"]),
        background=colors["red"],
    ),
    widget.Memory(
        **default_conf(bg=colors["dark"]),
        format="{MemUsed:.1f} / {MemTotal:.1f} GB",
        measure_mem="G",
        padding=10,
    ),
    separator(),
    widget.TextBox(
        **default_icon(icon=" ", fg=colors["white"]),
        background=colors["red"],
    ),
    widget.Clock(
        **default_conf(bg=colors["dark"]),
        format="%d/%m/%Y %A",
        padding=10,
    ),
    separator(),
    widget.TextBox(
        **default_icon(icon="", fontsize=17, fg=colors["white"]),
        background=colors["red"],
    ),
    widget.PulseVolume(
        **default_conf(bg=colors["dark"]),
        get_volume_command=True,
        update_interval=0.01,
        padding=10,
    ),
    separator(),
    widget.TextBox(
        **default_icon(icon="", fontsize=17, fg=colors["white"]),
        background=colors["red"],
    ),
    widget.OpenWeather(
        **default_conf(fg=colors["white"], bg=colors["dark"]),
        location='Lima',
        format='{location_city} {temp}°C',
        padding=10,
    ),
    separator(),
    widget.TextBox(
        **default_icon(icon="", fg=colors["white"]),
        background=colors["red"],
    ),
    widget.Pomodoro(
        **default_conf(fg=colors["white"], bg=colors["dark"]),
        padding=10,
        color_active=colors["white"],
        color_break=colors["white"],
        color_inactive=colors["white"],
        prefix_inactive="P /  ",
        prefix_break="P /  ",
        prefix_pause="P /  "
    ),
    separator(),
    widget.TextBox(
        **default_icon(icon="", fg=colors["white"]),
        background=colors["red"],
    ),
    widget.Clock(
        **default_conf(fg=colors["white"], bg=colors["dark"]),
        format="%I:%M:%S %p",
        padding=10,
    ),
    separator(),
]

widget_defaults = dict(
    **default_conf(),
)
extension_defaults = widget_defaults.copy()
