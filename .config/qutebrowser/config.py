import os

from qutebrowser.api import interceptor

import themes.default as theme

c.fonts.default_size = '12pt'
c.fonts.default_family = ['Lato']
# c.fonts.completion.category = 'bold default_size default_family'
# c.fonts.completion.entry = 'default_size default_family'
# c.fonts.contextmenu = None
# c.fonts.debug_console = 'default_size default_family'
# c.fonts.downloads = 'default_size default_family'
# c.fonts.hints = 'bold default_size default_family'
# c.fonts.keyhint = 'default_size default_family'
# c.fonts.messages.error = 'default_size default_family'
# c.fonts.messages.info = 'default_size default_family'
# c.fonts.messages.warning = 'default_size default_family'
# c.fonts.prompts = 'default_size sans-serif'
# c.fonts.statusbar = 'default_size default_family'
# c.fonts.tabs.selected = 'default_size default_family'
# c.fonts.tabs.unselected = 'default_size default_family'
# c.fonts.web.family.cursive = ''
# c.fonts.web.family.fantasy = ''
# c.fonts.web.family.fixed = ''
# c.fonts.web.family.sans_serif = ''
# c.fonts.web.family.serif = ''
# c.fonts.web.family.standard = ''
# c.fonts.web.size.default = 16
# c.fonts.web.size.default_fixed = 13
# c.fonts.web.size.minimum = 0
# c.fonts.web.size.minimum_logical = 6

# c.window.hide_decoration = False
# c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser'
c.window.transparent = False

c.colors.completion.category.fg = theme.title
c.colors.completion.category.bg = theme.background
c.colors.completion.category.border.top = theme.background
c.colors.completion.category.border.bottom = theme.background

# c.colors.completion.fg = ['white', 'white', 'white']
c.colors.completion.fg = theme.foreground
c.colors.completion.match.fg = theme.completion_match
c.colors.completion.odd.bg = theme.completion_odd
c.colors.completion.even.bg = theme.completion_even

c.colors.completion.item.selected.fg = theme.foreground
c.colors.completion.item.selected.bg = theme.completion_selected
c.colors.completion.item.selected.border.top = theme.completion_borders
c.colors.completion.item.selected.border.bottom = theme.completion_borders
c.colors.completion.item.selected.match.fg = theme.match

c.colors.completion.scrollbar.fg = theme.foreground
c.colors.completion.scrollbar.bg = theme.background

c.colors.keyhint.fg = theme.foreground
c.colors.keyhint.bg = theme.background
c.colors.keyhint.suffix.fg = theme.match
c.keyhint.radius = theme.whichkey_radius

c.colors.contextmenu.menu.fg = theme.foreground
c.colors.contextmenu.menu.bg = theme.background

c.colors.contextmenu.selected.fg = theme.foreground
c.colors.contextmenu.selected.bg = theme.contextmenu_selected_bg

c.colors.contextmenu.disabled.fg = theme.contextmenu_disabled_fg
c.colors.contextmenu.disabled.bg = theme.contextmenu_disabled_bg

c.colors.downloads.bar.bg = theme.background

c.colors.downloads.start.fg = theme.background
c.colors.downloads.start.bg = theme.loading

c.colors.downloads.stop.fg = theme.background
c.colors.downloads.stop.bg = theme.success

c.colors.downloads.error.fg = theme.error

c.colors.downloads.system.fg = 'rgb'
c.colors.downloads.system.bg = 'rgb'

# c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.8), stop:1 rgba(255, 197, 66, 0.8))'

c.colors.hints.fg = theme.background
c.colors.hints.bg = theme.hint_bg
c.colors.hints.match.fg = theme.foreground

c.colors.prompts.fg = theme.foreground
c.colors.prompts.bg = theme.background

c.colors.prompts.selected.fg = theme.foreground
c.colors.prompts.selected.bg = theme.prompt_selected_bg

c.colors.prompts.border = theme.background

c.statusbar.padding = {'top': 2, 'bottom': 2, 'left': 5, 'right': 5}
c.statusbar.position = 'bottom'
c.statusbar.show = 'always'
c.statusbar.widgets = ['keypress', 'progress', 'history', 'text: -- ', 'url', 'text: -- ', 'scroll']

# Color of the statusbar.
c.colors.statusbar.normal.fg = theme.status_normal_fg
c.colors.statusbar.normal.bg = theme.status_normal_bg

# Color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = theme.status_insert_fg
c.colors.statusbar.insert.bg = theme.status_insert_bg

# Color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = theme.status_passthrough_fg
c.colors.statusbar.passthrough.bg = theme.status_passthrough_bg

# Color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = theme.status_private_fg
c.colors.statusbar.private.bg = theme.status_private_bg

# Color of the statusbar in command mode.
c.colors.statusbar.command.fg = theme.status_command_fg
c.colors.statusbar.command.bg = theme.status_command_bg

# Color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = theme.status_command_private_fg
c.colors.statusbar.command.private.bg = theme.status_command_private_bg

# Color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = theme.status_caret_fg
c.colors.statusbar.caret.bg = theme.status_caret_bg

# Color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = theme.status_caret_selection_fg
c.colors.statusbar.caret.selection.bg = theme.status_caret_selection_bg

# Color of the progress bar.
c.colors.statusbar.progress.bg = theme.loading

c.colors.statusbar.url.fg = theme.loading
c.colors.statusbar.url.success.http.fg = theme.error
c.colors.statusbar.url.success.https.fg = theme.success
c.colors.statusbar.url.hover.fg = theme.foreground
c.colors.statusbar.url.warn.fg = theme.warning
c.colors.statusbar.url.error.fg = theme.fail

c.colors.tabs.bar.bg = theme.background

# Color gradient for the tab indicator.
c.colors.tabs.indicator.start = theme.loading
c.colors.tabs.indicator.stop = theme.success

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = theme.error

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
# - rgb: Interpolate in the RGB color system.
# - hsv: Interpolate in the HSV color system.
# - hsl: Interpolate in the HSL color system.
# - none: Do not show a gradient.
# c.colors.tabs.indicator.system = 'rgb'

c.colors.tabs.odd.fg = theme.foreground
c.colors.tabs.odd.bg = theme.tab_odd
c.colors.tabs.even.fg = theme.foreground
c.colors.tabs.even.bg = theme.tab_even
c.colors.tabs.pinned.odd.fg = theme.foreground
c.colors.tabs.pinned.odd.bg = theme.tab_odd
c.colors.tabs.pinned.even.fg = theme.foreground
c.colors.tabs.pinned.even.bg = theme.tab_even

c.colors.tabs.selected.odd.fg = theme.background
c.colors.tabs.selected.odd.bg = theme.tab_selected
c.colors.tabs.selected.even.fg = theme.background
c.colors.tabs.selected.even.bg = theme.tab_selected
c.colors.tabs.pinned.selected.odd.fg = theme.background
c.colors.tabs.pinned.selected.odd.bg = theme.tab_selected
c.colors.tabs.pinned.selected.even.fg = theme.background
c.colors.tabs.pinned.selected.even.bg = theme.tab_selected

c.colors.messages.info.fg = theme.foreground
c.colors.messages.info.bg = theme.background
c.colors.messages.info.border = theme.background

c.colors.messages.warning.fg = theme.background
c.colors.messages.warning.bg = theme.warning
c.colors.messages.warning.border = theme.warning

c.colors.messages.error.fg = theme.background
c.colors.messages.error.bg = theme.error
c.colors.messages.error.border = theme.error

c.messages.timeout = 5000

# c.colors.webpage.bg = theme.background

c.colors.webpage.darkmode.algorithm = 'lightness-cielab'

# c.colors.webpage.darkmode.contrast = 0.0

c.colors.webpage.darkmode.enabled = False

c.colors.webpage.darkmode.grayscale.all = False

c.colors.webpage.darkmode.grayscale.images = 0.0

c.colors.webpage.darkmode.policy.images = 'never'

c.colors.webpage.darkmode.policy.page = 'smart'

c.colors.webpage.darkmode.threshold.background = 205

c.colors.webpage.darkmode.threshold.text = 150

c.colors.webpage.preferred_color_scheme = "dark"

config.load_autoconfig(True)

c.backend = 'webengine'

c.changelog_after_upgrade = "major"

# Delay (in milliseconds) before updating completions after typing a
# character.
# Type: Int
# c.completion.delay = 0

# Default filesystem autocomplete suggestions for :open. The elements of
# this list show up in the completion window under the Filesystem
# category when the command line contains `:open` but no argument.
# Type: List of String
# c.completion.favorite_paths = []

# Height (in pixels or as percentage of the window) of the completion.
# Type: PercOrInt
# c.completion.height = '50%'

# Minimum amount of characters needed to update completions.
# Type: Int
# c.completion.min_chars = 1

# Which categories to show (in which order) in the :open completion.
# Type: FlagList
# Valid values:
# - searchengines
# - quickmarks
# - bookmarks
# - history
# - filesystem
# c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

# Move on to the next part when there's only one possible completion
# left.
# Type: Bool
# c.completion.quick = True

# Padding (in pixels) of the scrollbar handle in the completion window.
# Type: Int
# c.completion.scrollbar.padding = 2

# Width (in pixels) of the scrollbar in the completion window.
# Type: Int
# c.completion.scrollbar.width = 12

# When to show the autocompletion window.
# Type: String
# Valid values:
# - always: Whenever a completion is available.
# - auto: Whenever a completion is requested.
# - never: Never.
# c.completion.show = 'always'

# Shrink the completion to be smaller than the configured size if there
# are no scrollbars.
# Type: Bool
# c.completion.shrink = False

# Format of timestamps (e.g. for the history completion). See
# https://sqlite.org/lang_datefunc.html and
# https://docs.python.org/3/library/datetime.html#strftime-strptime-
# behavior for allowed substitutions, qutebrowser uses both sqlite and
# Python to format its timestamps.
# Type: String
# c.completion.timestamp_format = '%Y-%m-%d %H:%M'

# Execute the best-matching command on a partial match.
# Type: Bool
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
# Type: Int
# c.completion.web_history.max_items = -1

c.content.fullscreen.overlay_timeout = 3000

c.content.fullscreen.window = False

# c.content.headers.accept_language = 'en-US,en;q=0.9'

# c.content.headers.custom = {}

c.content.headers.do_not_track = True

c.content.headers.referer = 'same-domain'

c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}'

c.scrolling.bar = 'overlay'

c.scrolling.smooth = True

# Default zoom level.
# Type: Perc
c.zoom.default = '100%'

# Available zoom levels.
# Type: List of Perc
c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

# Number of zoom increments to divide the mouse wheel movements to.
# Type: Int
c.zoom.mouse_divider = 512

# Apply the zoom factor on a frame only to the text or to all content.
# Not available with the QtWebEngine backend
# Type: Bool
# c.zoom.text_only = False

# Require a confirmation before quitting the application.
# Type: ConfirmQuit
# Valid values:
# - always: Always show a confirmation.
# - multiple-tabs: Show a confirmation if multiple tabs are opened.
# - downloads: Show a confirmation if downloads are running
# - never: Never show a confirmation.
c.confirm_quit = ['downloads']

# Automatically start playing `<video>` elements.
# Type: Bool
c.content.autoplay = False

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
# Type: String
# c.content.default_encoding = 'iso-8859-1'

# Try to pre-fetch DNS entries to speed up browsing.
# Type: Bool
c.content.dns_prefetch = True

# Expand each subframe to its contents. This will flatten all the frames
# to become one scrollable page.
# Type: Bool
# c.content.frame_flattening = False

# Enable hyperlink auditing (`<a ping>`).
# Type: Bool
c.content.hyperlink_auditing = False

# Load images automatically in web pages.
# Type: Bool
c.content.images = True

# Allow locally loaded documents to access other local URLs.
# Type: Bool
# c.content.local_content_can_access_file_urls = True

# Allow locally loaded documents to access remote URLs.
# Type: Bool
# c.content.local_content_can_access_remote_urls = False

# Automatically mute tabs. Note that if the `:tab-mute` command is used,
# the mute status for the affected tab is now controlled manually, and
# this setting doesn't have any effect.
# Type: Bool
# c.content.mute = False

# Netrc-file for HTTP authentication. If unset, `~/.netrc` is used.
# Type: File
# c.content.netrc_file = None

c.new_instance_open_target = 'tab'

c.new_instance_open_target_window = 'last-focused'

# Directory to save downloads to. If unset, a sensible OS-specific default is used.
# Type: Directory
c.downloads.location.directory = None

# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
# Type: Bool
c.downloads.location.prompt = True

# Remember the last used download directory.
# Type: Bool
c.downloads.location.remember = True

# What to display in the download filename input.
# Type: String
# Valid values:
# - path: Show only the download path.
# - filename: Show only download filename.
# - both: Show download path and filename.
c.downloads.location.suggestion = 'path'

# Default program used to open downloads. If null, the default internal
# handler is used. Any `{}` in the string will be expanded to the
# filename, else the filename will be appended.
# Type: String
c.downloads.open_dispatcher = None

# Where to show the downloaded files.
# Type: VerticalPosition
# Valid values:
# - top
# - bottom
c.downloads.position = 'bottom'

# Duration (in milliseconds) to wait before removing finished downloads.
# If set to -1, downloads are never removed.
# Type: Int
c.downloads.remove_finished = 30000

c.prompt.filebrowser = True
c.prompt.radius = 0

c.url.auto_search = 'naive'

c.url.default_page = 'https://search.brave.com/'

# c.url.incdec_segments = ['path', 'query']

c.url.open_base_url = True

c.url.searchengines = {
    "DEFAULT": "https://search.brave.com/search?q={}",
    "aw"     : "https://wiki.archlinux.org/index.php?search={}",
    "aur"    : "https://aur.archlinux.org/packages?O=0&K={}",
    "r"      : "https://www.reddit.com/search/?q={}",
    "gh"     : "https://github.com/search?q={}&ref=opensearch",
    "od"     : "https://odysee.com/$/search?q={}",
    "yt"     : "https://www.youtube.com/results?search_query={}",
    "yth"    : "https://www.youtube.com/feed/history?query={}",
    "mx"     : "https://www.musixmatch.com/search/{}",
    "fa"     : "https://fontawesome.com/search?q={}&o=r",
    "pd"     : "https://www.protondb.com/search?q={}",
    "ne"     : "https://www.newegg.ca/p/pl?d={}",
    "auk"    : "https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}",
    "acom"   : "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}",
    "aca"    : "https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}",
    "gt"     : "https://translate.google.co.uk/?sl=auto&tl=en&text={}",
    "gtj"    : "https://translate.google.co.uk/?sl=auto&tl=ja&text={}",
    "gtr"    : "https://translate.google.co.uk/?sl=auto&tl=ru&text={}",
    "gd"     : "https://drive.google.com/drive/search?q={}",
    "gm"     : "https://www.google.com/maps/search/{}?hl=en&source=opensearch",
    "g"      : "https://www.google.com/search?q={}",
}

c.url.start_pages = ["https://search.brave.com"]

# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

# c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}

c.session.default_name = "autosave"

c.auto_save.session = True

c.auto_save.interval = 15000

# c.completion.cmd_history_max_items = 100

c.tabs.min_width = -1
c.tabs.max_width = 200

c.tabs.position = 'top'

c.tabs.show = 'multiple'

# c.tabs.show_switching_delay = 800

# c.tabs.width = '15%'

c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}

c.tabs.indicator.width = 3

# c.tabs.favicons.scale = 1.0

c.tabs.favicons.show = 'always'

# c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 5, 'right': 5}

c.tabs.title.alignment = 'left'

c.tabs.title.format = ' {perc}{audio}{private}{current_title}'

c.tabs.title.format_pinned = '{perc}{audio}{private}'

c.tabs.tooltips = True

c.tabs.new_position.related = 'next'

c.tabs.new_position.unrelated = 'last'

c.tabs.tabs_are_windows = False

c.tabs.mode_on_change = 'normal'

c.tabs.wrap = True

c.tabs.select_on_remove = 'next'

c.tabs.last_close = 'startpage'

c.tabs.undo_stack_size = -1

c.session.lazy_restore = True

c.tabs.pinned.frozen = True

c.tabs.pinned.shrink = True

# c.tabs.new_position.stacking = True

# c.tabs.focus_stack_size = 10

# c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Ctrl-I>': '<Tab>', '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}

config.unbind('<Ctrl-Q>') # quit ?
config.unbind('ZQ')       # quit
config.unbind('ZZ')       # quit --save

config.unbind('tCH') # config-cycle -p -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload
config.unbind('tCh') # config-cycle -p -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload
config.unbind('tCu') # config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload
config.unbind('tIH') # config-cycle -p -u *://*.{url:host}/* content.images ;; reload
config.unbind('tIh') # config-cycle -p -u *://{url:host}/* content.images ;; reload
config.unbind('tIu') # config-cycle -p -u {url} content.images ;; reload
config.unbind('tPH') # config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload
config.unbind('tPh') # config-cycle -p -u *://{url:host}/* content.plugins ;; reload
config.unbind('tPu') # config-cycle -p -u {url} content.plugins ;; reload
config.unbind('tSH') # config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload
config.unbind('tSh') # config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload
config.unbind('tSu') # config-cycle -p -u {url} content.javascript.enabled ;; reload
config.unbind('tcH') # config-cycle -p -t -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload
config.unbind('tch') # config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload
config.unbind('tcu') # config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload
config.unbind('tiH') # config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload
config.unbind('tih') # config-cycle -p -t -u *://{url:host}/* content.images ;; reload
config.unbind('tiu') # config-cycle -p -t -u {url} content.images ;; reload
config.unbind('tpH') # config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload
config.unbind('tph') # config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload
config.unbind('tpu') # config-cycle -p -t -u {url} content.plugins ;; reload
config.unbind('tsH') # config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload
config.unbind('tsh') # config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload
config.unbind('tsu') # config-cycle -p -t -u {url} content.javascript.enabled ;; reload

config.unbind('-') # zoom-out
config.unbind('+') # zoom-in
config.unbind('=') # zoom

# config.unbind('wo') # set-cmd-text -s :open -w
# config.unbind('wO') # set-cmd-text :open -w {url:pretty}

config.unbind('wh') # back -w
config.unbind('wl') # forward -w

# config.unbind('wp') # open -w -- {clipboard}
# config.unbind('wP') # open -w -- {primary}

config.unbind('ga') # open -t

config.unbind('d') # tab-close
config.unbind('D') # undo

config.unbind('T') # tab-focus
config.unbind('th') # back -t
config.unbind('tl') # forward -t

config.unbind('xo') # set-cmd-text -s :open -b
config.unbind('xO') # set-cmd-text :open -b -r {url:pretty}

config.unbind('Pp') # open -t -- {clipboard}
config.unbind('PP') # open -t -- {primary}

config.unbind('gm') # tab-move
config.unbind('g$') # tab-focus -1
config.unbind('g0') # tab-focus 1
config.unbind('g^') # tab-focus 1
config.unbind('gC') # tab-clone
config.unbind('gD') # tab-give
config.unbind('gJ') # tab-move +
config.unbind('gK') # tab-move -
config.unbind('co') # tab-only
config.unbind('<Ctrl-p>') # Pin Tab

config.unbind('ad') # download-cancel
config.unbind('gd') # download

config.unbind('Sh') # history

config.unbind('b')  # quickmark-load
config.unbind('B')  # quickmark-load -t
config.unbind('M')  # bookmark-add
config.unbind('Sq') # bookmark-list
config.unbind('Sb') # bookmark-list --jump

config.unbind(';r') # hint --rapid links tab-bg
config.unbind(';R') # hint --rapid links window
config.unbind(';d') # hint links download
config.unbind(';I') # hint images tab
config.unbind(';t') # hint inputs
config.unbind(';y') # hint links yank
config.unbind(';Y') # hint links yank-primary
config.unbind('gi') # hint inputs --first

config.unbind('gf')  # view-source
config.unbind('wi')  # devtools
config.unbind('wIf') # devtools-focus
config.unbind('wIh') # devtools left
config.unbind('wIj') # devtools bottom
config.unbind('wIk') # devtools top
config.unbind('wIl') # devtools right
config.unbind('wIw') # devtools window

config.bind('Ss', 'set')
config.bind('ss', 'set-cmd-text -s :set')
config.bind('sl', 'set-cmd-text -s :set -t')

config.bind('sk', 'set-cmd-text -s :bind')

config.bind('<Ctrl-Shift-Tab>', 'nop')

config.bind('sf', 'save')

config.bind('<F11>', 'fullscreen')

config.bind('<Space>tt', 'config-cycle tabs.show multiple never')
config.bind('<Space>tb', 'config-cycle statusbar.show always never')
config.bind('<Space>tz', 'config-cycle tabs.show multiple never ;; config-cycle statusbar.show always never')

config.bind('<Space>ca' , 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""')
config.bind('<Space>cd' , 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""')
config.bind('<Space>cg' , 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""')
config.bind('<Space>csd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""')
config.bind('<Space>csl', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""')

config.bind('r', 'reload')
config.bind('R', 'reload -f')
config.bind('<Ctrl-R>', 'reload -f')
config.bind('<F5>', 'reload')
config.bind('<Ctrl-F5>', 'reload -f')

config.bind('<Space>p', 'set-cmd-text -s :process')
config.bind('<Space>m', ':messages -t')

config.bind('<Alt-x>', 'set-cmd-text :')
config.bind(':', 'set-cmd-text :')
config.bind('/', 'set-cmd-text /')
config.bind('?', 'set-cmd-text ?')
config.bind('.', 'repeat-command')

config.bind('n', 'search-next')
config.bind('N', 'search-prev')

config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave ;; clear-messages')
config.bind('cm', 'clear-messages')

config.bind('q', 'macro-record')
config.bind('@', 'macro-run')

config.bind('<Space>qq', 'quit')
config.bind('<Space>qr', 'restart')

config.bind('<Space>hr', 'config-source')
config.bind('<Space>hh', 'help -t')
config.bind('<Space>hs', 'set-cmd-text -s :help -t')
config.bind('<F1>'     , 'help -t')

config.bind('<Space><Tab>c', 'session-save -c ;; set-cmd-text -s :session-load --clear')
config.bind('<Space><Tab>d', 'set-cmd-text -s :session-delete')
config.bind('<Space><Tab>l', 'set-cmd-text -s :session-load')
config.bind('<Space><Tab>R', 'session-load -f autosave')
config.bind('<Space><Tab>s', 'set-cmd-text -s :session-save --only-active-window')
config.bind('<Space><Tab>S', 'set-cmd-text -s :session-save')
config.bind('<Space><Tab>t', 'set-cmd-text -s :session-load -temp')
config.bind('<Space><Tab>u', 'session-save')
config.bind('<Space><Tab>x', 'set-cmd-text -s :session-delete')

config.bind('h', 'scroll left')
config.bind('j', 'scroll down')
config.bind('k', 'scroll up')
config.bind('l', 'scroll right')
config.bind('J', 'run-with-count 5 scroll down')
config.bind('K', 'run-with-count 5 scroll up')

config.bind('<Ctrl-B>', 'scroll-page 0 -1')
config.bind('<Ctrl-F>', 'scroll-page 0 1')
config.bind('<Ctrl-U>', 'scroll-page 0 -0.5')
config.bind('<Ctrl-D>', 'scroll-page 0 0.5')

config.bind('gg', 'scroll-to-perc 0')
config.bind('G', 'scroll-to-perc')

config.bind('<Ctrl-0>', 'zoom')
config.bind('<Ctrl-->', 'zoom-out')
config.bind('<Ctrl-=>', 'zoom-in')

config.bind('g=', 'navigate increment')
config.bind('g-', 'navigate decrement')
config.bind('gu', 'navigate up')
config.bind('gU', 'navigate up -t')
config.bind('[[', 'navigate prev')
config.bind(']]', 'navigate next')
config.bind('{{', 'navigate prev -t')
config.bind('}}', 'navigate next -t')

config.bind('<Space>wq', 'close')
config.bind('<Space>wO', 'window-only')

config.bind('wH', 'back -w')
config.bind('wL', 'forward -w')

config.bind('wf', 'hint all window')

config.bind('wb', 'set-cmd-text -s :quickmark-load -w')
config.bind('wB', 'set-cmd-text -s :bookmark-load -w')

config.bind('<Ctrl-N>', 'open -w')
config.bind('<Ctrl-Shift-W>', 'close')

config.bind('U', 'undo -w')
config.bind('<Space>wu', 'undo -w')

config.bind('<back>', 'back')
config.bind('<forward>', 'forward')
config.bind('H', 'back')
config.bind('L', 'forward')
config.bind('tH', 'back -t')
config.bind('tL', 'forward -t')

config.bind('<Ctrl-Shift-h>', 'back -b')
config.bind('<Ctrl-Shift-l>', 'forward -b')

config.bind('<Ctrl-h>', 'home')

config.bind('<Ctrl-T>', 'open -t')
config.bind('tn', 'open -t')

config.bind('o', 'set-cmd-text -s :open')

config.bind('O', 'set-cmd-text -s :open -t')
config.bind('<Space>to', 'set-cmd-text -s :open -t')
config.bind('<Space>tO', 'set-cmd-text :open -t {url:pretty}')
config.bind('gs', 'set-cmd-text -s :open -b')

config.bind('go', 'set-cmd-text :open {url:pretty}')

config.bind('gO', 'set-cmd-text :open -t -r {url:pretty}')
config.bind('gS', 'set-cmd-text :open -b -r {url:pretty}')

config.bind('pp', 'open -- {clipboard}')
config.bind('pP', 'open -- {primary}')

config.bind('<Space>tp', 'open -t -- {clipboard}')
config.bind('<Space>tP', 'open -t -- {primary}')

config.bind('<Return>', 'selection-follow')
config.bind('<Shift-Return>', 'selection-follow -t')

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
config.bind('<Space>`', 'tab-focus last')

config.bind('<Alt-PgDown>', 'tab-next')
config.bind('<Alt-PgUp>', 'tab-prev')
config.bind('<Alt-l>', 'tab-next')
config.bind('<Alt-h>', 'tab-prev')
config.bind('<Alt-Ctrl-l>', 'tab-focus stack-next')
config.bind('<Alt-Ctrl-h>', 'tab-focus stack-prev')
config.bind('<Alt-Shift-l>', 'tab-focus -1')
config.bind('<Alt-Shift-h>', 'tab-focus 1')

config.bind('gt', 'set-cmd-text -sr :tab-focus')
config.bind('<Space>,', 'set-cmd-text -sr :tab-focus')
config.bind('<Space><', 'set-cmd-text -sr :tab-select')

config.bind('<Ctrl-W>', 'tab-close')
config.bind('x', 'tab-close')
# config.bind('tO', 'tab-only')

config.bind('<Ctrl-Shift-T>', 'undo')
config.bind('u', 'undo')
config.bind('X', 'undo')

config.bind('tm', 'tab-move')
config.bind('tj', 'tab-move +')
config.bind('tk', 'tab-move -')
config.bind('tJ', 'tab-move end')
config.bind('tK', 'tab-move start')
config.bind('>', 'tab-move +')
config.bind('<', 'tab-move -')
config.bind('<Alt-j>', 'tab-move +')
config.bind('<Alt-k>', 'tab-move -')
config.bind('<Alt-Shift-j>', 'tab-move end')
config.bind('<Alt-Shift-k>', 'tab-move start')

config.bind('<Ctrl-c>', 'stop')
config.bind('<Alt-m>', 'tab-mute')
config.bind('<Alt-p>', 'tab-pin')
config.bind('<Alt-p>', 'tab-pin', mode='insert')
config.bind('<Ctrl-Alt-p>', 'print')

config.bind('tG', 'tab-give')
config.bind('tP', 'tab-give --private')
config.bind('tg', 'set-cmd-text -s :tab-give')
config.bind('tt', 'set-cmd-text -s :tab-take')

config.bind('tcc', 'tab-clone')
config.bind('tcG', 'tab-give --keep')
config.bind('tcP', 'tab-give --keep --private')
config.bind('tcg', 'set-cmd-text -s :tab-give --keep')
config.bind('tct', 'set-cmd-text -s :tab-take --keep')

config.bind('D', 'set-cmd-text -s :download')

config.bind('ds', 'download-cancel')
config.bind('dC', 'download-cancel')

config.bind('dx', 'download-remove')
config.bind('dr', 'download-retry')
config.bind('dc', 'download-clear')

config.bind('do', 'download-open')
config.bind('dX', 'download-delete')

config.bind('di', 'hint images download')
config.bind('dl', 'hint links download')
config.bind('dt', 'hint links spawn transmission-remote -a {hint-url}')
config.bind('da', 'hint links spawn alacritty -e youtube-dl -f bestaudio {hint-url}')
config.bind('dv', 'hint media spawn alacritty -e youtube-dl {hint-url}')

config.bind('dA', 'spawn alacritty -e youtube-dl -f bestaudio {url}')
config.bind('dV', 'spawn alacritty -e youtube-dl {url}')

config.bind('<Ctrl-P>', 'prompt-open-download --pdfjs', mode='prompt')
config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')

config.bind('ys', 'yank selection', mode='normal')
config.bind('<Ctrl-c>', 'yank selection', mode='normal')

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
config.bind('yi', 'hint images yank')
config.bind('Yi', 'hint images yank-primary')

config.bind('gq', 'bookmark-list --tab')
config.bind('gb', 'bookmark-list --tab --jump')

config.bind('bo', 'set-cmd-text -s :quickmark-load')
config.bind('Bo', 'set-cmd-text -s :bookmark-load')

config.bind('bO', 'set-cmd-text -s :quickmark-load -t')
config.bind('BO', 'set-cmd-text -s :bookmark-load -t')

config.bind('bs', 'quickmark-save')
config.bind('Bs', 'bookmark-add')
config.bind('ba', 'quickmark-add {url} "{title}" ;; message-info "Quickmark saved!"')
config.bind('bA', 'set-cmd-text -s :quickmark-add {url}')
config.bind('Ba', 'bookmark-add {url} "{title}"')
config.bind('BA', 'set-cmd-text -s :bookmark-add {url}')

config.bind('bd', 'quickmark-del ;; message-info "Quickmark {url} deleted!')
config.bind('Bd', 'bookmark-del')

config.bind('gh', 'history -t')

config.bind('f', 'hint')
config.bind('F', 'hint all tab')

config.bind(';i', 'hint inputs')

config.bind(';m', 'hint media')
config.bind(';p', 'hint images')
config.bind(';P', 'hint images tab')

config.bind(';h', 'hint all hover')

config.bind(';v', 'hint links spawn mpv --ytdl-format=best {hint-url}')
config.bind(';a', 'hint links spawn mpv --ytdl-format=best {hint-url} --no-video')

config.bind('<Ctrl-f>', 'hint --rapid')

config.bind(';ri', 'hint --rapid images tab-bg')
config.bind(';Ri', 'hint --rapid images window')

config.bind(';rl', 'hint --rapid links tab-bg')
config.bind(';Rl', 'hint --rapid links window')

config.bind(';o', 'hint links fill :open {hint-url}')
config.bind(';O', 'hint links fill :open -t -r {hint-url}')

config.bind(';da', 'hint all delete')
config.bind(';dl', 'hint links delete')
config.bind(';di', 'hint images delete')
config.bind(';dm', 'hint media delete')

config.bind('<Ctrl-p><a>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)"'                )
config.bind('<Ctrl-p><u>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --username-only')
config.bind('<Ctrl-p><p>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --password-only')
config.bind('<Ctrl-p><o>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --otp-only'     )

config.bind('<Ctrl-p><a>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)"'                , mode='insert')
config.bind('<Ctrl-p><u>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --username-only', mode='insert')
config.bind('<Ctrl-p><p>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --password-only', mode='insert')
config.bind('<Ctrl-p><o>', 'spawn --userscript qute-pass --username-target secret --username-pattern "(?:login|user): (.+)" --otp-only'     , mode='insert')

config.bind('<Space>vv', 'spawn mpv --ytdl-format=best {url}')                               # play current video
config.bind('<Space>aa', 'spawn mpv --ytdl-format=best {url} --no-video')                    # play current audio

config.bind('<Space>ds', 'view-source')

config.bind('<Space>dt', 'devtools')
config.bind('<Space>dd', 'devtools')
config.bind('<Space>df', 'devtools-focus')

config.bind('<Space>dH', 'devtools left')
config.bind('<Space>dL', 'devtools right')
config.bind('<Space>dJ', 'devtools bottom')
config.bind('<Space>dK', 'devtools top')
config.bind('<Space>dW', 'devtools window')

config.bind('<Space>dD', 'hint all delete')

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

config.bind('<Ctrl-E>'      , 'edit-command'           , mode='command')
config.bind('<Return>'      , 'command-accept'         , mode='command')
config.bind('<Ctrl-Return>' , 'command-accept --rapid' , mode='command')

config.bind('<Ctrl-k>'       , 'completion-item-focus prev'         , mode='command')
config.bind('<Ctrl-j>'       , 'completion-item-focus next'         , mode='command')
config.bind('<Ctrl-Shift-k>' , 'completion-item-focus prev-page'    , mode='command')
config.bind('<Ctrl-Shift-j>' , 'completion-item-focus next-page'    , mode='command')
config.bind('<Ctrl-Shift-h>' , 'completion-item-focus prev-category', mode='command')
config.bind('<Ctrl-Shift-l>' , 'completion-item-focus next-category', mode='command')

config.bind('<Ctrl-C>'       , 'completion-item-yank'               , mode='command')
config.bind('<Ctrl-D>'       , 'completion-item-del'                , mode='command')

config.bind('<Alt-Backspace>' , 'rl-backward-kill-word' , mode='command')
config.bind('<Ctrl-W>'        , 'rl-backward-kill-word' , mode='command')
config.bind('<Ctrl-Shift-W>'  , 'rl-unix-word-rubout'   , mode='command')
# config.bind('<Alt-D>'       , 'rl-kill-word'          , mode='command')
# config.bind('<Ctrl-?>'      , 'rl-delete-char'        , mode='command')

config.bind('<Ctrl-0>'       , 'rl-beginning-of-line' , mode='command')
config.bind('<Ctrl-Shift-$>' , 'rl-end-of-line'       , mode='command')
# config.bind('<Ctrl-A>'     , 'rl-beginning-of-line' , mode='command')

config.bind('<Ctrl-H>'       , 'rl-backward-word'     , mode='command')
config.bind('<Ctrl-L>'       , 'rl-forward-word'      , mode='command')
# config.bind('<Alt-B>'      , 'rl-backward-word'     , mode='command')
# config.bind('<Alt-F>'      , 'rl-forward-word'      , mode='command')

config.bind('<Ctrl-B>'       , 'rl-backward-char'     , mode='command')
config.bind('<Ctrl-F>'       , 'rl-forward-char'      , mode='command')

# config.bind('<Ctrl-K>'        , 'rl-kill-line'                        , mode='command')
# config.bind('<Ctrl-N>'        , 'command-history-next'                , mode='command')
# config.bind('<Ctrl-P>'        , 'command-history-prev'                , mode='command')
# config.bind('<Ctrl-Shift-C>'  , 'completion-item-yank --sel'          , mode='command')
# config.bind('<Ctrl-Shift-Tab>', 'completion-item-focus prev-category' , mode='command')
# config.bind('<Ctrl-Tab>'      , 'completion-item-focus next-category' , mode='command')
# config.bind('<Ctrl-U>'        , 'rl-unix-line-discard'                , mode='command')
# config.bind('<Ctrl-Y>'        , 'rl-yank'                             , mode='command')
# config.bind('<Down>'          , 'completion-item-focus --history next', mode='command')
# config.bind('<PgDown>'        , 'completion-item-focus next-page'     , mode='command')
# config.bind('<PgUp>'          , 'completion-item-focus prev-page'     , mode='command')
# config.bind('<Shift-Delete>'  , 'completion-item-del'                 , mode='command')
# config.bind('<Shift-Tab>'     , 'completion-item-focus prev'          , mode='command')
# config.bind('<Tab>'           , 'completion-item-focus next'          , mode='command')
# config.bind('<Up>'            , 'completion-item-focus --history prev', mode='command')

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

config.bind('<Alt-Shift-Y>', 'prompt-yank --sel'       , mode='yesno')
config.bind('<Alt-Y>'      , 'prompt-yank'             , mode='yesno')
config.bind('<Return>'     , 'prompt-accept'           , mode='yesno')
config.bind('N'            , 'prompt-accept --save no' , mode='yesno')
config.bind('Y'            , 'prompt-accept --save yes', mode='yesno')
config.bind('n'            , 'prompt-accept no'        , mode='yesno')
config.bind('y'            , 'prompt-accept yes'       , mode='yesno')

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

config.bind('<Ctrl-E>'       , 'edit-text'                   , mode='insert')

config.bind('<Mod1-H>'       , 'fake-key <Left>'             , mode='insert')
config.bind('<Mod1-J>'       , 'fake-key <Down>'             , mode='insert')
config.bind('<Mod1-K>'       , 'fake-key <Up>'               , mode='insert')
config.bind('<Mod1-L>'       , 'fake-key <Right>'            , mode='insert')
config.bind('<Mod1-Shift-H>' , 'fake-key <Shift-Left>'       , mode='insert')
config.bind('<Mod1-Shift-L>' , 'fake-key <Shift-Right>'      , mode='insert')
config.bind('<Ctrl-H>'       , 'fake-key <Ctrl-Left>'        , mode='insert')
config.bind('<Ctrl-J>'       , 'fake-key <End>'              , mode='insert')
config.bind('<Ctrl-K>'       , 'fake-key <Home>'             , mode='insert')
config.bind('<Ctrl-L>'       , 'fake-key <Ctrl-Right>'       , mode='insert')
config.bind('<Ctrl-Shift-H>' , 'fake-key <Ctrl-Shift-Left>'  , mode='insert')
config.bind('<Ctrl-Shift-L>' , 'fake-key <Ctrl-Shift-Right>' , mode='insert')
config.bind('<Ctrl-W>'       , 'fake-key <Ctrl-Backspace>'   , mode='insert')

config.bind('<Ctrl-Shift-V>', 'insert-text -- {primary}', mode='insert')
config.bind('<Shift-Ins>'   , 'insert-text -- {primary}', mode='insert')

config.bind('<Ctrl-B>', 'hint all tab-bg'          , mode='hint')
config.bind('<Ctrl-F>', 'hint links'               , mode='hint')
config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
config.bind('<Return>', 'hint-follow'              , mode='hint')

c.content.canvas_reading = True

def filter_yt(info: interceptor.Request):
    """Block the given request if necessary."""
    url = info.request_url
    if (
        url.host() == "www.youtube.com"
        and url.path() == "/get_video_info"
        and "&adformat=" in url.query()
    ):
        info.block()


interceptor.register(filter_yt)

c.content.blocking.enabled = True

c.content.blocking.method = "both"

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

# c.content.cache.appcache = True

# c.content.cache.maximum_pages = 0

# c.content.cache.size = None

c.content.desktop_capture = "ask"
c.content.geolocation = "ask"
c.content.media.audio_capture = "ask"
c.content.media.video_capture = "ask"
c.content.media.audio_video_capture = "ask"
c.content.mouse_lock = "ask"
c.content.notifications.enabled = "ask"
c.content.persistent_storage = 'ask'

# Show javascript alerts.
# Type: Bool
# c.content.javascript.alert = True

# Allow JavaScript to read from or write to the clipboard. With
# QtWebEngine, writing the clipboard as response to a user interaction
# is always allowed.
# Type: Bool
# c.content.javascript.can_access_clipboard = False

# Allow JavaScript to close tabs.
# Type: Bool
# c.content.javascript.can_close_tabs = False

# Allow JavaScript to open new tabs without user interaction.
# Type: Bool
# c.content.javascript.can_open_tabs_automatically = False

# Enable JavaScript.
# Type: Bool
# c.content.javascript.enabled = True

# Log levels to use for JavaScript console logging messages. When a
# JavaScript message with the level given in the dictionary key is
# logged, the corresponding dictionary value selects the qutebrowser
# logger to use. On QtWebKit, the "unknown" setting is always used. The
# following levels are valid: `none`, `debug`, `info`, `warning`,
# `error`.
# Type: Dict
# c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}

# Use the standard JavaScript modal dialog for `alert()` and
# `confirm()`.
# Type: Bool
# c.content.javascript.modal_dialog = False

# Show javascript prompts.
# Type: Bool
# c.content.javascript.prompt = True

c.content.notifications.presenter = 'auto'

c.content.notifications.show_origin = True

c.spellcheck.languages = [
    "en-US",
    "ru-RU",
]

c.hints.auto_follow = 'unique-match'

c.hints.auto_follow_timeout = 0

# c.hints.border = '1px solid #E3BE23'

# c.hints.chars = 'asdfghjkl'
c.hints.chars = 'qwertyuopasdfghjkzxcvbnm'

c.hints.dictionary = '/usr/share/dict/words'

# c.hints.find_implementation = 'python'

c.hints.hide_unmatched_rapid_hints = True

c.hints.leave_on_load = False

c.hints.min_chars = 1

c.hints.mode = 'letter'

c.hints.next_regexes = ['\\bnext\\b', '\\bmore\\b', '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b']

c.hints.prev_regexes = ['\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b']

c.hints.padding = {'top': 0, 'bottom': 0, 'left': 3, 'right': 3}

c.hints.radius = 3

c.hints.scatter = True

c.hints.selectors = {
    'all': ['a', 'area', 'textarea', 'select', 'input:not([type="hidden"])', 'button', 'frame', 'iframe', 'img', 'link', 'summary', '[contenteditable]:not([contenteditable="false"])', '[onclick]', '[onmousedown]', '[role="link"]', '[role="option"]', '[role="button"]', '[ng-click]', '[ngClick]', '[data-ng-click]', '[x-ng-click]', '[tabindex]'],
    'links': ['a[href]', 'area[href]', 'link[href]', '[role="link"][href]'],
    'images': ['img'],
    'media': ['audio', 'img', 'video'],
    'video': ['audio', 'video'],
    'url': ['[src]', '[href]'],
    'inputs': ['input[type="text"]', 'input[type="date"]', 'input[type="datetime-local"]', 'input[type="email"]', 'input[type="month"]', 'input[type="number"]', 'input[type="password"]', 'input[type="search"]', 'input[type="tel"]', 'input[type="time"]', 'input[type="url"]', 'input[type="week"]', 'input:not([type])', '[contenteditable]:not([contenteditable="false"])', 'textarea']
}

c.hints.uppercase = False

c.keyhint.delay = 500
c.keyhint.blacklist = []

c.editor.command = ['alacritty', '-e', 'vim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

c.editor.encoding = 'utf-8'

# c.content.pdfjs = False
# c.content.plugins = False
# c.content.prefers_reduced_motion = False
# c.content.print_element_backgrounds = True
c.content.private_browsing = False
# c.content.proxy_dns_requests = True
# c.content.site_specific_quirks.enabled = True
# c.content.webgl = True

# c.content.proxy = 'system'

# c.content.register_protocol_handler = 'ask'

# c.content.site_specific_quirks.skip = ['js-string-replaceall']

# c.content.tls.certificate_errors = 'ask'

# c.content.unknown_url_scheme_policy = 'allow-from-user-interaction'

# c.content.user_stylesheets = ["~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css"]

# c.content.webrtc_ip_handling_policy = 'all-interfaces'

# c.content.xss_auditing = False

c.history_gap_interval = 30

c.fileselect.handler = 'external'

c.fileselect.folder.command = ['alacritty', '--class', 'dialog,dialog', '-e', 'vifmrun', '--choose-dir', '{}']
c.fileselect.single_file.command = ['alacritty', '--class', 'dialog,dialog', '-e', 'vifmrun', '--choose-files', '{}']
c.fileselect.multiple_files.command = ['alacritty', '--class', 'dialog,dialog', '-e', 'vifmrun', '--choose-files', '{}']

# c.fileselect.single_file.command = ['alacritty', '--class', 'dialog,dialog', '-e', 'ranger', '--choosefile={}']
# c.fileselect.multiple_files.command = ['alacritty', '--class', 'dialog,dialog', '-e', 'ranger', '--choosefiles={}']

c.input.escape_quits_reporter = True

c.input.forward_unbound_keys = 'auto'

c.input.insert_mode.auto_enter = True

c.input.insert_mode.auto_leave = False

c.input.insert_mode.auto_load = False

c.input.insert_mode.leave_on_load = True

c.input.insert_mode.plugins = False

c.input.links_included_in_focus_chain = False

c.input.media_keys = True

c.input.mouse.back_forward_buttons = True

c.input.mouse.rocker_gestures = False

c.input.partial_timeout = 30000

c.input.spatial_navigation = False

c.search.ignore_case = 'smart'

c.search.incremental = True

c.search.wrap = True

c.tabs.background = True

c.tabs.close_mouse_button = 'middle'

c.tabs.close_mouse_button_on_bar = 'new-tab'

c.tabs.mousewheel_switching = False

# c.qt.args = []

# c.qt.environ = {}

# c.qt.force_platform = None

# c.qt.force_platformtheme = None

# c.qt.force_software_rendering = 'none'

# c.qt.highdpi = False

c.qt.chromium.low_end_device_mode = 'auto'

c.qt.chromium.process_model = 'process-per-site-instance'

# c.qt.workarounds.locale = False

# c.qt.workarounds.remove_service_workers = False

# c.logging.level.console = 'info'

# c.logging.level.ram = 'debug'

if os.path.isfile(os.path.expanduser('~/.config/qutebrowser/local.py')):
    config.source('local.py')
