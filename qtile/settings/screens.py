from libqtile import bar;
from libqtile.config import Screen;
from .widgets import widget_list;

screens=[
    Screen(top=bar.Bar(widget_list, 22, margin=[10, 10, 0, 10], background="#111111", opacity=1, border_color="#111111", border_width=5)),
];
