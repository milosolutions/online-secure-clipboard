angular.module('encryptionApp').config(['$qProvider', function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
}]);

angular.module('encryptionApp').config(function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

angular.module('encryptionApp').config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

angular.module('encryptionApp').config(function ($stateProvider, $urlRouterProvider) {
    var indexState = {
        name: 'index',
        url: '/',
        component: 'index'
    };

    var detailState = {
        name: 'detail',
        url: '/paste/{id}',
        component: 'detail'
    };

    $urlRouterProvider.otherwise('/');

    $stateProvider.state(indexState);
    $stateProvider.state(detailState);
});
