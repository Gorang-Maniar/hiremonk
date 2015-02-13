(function () {

    'use strict';

    angular.module('HiremonkApp', ['ngRoute','ngCookies','satellizer'])

        .config(['$routeProvider',

            function ($routeProvider) {

                $routeProvider

                    .when('/signup', {
                        templateUrl: '../views/pages/login-signup.html',
                        controller: 'loginController'
                    })
                    .when('/', {
                        templateUrl: '../views/pages/login-signup.html',
                        controller: 'loginController'
                    })
                    .otherwise({
                        redirectTo: '/'
                    });

            }
        ]);

}());