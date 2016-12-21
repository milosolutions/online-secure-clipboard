angular.
    module('detail').
    component('detail', {
        templateUrl: '/static/js/app/detail/detail.template.html',
        controller: function ($stateParams, Paste) {
            var self = this,
                text = $('#text'),
                password = $('#password'),
                decryptedText,
                originalText,
                paste;

            paste = Paste.get({pasteId:  $stateParams.id}, function (paste) {
                originalText = paste.text;
                self.text = JSON.parse(originalText).ct;
            });

            password.on('input', function () {
                if (this.value) {
                    decryptedText = CryptoJS.AES.decrypt(originalText, this.value, {format: JsonFormatter});
                    text.val(decryptedText.toString(CryptoJS.enc.Utf8));

                } else
                    text.val(originalText);
            });
        }

    });
