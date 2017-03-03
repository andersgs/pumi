(function () {
    'use strict';

    angular
    .module('pumi.epidata', [
        'pumi.epidata.controllers',
        'pumi.epidata.services'
    ]);

    angular
    .module('pumi.epidata.controllers', []);

    angular
    .module('pumi.epidata.services', ['ngCookies']);
})();
