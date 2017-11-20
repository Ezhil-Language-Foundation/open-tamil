/**
        spellchecker_language : 'ta_IN',
        spellchecker_callback: ta_spellchecker_cb
        
function ta_spellchecker_cb(method, text, success, failure) {
      tinymce.util.JSONRequest.sendRPC({
            url: "/spellchecker",
            method: "spellcheck",
            params: {
              lang: this.getLanguage(),
              words: text.match(this.getWordCharPattern())
            },
            success: function(result) {
              success(result);
            },
            error: function(error, xhr) {
              failure("Spellcheck error:" + xhr.status);
            }
     });    
};
*/
