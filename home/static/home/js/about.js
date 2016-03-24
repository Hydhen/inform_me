app.controller('AboutCtrl', function ($scope) {
    $scope.about = djangoVar.about;
    $scope.json = $scope.about;
});
