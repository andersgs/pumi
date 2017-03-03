
(function () {
    'use strict';

    angular
    .module('pumi.routes')
    .config(config);

    config.$inject = ['$routeProvider'];

    /**
    * @name config
    * @desc Define valid application routers
    **/
    function config($routeProvider) {
        $routeProvider.when('/login', {
            controller: 'LoginController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/authentication/login.html'
        }).otherwise('/');
    }
})();
