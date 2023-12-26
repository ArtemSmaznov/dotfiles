(define-configuration browser
    ((theme theme:+dark-theme+)))

;; (defmethod customize-instance ((browser browser) &key)
;;   (setf (slot-value browser 'default-new-buffer-url) "nyxt:new"))

(define-configuration
    (web-buffer panel-buffer
                nyxt/mode/editor:editor-buffer)
    ((default-modes
      (pushnew 'nyxt/mode/vi:vi-normal-mode %slot-value%))))

(define-configuration (web-buffer input-buffer)
    ((override-map
      (let ((map (make-keymap "override-map")))
        (define-key map
          "M-x" 'execute-command
          "g t" 'switch-buffer
          "C-space" 'nothing)))))
