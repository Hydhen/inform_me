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

    app.controller('MenuCtrl', function($scope, $mdSidenav) {
        console.log("On index");
        function toggleMenu() {
            $mdSidenav('menu').toggle();
        }

        function isMenuOpen() {
            return $mdSidenav('menu').isOpen();
        }

        $scope.toggleMenu = toggleMenu;
        $scope.isMenuOpen = isMenuOpen;
    });
