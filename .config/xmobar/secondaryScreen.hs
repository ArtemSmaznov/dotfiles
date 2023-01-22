Config {
   -- appearance
     font            = "xft:SF Pro Text Regular:size=9:bold:antialias=true"
   , additionalFonts = [ "xft:Hack Nerd Font Mono:style=Regular:pixelsize=22"    -- 1
                       , "xft:Hack Nerd Font Mono:style=Regular:pixelsize=28"    -- 2
                       , "xft:Hack Nerd Font Mono:style=Regular:pixelsize=32"    -- 3
                       , "xft:Source Han Sans JP"                                -- 4
                       , "xft:Font Awesome 6 Free Solid:pixelsize=16"            -- 5 used for workspaces in xmonad
                       , "xft:Font Awesome 6 Free Solid:pixelsize=14"            -- 6 used for network arrows
                       ]
   , bgColor         = "#282828"
   , fgColor         = "#ebdbb2"
   , position        = TopH 24
   , lowerOnStart     = True    -- send to bottom of window stack on start
   , hideOnStart      = False   -- start with window unmapped (hidden)
   , allDesktops      = True    -- show on all desktops
   , overrideRedirect = True    -- set the Override Redirect flag (Xlib)
   , pickBroadest     = False   -- choose widest display (multi-monitor)
   , persistent       = True    -- enable/disable hiding (True = disabled)
   , sepChar  = "%"   -- delineator between plugin names and straight text
   , alignSep = "}{"  -- separator between left-right alignment
   , iconRoot = ".config/xmobar/xpm/"
   , commands =
        [ Run Com "echo" ["<fc=#7c6f64>|</fc>"] "sep" 36000
        , Run Com "echo" ["<action=`rofi -show drun`> <fn=3><fc=#1793d1>\xf303</fc></fn></action>"] "logo" 36000
        , Run Date
          "%l:%M %p "
          "time" 10
        , Run UnsafeStdinReader
        , Run MPD
          ["-t", "  <statei>  <artist> - <title> [<flags>] " -- ["-t", "<box type=Bottom width=2 mb=2 color=#fabd2f> <statei>  <artist> - <title> </box>"
               , "--"
               , "-P", "<fn=1></fn>" -- play icon
               , "-Z", "<fn=1></fn>" -- pause icon
               , "-S", "<fn=1></fn>" -- stop icon
               ] 10
        , Run Com "echo" ["<action=`.local/bin/dm-scripts/dm-lang`> "] "_ks" 3600
        , Run Kbd
          [ ("us" , "<fc=#fabd2f>US</fc>")
          , ("ru" , "<fc=#458588>RU</fc>")
          , ("jp" , "<fn=4><fc=#fbf1c7>日本</fc></fn>")
          ]
        , Run Com "echo" [" </action>"] "_ke" 3600
        , Run Com "echo" ["<box type=Bottom width=2 mb=2 color=#fb4934><action=`alacritty -e sudo pacman -Syu`>  <fn=1>\xf0f3</fn>  "] "_us" 3600
        , Run Com ".local/bin/dm-scripts/helpers/updates" [] "updates" 3600
        , Run Com "echo" ["  </action></box>"] "_ue" 3600
        , Run BatteryP ["cat /sys/class/sony_controller_battery_a0:ab:51:62:65:1d/capacity"]
          ["-t", "<acstatus><watts> <left>%"
               , "--low", "20"
               -- , "--"
               ] 100
        , Run DynNetwork
          ["-t", "<box type=Bottom width=2 mb=2 color=#8ec07c>  <fn=1>\xf484</fn>  <rx> <fn=6>\xf309\xf30c</fn> <tx> </box>"
               , "-S", "True"
               , "--"
               , "--devices", "eno1,wlan0,enp2s0f0"
               ] 20
        , Run CoreTemp
          ["-t", "<box type=Bottom width=2 mb=2 color=#d3869b><action=`alacritty -e htop`>  <fn=1>\xf85a</fn>  <core0>° "
               -- High CPU Temp
               , "-H", "70"
               , "-h", "#fb4934"
               -- Low CPU Temp
               , "-L", "40"
               , "-l", "#b8bb26"
               ] 20
        , Run Cpu
          ["-t", "(<total>%)  </action></box>"
               -- High CPU Load
               , "-H", "80"
               , "-h", "#fb4934"
               -- Low CPU Load
               , "-L", "5"
               , "-l", "#b8bb26"
               ] 20
        , Run Memory
          ["-t", "<box type=Bottom width=2 mb=2 color=#83a598><action=`alacritty -e htop`>  <fn=1>\xf2db</fn>  <used> M (<usedratio>%)  </action></box>"
               ] 20
        , Run Volume "default" "Master"
          ["-t", "<box type=Bottom width=2 mb=2 color=#b8bb26><action=`alacritty -e alsamixer`>  <status>  <volume>%</action>  </box>"
               , "--"
               -- ON Icon
               , "-O", "<fn=2>\xfa7d</fn>"
               , "-C", "#b8bb26"
               -- OFF Icon
               , "-o", "<fn=2>\xfa80</fn>"
               , "-c", "#fb4934"
               ] 10
        , Run Date
          "<action=`emacsclient -c -a 'emacs' --eval '(cfw:open-org-calendar)'`>  <fn=1>\xf5f5</fn>  %a, %d %b %Y  </action>"
          "date" 3600
        , Run Uptime
          ["-t", "<box type=Bottom width=2 mb=2 color=#fabd2f>  <fn=2>\xf0aa</fn>  <days>d <hours>h  </box>"
               ] 3600
        , Run Com ".config/xmobar/trayer-padding-icon.sh" [] "trayerpad" 20
]
   , template = "%logo% %time% %sep% %UnsafeStdinReader% } { %mpd% %sep% %kbd% %sep% %default:Master% %uptime% %sep% %date% "
   }
