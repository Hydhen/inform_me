app.controller('RulesCtrl', function ($scope) {
    $scope.rules = djangoVar.rules;
    $scope.json = $scope.rules;

    console.log($scope.json);
});
