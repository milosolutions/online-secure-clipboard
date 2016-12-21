angular.
    module('core.paste').
    factory('Paste', ['$resource',
        function ($resource) {
            return $resource('api/pastes/:pasteId');
        }
    ]);
