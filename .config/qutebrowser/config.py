# Hide the window decoration.  This setting requires a restart on
# Wayland.
## Type: Bool
# c.window.hide_decoration = False

# Format to use for the window title. The same placeholders like for
# `tabs.title.format` are defined.
## Type: FormatString
# c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser'

# Set the main window background to transparent.  This allows having a
# transparent tab- or statusbar (might require a compositor such as
# picom). However, it breaks some functionality such as dmenu embedding
# via its `-w` option. On some systems, it was additionally reported
# that main window transparency negatively affects performance.  Note
# this setting only affects windows opened after setting it.
## Type: Bool
# c.window.transparent = False

# Default font size to use. Whenever "default_size" is used in a font
# setting, it's replaced with the size listed here. Valid values are
# either a float value with a "pt" suffix, or an integer value with a
# "px" suffix.
## Type: String
c.fonts.default_size = '14pt'

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font
# c.fonts.default_family = []

# Font used in the completion categories.
## Type: Font
# c.fonts.completion.category = 'bold default_size default_family'

# Font used in the completion widget.
## Type: Font
# c.fonts.completion.entry = 'default_size default_family'

# Font used for the context menu. If set to null, the Qt default is
# used.
## Type: Font
# c.fonts.contextmenu = None

# Font used for the debugging console.
## Type: Font
# c.fonts.debug_console = 'default_size default_family'

# Font used for the downloadbar.
## Type: Font
# c.fonts.downloads = 'default_size default_family'

# Font used for the hints.
## Type: Font
# c.fonts.hints = 'bold default_size default_family'

# Font used in the keyhint widget.
## Type: Font
# c.fonts.keyhint = 'default_size default_family'

# Font used for error messages.
## Type: Font
# c.fonts.messages.error = 'default_size default_family'

# Font used for info messages.
## Type: Font
# c.fonts.messages.info = 'default_size default_family'

# Font used for warning messages.
## Type: Font
# c.fonts.messages.warning = 'default_size default_family'

# Font used for prompts.
## Type: Font
# c.fonts.prompts = 'default_size sans-serif'

# Font used in the statusbar.
## Type: Font
# c.fonts.statusbar = 'default_size default_family'

# Font used for selected tabs.
## Type: Font
# c.fonts.tabs.selected = 'default_size default_family'

# Font used for unselected tabs.
## Type: Font
# c.fonts.tabs.unselected = 'default_size default_family'

# Font family for cursive fonts.
## Type: FontFamily
# c.fonts.web.family.cursive = ''

# Font family for fantasy fonts.
## Type: FontFamily
# c.fonts.web.family.fantasy = ''

# Font family for fixed fonts.
## Type: FontFamily
# c.fonts.web.family.fixed = ''

# Font family for sans-serif fonts.
## Type: FontFamily
# c.fonts.web.family.sans_serif = ''

# Font family for serif fonts.
## Type: FontFamily
# c.fonts.web.family.serif = ''

# Font family for standard fonts.
## Type: FontFamily
# c.fonts.web.family.standard = ''

# Default font size (in pixels) for regular text.
## Type: Int
# c.fonts.web.size.default = 16

# Default font size (in pixels) for fixed-pitch text.
## Type: Int
# c.fonts.web.size.default_fixed = 13

# Hard minimum font size (in pixels).
## Type: Int
# c.fonts.web.size.minimum = 0

# Minimum logical font size (in pixels) that is applied when zooming
# out.
## Type: Int
# c.fonts.web.size.minimum_logical = 6

# Gruvbox dark, soft scheme by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)

grey_0 = "#32302f"
grey_10 = "#3c3836"
grey_25 = "#504945"
grey_40 = "#665c54"
grey_55 = "#bdae93"
grey_70 = "#d5c4a1"
grey_85 = "#ebdbb2"
grey_100 = "#fbf1c7"
red = "#fb4934"
orange = "#fe8019"
yellow = "#fabd2f"
green = "#b8bb26"
cyan = "#8ec07c"
blue = "#83a598"
magenta = "#d3869b"
brown = "#d65d0e"

# special
foreground = "#c0b18b"
background = "#1f1f1f"

# black
color0 = "#4a3637"
color8 = "#402e2e"

# red
color1 = "#d17b49"
color9 = "#ac5d2f"

# green
color2 = "#7b8748"
color10 = "#647035"

# yellow
color3 = "#af865a"
color11 = "#8f6840"

# blue
color4 = "#535c5c"
color12 = "#444b4b"

# magenta
color5 = "#775759"
color13 = "#614445"

# cyan
color6 = "#6d715e"
color14 = "#585c49"

# white
color7 = "#c0b18b"
color15 = "#978965"

# --- End of import section ---

# Rassigning variable names
black_0 = color0
black_dark_8 = color8
red_1 = color1
red_dark_9 = color9
green_2 = color2
green_dark_10 = color10
yellow_3 = color3
yellow_dark_11 = color11
blue_4 = color4
blue_dark_12 = color12
magenta_5 = color5
magenta_dark_13 = color13
cyan_6 = color6
cyan_dark_14 = color14
white_7 = color7
white_dark_15 = color15

c.colors.completion.category.fg = yellow
c.colors.completion.category.bg = grey_0
c.colors.completion.category.border.top = grey_0
c.colors.completion.category.border.bottom = grey_0

# c.colors.completion.fg = ['white', 'white', 'white']
c.colors.completion.fg = grey_70
c.colors.completion.match.fg = green
c.colors.completion.odd.bg = grey_10
c.colors.completion.even.bg = grey_0

c.colors.completion.item.selected.fg = grey_70
c.colors.completion.item.selected.bg = grey_25
c.colors.completion.item.selected.border.top = grey_25
c.colors.completion.item.selected.border.bottom = grey_25
c.colors.completion.item.selected.match.fg = green

c.colors.completion.scrollbar.fg = grey_70
c.colors.completion.scrollbar.bg = grey_0

c.colors.contextmenu.disabled.bg = grey_10
c.colors.contextmenu.disabled.fg = grey_55
c.colors.contextmenu.menu.bg = grey_0
c.colors.contextmenu.menu.fg =  grey_70
c.colors.contextmenu.selected.bg = grey_25
c.colors.contextmenu.selected.fg = grey_70

# Background color of disabled items in the context menu. If set to
# null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.disabled.bg = None

# Foreground color of disabled items in the context menu. If set to
# null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.disabled.fg = None

# Background color of the context menu. If set to null, the Qt default
# is used.
## Type: QssColor
# c.colors.contextmenu.menu.bg = None

# Foreground color of the context menu. If set to null, the Qt default
# is used.
## Type: QssColor
# c.colors.contextmenu.menu.fg = None

# Background color of the context menu's selected item. If set to null,
# the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.selected.bg = None

# Foreground color of the context menu's selected item. If set to null,
# the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.selected.fg = None

c.colors.downloads.bar.bg = grey_0
c.colors.downloads.start.fg = grey_0
c.colors.downloads.start.bg = blue
c.colors.downloads.stop.fg = grey_0
c.colors.downloads.stop.bg = cyan
c.colors.downloads.error.fg = red

# Background color for the download bar.
## Type: QssColor
# c.colors.downloads.bar.bg = 'black'

# Background color for downloads with errors.
## Type: QtColor
# c.colors.downloads.error.bg = 'red'

# Foreground color for downloads with errors.
## Type: QtColor
# c.colors.downloads.error.fg = 'white'

# Color gradient start for download backgrounds.
## Type: QtColor
# c.colors.downloads.start.bg = '#0000aa'

# Color gradient start for download text.
## Type: QtColor
# c.colors.downloads.start.fg = 'white'

# Color gradient stop for download backgrounds.
## Type: QtColor
# c.colors.downloads.stop.bg = '#00aa00'

# Color gradient end for download text.
## Type: QtColor
# c.colors.downloads.stop.fg = 'white'

# Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
# Valid values:
# - rgb: Interpolate in the RGB color system.
# - hsv: Interpolate in the HSV color system.
# - hsl: Interpolate in the HSL color system.
# - none: Don't show a gradient.
# c.colors.downloads.system.bg = 'rgb'

# Color gradient interpolation system for download text.
## Type: ColorSystem
# Valid values:
# - rgb: Interpolate in the RGB color system.
# - hsv: Interpolate in the HSV color system.
# - hsl: Interpolate in the HSL color system.
# - none: Don't show a gradient.
# c.colors.downloads.system.fg = 'rgb'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
## Type: QssColor
# c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.8), stop:1 rgba(255, 197, 66, 0.8))'

# Font color for hints.
## Type: QssColor
# c.colors.hints.fg = 'black'

# Font color for the matched part of hints.
## Type: QtColor
# c.colors.hints.match.fg = 'green'

# Background color of the keyhint widget.
## Type: QssColor
# c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'

# Text color for the keyhint widget.
## Type: QssColor
# c.colors.keyhint.fg = '#FFFFFF'

# Highlight color for keys to complete the current keychain.
## Type: QssColor
# c.colors.keyhint.suffix.fg = '#FFFF00'
c.colors.hints.fg = grey_0
c.colors.hints.bg = yellow
c.colors.hints.match.fg = grey_70

c.colors.keyhint.fg = grey_70
c.colors.keyhint.suffix.fg = grey_70
c.colors.keyhint.bg = grey_0

c.colors.messages.error.fg = grey_0
c.colors.messages.error.bg = red
c.colors.messages.error.border = red
c.colors.messages.warning.fg = grey_0
c.colors.messages.warning.bg = magenta
c.colors.messages.warning.border = magenta
c.colors.messages.info.fg = grey_70
c.colors.messages.info.bg = grey_0
c.colors.messages.info.border = grey_0

# Background color of an error message.
## Type: QssColor
# c.colors.messages.error.bg = 'red'

# Border color of an error message.
## Type: QssColor
# c.colors.messages.error.border = '#bb0000'

# Foreground color of an error message.
## Type: QssColor
# c.colors.messages.error.fg = 'white'

# Background color of an info message.
## Type: QssColor
# c.colors.messages.info.bg = 'black'

# Border color of an info message.
## Type: QssColor
# c.colors.messages.info.border = '#333333'

# Foreground color of an info message.
## Type: QssColor
# c.colors.messages.info.fg = 'white'

# Background color of a warning message.
## Type: QssColor
# c.colors.messages.warning.bg = 'darkorange'

# Border color of a warning message.
## Type: QssColor
# c.colors.messages.warning.border = '#d47300'

# Foreground color of a warning message.
## Type: QssColor
# c.colors.messages.warning.fg = 'black'

c.colors.prompts.fg = grey_70
c.colors.prompts.border = grey_0
c.colors.prompts.bg = grey_0
c.colors.prompts.selected.bg = grey_25
c.colors.prompts.selected.fg = grey_70

# Background color for prompts.
## Type: QssColor
# c.colors.prompts.bg = '#444444'

# Border used around UI elements in prompts.
## Type: String
# c.colors.prompts.border = '1px solid gray'

# Foreground color for prompts.
## Type: QssColor
# c.colors.prompts.fg = 'white'

# Background color for the selected item in filename prompts.
## Type: QssColor
# c.colors.prompts.selected.bg = 'grey'

# Foreground color for the selected item in filename prompts.
## Type: QssColor
# c.colors.prompts.selected.fg = 'white'

# Color of the statusbar.
c.colors.statusbar.normal.fg = green
c.colors.statusbar.normal.bg = grey_0

# Color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = grey_0
c.colors.statusbar.insert.bg = blue

# Color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = grey_0
c.colors.statusbar.passthrough.bg = cyan

# Color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = grey_0
c.colors.statusbar.private.bg = grey_10

# Color of the statusbar in command mode.
c.colors.statusbar.command.fg = grey_70
c.colors.statusbar.command.bg = grey_0

# Color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = grey_70
c.colors.statusbar.command.private.bg = grey_0

# Color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = grey_0
c.colors.statusbar.caret.bg = magenta

# Color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = grey_0
c.colors.statusbar.caret.selection.bg = blue

# Color of the progress bar.
c.colors.statusbar.progress.bg = blue

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = grey_70

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = red

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = grey_70

# Foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.http.fg = cyan
c.colors.statusbar.url.success.https.fg = green

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = magenta

# Background color for webpages if unset (or empty to use the theme's
# color).
## Type: QtColor
# c.colors.webpage.bg = grey_0

c.colors.tabs.bar.bg = grey_0

# Color gradient for the tab indicator.
c.colors.tabs.indicator.start = blue
c.colors.tabs.indicator.stop = brown

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = red

# Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
# Valid values:
# - rgb: Interpolate in the RGB color system.
# - hsv: Interpolate in the HSV color system.
# - hsl: Interpolate in the HSL color system.
# - none: Do not show a gradient.
# c.colors.tabs.indicator.system = 'rgb'

c.colors.tabs.odd.fg = grey_70
c.colors.tabs.odd.bg = grey_10
c.colors.tabs.even.fg = grey_70
c.colors.tabs.even.bg = grey_0
c.colors.tabs.pinned.odd.fg = grey_70
c.colors.tabs.pinned.odd.bg = grey_25
c.colors.tabs.pinned.even.fg = grey_70
c.colors.tabs.pinned.even.bg = grey_25

c.colors.tabs.selected.odd.fg = grey_0
c.colors.tabs.selected.odd.bg = cyan
c.colors.tabs.selected.even.fg = grey_0
c.colors.tabs.selected.even.bg = cyan
c.colors.tabs.pinned.selected.odd.fg = grey_0
c.colors.tabs.pinned.selected.odd.bg = cyan
c.colors.tabs.pinned.selected.even.fg = grey_0
c.colors.tabs.pinned.selected.even.bg = cyan

# Which algorithm to use for modifying how colors are rendered with
# darkmode. The `lightness-cielab` value was added with QtWebEngine 5.14
# and is treated like `lightness-hsl` with older QtWebEngine versions.
## Type: String
# Valid values:
# - lightness-cielab: Modify colors by converting them to CIELAB color space and inverting the L value. Not available with Qt < 5.14.
# - lightness-hsl: Modify colors by converting them to the HSL color space and inverting the lightness (i.e. the "L" in HSL).
# - brightness-rgb: Modify colors by subtracting each of r, g, and b from their maximum value.
# c.colors.webpage.darkmode.algorithm = 'lightness-cielab'

# Contrast for dark mode. This only has an effect when
# `colors.webpage.darkmode.algorithm` is set to `lightness-hsl` or
# `brightness-rgb`.
## Type: Float
# c.colors.webpage.darkmode.contrast = 0.0

# Render all web contents using a dark theme. Example configurations
# from Chromium's `chrome://flags`:  - "With simple HSL/CIELAB/RGB-based
# inversion": Set   `colors.webpage.darkmode.algorithm` accordingly.  -
# "With selective image inversion": Set
# `colors.webpage.darkmode.policy.images` to `smart`.  - "With selective
# inversion of non-image elements": Set
# `colors.webpage.darkmode.threshold.text` to 150 and
# `colors.webpage.darkmode.threshold.background` to 205.  - "With
# selective inversion of everything": Combines the two variants   above.
# ## Type: Bool
# c.colors.webpage.darkmode.enabled = True

# Render all colors as grayscale. This only has an effect when
# `colors.webpage.darkmode.algorithm` is set to `lightness-hsl` or
# `brightness-rgb`.
## Type: Bool
# c.colors.webpage.darkmode.grayscale.all = False

# Desaturation factor for images in dark mode. If set to 0, images are
# left as-is. If set to 1, images are completely grayscale. Values
# between 0 and 1 desaturate the colors accordingly.
## Type: Float
# c.colors.webpage.darkmode.grayscale.images = 0.0

# Which images to apply dark mode to. With QtWebEngine 5.15.0, this
# setting can cause frequent renderer process crashes due to a
# https://codereview.qt-project.org/c/qt/qtwebengine-
# chromium/+/304211[bug in Qt].
## Type: String
# Valid values:
# - always: Apply dark mode filter to all images.
# - never: Never apply dark mode filter to any images.
# - smart: Apply dark mode based on image content. Not available with Qt 5.15.0.
# c.colors.webpage.darkmode.policy.images = 'smart'

# Which pages to apply dark mode to. The underlying Chromium setting has
# been removed in QtWebEngine 5.15.3, thus this setting is ignored
# there. Instead, every element is now classified individually.
## Type: String
# Valid values:
# - always: Apply dark mode filter to all frames, regardless of content.
# - smart: Apply dark mode filter to frames based on background color.
c.colors.webpage.darkmode.policy.page = 'smart'

# Threshold for inverting background elements with dark mode. Background
# elements with brightness above this threshold will be inverted, and
# below it will be left as in the original, non-dark-mode page. Set to
# 256 to never invert the color or to 0 to always invert it. Note: This
# behavior is the opposite of `colors.webpage.darkmode.threshold.text`!
## Type: Int
c.colors.webpage.darkmode.threshold.background = 205

# Threshold for inverting text with dark mode. Text colors with
# brightness below this threshold will be inverted, and above it will be
# left as in the original, non-dark-mode page. Set to 256 to always
# invert text color or to 0 to never invert text color.
## Type: Int
c.colors.webpage.darkmode.threshold.text = 150

# Value to use for `prefers-color-scheme:` for websites. The "light"
# value is only available with QtWebEngine 5.15.2+. On older versions,
# it is the same as "auto". The "auto" value is broken on QtWebEngine
# 5.15.2 due to a Qt bug. There, it will fall back to "light"
# unconditionally.
## Type: String
# Valid values:
# - auto: Use the system-wide color scheme setting.
# - light: Force a light theme.
# - dark: Force a dark theme.
c.colors.webpage.preferred_color_scheme = "dark"

config.load_autoconfig(True)

c.messages.timeout = 9000

# Backend to use to display websites. qutebrowser supports two different
# web rendering engines / backends, QtWebEngine and QtWebKit (not
# recommended). QtWebEngine is Qt's official successor to QtWebKit, and
# both the default/recommended backend. It's based on a stripped-down
# Chromium and regularly updated with security fixes and new features by
# the Qt project: https://wiki.qt.io/QtWebEngine QtWebKit was
# qutebrowser's original backend when the project was started. However,
# support for QtWebKit was discontinued by the Qt project with Qt 5.6 in
# 2016. The development of QtWebKit was picked up in an official fork:
# https://github.com/qtwebkit/qtwebkit - however, the project seems to
# have stalled again. The latest release (5.212.0 Alpha 4) from March
# 2020 is based on a WebKit version from 2016, with many known security
# vulnerabilities. Additionally, there is no process isolation and
# sandboxing. Due to all those issues, while support for QtWebKit is
# still available in qutebrowser for now, using it is strongly
# discouraged.
## Type: String
# Valid values:
# - webengine: Use QtWebEngine (based on Chromium - recommended).
# - webkit: Use QtWebKit (based on WebKit, similar to Safari - many known security issues!).
# c.backend = 'webengine'

# When to show a changelog after qutebrowser was upgraded.
## Type: String
# Valid values:
# - major: Show changelog for major upgrades (e.g. v2.0.0 -> v3.0.0).
# - minor: Show changelog for major and minor upgrades (e.g. v2.0.0 -> v2.1.0).
# - patch: Show changelog for major, minor and patch upgrades (e.g. v2.0.0 -> v2.0.1).
# - never: Never show changelog after upgrades.
c.changelog_after_upgrade = "major"

# Delay (in milliseconds) before updating completions after typing a
# character.
## Type: Int
# c.completion.delay = 0

# Default filesystem autocomplete suggestions for :open. The elements of
# this list show up in the completion window under the Filesystem
# category when the command line contains `:open` but no argument.
# Type: List of String
# c.completion.favorite_paths = []

# Height (in pixels or as percentage of the window) of the completion.
## Type: PercOrInt
# c.completion.height = '50%'

# Minimum amount of characters needed to update completions.
## Type: Int
# c.completion.min_chars = 1

# Which categories to show (in which order) in the :open completion.
## Type: FlagList
# Valid values:
##   - searchengines
##   - quickmarks
##   - bookmarks
##   - history
##   - filesystem
# c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

# Move on to the next part when there's only one possible completion
# left.
## Type: Bool
# c.completion.quick = True

# Padding (in pixels) of the scrollbar handle in the completion window.
## Type: Int
# c.completion.scrollbar.padding = 2

# Width (in pixels) of the scrollbar in the completion window.
## Type: Int
# c.completion.scrollbar.width = 12

# When to show the autocompletion window.
## Type: String
# Valid values:
# - always: Whenever a completion is available.
# - auto: Whenever a completion is requested.
# - never: Never.
# c.completion.show = 'always'

# Shrink the completion to be smaller than the configured size if there
# are no scrollbars.
## Type: Bool
# c.completion.shrink = False

# Format of timestamps (e.g. for the history completion). See
# https://sqlite.org/lang_datefunc.html and
# https://docs.python.org/3/library/datetime.html#strftime-strptime-
# behavior for allowed substitutions, qutebrowser uses both sqlite and
# Python to format its timestamps.
## Type: String
# c.completion.timestamp_format = '%Y-%m-%d %H:%M'

# Execute the best-matching command on a partial match.
## Type: Bool
# c.completion.use_best_match = False

# A list of patterns which should not be shown in the history. This only
# affects the completion. Matching URLs are still saved in the history
# (and visible on the `:history` page), but hidden in the completion.
# Changing this setting will cause the completion history to be
# regenerated on the next start, which will take a short while.
# Type: List of UrlPattern
# c.completion.web_history.exclude = []

# Number of URLs to show in the web history. 0: no history / -1:
# unlimited
## Type: Int
# c.completion.web_history.max_items = -1

# Set fullscreen notification overlay timeout in milliseconds. If set to
# 0, no overlay will be displayed.
## Type: Int
# c.content.fullscreen.overlay_timeout = 3000

# Limit fullscreen to the browser window (does not expand to fill the
# screen).
## Type: Bool
# c.content.fullscreen.window = False

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
## Type: String
# c.content.headers.accept_language = 'en-US,en;q=0.9'

# Custom headers for qutebrowser HTTP requests.
## Type: Dict
# c.content.headers.custom = {}

# Value to send in the `DNT` header. When this is set to true,
# qutebrowser asks websites to not track your identity. If set to null,
# the DNT header is not sent at all.
## Type: Bool
# c.content.headers.do_not_track = True

# When to send the Referer header. The Referer header tells websites
# from which website you were coming from when visiting them. No restart
# is needed with QtWebKit.
## Type: String
# Valid values:
# - always: Always send the Referer.
# - never: Never send the Referer. This is not recommended, as some sites may break.
# - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
# c.content.headers.referer = 'same-domain'

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
## Type: FormatString
# c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}'

c.tabs.background = True

c.tabs.close_mouse_button = 'middle'

c.tabs.close_mouse_button_on_bar = 'new-tab'

# c.tabs.favicons.scale = 1.0

c.tabs.favicons.show = 'always'

# c.tabs.focus_stack_size = 10

c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}

c.tabs.indicator.width = 3

c.tabs.last_close = 'startpage'

c.tabs.max_width = 200

# c.tabs.min_width = -1

c.tabs.mode_on_change = 'normal'

c.tabs.mousewheel_switching = True

c.tabs.new_position.related = 'next'

# c.tabs.new_position.stacking = True

c.tabs.new_position.unrelated = 'last'

# c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 5, 'right': 5}

c.tabs.pinned.frozen = True

c.tabs.pinned.shrink = True

c.tabs.position = 'top'

c.tabs.select_on_remove = 'next'

c.tabs.show = 'multiple'

# c.tabs.show_switching_delay = 800

c.tabs.tabs_are_windows = False

c.tabs.title.alignment = 'left'

c.tabs.title.format = '{audio}{private} {current_title}'

c.tabs.title.format_pinned = '{audio}{private}'

# c.tabs.tooltips = True

# c.tabs.undo_stack_size = 100

# c.tabs.width = '15%'

c.tabs.wrap = True

# Default zoom level.
## Type: Perc
# c.zoom.default = '100%'

# Available zoom levels.
# Type: List of Perc
# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

# Number of zoom increments to divide the mouse wheel movements to.
## Type: Int
# c.zoom.mouse_divider = 512

# Apply the zoom factor on a frame only to the text or to all content.
## Type: Bool
# c.zoom.text_only = False

# Require a confirmation before quitting the application.
## Type: ConfirmQuit
# Valid values:
# - always: Always show a confirmation.
# - multiple-tabs: Show a confirmation if multiple tabs are opened.
# - downloads: Show a confirmation if downloads are running
# - never: Never show a confirmation.
c.confirm_quit = ['downloads']

# Automatically start playing `<video>` elements.
## Type: Bool
c.content.autoplay = False

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
## Type: String
# c.content.default_encoding = 'iso-8859-1'

# Try to pre-fetch DNS entries to speed up browsing.
## Type: Bool
c.content.dns_prefetch = True

# Expand each subframe to its contents. This will flatten all the frames
# to become one scrollable page.
## Type: Bool
# c.content.frame_flattening = False

# Enable hyperlink auditing (`<a ping>`).
## Type: Bool
# c.content.hyperlink_auditing = False

# Load images automatically in web pages.
## Type: Bool
# c.content.images = True

# Allow locally loaded documents to access other local URLs.
## Type: Bool
# c.content.local_content_can_access_file_urls = True

# Allow locally loaded documents to access remote URLs.
## Type: Bool
# c.content.local_content_can_access_remote_urls = False

# Automatically mute tabs. Note that if the `:tab-mute` command is used,
# the mute status for the affected tab is now controlled manually, and
# this setting doesn't have any effect.
## Type: Bool
# c.content.mute = False

# Netrc-file for HTTP authentication. If unset, `~/.netrc` is used.
## Type: File
# c.content.netrc_file = None

c.new_instance_open_target = 'tab'

c.new_instance_open_target_window = 'last-focused'

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
## Type: Directory
c.downloads.location.directory = None

# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
## Type: Bool
c.downloads.location.prompt = True

# Remember the last used download directory.
## Type: Bool
c.downloads.location.remember = True

# What to display in the download filename input.
## Type: String
# Valid values:
# - path: Show only the download path.
# - filename: Show only download filename.
# - both: Show download path and filename.
c.downloads.location.suggestion = 'path'

# Default program used to open downloads. If null, the default internal
# handler is used. Any `{}` in the string will be expanded to the
# filename, else the filename will be appended.
## Type: String
# c.downloads.open_dispatcher = None

# Where to show the downloaded files.
## Type: VerticalPosition
# Valid values:
##   - top
##   - bottom
c.downloads.position = 'bottom'

# Duration (in milliseconds) to wait before removing finished downloads.
# If set to -1, downloads are never removed.
## Type: Int
c.downloads.remove_finished = -1

# Show a filebrowser in download prompts.
## Type: Bool
c.prompt.filebrowser = True

# Rounding radius (in pixels) for the edges of prompts.
## Type: Int
c.prompt.radius = 0

c.url.auto_search = 'naive'

c.url.default_page = 'https://search.brave.com/'

# c.url.incdec_segments = ['path', 'query']

c.url.open_base_url = True

c.url.searchengines = {
    "DEFAULT": "https://search.brave.com/search?q={}",
    "ArchWiki": "https://wiki.archlinux.org/index.php?search={}",
    "QtileDocs": "http://docs.qtile.org/en/latest/search.html?q{}&check_keywords=yes&area=default",
    "GitHub": "https://github.com/search?q={}&ref=opensearch",
    "YouTube": "https://www.youtube.com/results?search_query={}",
    "Odysee": "https://odysee.com/$/search?q={}",
    "GoogleDrive": "https://drive.google.com/drive/search?q={}",
    "GoogleMaps": "https://www.google.com/maps/search/{}?hl=en&source=opensearch",
    "GoogleImages": "https://www.google.com/search?q={}",
    "Google": "https://www.google.com/search?q={}",
    "AmazonUK": "https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}",
    "AmazonCOM": "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}",
    "AmazonCA": "https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}",
}

c.url.start_pages = ["https://search.brave.com"]

# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

# c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}

c.auto_save.session = True

c.auto_save.interval = 15000

# Number of commands to save in the command history. 0: no history / -1:
# unlimited
## Type: Int
# c.completion.cmd_history_max_items = 100

# c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Ctrl-I>': '<Tab>', '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}

config.unbind('<Ctrl-Q>')
config.unbind('ZQ')
config.unbind('ZZ')

config.unbind('gf')

config.unbind('tCH')
config.unbind('tCh')
config.unbind('tCu')
config.unbind('tIH')
config.unbind('tIh')
config.unbind('tIu')
config.unbind('tPH')
config.unbind('tPh')
config.unbind('tPu')
config.unbind('tSH')
config.unbind('tSh')
config.unbind('tSu')
config.unbind('tcH')
config.unbind('tch')
config.unbind('tcu')
config.unbind('tiH')
config.unbind('tih')
config.unbind('tiu')
config.unbind('tpH')
config.unbind('tph')
config.unbind('tpu')
config.unbind('tsH')
config.unbind('tsh')
config.unbind('tsu')

config.unbind('-')
config.unbind('+')
config.unbind('=')

config.unbind('ga')

config.unbind('d')
config.unbind('D')

config.unbind('T')

config.unbind('xo')
config.unbind('xO')

config.unbind('gm')
config.unbind('g$')
config.unbind('g0')
config.unbind('g^')
config.unbind('gC')
config.unbind('gD')
config.unbind('gJ')
config.unbind('gK')
config.unbind('co')

config.unbind('ad')
config.unbind('gd')

config.unbind('Sh')

config.unbind('b')
config.unbind('B')
config.unbind('M')
config.unbind('Sq')
config.unbind('Sb')

config.unbind(';r')
config.unbind(';R')
config.unbind(';d')
config.unbind(';I')
config.unbind(';t')
config.unbind(';y')
config.unbind(';Y')
config.unbind('gi')

config.bind('Ss', 'set')
config.bind('ss', 'set-cmd-text -s :set')
config.bind('sl', 'set-cmd-text -s :set -t')

config.bind('sk', 'set-cmd-text -s :bind')
config.bind('<F1>', 'help -t')

config.bind('<Ctrl-Shift-Tab>', 'nop')

config.bind('sf', 'save')

config.bind('ws', 'view-source')

config.bind('wi', 'devtools')
config.bind('wIf', 'devtools-focus')

config.bind('wIh', 'devtools left')
config.bind('wIl', 'devtools right')
config.bind('wIj', 'devtools bottom')
config.bind('wIk', 'devtools top')
config.bind('wIw', 'devtools window')

config.bind('zCH', 'config-cycle -p -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
config.bind('zCh', 'config-cycle -p -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
config.bind('zCu', 'config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload')
config.bind('zIH', 'config-cycle -p -u *://*.{url:host}/* content.images ;; reload')
config.bind('zIh', 'config-cycle -p -u *://{url:host}/* content.images ;; reload')
config.bind('zIu', 'config-cycle -p -u {url} content.images ;; reload')
config.bind('zPH', 'config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload')
config.bind('zPh', 'config-cycle -p -u *://{url:host}/* content.plugins ;; reload')
config.bind('zPu', 'config-cycle -p -u {url} content.plugins ;; reload')
config.bind('zSH', 'config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload')
config.bind('zSh', 'config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload')
config.bind('zSu', 'config-cycle -p -u {url} content.javascript.enabled ;; reload')
config.bind('zcH', 'config-cycle -p -t -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
config.bind('zch', 'config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
config.bind('zcu', 'config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload')
config.bind('ziH', 'config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload')
config.bind('zih', 'config-cycle -p -t -u *://{url:host}/* content.images ;; reload')
config.bind('ziu', 'config-cycle -p -t -u {url} content.images ;; reload')
config.bind('zpH', 'config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload')
config.bind('zph', 'config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload')
config.bind('zpu', 'config-cycle -p -t -u {url} content.plugins ;; reload')
config.bind('zsH', 'config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload')
config.bind('zsh', 'config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload')
config.bind('zsu', 'config-cycle -p -t -u {url} content.javascript.enabled ;; reload')

config.bind('h', 'scroll left')
config.bind('j', 'scroll down')
config.bind('k', 'scroll up')
config.bind('l', 'scroll right')

config.bind('<Ctrl-B>', 'scroll-page 0 -1')
config.bind('<Ctrl-F>', 'scroll-page 0 1')
config.bind('<Ctrl-U>', 'scroll-page 0 -0.5')
config.bind('<Ctrl-D>', 'scroll-page 0 0.5')

config.bind('gg', 'scroll-to-perc 0')
config.bind('G', 'scroll-to-perc')

config.bind('<Ctrl-A>', 'navigate increment')
config.bind('<Ctrl-X>', 'navigate decrement')
config.bind('gu', 'navigate up')
config.bind('gU', 'navigate up -t')
config.bind('[[', 'navigate prev')
config.bind(']]', 'navigate next')
config.bind('{{', 'navigate prev -t')
config.bind('}}', 'navigate next -t')

config.bind('<Ctrl-0>', 'zoom')
config.bind('<Ctrl-->', 'zoom-out')
config.bind('<Ctrl-=>', 'zoom-in')

config.bind('<Alt-x>', 'set-cmd-text :')
config.bind(':', 'set-cmd-text :')
config.bind('/', 'set-cmd-text /')
config.bind('?', 'set-cmd-text ?')
config.bind('.', 'repeat-command')

config.bind('n', 'search-next')
config.bind('N', 'search-prev')

config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave ;; clear-messages')

config.bind('r', 'reload')
config.bind('R', 'reload -f')
config.bind('<F5>', 'reload')
config.bind('<Ctrl-F5>', 'reload -f')

config.bind('<F11>', 'fullscreen')

config.bind('q', 'macro-record')
config.bind('@', 'macro-run')

config.bind('wh', 'back -w')
config.bind('wl', 'forward -w')

config.bind('wf', 'hint all window')
config.bind('wo', 'set-cmd-text -s :open -w')
config.bind('wO', 'set-cmd-text :open -w {url:pretty}')

config.bind('wb', 'set-cmd-text -s :quickmark-load -w')
config.bind('wB', 'set-cmd-text -s :bookmark-load -w')

config.bind('wp', 'open -w -- {clipboard}')
config.bind('wP', 'open -w -- {primary}')

config.bind('<Ctrl-N>', 'open -w')
config.bind('<Ctrl-Shift-W>', 'close')

config.bind('U', 'undo -w')

config.bind('<back>', 'back')
config.bind('<forward>', 'forward')
config.bind('H', 'back')
config.bind('L', 'forward')

config.bind('tH', 'back -t')
config.bind('tL', 'forward -t')

config.bind('<Ctrl-h>', 'home')

config.bind('<Ctrl-T>', 'open -t')
config.bind('tn', 'open -t')

config.bind('o', 'set-cmd-text -s :open')

config.bind('O', 'set-cmd-text -s :open -t')
config.bind('gs', 'set-cmd-text -s :open -b')

config.bind('go', 'set-cmd-text :open {url:pretty}')

config.bind('gO', 'set-cmd-text :open -t -r {url:pretty}')
config.bind('gS', 'set-cmd-text :open -b -r {url:pretty}')

config.bind('pp', 'open -- {clipboard}')
config.bind('pP', 'open -- {primary}')

config.bind('Pp', 'open -t -- {clipboard}')
config.bind('PP', 'open -t -- {primary}')

config.bind('<Return>', 'selection-follow')

config.bind('<Ctrl-Return>', 'selection-follow -t')

config.bind('t0', 'tab-focus 1')
config.bind('t^', 'tab-focus 1')
config.bind('<Alt-1>', 'tab-focus 1')
config.bind('<Alt-2>', 'tab-focus 2')
config.bind('<Alt-3>', 'tab-focus 3')
config.bind('<Alt-4>', 'tab-focus 4')
config.bind('<Alt-5>', 'tab-focus 5')
config.bind('<Alt-6>', 'tab-focus 6')
config.bind('<Alt-7>', 'tab-focus 7')
config.bind('<Alt-8>', 'tab-focus 8')
config.bind('<Alt-9>', 'tab-focus 9')
config.bind('<Alt-0>', 'tab-focus -1')
config.bind('t$', 'tab-focus -1')
config.bind('<Ctrl-Tab>', 'tab-focus last')
config.bind('<Ctrl-^>', 'tab-focus last')

config.bind('<Ctrl-PgDown>', 'tab-next')
config.bind('<Ctrl-PgUp>', 'tab-prev')
config.bind('J', 'tab-next')
config.bind('K', 'tab-prev')

config.bind('gt', 'set-cmd-text -sr :tab-focus')

config.bind('<Ctrl-W>', 'tab-close')
config.bind('x', 'tab-close')
config.bind('tc', 'tab-close')
config.bind('tO', 'tab-only')

config.bind('<Ctrl-Shift-T>', 'undo')
config.bind('u', 'undo')
config.bind('X', 'undo')

config.bind('tm', 'tab-move')
config.bind('tJ', 'tab-move +')
config.bind('tK', 'tab-move -')
config.bind('>', 'tab-move +')
config.bind('<', 'tab-move -')

config.bind('<Ctrl-c>', 'stop')
config.bind('<Ctrl-m>', 'tab-mute')
config.bind('<Ctrl-p>', 'tab-pin')
config.bind('tp', 'tab-pin')
config.bind('tC', 'tab-clone')
config.bind('tP', 'tab-give')
config.bind('<Ctrl-Alt-p>', 'print')

config.bind('D', 'set-cmd-text -s :download')

config.bind('di', 'hint images download')
config.bind('dl', 'hint links download')

config.bind('ds', 'download-cancel')
config.bind('dC', 'download-cancel')

config.bind('dx', 'download-remove')
config.bind('dr', 'download-retry')
config.bind('dc', 'download-clear')

config.bind('do', 'download-open')
config.bind('dX', 'download-delete')

config.bind('<Ctrl-P>', 'prompt-open-download --pdfjs', mode='prompt')
config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')

config.bind('gh', 'history -t')

config.bind('gq', 'bookmark-list')
config.bind('gb', 'bookmark-list')
config.bind('gB', 'bookmark-list --jump')

config.bind('bo', 'set-cmd-text -s :quickmark-load')
config.bind('Bo', 'set-cmd-text -s :bookmark-load')

config.bind('bO', 'set-cmd-text -s :quickmark-load -t')
config.bind('BO', 'set-cmd-text -s :bookmark-load -t')

config.bind('bs', 'quickmark-save')
config.bind('Bs', 'bookmark-add')
config.bind('ba', 'quickmark-add')
config.bind('Ba', 'bookmark-add')

config.bind('bd', 'quickmark-del')
config.bind('Bd', 'bookmark-del')

config.bind('f', 'hint')
config.bind('F', 'hint all tab')

config.bind(';i', 'hint inputs')

config.bind(';p', 'hint images')
config.bind(';P', 'hint images tab')

config.bind(';h', 'hint all hover')

config.bind(';ri', 'hint --rapid images tab-bg')
config.bind(';Ri', 'hint --rapid images window')

config.bind(';rl', 'hint --rapid links tab-bg')
config.bind(';Rl', 'hint --rapid links window')

config.bind(';o', 'hint links fill :open {hint-url}')
config.bind(';O', 'hint links fill :open -t -r {hint-url}')

config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
config.bind('<Ctrl-F>', 'hint links', mode='hint')
config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
config.bind('<Return>', 'hint-follow', mode='hint')

config.bind('cm', 'clear-messages')

config.bind('yy', 'yank')
config.bind('Yy', 'yank -s')

config.bind('yp', 'yank pretty-url')
config.bind('Yp', 'yank pretty-url -s')

config.bind('yd', 'yank domain')
config.bind('Yd', 'yank domain -s')

config.bind('yt', 'yank title')
config.bind('Yt', 'yank title -s')

config.bind('ym', 'yank inline [{title}]({url})')
config.bind('Ym', 'yank inline [{title}]({url}) -s')

config.bind('yo', 'yank inline [[{url}][{title}]]')
config.bind('Yo', 'yank inline [[{url}][{title}]] -s')

config.bind('yl', 'hint links yank')
config.bind('Yl', 'hint links yank-primary')

config.bind('<Alt-p><a>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)"')
config.bind('<Alt-p><u>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --username-only')
config.bind('<Alt-p><p>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --password-only')
config.bind('<Alt-p><o>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --otp-only')

config.bind('<Alt-p><a>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)"', mode='insert')
config.bind('<Alt-p><u>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --username-only', mode='insert')
config.bind('<Alt-p><p>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --password-only', mode='insert')
config.bind('<Alt-p><o>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --otp-only', mode='insert')

config.bind('I', 'open --private')
config.bind('<Ctrl-Shift-N>', 'open -p')
config.bind('i', 'mode-enter insert')
config.bind('v', 'mode-enter caret')
config.bind('V', 'mode-enter caret ;; selection-toggle --line')
config.bind('<Ctrl-V>', 'mode-enter passthrough')
config.bind("'", 'mode-enter jump_mark')
config.bind('m', 'mode-enter set_mark')
config.bind('c', 'mode-enter normal', mode='caret')
config.bind('<Escape>', 'mode-leave', mode='caret')
config.bind('<Escape>', 'mode-leave', mode='insert')
config.bind('<Escape>', 'mode-leave', mode='command')
config.bind('<Escape>', 'mode-leave', mode='hint')
config.bind('<Escape>', 'mode-leave', mode='prompt')
config.bind('<Escape>', 'mode-leave', mode='register')
config.bind('<Escape>', 'mode-leave', mode='yesno')
config.bind('<Shift-Escape>', 'mode-leave', mode='passthrough')

config.bind('<Ctrl-k>', 'completion-item-focus prev', mode='command')
config.bind('<Ctrl-j>', 'completion-item-focus next', mode='command')

# config.bind('<Alt-B>', 'rl-backward-word', mode='command')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='command')
# config.bind('<Alt-D>', 'rl-kill-word', mode='command')
# config.bind('<Alt-F>', 'rl-forward-word', mode='command')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='command')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='command')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='command')
# config.bind('<Ctrl-C>', 'completion-item-yank', mode='command')
# config.bind('<Ctrl-D>', 'completion-item-del', mode='command')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='command')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='command')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='command')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='command')
# config.bind('<Ctrl-N>', 'command-history-next', mode='command')
# config.bind('<Ctrl-P>', 'command-history-prev', mode='command')
# config.bind('<Ctrl-Return>', 'command-accept --rapid', mode='command')
# config.bind('<Ctrl-Shift-C>', 'completion-item-yank --sel', mode='command')
# config.bind('<Ctrl-Shift-Tab>', 'completion-item-focus prev-category', mode='command')
# config.bind('<Ctrl-Tab>', 'completion-item-focus next-category', mode='command')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='command')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='command')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='command')
# config.bind('<Down>', 'completion-item-focus --history next', mode='command')
# config.bind('<PgDown>', 'completion-item-focus next-page', mode='command')
# config.bind('<PgUp>', 'completion-item-focus prev-page', mode='command')
# config.bind('<Return>', 'command-accept', mode='command')
# config.bind('<Shift-Delete>', 'completion-item-del', mode='command')
# config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
# config.bind('<Tab>', 'completion-item-focus next', mode='command')
# config.bind('<Up>', 'completion-item-focus --history prev', mode='command')

config.bind('<Tab>', 'prompt-item-focus next', mode='prompt')
config.bind('<Shift-Tab>', 'prompt-item-focus prev', mode='prompt')

config.bind('<Ctrl-k>', 'prompt-item-focus prev', mode='prompt')
config.bind('<Ctrl-j>', 'prompt-item-focus next', mode='prompt')
config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')
config.bind('<Down>', 'prompt-item-focus next', mode='prompt')

config.bind('<Return>', 'prompt-accept', mode='prompt')

config.bind('<Ctrl-W>', 'rl-backward-kill-word', mode='prompt')
config.bind('<Ctrl-Backspace>', 'rl-backward-kill-word', mode='prompt')
config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='prompt')

# config.bind('<Alt-B>', 'rl-backward-word', mode='prompt')
# config.bind('<Alt-D>', 'rl-kill-word', mode='prompt')
# config.bind('<Alt-F>', 'rl-forward-word', mode='prompt')
# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='prompt')
# config.bind('<Alt-Y>', 'prompt-yank', mode='prompt')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='prompt')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='prompt')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='prompt')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='prompt')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='prompt')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='prompt')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='prompt')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='prompt')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='prompt')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='prompt')

# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='yesno')
# config.bind('<Alt-Y>', 'prompt-yank', mode='yesno')
# config.bind('<Return>', 'prompt-accept', mode='yesno')
# config.bind('N', 'prompt-accept --save no', mode='yesno')
# config.bind('Y', 'prompt-accept --save yes', mode='yesno')
# config.bind('n', 'prompt-accept no', mode='yesno')
# config.bind('y', 'prompt-accept yes', mode='yesno')

# config.bind('$', 'move-to-end-of-line', mode='caret')
# config.bind('0', 'move-to-start-of-line', mode='caret')
# config.bind('<Ctrl-Space>', 'selection-drop', mode='caret')
# config.bind('<Return>', 'yank selection', mode='caret')
# config.bind('<Space>', 'selection-toggle', mode='caret')
# config.bind('G', 'move-to-end-of-document', mode='caret')
# config.bind('H', 'scroll left', mode='caret')
# config.bind('J', 'scroll down', mode='caret')
# config.bind('K', 'scroll up', mode='caret')
# config.bind('L', 'scroll right', mode='caret')
# config.bind('V', 'selection-toggle --line', mode='caret')
# config.bind('Y', 'yank selection -s', mode='caret')
# config.bind('[', 'move-to-start-of-prev-block', mode='caret')
# config.bind(']', 'move-to-start-of-next-block', mode='caret')
# config.bind('b', 'move-to-prev-word', mode='caret')
# config.bind('e', 'move-to-end-of-word', mode='caret')
# config.bind('gg', 'move-to-start-of-document', mode='caret')
# config.bind('h', 'move-to-prev-char', mode='caret')
# config.bind('j', 'move-to-next-line', mode='caret')
# config.bind('k', 'move-to-prev-line', mode='caret')
# config.bind('l', 'move-to-next-char', mode='caret')
# config.bind('o', 'selection-reverse', mode='caret')
# config.bind('v', 'selection-toggle', mode='caret')
# config.bind('w', 'move-to-next-word', mode='caret')
# config.bind('y', 'yank selection', mode='caret')
# config.bind('{', 'move-to-end-of-prev-block', mode='caret')
# config.bind('}', 'move-to-end-of-next-block', mode='caret')

# config.bind('<Ctrl-E>', 'edit-text', mode='insert')
# config.bind('<Shift-Ins>', 'insert-text -- {primary}', mode='insert')

# c.content.canvas_reading = True

c.content.blocking.enabled = True

c.content.blocking.method = "auto"

c.content.blocking.adblock.lists = [
    'https://easylist.to/easylist/easylist.txt',
    'https://easylist.to/easylist/easyprivacy.txt',
    # 'https://secure.fanboy.co.nz/fanboy-cookiemonster.txt',
    # 'https://easylist.to/easylist/fanboy-social.txt',
    # 'https://secure.fanboy.co.nz/fanboy-annoyance.txt',
]

# c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

c.content.blocking.whitelist = []

c.content.cookies.accept = "no-3rdparty"

c.content.cookies.store = True

c.content.local_storage = True

c.content.cache.appcache = True

# c.content.cache.maximum_pages = 0

# c.content.cache.size = None

# Allow websites to share screen content.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
c.content.desktop_capture = "ask"

# Allow websites to request geolocations.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
c.content.geolocation = "ask"

# Allow websites to record audio.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
c.content.media.audio_capture = "ask"

# Allow websites to record audio and video.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
c.content.media.audio_video_capture = "ask"

# Allow websites to record video.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
c.content.media.video_capture = "ask"

# Allow websites to lock your mouse pointer.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
c.content.mouse_lock = "ask"

# Allow websites to show notifications.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
c.content.notifications.enabled = "ask"

# Allow websites to request persistent storage quota via
# `navigator.webkitPersistentStorage.requestQuota`.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
c.content.persistent_storage = 'ask'

# Show javascript alerts.
## Type: Bool
# c.content.javascript.alert = True

# Allow JavaScript to read from or write to the clipboard. With
# QtWebEngine, writing the clipboard as response to a user interaction
# is always allowed.
## Type: Bool
# c.content.javascript.can_access_clipboard = False

# Allow JavaScript to close tabs.
## Type: Bool
# c.content.javascript.can_close_tabs = False

# Allow JavaScript to open new tabs without user interaction.
## Type: Bool
# c.content.javascript.can_open_tabs_automatically = False

# Enable JavaScript.
## Type: Bool
# c.content.javascript.enabled = True

# Log levels to use for JavaScript console logging messages. When a
# JavaScript message with the level given in the dictionary key is
# logged, the corresponding dictionary value selects the qutebrowser
# logger to use. On QtWebKit, the "unknown" setting is always used. The
# following levels are valid: `none`, `debug`, `info`, `warning`,
# `error`.
## Type: Dict
# c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}

# Use the standard JavaScript modal dialog for `alert()` and
# `confirm()`.
## Type: Bool
# c.content.javascript.modal_dialog = False

# Show javascript prompts.
## Type: Bool
# c.content.javascript.prompt = True

# What notification presenter to use for web notifications. Note that
# not all implementations support all features of notifications: - With
# PyQt 5.14, any setting other than `qt` does not support  the `click`
# and   `close` events, as well as the `tag` option to replace existing
# notifications. - The `qt` and `systray` options only support showing
# one notification at the time   and ignore the `tag` option to replace
# existing notifications. - The `herbe` option only supports showing one
# notification at the time and doesn't   show icons. - The `messages`
# option doesn't show icons and doesn't support the `click` and
# `close` events.
## Type: String
# Valid values:
# - auto: Tries `libnotify`, `systray` and `messages`, uses the first one available without showing error messages.
# - qt: Use Qt's native notification presenter, based on a system tray icon. Switching from or to this value requires a restart of qutebrowser. Recommended over `systray` on PyQt 5.14.
# - libnotify: Shows messages via DBus in a libnotify-compatible way. If DBus isn't available, falls back to `systray` or `messages`, but shows an error message.
# - systray: Use a notification presenter based on a systray icon. Falls back to `libnotify` or `messages` if not systray is available. This is a reimplementation of the `qt` setting value, but with the possibility to switch to it at runtime.
# - messages: Show notifications as qutebrowser messages. Most notification features aren't available.
# - herbe: (experimental!) Show notifications using herbe (github.com/dudik/herbe). Most notification features aren't available.
# c.content.notifications.presenter = 'auto'

# Whether to show the origin URL for notifications. Note that URL
# patterns with this setting only get matched against the origin part of
# the URL, so e.g. paths in patterns will never match. Note that with
# the `qt` presenter, origins are never shown.
## Type: Bool
# c.content.notifications.show_origin = True

c.spellcheck.languages = [
    "en-US",
    "ru-RU",
]

# Padding (in pixels) for the statusbar.
## Type: Padding
# c.statusbar.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 0}

# Position of the status bar.
## Type: VerticalPosition
# Valid values:
##   - top
##   - bottom
# c.statusbar.position = 'bottom'

# When to show the statusbar.
## Type: String
# Valid values:
# - always: Always show the statusbar.
# - never: Always hide the statusbar.
# - in-mode: Show the statusbar when in modes other than normal mode.
# c.statusbar.show = 'always'

# List of widgets displayed in the statusbar.
# Type: List of StatusbarWidget
# Valid values:
# - url: Current page URL.
# - scroll: Percentage of the current page position like `10%`.
# - scroll_raw: Raw percentage of the current page position like `10`.
# - history: Display an arrow when possible to go back/forward in history.
# - tabs: Current active tab, e.g. `2`.
# - keypress: Display pressed keys when composing a vi command.
# - progress: Progress bar for the current page loading.
# - text:foo: Display the static text after the colon, `foo` in the example.
# c.statusbar.widgets = ['keypress', 'url', 'scroll', 'history', 'tabs', 'progress']

# Allow pdf.js to view PDF files in the browser. Note that the files can
# still be downloaded by clicking the download button in the pdf.js
# viewer.
## Type: Bool
# c.content.pdfjs = False

# Enable plugins in Web pages.
## Type: Bool
# c.content.plugins = False

# Request websites to minimize non-essentials animations and motion.
# This results in the `prefers-reduced-motion` CSS media query to
# evaluate to `reduce` (rather than `no-preference`). On Windows, if
# this setting is set to False, the system-wide animation setting is
# considered.
## Type: Bool
# c.content.prefers_reduced_motion = False

# Draw the background color and images also when the page is printed.
## Type: Bool
# c.content.print_element_backgrounds = True

# Open new windows in private browsing mode which does not record
# visited pages.
## Type: Bool
# c.content.private_browsing = False

# Proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL. Note that with QtWebEngine, it will
# take a couple of seconds until the change is applied, if this value is
# changed at runtime.
## Type: Proxy
# Valid values:
# - system: Use the system wide proxy.
# - none: Don't use any proxy
# c.content.proxy = 'system'

# Send DNS requests over the configured proxy.
## Type: Bool
# c.content.proxy_dns_requests = True

# Allow websites to register protocol handlers via
# `navigator.registerProtocolHandler`.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
# c.content.register_protocol_handler = 'ask'

# Enable quirks (such as faked user agent headers) needed to get
# specific sites to work properly.
## Type: Bool
# c.content.site_specific_quirks.enabled = True

# Disable a list of named quirks. The js-string-replaceall quirk is
# needed for Nextcloud Calendar < 2.2.0 with QtWebEngine < 5.15.3.
# However, the workaround is not fully compliant to the ECMAScript spec
# and might cause issues on other websites, so it's disabled by default.
## Type: FlagList
# Valid values:
##   - ua-whatsapp
##   - ua-google
##   - ua-slack
##   - ua-googledocs
##   - js-whatsapp-web
##   - js-discord
##   - js-string-replaceall
##   - js-globalthis
##   - js-object-fromentries
##   - misc-krunker
##   - misc-mathml-darkmode
# c.content.site_specific_quirks.skip = ['js-string-replaceall']

# How to proceed on TLS certificate errors.
## Type: String
# Valid values:
# - ask: Ask how to proceed for every certificate error (unless non-overridable due to HSTS).
# - ask-block-thirdparty: Ask how to proceed for normal page loads, but silently block resource loads.
# - block: Automatically block loading on certificate errors.
# - load-insecurely: Force loading pages despite certificate errors. This is *insecure* and should be avoided. Instead of using this, consider fixing the underlying issue or importing a self-signed certificate via `certutil` (or Chromium) instead.
# c.content.tls.certificate_errors = 'ask'

# How navigation requests to URLs with unknown schemes are handled.
## Type: String
# Valid values:
# - disallow: Disallows all navigation requests to URLs with unknown schemes.
# - allow-from-user-interaction: Allows navigation requests to URLs with unknown schemes that are issued from user-interaction (like a mouse-click), whereas other navigation requests (for example from JavaScript) are suppressed.
# - allow-all: Allows all navigation requests to URLs with unknown schemes.
# c.content.unknown_url_scheme_policy = 'allow-from-user-interaction'

# List of user stylesheet filenames to use.
# Type: List of File, or File
# c.content.user_stylesheets = []

# Enable WebGL.
## Type: Bool
# c.content.webgl = True

# Which interfaces to expose via WebRTC.
## Type: String
# Valid values:
# - all-interfaces: WebRTC has the right to enumerate all interfaces and bind them to discover public interfaces.
# - default-public-and-private-interfaces: WebRTC should only use the default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
# - default-public-interface-only: WebRTC should only use the default route used by http. This doesn't expose any local addresses.
# - disable-non-proxied-udp: WebRTC should only use TCP to contact peers or servers unless the proxy server supports UDP. This doesn't expose any local addresses either.
# c.content.webrtc_ip_handling_policy = 'all-interfaces'

# Monitor load requests for cross-site scripting attempts. Suspicious
# scripts will be blocked and reported in the devtools JavaScript
# console. Note that bypasses for the XSS auditor are widely known and
# it can be abused for cross-site info leaks in some scenarios, see:
# https://www.chromium.org/developers/design-documents/xss-auditor
## Type: Bool
# c.content.xss_auditing = False

# Editor (and arguments) to use for the `edit-*` commands. The following
# placeholders are defined:  * `{file}`: Filename of the file to be
# edited. * `{line}`: Line in which the caret is found in the text. *
# `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
## Type: ShellCommand
# c.editor.command = ['gvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

# Encoding to use for the editor.
## Type: Encoding
# c.editor.encoding = 'utf-8'

# Command (and arguments) to use for selecting a single folder in forms.
# The command should write the selected folder path to the specified
# file or stdout. The following placeholders are defined: * `{}`:
# Filename of the file to be written to. If not contained in any
# argument, the   standard output of the command is read instead.
## Type: ShellCommand
# c.fileselect.folder.command = ['xterm', '-e', 'ranger', '--choosedir={}']

# Handler for selecting file(s) in forms. If `external`, then the
# commands specified by `fileselect.single_file.command` and
# `fileselect.multiple_files.command` are used to select one or multiple
# files respectively.
## Type: String
# Valid values:
# - default: Use the default file selector.
# - external: Use an external command.
# c.fileselect.handler = 'default'

# Command (and arguments) to use for selecting multiple files in forms.
# The command should write the selected file paths to the specified file
# or to stdout, separated by newlines. The following placeholders are
# defined: * `{}`: Filename of the file to be written to. If not
# contained in any argument, the   standard output of the command is
# read instead.
## Type: ShellCommand
# c.fileselect.multiple_files.command = ['xterm', '-e', 'ranger', '--choosefiles={}']

# Command (and arguments) to use for selecting a single file in forms.
# The command should write the selected file path to the specified file
# or stdout. The following placeholders are defined: * `{}`: Filename of
# the file to be written to. If not contained in any argument, the
# standard output of the command is read instead.
## Type: ShellCommand
# c.fileselect.single_file.command = ['xterm', '-e', 'ranger', '--choosefile={}']

# When a hint can be automatically followed without pressing Enter.
## Type: String
# Valid values:
# - always: Auto-follow whenever there is only a single hint on a page.
# - unique-match: Auto-follow whenever there is a unique non-empty match in either the hint string (word mode) or filter (number mode).
# - full-match: Follow the hint when the user typed the whole hint (letter, word or number mode) or the element's text (only in number mode).
# - never: The user will always need to press Enter to follow a hint.
# c.hints.auto_follow = 'unique-match'

# Duration (in milliseconds) to ignore normal-mode key bindings after a
# successful auto-follow.
## Type: Int
# c.hints.auto_follow_timeout = 0

# CSS border value for hints.
## Type: String
# c.hints.border = '1px solid #E3BE23'

# Characters used for hint strings.
## Type: UniqueCharString
# c.hints.chars = 'asdfghjkl'

# Dictionary file to be used by the word hints.
## Type: File
# c.hints.dictionary = '/usr/share/dict/words'

# Which implementation to use to find elements to hint.
## Type: String
# Valid values:
# - javascript: Better but slower
# - python: Slightly worse but faster
# c.hints.find_implementation = 'python'

# Hide unmatched hints in rapid mode.
## Type: Bool
# c.hints.hide_unmatched_rapid_hints = True

# Leave hint mode when starting a new page load.
## Type: Bool
# c.hints.leave_on_load = False

# Minimum number of characters used for hint strings.
## Type: Int
# c.hints.min_chars = 1

# Mode to use for hints.
## Type: String
# Valid values:
# - number: Use numeric hints. (In this mode you can also type letters from the hinted element to filter and reduce the number of elements that are hinted.)
# - letter: Use the characters in the `hints.chars` setting.
# - word: Use hints words based on the html elements and the extra words.
# c.hints.mode = 'letter'

# Comma-separated list of regular expressions to use for 'next' links.
# Type: List of Regex
# c.hints.next_regexes = ['\\bnext\\b', '\\bmore\\b', '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b']

# Padding (in pixels) for hints.
## Type: Padding
# c.hints.padding = {'top': 0, 'bottom': 0, 'left': 3, 'right': 3}

# Comma-separated list of regular expressions to use for 'prev' links.
# Type: List of Regex
# c.hints.prev_regexes = ['\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b']

# Rounding radius (in pixels) for the edges of hints.
## Type: Int
# c.hints.radius = 3

# Scatter hint key chains (like Vimium) or not (like dwb). Ignored for
# number hints.
## Type: Bool
# c.hints.scatter = True

# CSS selectors used to determine which elements on a page should have
# hints.
## Type: Dict
# c.hints.selectors = {'all': ['a', 'area', 'textarea', 'select', 'input:not([type="hidden"])', 'button', 'frame', 'iframe', 'img', 'link', 'summary', '[contenteditable]:not([contenteditable="false"])', '[onclick]', '[onmousedown]', '[role="link"]', '[role="option"]', '[role="button"]', '[ng-click]', '[ngClick]', '[data-ng-click]', '[x-ng-click]', '[tabindex]'], 'links': ['a[href]', 'area[href]', 'link[href]', '[role="link"][href]'], 'images': ['img'], 'media': ['audio', 'img', 'video'], 'url': ['[src]', '[href]'], 'inputs': ['input[type="text"]', 'input[type="date"]', 'input[type="datetime-local"]', 'input[type="email"]', 'input[type="month"]', 'input[type="number"]', 'input[type="password"]', 'input[type="search"]', 'input[type="tel"]', 'input[type="time"]', 'input[type="url"]', 'input[type="week"]', 'input:not([type])', '[contenteditable]:not([contenteditable="false"])', 'textarea']}

# Make characters in hint strings uppercase.
## Type: Bool
# c.hints.uppercase = False

# Allow Escape to quit the crash reporter.
## Type: Bool
# c.input.escape_quits_reporter = True

# Which unbound keys to forward to the webview in normal mode.
## Type: String
# Valid values:
# - all: Forward all unbound keys.
# - auto: Forward unbound non-alphanumeric keys.
# - none: Don't forward any keys.
# c.input.forward_unbound_keys = 'auto'

# Enter insert mode if an editable element is clicked.
## Type: Bool
# c.input.insert_mode.auto_enter = True

# Leave insert mode if a non-editable element is clicked.
## Type: Bool
# c.input.insert_mode.auto_leave = True

# Automatically enter insert mode if an editable element is focused
# after loading the page.
## Type: Bool
# c.input.insert_mode.auto_load = False

# Leave insert mode when starting a new page load. Patterns may be
# unreliable on this setting, and they may match the url you are
# navigating to, or the URL you are navigating from.
## Type: Bool
# c.input.insert_mode.leave_on_load = True

# Switch to insert mode when clicking flash and other plugins.
## Type: Bool
# c.input.insert_mode.plugins = False

# Include hyperlinks in the keyboard focus chain when tabbing.
## Type: Bool
# c.input.links_included_in_focus_chain = True

# Whether the underlying Chromium should handle media keys. On Linux,
# disabling this also disables Chromium's MPRIS integration.
## Type: Bool
# c.input.media_keys = True

# Enable back and forward buttons on the mouse.
## Type: Bool
# c.input.mouse.back_forward_buttons = True

# Enable Opera-like mouse rocker gestures. This disables the context
# menu.
## Type: Bool
# c.input.mouse.rocker_gestures = False

# Timeout (in milliseconds) for partially typed key bindings. If the
# current input forms only partial matches, the keystring will be
# cleared after this time. If set to 0, partially typed bindings are
# never cleared.
## Type: Int
# c.input.partial_timeout = 0

# Enable spatial navigation. Spatial navigation consists in the ability
# to navigate between focusable elements in a Web page, such as
# hyperlinks and form controls, by using Left, Right, Up and Down arrow
# keys. For example, if the user presses the Right key, heuristics
# determine whether there is an element he might be trying to reach
# towards the right and which element he probably wants.
## Type: Bool
# c.input.spatial_navigation = False

# Keychains that shouldn't be shown in the keyhint dialog. Globs are
# supported, so `;*` will blacklist all keychains starting with `;`. Use
# `*` to disable keyhints.
# Type: List of String
# c.keyhint.blacklist = []

# Time (in milliseconds) from pressing a key to seeing the keyhint
# dialog.
## Type: Int
# c.keyhint.delay = 500

# Rounding radius (in pixels) for the edges of the keyhint dialog.
## Type: Int
# c.keyhint.radius = 6

# Maximum time (in minutes) between two history items for them to be
# considered being from the same browsing session. Items with less time
# between them are grouped when being displayed in `:history`. Use -1 to
# disable separation.
## Type: Int
# c.history_gap_interval = 30

# Level for console (stdout/stderr) logs. Ignored if the `--loglevel` or
# `--debug` CLI flags are used.
## Type: LogLevel
# Valid values:
##   - vdebug
##   - debug
##   - info
##   - warning
##   - error
##   - critical
# c.logging.level.console = 'info'

# Level for in-memory logs.
## Type: LogLevel
# Valid values:
##   - vdebug
##   - debug
##   - info
##   - warning
##   - error
##   - critical
# c.logging.level.ram = 'debug'

# Additional arguments to pass to Qt, without leading `--`. With
# QtWebEngine, some Chromium arguments (see
# https://peter.sh/experiments/chromium-command-line-switches/ for a
# list) will work.
# Type: List of String
# c.qt.args = []

# Additional environment variables to set. Setting an environment
# variable to null/None will unset it.
## Type: Dict
# c.qt.environ = {}

# Force a Qt platform to use. This sets the `QT_QPA_PLATFORM`
# environment variable and is useful to force using the XCB plugin when
# running QtWebEngine on Wayland.
## Type: String
# c.qt.force_platform = None

# Force a Qt platformtheme to use. This sets the `QT_QPA_PLATFORMTHEME`
# environment variable which controls dialogs like the filepicker. By
# default, Qt determines the platform theme based on the desktop
# environment.
## Type: String
# c.qt.force_platformtheme = None

# Force software rendering for QtWebEngine. This is needed for
# QtWebEngine to work with Nouveau drivers and can be useful in other
# scenarios related to graphic issues.
## Type: String
# Valid values:
# - software-opengl: Tell LibGL to use a software implementation of GL (`LIBGL_ALWAYS_SOFTWARE` / `QT_XCB_FORCE_SOFTWARE_OPENGL`)
# - qt-quick: Tell Qt Quick to use a software renderer instead of OpenGL. (`QT_QUICK_BACKEND=software`)
# - chromium: Tell Chromium to disable GPU support and use Skia software rendering instead. (`--disable-gpu`)
# - none: Don't force software rendering.
# c.qt.force_software_rendering = 'none'

# Turn on Qt HighDPI scaling. This is equivalent to setting
# QT_AUTO_SCREEN_SCALE_FACTOR=1 or QT_ENABLE_HIGHDPI_SCALING=1 (Qt >=
# 5.14) in the environment. It's off by default as it can cause issues
# with some bitmap fonts. As an alternative to this, it's possible to
# set font sizes and the `zoom.default` setting.
## Type: Bool
# c.qt.highdpi = False

# When to use Chromium's low-end device mode. This improves the RAM
# usage of renderer processes, at the expense of performance.
## Type: String
# Valid values:
# - always: Always use low-end device mode.
# - auto: Decide automatically (uses low-end mode with < 1 GB available RAM).
# - never: Never use low-end device mode.
# c.qt.low_end_device_mode = 'auto'

# Which Chromium process model to use. Alternative process models use
# less resources, but decrease security and robustness. See the
# following pages for more details:    -
# https://www.chromium.org/developers/design-documents/process-models
# - https://doc.qt.io/qt-5/qtwebengine-features.html#process-models
## Type: String
# Valid values:
# - process-per-site-instance: Pages from separate sites are put into separate processes and separate visits to the same site are also isolated.
# - process-per-site: Pages from separate sites are put into separate processes. Unlike Process per Site Instance, all visits to the same site will share an OS process. The benefit of this model is reduced memory consumption, because more web pages will share processes. The drawbacks include reduced security, robustness, and responsiveness.
# - single-process: Run all tabs in a single process. This should be used for debugging purposes only, and it disables `:open --private`.
# c.qt.process_model = 'process-per-site-instance'

# Work around locale parsing issues in QtWebEngine 5.15.3. With some
# locales, QtWebEngine 5.15.3 is unusable without this workaround. In
# affected scenarios, QtWebEngine will log "Network service crashed,
# restarting service." and only display a blank page. However, It is
# expected that distributions shipping QtWebEngine 5.15.3 follow up with
# a proper fix soon, so it is disabled by default.
## Type: Bool
# c.qt.workarounds.locale = False

# Delete the QtWebEngine Service Worker directory on every start. This
# workaround can help with certain crashes caused by an unknown
# QtWebEngine bug related to Service Workers. Those crashes happen
# seemingly immediately on Windows; after one hour of operation on other
# systems. Note however that enabling this option *can lead to data
# loss* on some pages (as Service Worker data isn't persisted) and will
# negatively impact start-up time.
## Type: Bool
# c.qt.workarounds.remove_service_workers = False

# When/how to show the scrollbar.
## Type: String
# Valid values:
# - always: Always show the scrollbar.
# - never: Never show the scrollbar.
# - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
# - overlay: Show an overlay scrollbar. On macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
# c.scrolling.bar = 'overlay'

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
## Type: Bool
c.scrolling.smooth = True

# When to find text on a page case-insensitively.
## Type: IgnoreCase
# Valid values:
# - always: Search case-insensitively.
# - never: Search case-sensitively.
# - smart: Search case-sensitively if there are capital characters.
# c.search.ignore_case = 'smart'

# Find text on a page incrementally, renewing the search for each typed
# character.
## Type: Bool
# c.search.incremental = True

# Wrap around at the top and bottom of the page when advancing through
# text matches using `:search-next` and `:search-prev`.
## Type: Bool
# c.search.wrap = True

# Name of the session to save by default. If this is set to null, the
# session which was last loaded is saved.
## Type: SessionName
# c.session.default_name = None

# Load a restored tab as soon as it takes focus.
## Type: Bool
# c.session.lazy_restore = False
