/**
* authentication
* @namespace pumi.epidata.services
* */
(function () {
    'use strict';

    angular
    .module('pumi.epidata.services')
    .factory('Authentication', Authentication);

    Authentication.$inject = ['$cookies', '$http'];

    /**
    * @namespace Authentication
    * @return {Factory}
    **/
    function Authentication($cookies, $http) {
        /**
        * @name Authentication
        * @desc The Factory to be returned
        **/
        var Authentication = {
            // register: register,
            login: login,
            getAuthenticatedAccount: getAuthenticatedAccount,
            setAuthenticatedAccount: setAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            unauthenticate: unauthenticate
        };

        return Authentication;

        ///////////////////////////////////////////////

        // /**
        // * @name register
        // * @desc Try to register a new username
        // * @param {string} email The email entered by the user
        // * @param {string} username The username entered by the username
        // * @param {string} password The password entered by the user
        // * @returns {Promise}
        // * @memberOf epumi.epidata.services.Authentication
        // **/
        //
        // function register(password, username) {
        //     return $http.post('/api/v1/accounts/', {
        //         password: password,
        //         username: username
        //     }).then(registerSuccessFn,registerErrorFn);
        //
        //     /**
        //     * @name registerSuccessFn
        //     * @desc Log the new user in
        //     **/
        //     function registerSuccessFn(data, status, headers, config) {
        //         Authentication.login(email, password);
        //     }
        //
        //     /**
        //     * @name registerErrorFn
        //     * @desc Log 'Epic failure!' to the console
        //     **/
        //     function registerErrorFn(data, status, headers, config) {
        //         console.error('Epic failure!');
        //     }
        // }

        /**
        * @name login
        * @desc Try to log in with email `email` and password `password`
        * @param {string} email The email entered by the username
        * @param {string} password The password entered by the user
        * returns {Promise}
        * @memberOf pumi.epidata.service.Authentication
        **/
        function login(username, password) {
            console.log(username, password);
            return $http.post('/api/v1/login/', {
                username: username,
                password: password
            }).then(loginSuccessFn, loginErrorFn);

            /**
            * @name loginSuccessFn
            * @desc Set the authenticated account and redirect to index
            **/
            function loginSuccessFn(data, status, headers, config) {
                Authentication.setAuthenticatedAccount(data.data);
                window.location = '/';
            }

            /**
            * @name loginEfforFn
            * @desc Log "Epic failure!" to the console
            **/
            function loginErrorFn(data, status, headers, config){
                console.error('Epic failure!');
            }
        }

        /**
        * @name getAuthenticateAccount
        * @desc Return the currently authenticated account
        * @returns {object|undefiled} Account if authenticated, else `undefined`
        * @memberOf pumi.epidata.services.authentication
        **/
        function getAuthenticatedAccount() {
            if(!$cookies.authenticatedAccount) {
                return;
            }
            return JSON.parse($cookies.authenticatedAcccount);
        }

        /**
        * @name IsAuthenticated
        * @desc Check if the current user is authenticated
        * @returns {boolean} True is user is authenticated, else false.
        * @memberOf thinkster.authentication.services.authentication
        **/
        function isAuthenticated() {
            return !!$cookies.authenticatedAccount;
        }

        /**
        * @name setAuthenticatedAccount
        * @desc Stringify the account object and store it in a cookie
        * @param {Object} user The account object to be stored
        * @returns {undefined}
        * @memberOf pumi.epidata.services.authentication
        **/
        function setAuthenticatedAccount(account) {
            $cookies.authenticatedAccount = JSON.stringify(account);
        }

        /**
        * @name unauthenticate
        * @desc Delete the cookie where the user object is stored
        * @returns {undefined}
        * @memberOf pumi.epidata.services.authentication
        **/
        function unauthenticate() {
            delete $cookies.authenticatedAccount;
        }
    }
})();
