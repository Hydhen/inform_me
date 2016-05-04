var app = angular.module('InformMe', ['ngMaterial', 'ngSanitize', 'ngRoute']);

app.config(['$routeProvider', '$interpolateProvider', '$mdThemingProvider',
    function($routeProvider, $interpolateProvider, $mdThemingProvider) {
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('green');
        $routeProvider.when('/', {
            controller: 'HomeCtrl',
            templateUrl: 'home.html',
        }).when('/login', {
            controller: 'LoginCtrl',
            templateUrl: 'login.html'
        }).when('/about', {
            controller: 'AboutCtrl',
            templateUrl: 'about.html'
        }).when('/rules', {
            controller: 'RulesCtrl',
            templateUrl: 'rules.html'
        }).when('/project', {
            controller: 'ProjectCtrl',
            templateUrl: 'project.html'
        }).when('/staff', {
            controller: 'StaffCtrl',
            templateUrl: 'staff.html'
        })
}]);

app.controller('MenuCtrl', function($scope, $mdSidenav, $http, $mdToast, $window, $location) {
    function toggleMenu() {
        $mdSidenav('menu').toggle();
    }

    function isMenuOpen() {
        return $mdSidenav('menu').isOpen();
    }

    request = $http.get('http://' + $location.host() + '/api/islogged').then(
         function successCallback(response) {
             console.log(response.data);
             $scope.username = response.data
         },
         function errorCallback(response){
             console.log("error");
             console.log(response);
         });

    function logout() {
        request = $http.get('http://' + $location.host() + '/api/logout').then(
             function successCallback(response) {
                 console.log(response);
                 $scope.json = response.data;
                 $window.location.reload();
             },
             function errorCallback(response){
                 console.log("error");
                 console.log(response);
             });
    }

    $scope.toggleMenu = toggleMenu;
    $scope.isMenuOpen = isMenuOpen;
    $scope.logout = logout;
});
