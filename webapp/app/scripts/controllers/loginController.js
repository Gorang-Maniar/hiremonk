(function () {

    'use strict';

    angular.module('HiremonkApp').
        controller('loginController', loginController);

    loginController.$inject = ['$scope', '$rootScope', '$auth', 'authService'];

    function loginController($scope, $rootScope, $auth, authService) {

        var username;

        var email;

        var password;

        var signup = function () {
            console.log("inside signup of controller");
            authService.register({email: $scope.email, password: $scope.password, username: $scope.username})
                .then(function(){
                    console.log("you have signed up");
                })
                .catch(function(response){
                   console.log("you have not signed up");
                });
        };


        var login = function (user) {
            $auth.login({ email: $scope.email, password: $scope.password })
                .then(function () {
                    console.log("you have successfully logged in");
                })
                .catch(function (response) {
                    console.log("you were unable to login");
                });
        };

        var authenticate = function (provider) {
            $auth.authenticate(provider)
                .then(function () {
                    console.log("you have successfully authenticated");
                })
                .catch(function (response) {
                    console.log("you were not able to autenticate");
                });
        };

    }

}());
