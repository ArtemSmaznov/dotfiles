# special
foreground = "#c0b18b"
foreground_bold = "#c0b18b"
cursorColor = "#c0b18b"
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

c.colors.completion.category.fg = foreground
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 ' + background + ', stop:1 ' + black_dark_8 + ')'
c.colors.completion.category.border.top = background
c.colors.completion.category.border.bottom = black_dark_8

# c.colors.completion.fg = ['white', 'white', 'white']
c.colors.completion.fg = foreground
c.colors.completion.match.fg = red_dark_9
c.colors.completion.odd.bg = cyan_dark_14
c.colors.completion.even.bg = background

c.colors.completion.item.selected.fg = white_dark_15
c.colors.completion.item.selected.match.fg = '#ff4444'
c.colors.completion.item.selected.bg = black_dark_8
c.colors.completion.item.selected.border.bottom = black_dark_8
c.colors.completion.item.selected.border.top = black_dark_8

c.colors.completion.scrollbar.fg = foreground
c.colors.completion.scrollbar.bg = background

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

# Background color of the statusbar in caret mode.
## Type: QssColor
# c.colors.statusbar.caret.bg = 'purple'

# Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = foreground

# Background color of the statusbar in caret mode with a selection.
## Type: QssColor
# c.colors.statusbar.caret.selection.bg = '#a12dff'

# Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = foreground

# Background color of the statusbar in command mode.
## Type: QssColor
# c.colors.statusbar.command.bg = 'black'

# Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = foreground

# Background color of the statusbar in private browsing + command mode.
## Type: QssColor
# c.colors.statusbar.command.private.bg = 'darkslategray'

# Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = foreground

# Background color of the statusbar in insert mode.
## Type: QssColor
# c.colors.statusbar.insert.bg = 'darkgreen'

# Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = foreground

# Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = background

# Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = foreground

# Background color of the statusbar in passthrough mode.
## Type: QssColor
# c.colors.statusbar.passthrough.bg = 'darkblue'

# Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = foreground

# Background color of the statusbar in private browsing mode.
## Type: QssColor
# c.colors.statusbar.private.bg = '#666666'

# Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = foreground

# Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = foreground

# Foreground color of the URL in the statusbar on error.
## Type: QssColor
# c.colors.statusbar.url.error.fg = 'orange'

# Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = foreground

# Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
# c.colors.statusbar.url.hover.fg = 'aqua'

# Foreground color of the URL in the statusbar on successful load
# (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = foreground

# Foreground color of the URL in the statusbar on successful load
# (https).
## Type: QssColor
# c.colors.statusbar.url.success.https.fg = 'lime'

# Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
# c.colors.statusbar.url.warn.fg = 'yellow'

c.colors.tabs.bar.bg = '#555555'

# Color for the tab indicator on errors.
## Type: QtColor
# c.colors.tabs.indicator.error = '#ff0000'

# Color gradient for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.start = '#0000aa'
# c.colors.tabs.indicator.stop = '#00aa00'

# Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
# Valid values:
# - rgb: Interpolate in the RGB color system.
# - hsv: Interpolate in the HSV color system.
# - hsl: Interpolate in the HSL color system.
# - none: Do not show a gradient.
# c.colors.tabs.indicator.system = 'rgb'

c.colors.tabs.selected.odd.fg = foreground
c.colors.tabs.selected.odd.bg = background
c.colors.tabs.selected.even.fg = foreground
c.colors.tabs.selected.even.bg = background

c.colors.tabs.odd.fg = 'black'
c.colors.tabs.odd.bg = 'grey'
c.colors.tabs.even.fg = 'black'
c.colors.tabs.even.bg = 'darkgrey'

# Background color of pinned unselected even tabs.
## Type: QtColor
# c.colors.tabs.pinned.even.bg = 'darkseagreen'

# Foreground color of pinned unselected even tabs.
## Type: QtColor
c.colors.tabs.pinned.even.fg = foreground

# Background color of pinned unselected odd tabs.
## Type: QtColor
# c.colors.tabs.pinned.odd.bg = 'seagreen'

# Foreground color of pinned unselected odd tabs.
## Type: QtColor
c.colors.tabs.pinned.odd.fg = foreground

# Background color of pinned selected even tabs.
## Type: QtColor
# c.colors.tabs.pinned.selected.even.bg = 'black'

# Foreground color of pinned selected even tabs.
## Type: QtColor
c.colors.tabs.pinned.selected.even.fg = foreground

# Background color of pinned selected odd tabs.
## Type: QtColor
# c.colors.tabs.pinned.selected.odd.bg = 'black'

# Foreground color of pinned selected odd tabs.
## Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = foreground

# Background color for webpages if unset (or empty to use the theme's
# color).
## Type: QtColor
c.colors.webpage.bg = background

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
c.colors.webpage.darkmode.enabled = True

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

# Require a confirmation before quitting the application.
## Type: ConfirmQuit
# Valid values:
# - always: Always show a confirmation.
# - multiple-tabs: Show a confirmation if multiple tabs are opened.
# - downloads: Show a confirmation if downloads are running
# - never: Never show a confirmation.
# c.confirm_quit = ['never']

# Automatically start playing `<video>` elements.
## Type: Bool
# c.content.autoplay = True

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

# c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}

# Time interval (in milliseconds) between auto-saves of
# config/cookies/etc.
## Type: Int
# c.auto_save.interval = 15000

# Always restore open sites when qutebrowser is reopened. Without this
# option set, `:wq` (`:quit --save`) needs to be used to save open tabs
# (and restore them), while quitting qutebrowser in any other way will
# not save/restore the session. By default, this will save to the
# session which was last loaded. This behavior can be customized via the
# `session.default_name` setting.
## Type: Bool
# c.auto_save.session = True

# Number of commands to save in the command history. 0: no history / -1:
# unlimited
## Type: Int
# c.completion.cmd_history_max_items = 100

# Map keys to other keys, so that they are equivalent in all modes. When
# the key used as dictionary-key is pressed, the binding for the key
# used as dictionary-value is invoked instead. This is useful for global
# remappings of keys, for example to map <Ctrl-[> to <Escape>. NOTE:
# This should only be used if two keys should always be equivalent, i.e.
# for things like <Enter> (keypad) and <Return> (non-keypad). For normal
# command bindings, qutebrowser works differently to vim: You always
# bind keys to commands, usually via `:bind` or `config.bind()`. Instead
# of using this setting, consider finding the command a key is bound to
# (e.g. via `:bind gg`) and then binding the same command to the desired
# key. Note that when a key is bound (via `bindings.default` or
# `bindings.commands`), the mapping is ignored.
## Type: Dict
# c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Ctrl-I>': '<Tab>', '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}

# Allow websites to read canvas elements. Note this is needed for some
# websites to work properly.
## Type: Bool
# c.content.canvas_reading = True

# List of URLs to ABP-style adblocking rulesets.  Only used when Brave's
# ABP-style adblocker is used (see `content.blocking.method`).  You can
# find an overview of available lists here:
# https://adblockplus.org/en/subscriptions - note that the special
# `subscribe.adblockplus.org` links aren't handled by qutebrowser, you
# will instead need to find the link to the raw `.txt` file (e.g. by
# extracting it from the `location` parameter of the subscribe URL and
# URL-decoding it).
# Type: List of Url
# c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt']

# Enable the ad/host blocker
## Type: Bool
c.content.blocking.enabled = True

# List of URLs to host blocklists for the host blocker.  Only used when
# the simple host-blocker is used (see `content.blocking.method`).  The
# file can be in one of the following formats:  - An `/etc/hosts`-like
# file - One host per line - A zip-file of any of the above, with either
# only one file, or a file   named `hosts` (with any extension).  It's
# also possible to add a local file or directory via a `file://` URL. In
# case of a directory, all files in the directory are read as adblock
# lists.  The file `~/.config/qutebrowser/blocked-hosts` is always read
# if it exists.
# Type: List of Url
# c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

# Which method of blocking ads should be used.  Support for Adblock Plus
# (ABP) syntax blocklists using Brave's Rust library requires the
# `adblock` Python package to be installed, which is an optional
# dependency of qutebrowser. It is required when either `adblock` or
# `both` are selected.
## Type: String
# Valid values:
# - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
# - adblock: Use Brave's ABP-style adblocker
# - hosts: Use hosts blocking
# - both: Use both hosts blocking and Brave's ABP-style adblocker
c.content.blocking.method = "auto"

# A list of patterns that should always be loaded, despite being blocked
# by the ad-/host-blocker. Local domains are always exempt from
# adblocking. Note this whitelists otherwise blocked requests, not
# first-party URLs. As an example, if `example.org` loads an ad from
# `ads.example.org`, the whitelist entry could be
# `https://ads.example.org/*`. If you want to disable the adblocker on a
# given page, use the `content.blocking.enabled` setting with a URL
# pattern instead.
# Type: List of UrlPattern
# c.content.blocking.whitelist = []

# Enable support for the HTML 5 web application cache feature. An
# application cache acts like an HTTP cache in some sense. For documents
# that use the application cache via JavaScript, the loader engine will
# first ask the application cache for the contents, before hitting the
# network.
## Type: Bool
# c.content.cache.appcache = True

# Maximum number of pages to hold in the global memory page cache. The
# page cache allows for a nicer user experience when navigating forth or
# back to pages in the forward/back history, by pausing and resuming up
# to _n_ pages. For more information about the feature, please refer to:
# https://webkit.org/blog/427/webkit-page-cache-i-the-basics/
## Type: Int
# c.content.cache.maximum_pages = 0

# Size (in bytes) of the HTTP network cache. Null to use the default
# value. With QtWebEngine, the maximum supported value is 2147483647 (~2
# GB).
## Type: Int
# c.content.cache.size = None

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
## Type: String
# Valid values:
# - all: Accept all cookies.
# - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
# - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
# - never: Don't accept cookies at all.
# c.content.cookies.accept = "no-3rdparty"
c.content.cookies.accept = "all"

# Store cookies.
## Type: Bool
# c.content.cookies.store = True

# Enable support for HTML 5 local storage and Web SQL.
## Type: Bool
# c.content.local_storage = True

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



# Allow pdf.js to view PDF files in the browser. Note that the files can
# still be downloaded by clicking the download button in the pdf.js
# viewer.
## Type: Bool
# c.content.pdfjs = False

# Allow websites to request persistent storage quota via
# `navigator.webkitPersistentStorage.requestQuota`.
## Type: BoolAsk
# Valid values:
##   - true
##   - false
##   - ask
# c.content.persistent_storage = 'ask'

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

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
## Type: Directory
# c.downloads.location.directory = None

# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
## Type: Bool
# c.downloads.location.prompt = True

# Remember the last used download directory.
## Type: Bool
# c.downloads.location.remember = True

# What to display in the download filename input.
## Type: String
# Valid values:
# - path: Show only the download path.
# - filename: Show only download filename.
# - both: Show download path and filename.
# c.downloads.location.suggestion = 'path'

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
# c.downloads.position = 'top'

# Duration (in milliseconds) to wait before removing finished downloads.
# If set to -1, downloads are never removed.
## Type: Int
# c.downloads.remove_finished = -1

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

# Maximum time (in minutes) between two history items for them to be
# considered being from the same browsing session. Items with less time
# between them are grouped when being displayed in `:history`. Use -1 to
# disable separation.
## Type: Int
# c.history_gap_interval = 30

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

# Duration (in milliseconds) to show messages in the statusbar for. Set
# to 0 to never clear messages.
## Type: Int
# c.messages.timeout = 3000

# How to open links in an existing instance if a new one is launched.
# This happens when e.g. opening a link from a terminal. See
# `new_instance_open_target_window` to customize in which window the
# link is opened in.
## Type: String
# Valid values:
# - tab: Open a new tab in the existing window and activate the window.
# - tab-bg: Open a new background tab in the existing window and activate the window.
# - tab-silent: Open a new tab in the existing window without activating the window.
# - tab-bg-silent: Open a new background tab in the existing window without activating the window.
# - window: Open in a new window.
# - private-window: Open in a new private window.
# c.new_instance_open_target = 'tab'

# Which window to choose when opening links as new tabs. When
# `new_instance_open_target` is set to `window`, this is ignored.
## Type: String
# Valid values:
# - first-opened: Open new tabs in the first (oldest) opened window.
# - last-opened: Open new tabs in the last (newest) opened window.
# - last-focused: Open new tabs in the most recently focused window.
# - last-visible: Open new tabs in the most recently visible window.
# c.new_instance_open_target_window = 'last-focused'

# Show a filebrowser in download prompts.
## Type: Bool
# c.prompt.filebrowser = True

# Rounding radius (in pixels) for the edges of prompts.
## Type: Int
# c.prompt.radius = 8

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

# Languages to use for spell checking. You can check for available
# languages and install dictionaries using scripts/dictcli.py. Run the
# script with -h/--help for instructions.
# Type: List of String
# Valid values:
# - af-ZA: Afrikaans (South Africa)
# - bg-BG: Bulgarian (Bulgaria)
# - ca-ES: Catalan (Spain)
# - cs-CZ: Czech (Czech Republic)
# - da-DK: Danish (Denmark)
# - de-DE: German (Germany)
# - el-GR: Greek (Greece)
# - en-AU: English (Australia)
# - en-CA: English (Canada)
# - en-GB: English (United Kingdom)
# - en-US: English (United States)
# - es-ES: Spanish (Spain)
# - et-EE: Estonian (Estonia)
# - fa-IR: Farsi (Iran)
# - fo-FO: Faroese (Faroe Islands)
# - fr-FR: French (France)
# - he-IL: Hebrew (Israel)
# - hi-IN: Hindi (India)
# - hr-HR: Croatian (Croatia)
# - hu-HU: Hungarian (Hungary)
# - id-ID: Indonesian (Indonesia)
# - it-IT: Italian (Italy)
# - ko: Korean
# - lt-LT: Lithuanian (Lithuania)
# - lv-LV: Latvian (Latvia)
# - nb-NO: Norwegian (Norway)
# - nl-NL: Dutch (Netherlands)
# - pl-PL: Polish (Poland)
# - pt-BR: Portuguese (Brazil)
# - pt-PT: Portuguese (Portugal)
# - ro-RO: Romanian (Romania)
# - ru-RU: Russian (Russia)
# - sh: Serbo-Croatian
# - sk-SK: Slovak (Slovakia)
# - sl-SI: Slovenian (Slovenia)
# - sq: Albanian
# - sr: Serbian
# - sv-SE: Swedish (Sweden)
# - ta-IN: Tamil (India)
# - tg-TG: Tajik (Tajikistan)
# - tr-TR: Turkish (Turkey)
# - uk-UA: Ukrainian (Ukraine)
# - vi-VN: Vietnamese (Viet Nam)
# c.spellcheck.languages = []

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

# Open new tabs (middleclick/ctrl+click) in the background.
## Type: Bool
# c.tabs.background = True

# Mouse button with which to close tabs.
## Type: String
# Valid values:
# - right: Close tabs on right-click.
# - middle: Close tabs on middle-click.
# - none: Don't close tabs using the mouse.
# c.tabs.close_mouse_button = 'middle'

# How to behave when the close mouse button is pressed on the tab bar.
## Type: String
# Valid values:
# - new-tab: Open a new tab.
# - close-current: Close the current tab.
# - close-last: Close the last tab.
# - ignore: Don't do anything.
# c.tabs.close_mouse_button_on_bar = 'new-tab'

# Scaling factor for favicons in the tab bar. The tab size is unchanged,
# so big favicons also require extra `tabs.padding`.
## Type: Float
# c.tabs.favicons.scale = 1.0

# When to show favicons in the tab bar. When switching this from never
# to always/pinned, note that favicons might not be loaded yet, thus
# tabs might require a reload to display them.
## Type: String
# Valid values:
# - always: Always show favicons.
# - never: Always hide favicons.
# - pinned: Show favicons only on pinned tabs.
# c.tabs.favicons.show = 'always'

# Maximum stack size to remember for tab switches (-1 for no maximum).
## Type: Int
# c.tabs.focus_stack_size = 10

# Padding (in pixels) for tab indicators.
## Type: Padding
# c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}

# Width (in pixels) of the progress indicator (0 to disable).
## Type: Int
# c.tabs.indicator.width = 3

# How to behave when the last tab is closed. If the
# `tabs.tabs_are_windows` setting is set, this is ignored and the
# behavior is always identical to the `close` value.
## Type: String
# Valid values:
# - ignore: Don't do anything.
# - blank: Load a blank page.
# - startpage: Load the start page.
# - default-page: Load the default page.
# - close: Close the window.
# c.tabs.last_close = 'ignore'

# Maximum width (in pixels) of tabs (-1 for no maximum). This setting
# only applies when tabs are horizontal. This setting does not apply to
# pinned tabs, unless `tabs.pinned.shrink` is False. This setting may
# not apply properly if max_width is smaller than the minimum size of
# tab contents, or smaller than tabs.min_width.
## Type: Int
# c.tabs.max_width = -1

# Minimum width (in pixels) of tabs (-1 for the default minimum size
# behavior). This setting only applies when tabs are horizontal. This
# setting does not apply to pinned tabs, unless `tabs.pinned.shrink` is
# False.
## Type: Int
# c.tabs.min_width = -1

# When switching tabs, what input mode is applied.
## Type: String
# Valid values:
# - persist: Retain the current mode.
# - restore: Restore previously saved mode.
# - normal: Always revert to normal mode.
# c.tabs.mode_on_change = 'normal'

# Switch between tabs using the mouse wheel.
## Type: Bool
# c.tabs.mousewheel_switching = True

# Position of new tabs opened from another tab. See
# `tabs.new_position.stacking` for controlling stacking behavior.
## Type: NewTabPosition
# Valid values:
# - prev: Before the current tab.
# - next: After the current tab.
# - first: At the beginning.
# - last: At the end.
# c.tabs.new_position.related = 'next'

# Stack related tabs on top of each other when opened consecutively.
# Only applies for `next` and `prev` values of
# `tabs.new_position.related` and `tabs.new_position.unrelated`.
## Type: Bool
# c.tabs.new_position.stacking = True

# Position of new tabs which are not opened from another tab. See
# `tabs.new_position.stacking` for controlling stacking behavior.
## Type: NewTabPosition
# Valid values:
# - prev: Before the current tab.
# - next: After the current tab.
# - first: At the beginning.
# - last: At the end.
# c.tabs.new_position.unrelated = 'last'

# Padding (in pixels) around text for tabs.
## Type: Padding
# c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 5, 'right': 5}

# Force pinned tabs to stay at fixed URL.
## Type: Bool
# c.tabs.pinned.frozen = True

# Shrink pinned tabs down to their contents.
## Type: Bool
# c.tabs.pinned.shrink = True

# Position of the tab bar.
## Type: Position
# Valid values:
##   - top
##   - bottom
##   - left
##   - right
# c.tabs.position = 'top'

# Which tab to select when the focused tab is removed.
## Type: SelectOnRemove
# Valid values:
# - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
# - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
# - last-used: Select the previously selected tab.
# c.tabs.select_on_remove = 'next'

# When to show the tab bar.
## Type: String
# Valid values:
# - always: Always show the tab bar.
# - never: Always hide the tab bar.
# - multiple: Hide the tab bar if only one tab is open.
# - switching: Show the tab bar when switching tabs.
# c.tabs.show = 'always'

# Duration (in milliseconds) to show the tab bar before hiding it when
# tabs.show is set to 'switching'.
## Type: Int
# c.tabs.show_switching_delay = 800

# Open a new window for every tab.
## Type: Bool
# c.tabs.tabs_are_windows = False

# Alignment of the text inside of tabs.
## Type: TextAlignment
# Valid values:
##   - left
##   - right
##   - center
# c.tabs.title.alignment = 'left'

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of
# the current web page. * `{title_sep}`: The string `" - "` if a title
# is set, empty otherwise. * `{index}`: Index of this tab. *
# `{aligned_index}`: Index of this tab padded with spaces to have the
# same   width. * `{id}`: Internal tab ID of this tab. * `{scroll_pos}`:
# Page scroll position. * `{host}`: Host of the current web page. *
# `{backend}`: Either `webkit` or `webengine` * `{private}`: Indicates
# when private mode is enabled. * `{current_url}`: URL of the current
# web page. * `{protocol}`: Protocol (http/https/...) of the current web
# page. * `{audio}`: Indicator for audio/mute status.
## Type: FormatString
# c.tabs.title.format = '{audio}{index}: {current_title}'

# Format to use for the tab title for pinned tabs. The same placeholders
# like for `tabs.title.format` are defined.
## Type: FormatString
# c.tabs.title.format_pinned = '{index}'

# Show tooltips on tabs. Note this setting only affects windows opened
# after it has been set.
## Type: Bool
# c.tabs.tooltips = True

# Number of closed tabs (per window) and closed windows to remember for
# :undo (-1 for no maximum).
## Type: Int
# c.tabs.undo_stack_size = 100

# Width (in pixels or as percentage of the window) of the tab bar if
# it's vertical.
## Type: PercOrInt
# c.tabs.width = '15%'

# Wrap when changing tabs.
## Type: Bool
# c.tabs.wrap = True

# What search to start when something else than a URL is entered.
## Type: String
# Valid values:
# - naive: Use simple/naive check.
# - dns: Use DNS requests (might be slow!).
# - never: Never search automatically.
# - schemeless: Always search automatically unless URL explicitly contains a scheme.
# c.url.auto_search = 'naive'

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
## Type: FuzzyUrl
# c.url.default_page = 'https://start.duckduckgo.com/'

# URL segments where `:navigate increment/decrement` will search for a
# number.
## Type: FlagList
# Valid values:
##   - host
##   - port
##   - path
##   - query
##   - anchor
# c.url.incdec_segments = ['path', 'query']

# Open base URL of the searchengine if a searchengine shortcut is
# invoked without parameters.
## Type: Bool
# c.url.open_base_url = False

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
# multiple times.  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
## Type: Dict
c.url.searchengines = {"DEFAULT": "https://search.brave.com/search?q={}"}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = ["https://search.brave.com"]

# URL parameters to strip with `:yank url`.
# Type: List of String
# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

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

# Bindings for normal mode
# config.bind("'", 'mode-enter jump_mark')
# config.bind('+', 'zoom-in')
# config.bind('-', 'zoom-out')
# config.bind('.', 'repeat-command')
# config.bind('/', 'set-cmd-text /')
# config.bind(':', 'set-cmd-text :')
# config.bind(';I', 'hint images tab')
# config.bind(';O', 'hint links fill :open -t -r {hint-url}')
# config.bind(';R', 'hint --rapid links window')
# config.bind(';Y', 'hint links yank-primary')
# config.bind(';b', 'hint all tab-bg')
# config.bind(';d', 'hint links download')
# config.bind(';f', 'hint all tab-fg')
# config.bind(';h', 'hint all hover')
# config.bind(';i', 'hint images')
# config.bind(';o', 'hint links fill :open {hint-url}')
# config.bind(';r', 'hint --rapid links tab-bg')
# config.bind(';t', 'hint inputs')
# config.bind(';y', 'hint links yank')
# config.bind('<Alt-1>', 'tab-focus 1')
# config.bind('<Alt-2>', 'tab-focus 2')
# config.bind('<Alt-3>', 'tab-focus 3')
# config.bind('<Alt-4>', 'tab-focus 4')
# config.bind('<Alt-5>', 'tab-focus 5')
# config.bind('<Alt-6>', 'tab-focus 6')
# config.bind('<Alt-7>', 'tab-focus 7')
# config.bind('<Alt-8>', 'tab-focus 8')
# config.bind('<Alt-9>', 'tab-focus -1')
# config.bind('<Alt-m>', 'tab-mute')
# config.bind('<Ctrl-A>', 'navigate increment')
# config.bind('<Ctrl-Alt-p>', 'print')
# config.bind('<Ctrl-B>', 'scroll-page 0 -1')
# config.bind('<Ctrl-D>', 'scroll-page 0 0.5')
# config.bind('<Ctrl-F5>', 'reload -f')
# config.bind('<Ctrl-F>', 'scroll-page 0 1')
# config.bind('<Ctrl-N>', 'open -w')
# config.bind('<Ctrl-PgDown>', 'tab-next')
# config.bind('<Ctrl-PgUp>', 'tab-prev')
# config.bind('<Ctrl-Q>', 'quit')
# config.bind('<Ctrl-Return>', 'selection-follow -t')
# config.bind('<Ctrl-Shift-N>', 'open -p')
# config.bind('<Ctrl-Shift-T>', 'undo')
# config.bind('<Ctrl-Shift-Tab>', 'nop')
# config.bind('<Ctrl-Shift-W>', 'close')
# config.bind('<Ctrl-T>', 'open -t')
# config.bind('<Ctrl-Tab>', 'tab-focus last')
# config.bind('<Ctrl-U>', 'scroll-page 0 -0.5')
# config.bind('<Ctrl-V>', 'mode-enter passthrough')
# config.bind('<Ctrl-W>', 'tab-close')
# config.bind('<Ctrl-X>', 'navigate decrement')
# config.bind('<Ctrl-^>', 'tab-focus last')
# config.bind('<Ctrl-h>', 'home')
# config.bind('<Ctrl-p>', 'tab-pin')
# config.bind('<Ctrl-s>', 'stop')
# config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave')
# config.bind('<F11>', 'fullscreen')
# config.bind('<F5>', 'reload')
# config.bind('<Return>', 'selection-follow')
# config.bind('<back>', 'back')
# config.bind('<forward>', 'forward')
# config.bind('=', 'zoom')
# config.bind('?', 'set-cmd-text ?')
# config.bind('@', 'macro-run')
# config.bind('B', 'set-cmd-text -s :quickmark-load -t')
# config.bind('D', 'tab-close -o')
# config.bind('F', 'hint all tab')
# config.bind('G', 'scroll-to-perc')
# config.bind('H', 'back')
# config.bind('J', 'tab-next')
# config.bind('K', 'tab-prev')
# config.bind('L', 'forward')
# config.bind('M', 'bookmark-add')
# config.bind('N', 'search-prev')
# config.bind('O', 'set-cmd-text -s :open -t')
# config.bind('PP', 'open -t -- {primary}')
# config.bind('Pp', 'open -t -- {clipboard}')
# config.bind('R', 'reload -f')
# config.bind('Sb', 'bookmark-list --jump')
# config.bind('Sh', 'history')
# config.bind('Sq', 'bookmark-list')
# config.bind('Ss', 'set')
# config.bind('T', 'set-cmd-text -sr :tab-focus')
# config.bind('U', 'undo -w')
# config.bind('V', 'mode-enter caret ;; selection-toggle --line')
# config.bind('ZQ', 'quit')
# config.bind('ZZ', 'quit --save')
# config.bind('[[', 'navigate prev')
# config.bind(']]', 'navigate next')
# config.bind('`', 'mode-enter set_mark')
# config.bind('ad', 'download-cancel')
# config.bind('b', 'set-cmd-text -s :quickmark-load')
# config.bind('cd', 'download-clear')
# config.bind('co', 'tab-only')
# config.bind('d', 'tab-close')
# config.bind('f', 'hint')
# config.bind('g$', 'tab-focus -1')
# config.bind('g0', 'tab-focus 1')
# config.bind('gB', 'set-cmd-text -s :bookmark-load -t')
# config.bind('gC', 'tab-clone')
# config.bind('gD', 'tab-give')
# config.bind('gJ', 'tab-move +')
# config.bind('gK', 'tab-move -')
# config.bind('gO', 'set-cmd-text :open -t -r {url:pretty}')
# config.bind('gU', 'navigate up -t')
# config.bind('g^', 'tab-focus 1')
# config.bind('ga', 'open -t')
# config.bind('gb', 'set-cmd-text -s :bookmark-load')
# config.bind('gd', 'download')
# config.bind('gf', 'view-source')
# config.bind('gg', 'scroll-to-perc 0')
# config.bind('gi', 'hint inputs --first')
# config.bind('gm', 'tab-move')
# config.bind('go', 'set-cmd-text :open {url:pretty}')
# config.bind('gt', 'set-cmd-text -s :tab-select')
# config.bind('gu', 'navigate up')
# config.bind('h', 'scroll left')
# config.bind('i', 'mode-enter insert')
# config.bind('j', 'scroll down')
# config.bind('k', 'scroll up')
# config.bind('l', 'scroll right')
# config.bind('m', 'quickmark-save')
# config.bind('n', 'search-next')
# config.bind('o', 'set-cmd-text -s :open')
# config.bind('pP', 'open -- {primary}')
# config.bind('pp', 'open -- {clipboard}')
# config.bind('q', 'macro-record')
# config.bind('r', 'reload')
# config.bind('sf', 'save')
# config.bind('sk', 'set-cmd-text -s :bind')
# config.bind('sl', 'set-cmd-text -s :set -t')
# config.bind('ss', 'set-cmd-text -s :set')
# config.bind('tCH', 'config-cycle -p -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tCh', 'config-cycle -p -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tCu', 'config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tIH', 'config-cycle -p -u *://*.{url:host}/* content.images ;; reload')
# config.bind('tIh', 'config-cycle -p -u *://{url:host}/* content.images ;; reload')
# config.bind('tIu', 'config-cycle -p -u {url} content.images ;; reload')
# config.bind('tPH', 'config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload')
# config.bind('tPh', 'config-cycle -p -u *://{url:host}/* content.plugins ;; reload')
# config.bind('tPu', 'config-cycle -p -u {url} content.plugins ;; reload')
# config.bind('tSH', 'config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tSh', 'config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tSu', 'config-cycle -p -u {url} content.javascript.enabled ;; reload')
# config.bind('tcH', 'config-cycle -p -t -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tch', 'config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tcu', 'config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('th', 'back -t')
# config.bind('tiH', 'config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload')
# config.bind('tih', 'config-cycle -p -t -u *://{url:host}/* content.images ;; reload')
# config.bind('tiu', 'config-cycle -p -t -u {url} content.images ;; reload')
# config.bind('tl', 'forward -t')
# config.bind('tpH', 'config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload')
# config.bind('tph', 'config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload')
# config.bind('tpu', 'config-cycle -p -t -u {url} content.plugins ;; reload')
# config.bind('tsH', 'config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tsh', 'config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tsu', 'config-cycle -p -t -u {url} content.javascript.enabled ;; reload')
# config.bind('u', 'undo')
# config.bind('v', 'mode-enter caret')
# config.bind('wB', 'set-cmd-text -s :bookmark-load -w')
# config.bind('wIf', 'devtools-focus')
# config.bind('wIh', 'devtools left')
# config.bind('wIj', 'devtools bottom')
# config.bind('wIk', 'devtools top')
# config.bind('wIl', 'devtools right')
# config.bind('wIw', 'devtools window')
# config.bind('wO', 'set-cmd-text :open -w {url:pretty}')
# config.bind('wP', 'open -w -- {primary}')
# config.bind('wb', 'set-cmd-text -s :quickmark-load -w')
# config.bind('wf', 'hint all window')
# config.bind('wh', 'back -w')
# config.bind('wi', 'devtools')
# config.bind('wl', 'forward -w')
# config.bind('wo', 'set-cmd-text -s :open -w')
# config.bind('wp', 'open -w -- {clipboard}')
# config.bind('xO', 'set-cmd-text :open -b -r {url:pretty}')
# config.bind('xo', 'set-cmd-text -s :open -b')
# config.bind('yD', 'yank domain -s')
# config.bind('yM', 'yank inline [{title}]({url}) -s')
# config.bind('yP', 'yank pretty-url -s')
# config.bind('yT', 'yank title -s')
# config.bind('yY', 'yank -s')
# config.bind('yd', 'yank domain')
# config.bind('ym', 'yank inline [{title}]({url})')
# config.bind('yp', 'yank pretty-url')
# config.bind('yt', 'yank title')
# config.bind('yy', 'yank')
# config.bind('{{', 'navigate prev -t')
# config.bind('}}', 'navigate next -t')

# Bindings for caret mode
# config.bind('$', 'move-to-end-of-line', mode='caret')
# config.bind('0', 'move-to-start-of-line', mode='caret')
# config.bind('<Ctrl-Space>', 'selection-drop', mode='caret')
# config.bind('<Escape>', 'mode-leave', mode='caret')
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
# config.bind('c', 'mode-enter normal', mode='caret')
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

# Bindings for command mode
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
# config.bind('<Escape>', 'mode-leave', mode='command')
# config.bind('<PgDown>', 'completion-item-focus next-page', mode='command')
# config.bind('<PgUp>', 'completion-item-focus prev-page', mode='command')
# config.bind('<Return>', 'command-accept', mode='command')
# config.bind('<Shift-Delete>', 'completion-item-del', mode='command')
# config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
# config.bind('<Tab>', 'completion-item-focus next', mode='command')
# config.bind('<Up>', 'completion-item-focus --history prev', mode='command')

# Bindings for hint mode
# config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
# config.bind('<Ctrl-F>', 'hint links', mode='hint')
# config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
# config.bind('<Escape>', 'mode-leave', mode='hint')
# config.bind('<Return>', 'hint-follow', mode='hint')

# Bindings for insert mode
# config.bind('<Ctrl-E>', 'edit-text', mode='insert')
# config.bind('<Escape>', 'mode-leave', mode='insert')
# config.bind('<Shift-Ins>', 'insert-text -- {primary}', mode='insert')

# Bindings for passthrough mode
# config.bind('<Shift-Escape>', 'mode-leave', mode='passthrough')

# Bindings for prompt mode
# config.bind('<Alt-B>', 'rl-backward-word', mode='prompt')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='prompt')
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
# config.bind('<Ctrl-P>', 'prompt-open-download --pdfjs', mode='prompt')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='prompt')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='prompt')
# config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='prompt')
# config.bind('<Down>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Escape>', 'mode-leave', mode='prompt')
# config.bind('<Return>', 'prompt-accept', mode='prompt')
# config.bind('<Shift-Tab>', 'prompt-item-focus prev', mode='prompt')
# config.bind('<Tab>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')

# Bindings for register mode
# config.bind('<Escape>', 'mode-leave', mode='register')

# Bindings for yesno mode
# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='yesno')
# config.bind('<Alt-Y>', 'prompt-yank', mode='yesno')
# config.bind('<Escape>', 'mode-leave', mode='yesno')
# config.bind('<Return>', 'prompt-accept', mode='yesno')
# config.bind('N', 'prompt-accept --save no', mode='yesno')
# config.bind('Y', 'prompt-accept --save yes', mode='yesno')
# config.bind('n', 'prompt-accept no', mode='yesno')
# config.bind('y', 'prompt-accept yes', mode='yesno')
