(function () {
    'use strict';

    angular
      .module('pumi', [
          'pumi.config',
          'pumi.routes',
          'pumi.epidata',
      ]);

      angular
      .module('pumi.routes', ['ngRoute']);

      angular
      .module('pumi.config', []);

      angular
      .module('pumi')
      .run(run);

      run.$inject = ['$http'];

      /**
      * @name run
      * @desc Update xsrf $htpp headers to align with Django's defaults
      **/
      function run($http) {
          $http.defaults.xsrfHeaderName = 'X-CSRFToken';
          $http.defaults.xsrfCookieName = 'csrftoken';
      }
})();
