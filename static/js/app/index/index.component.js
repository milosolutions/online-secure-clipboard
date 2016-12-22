angular.
    module('index').
    component('index', {
        templateUrl: '/static/js/app/index/index.template.html',
        controller: function (Paste, $state) {
            var text = $('#text'),
                password = $('#password'),
                expiry = $('#expiry'),
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

            function getDate(daysDelta) {
                var today = new Date();
                if (daysDelta) {
                    today.setDate(today.getDate() + daysDelta)
                }
                var dd = today.getDate();
                var mm = today.getMonth() + 1; //January is 0!

                var yyyy = today.getFullYear();
                if (dd < 10) {
                    dd = '0' + dd;
                }
                if (mm < 10) {
                    mm = '0' + mm;
                }
                return yyyy + '-' + mm + '-' + dd;
            }

            function expiryChange() {
                var expiryDate = getDate(parseInt(this.value) + 1);
                $('b.expiration').text(expiryDate + ' 00:01')
            }

            expiry.on('change', expiryChange);

            // trigger change event in order to display default expiry date help text
            expiry.change();

            $('form').on('submit', function (e) {
                e.preventDefault();

                var paste = new Paste();
                paste.text = encrypted.val();
                paste.expiry = expiry.val();
                paste.created_date = getDate();

                Paste.save(paste, function (data) {
                    $state.go('detail', {'id': data.id})
                }, function (error) {
                    $.each(error.data, function (field, errors) {
                        var $field = $('#' + field),
                            $parent = $field.parent(),
                            errorMessages = '';

                        $parent.addClass('has-error');

                        $.each(errors, function () {
                            errorMessages += '<li>' + this + '</li>';
                        });
                        $parent.append('<ul>' + errorMessages + '</ul>');

                    })
                })
            })

        }

    });
