(in-package #:nyxt-user)

(define-configuration window
  ((message-buffer-style
    (str:concat
     %slot-default%
     (cl-css:css
      '((body
         :background-color "#1F1F1F"
         :color "#C0B18B")))))))

(define-configuration prompt-buffer
  ((style (str:concat
           %slot-default%
           (cl-css:css
            '((body
               :background-color "#1F1F1F"
               :color "#C0B18B")
              ("#prompt-area"
               :background-color "#1F1F1F")
              ("#input"
               :background-color "#C0B18B")
              (".source-name"
               :color "#1F1F1F"
               :background-color "#556B2F")
              (".source-content"
               :background-color "#1F1F1F")
              (".source-content th"
               :border "1px solid #556B2F"
               :background-color "#1F1F1F")
              ("#selection"
               :background-color "#CD5C5C"
               :color "#1F1F1F")
              (.marked :background-color "#8B3A3A"
                       :font-weight "bold"
                       :color "#C0B18B")
              (.selected :background-color "#1F1F1F"
                         :color "#C0B18B")))))))

(define-configuration internal-buffer
  ((style
    (str:concat
     %slot-default%
     (cl-css:css
      '((title
         :color "#CD5C5C")
        (body
         :background-color "#1F1F1F"
         :color "lightgray")
        (hr
         :color "darkgray")
        (a
         :color "#556B2F")
        (.button
         :color "lightgray"
         :background-color "#556B2F")))))))

(define-configuration nyxt/history-tree-mode:history-tree-mode
  ((nyxt/history-tree-mode::style
    (str:concat
     %slot-default%
     (cl-css:css
      '((body
         :background-color "#1F1F1F"
         :color "lightgray")
        (hr
         :color "darkgray")
        (a
         :color "#556B2F")
        ("ul li::before"
         :background-color "#C0B18B")
        ("ul li::after"
         :background-color "#C0B18B")
        ("ul li:only-child::before"
         :background-color "#C0B18B")))))))

(define-configuration nyxt/web-mode:web-mode
  ((nyxt/web-mode:highlighted-box-style
    (cl-css:css
     '((".nyxt-hint.nyxt-highlight-hint"
        :background "#CD5C5C")))
    :documentation "The style of highlighted boxes, e.g. link hints.")))

(define-configuration status-buffer
  ((style (str:concat
           %slot-default%
           (cl-css:css
            '(("#controls"
               :border-top "1px solid white")
              ("#url"
               :background-color "#1F1F1F"
               :color "#C0B18B"
               :border-top "1px solid white")
              ("#modes"
               :background-color "#1F1F1F"
               :border-top "1px solid white")
              ("#tabs"
               :background-color "#CD5C5C"
               :color "#1F1F1F"
               :border-top "1px solid white")))))))

(define-configuration nyxt/style-mode:dark-mode
  ((style #.(cl-css:css
             '((*
                :background-color "black !important"
                :background-image "none !important"
                :color "#C0B18B")
               (a
                :background-color "black !important"
                :background-image "none !important"
                :color "#556B2F !important"))))))

(define-configuration buffer
  ((default-modes (append '(nyxt::vi-normal-mode) %slot-default%))))
(define-configuration prompt-buffer
  ((default-modes (append '(nyxt::vi-insert-mode) %slot-default%))))

(define-configuration web-buffer
  ((default-new-buffer-url "https://search.brave.com/")))

(defvar *my-search-engines*
  (list
   '("archwiki" "https://wiki.archlinux.org/index.php?search=~a" "https://wiki.archlinux.org/")
   '("qtiledocs" "http://docs.qtile.org/en/latest/search.html?q=~a&check_keywords=yes&area=default" "http://docs.qtile.org/")
   '("github" "https://github.com/search?q=~a&ref=opensearch" "https://github.com/")
   '("youtube" "https://www.youtube.com/results?search_query=~a" "https://www.youtube.com/")
   '("odysee" "https://odysee.com/$/search?q=~a" "https://odysee.com/")
   '("googledrive" "https://drive.google.com/drive/search?q=~a" "https://drive.google.com/")
   '("googlemaps" "https://www.google.com/maps/search/~a?hl=en&source=opensearch" "https://www.google.com/")
   '("googleimages" "https://www.google.com/search?q=~a" "https://www.google.com/")
   '("google" "https://www.google.com/search?q=~a" "https://www.google.com/")
   '("amazonuk" "https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=~a" "https://www.amazon.co.uk/")
   '("amazoncom" "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=~a" "https://www.amazon.com/")
   '("amazonca" "https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=~a" "https://www.amazon.ca/")
   '("brave" "https://search.brave.com/search?q=~a" "https://search.brave.com/")
   ))

(define-configuration buffer
  ((search-engines (append %slot-default%
                           (mapcar (lambda (engine) (apply 'make-search-engine engine))
                                   *my-search-engines*)))))
