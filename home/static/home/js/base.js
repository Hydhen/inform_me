var app = angular.module('InformMe', ['ngMaterial']);

app.config(function($interpolateProvider, $mdThemingProvider) {
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    $mdThemingProvider.theme('default')
        .primaryPalette('blue')
        .accentPalette('green');
})

app.controller('MenuCtrl', function($scope, $mdSidenav) {
    function toggleMenu() {
        $mdSidenav('menu').toggle();
    }

    function isMenuOpen() {
        return $mdSidenav('menu').isOpen();
    }

    $scope.toggleMenu = toggleMenu;
    $scope.isMenuOpen = isMenuOpen;
});
