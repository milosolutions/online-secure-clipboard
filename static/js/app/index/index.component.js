angular.
    module('index').
    component('index', {
        templateUrl: '/static/js/app/index/index.template.html',
        controller: function () {
            var text = $('#text'),
                password = $('#password'),
                expire = $('#expire'),
                encrypted = $('#encrypted'),
                originalText,
                encryptedObj;

            text.on('change', function () {
               originalText = this.value
            });

            password.on('input', function () {
                text.attr('readonly', 'readonly');
                if (this.value) {
                    encryptedObj = CryptoJS.AES.encrypt(originalText, this.value, {format: JsonFormatter});
                    encrypted.val(encryptedObj.toString());
                    text.val(JSON.parse(encryptedObj).ct);
                } else
                    text.val(originalText);
            });

            $('form').on('submit', function (e) {
                e.preventDefault();
                console.log({'text': encryptedText.toString(), 'expire': expire.val()})
            })

        }

    });
